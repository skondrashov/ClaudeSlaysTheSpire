# Interface Bugs

Known issues in the CommunicationMod / relay / cmd.py / state_formatter pipeline. Each entry: what happens, root cause (if known), impact, status, affected runs.

---

## IB-001: Card index shifting in batched turn() commands

**What:** When playing multiple cards via `turn()`, indices are pre-computed for the entire batch. After each card play, hand indices shift (card removed = everything after it moves down by 1). The pre-computed indices become wrong after the first play.

**Root cause:** `turn()` sends all actions as a single batch. CommunicationMod executes them sequentially, but the indices were calculated against the original hand state.

**Impact:** FATAL. Multiple confirmed deaths from wrong card played.

**Affected runs:** 3, 21, 22, 57, 133 (Elixir variant), 190 (Eruption+ into Wrath, killed by Guardian), 212 (Meditate instead of Wallop)

**Repro seed:** `start WATCHER 0 -1241838559258863033` (Run 190). Play to F16 Guardian fight. Hand has Eruption+ adjacent to other cards. Batch `turn()` with 3+ plays — Eruption+ shifts into a slot the agent didn't intend, enters Wrath without exit.

**Status:** FIXED (2026-05-23). `turn()` now snapshots the hand at turn start. Numeric indices are resolved against the snapshot to get card identity (name + upgrades), then the card is found in the current hand by identity. Index shifts from playing cards are handled automatically. Cost is excluded from identity matching so Corruption/Madness/Enlightenment don't break it. Falls back to name-only match if upgrades change (Armaments+).

---

## IB-002: GRID index mismatch during combat

**What:** When a card triggers a GRID selection screen during combat (e.g., Omniscience "choose a card to play twice"), the state formatter showed the combat hand instead of the GRID. Agent used hand indices for GRID selection, picking the wrong card.

**Root cause:** `state_formatter.py` `format_state()` had GRID/HAND_SELECT checks behind an `elif` after the `if phase == "COMBAT"` check. During combat, the COMBAT branch always won, hiding the GRID screen.

**Impact:** FATAL. Run 212 Floor 39: Omniscience+ played, agent chose index 5 expecting Wallop+, got Strike instead. Died at 1 HP to Spire Growth.

**Affected runs:** 212 (fatal, F39 Spire Growth), 212 (non-fatal, earlier Darklings fight -- chose Defend instead of Judgment)

**Repro seed:** `start WATCHER 0 7093840872599109358` (Run 212). Play to F39. Deck includes Omniscience+ — playing it mid-combat opens a GRID selection screen. Before the fix, the agent saw hand indices instead of GRID indices.

**Status:** FIXED (2026-05-22). Moved GRID/HAND_SELECT checks before COMBAT check in format_state(). GRID now shows first with combat context below. Guidance text updated to emphasize GRID indices differ from hand indices.

---

## IB-003: Shop index/translation mismatches

**What:** `choose N` at shops translates to an unexpected item name in the log/translated field. The actual purchase appears to execute correctly (the right card/relic ends up in the deck/inventory), but the translated field shows a different card name.

**Root cause:** Unknown. Possibly the shop item ordering in CommunicationMod differs from what the state formatter displays, or the translation layer maps to the wrong item name for logging. The actual game execution uses the correct index.

**Impact:** Low (cosmetic/logging). No confirmed wrong purchase. But creates confusion when reviewing run logs and could eventually cause a real mispurchase if the display mismatch reflects an actual index offset.

**Affected runs:** 142 (intended Evolve, translated "Buy Bandage Up"), 143 (intended Evolve, translated "Buy Finesse"; intended removal, translated "Buy Cleave"), 168 (intended Piercing Wail, translated "Buy Infinite Blades"), 190 (intended card removal, translated "Buy Follow-Up"; intended Rushdown, translated "Buy Dramatic Entrance")

**Repro seed:** `start WATCHER 0 -1241838559258863033` (Run 190). Navigate to any shop floor. Send `choose N` for various items and compare the translated field against what's actually at that index. No individual run file for 142/143/168 (predate JSON format).

**Status:** OPEN. Cosmetic only — no gameplay impact confirmed.

**Fix:** The display uses `_translate_command()` to map indices back to item names for logging. This function may use a different item ordering than `_build_shop_choice_list()` (which matches CommunicationMod's actual indexing). Align the two, or just suppress the translated field for shop commands since the agent uses names (not indices) anyway. Low priority — the actual purchases are correct.

---

## IB-004: Map navigation timeout

**What:** `choose N` on the MAP screen sometimes hangs for 60 seconds, then relay.py returns `{"status": "ok", "note": "command sent, state pending"}`. The game doesn't process the map node selection.

**Root cause:** CommunicationMod doesn't directly navigate map nodes. It uses `MapRoomNodeHoverPatch` to simulate hovering over the target node, then sets `doHover = true` and `dungeonMapScreen.clicked = true`. This hover-then-click simulation can fail if the game doesn't process the hover in time (race condition).

**Impact:** Medium. Causes 60s delays and potential confusion. Agent may retry or attempt alternative navigation. Rare -- one confirmed occurrence.

**Affected runs:** One occurrence observed (exact run not logged). Rare enough to not warrant a fix, but worth tracking frequency.

**Status:** OPEN. Accepted as intermittent.

**Fix:** Two options:
1. **cmd.py retry** — If `send()` gets a "state pending" response on a MAP screen, auto-retry the same `choose` command after a short delay (2-3s). Simple, handles the race condition without touching the mod.
2. **CommunicationMod fork** — Replace the hover-patch approach with direct room node navigation. Heavy lift, but would also fix any other hover-related edge cases. Only worth it if frequency increases.

---

## IB-005: HAND_SELECT index shifting (multi-select)

**What:** During HAND_SELECT screens that allow multiple card selections (e.g., Elixir "exhaust up to 2 cards"), indices shift after each selection. Agent selects index N expecting card X, but card X has shifted to a different index after the first selection.

**Root cause:** Same underlying issue as IB-001 but in the HAND_SELECT context. CommunicationMod removes the selected card from the selection list, shifting all subsequent indices.

**Impact:** FATAL. Run 133: Elixir multi-select, chose index 3 expecting Wound, got Shockwave (only Weak source). Shockwave exhausted, making incoming damage unsurvivable.

**Affected runs:** 133 (fatal -- Shockwave exhausted instead of Wound)

**Repro seed:** Run 133, IRONCLAD A0 (seed not recorded — predates seed logging). To reproduce conditions: any run with Elixir in hand + mixed card types. Use Elixir, select index 3, verify the card at index 3 is what you expected after the first selection shifted indices.

**Status:** FIXED (2026-05-23). `send()` now snapshots the HAND_SELECT card list when the screen first appears. Numeric `choose N` commands are resolved against the snapshot to get card identity, then found in the current (shifted) list. Same identity matching as IB-001 (name + upgrades, cost-independent, name-only fallback). Snapshot clears when leaving HAND_SELECT.

---

## IB-006: Snecko Eye breaks name-based card resolution

**What:** Snecko Eye randomizes card costs each turn. When multiple copies of the same card are in hand with different randomized costs, name-based resolution (`play CardName target`) may select the wrong copy (e.g., the 3-cost copy instead of the 0-cost copy).

**Root cause:** Name resolution finds the first card matching the name. With Snecko Eye, copies of the same card have different costs, making them functionally different but indistinguishable by name.

**Impact:** Medium. Can waste energy by playing the expensive copy when a cheap copy exists.

**Affected runs:** 215 (first Watcher win had Snecko Eye -- workaround used), potentially others with Snecko Eye.

**Repro seed:** `start WATCHER 0 5742301588378060269` (Run 215). This run picks up Snecko Eye. Once active, any turn with duplicate cards in hand (e.g., two Strikes at different randomized costs) will show the issue — `play Strike 0` always picks the first one regardless of cost.

**Status:** MOSTLY FIXED in code — `_resolve_card_name` already picks the cheapest copy when multiple cards share the same name (line 354: `best_card_cost` comparison). So `play Strike 0` picks the 0-cost Strike over the 3-cost one.

**Remaining gap:** Agent can't target a SPECIFIC expensive copy when it wants to (rare — almost never correct to pick the expensive one). Would need a syntax extension like `play Strike#2 0` to select by position, or CommunicationMod card UUID support.

**Fix:** Probably already sufficient. The cheapest-first heuristic is correct 99%+ of the time. Monitor for cases where the agent actually needs a specific copy.

---

## IB-007: Relay timeout on slow game state responses

**What:** relay.py waits 60 seconds for CommunicationMod to return game state after a command. If the game is slow (loading, animation, transition), the relay returns a "state pending" response and the agent must re-poll.

**Root cause:** Fixed 60-second timeout in relay.py `command_result.wait(timeout=60)`. Some game transitions (act transitions, boss deaths, long animations) take longer than expected.

**Impact:** Low. Causes delays but not wrong actions. Agent can recover by calling `state()` again.

**Affected runs:** Occasional across many runs. Not systematically tracked.

**Status:** OPEN. Low priority.

**Fix:** Add auto-retry in `send()` — if the response is "state pending", wait 3s and call `state()` to re-poll. Caps at 2 retries. Simple change in cmd.py, no mod changes needed.

---

## IB-008: Double-end command causes extra enemy turn

**What:** Agent sends `end` twice in a single turn. The game processes both, causing an extra enemy turn. The agent's second `end` fires because the state appears unchanged after the first one (state fetch returns before the turn fully resolves).

**Root cause:** Race condition between cmd.py's `send("end")` and CommunicationMod's turn resolution. The first `end` is accepted but the state returned still shows the player's turn (hasn't transitioned yet). The agent sees "still my turn" and sends `end` again, which gets queued and processed as ending the NEXT player turn immediately.

**Impact:** FATAL. Run 216: extra enemy turn cost 22 HP against Sentries, generating additional Dazes that snowballed into death.

**Affected runs:** 216 (fatal — Sentries)

**Repro seed:** `start IRONCLAD 5 9128496640971033917` (Run 216). Play to F14 Sentries. In a turn with no playable cards, send `end` and immediately send `end` again before the state updates.

**Status:** OPEN. Documented in `interface/sts1/tools.md` as known issue. Agent prompt now says "one `end` per turn" but no cmd.py-level guard.

**Fix:** cmd.py should track whether `end` has been sent this turn and reject duplicates. Add a `_turn_ended` flag that's set on `end` and cleared when state shows a new turn (different turn number or enemy phase). Simple guard in `send()`.

---

## IB-009: Duplicate run logging (double GAME_OVER)

**What:** A single run produces two run log files (e.g., run_216.json and run_217.json with identical content). The stats counter also double-counts the run.

**Root cause:** Likely the GAME_OVER detection in cmd.py or regen_stats.py fires twice — once when the game over screen appears and once when the player proceeds through it. Or stream.py's event handler logs the run end twice.

**Impact:** Low. Creates duplicate files and inflates run counts. Caught manually and cleaned up, but wastes time.

**Affected runs:** 216/217 (identical), 220/221 (two genuine runs but agent wasn't told to stop after one)

**Status:** OPEN. Workaround: "Play only ONE run" in agent prompt prevents the two-genuine-runs case. The identical-duplicate case (216/217) needs investigation in cmd.py's GAME_OVER handler.

**Fix:** Investigate whether `_log_run()` in cmd.py can fire twice for the same game_over event. Add a guard (e.g., check if run file already exists before writing). Also check regen_stats.py deduplication.

---

## Tracking

When a new interface bug is observed, add it here with:
- **IB-NNN** identifier
- What happened (observable behavior)
- Root cause (if known)
- Impact (FATAL / Medium / Low / Cosmetic)
- Affected runs
- Status (OPEN / FIXED / MITIGATED / MONITORING)

Reference this file from run audits and observations when interface bugs contribute to deaths or misplays.
