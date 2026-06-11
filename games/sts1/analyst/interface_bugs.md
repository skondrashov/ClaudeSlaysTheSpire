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

**Affected runs:** 216 (fatal — Sentries), 240 (fatal contribution — F25 Centurion+Mystic: `end` re-sent after an empty `{}` state echo, T2 eaten with 5 cards unplayed, 12 HP; the same lag also produced a wrong-card index re-send. See analyst/audits/run_240.md §4-5.)

**Repro seed:** `start IRONCLAD 5 9128496640971033917` (Run 216). Play to F14 Sentries. In a turn with no playable cards, send `end` and immediately send `end` again before the state updates.

**Status:** FIXED — verified in the wild (run 242: zero interface HP lost across 48 floors; four benign empty echoes recovered correctly, no duplicate `end` fired). The relay-race fix (post-run-240) plus the batch no-op tripwire (commit 974add1 — a `play` must remove the card from hand at state level; it caught and flagged one silent no-op in run 242, replayed by name) closed the family. Keep the habit rule (empty/unchanged echo after `end` → re-poll, never re-send) as cheap insurance.

**Fix:** cmd.py should track whether `end` has been sent this turn and reject duplicates. Add a `_turn_ended` flag that's set on `end` and cleared when state shows a new turn (different turn number or enemy phase). Simple guard in `send()`.

---

## IB-009: Duplicate run logging (double GAME_OVER)

**What:** A single run produces two run log files (e.g., run_216.json and run_217.json with identical content). The stats counter also double-counts the run.

**Root cause:** Likely the GAME_OVER detection in cmd.py or regen_stats.py fires twice — once when the game over screen appears and once when the player proceeds through it. Or stream.py's event handler logs the run end twice.

**Impact:** Low. Creates duplicate files and inflates run counts. Caught manually and cleaned up, but wastes time.

**Affected runs:** 216/217 (identical), 220/221 (two genuine runs but agent wasn't told to stop after one), 240/241 (identical — run_241 was a duplicate from a double GAME_OVER proceed; removed)

**Status:** REPORTED FIXED by the maintainer after the run 240/241 duplicate (capture bug). Previously OPEN.

**Fix:** Investigate whether `_log_run()` in cmd.py can fire twice for the same game_over event. Add a guard (e.g., check if run file already exists before writing). Also check regen_stats.py deduplication.

---

## IB-010: Event-screen choice desync ALTERS GAMEPLAY (executes a different option than echoed)

**What:** At an event, `choose 1` echoed "[Offer: 182 Gold] Lose all Gold. Obtain a Relic." but the game executed [Leave]: gold unchanged, no relic, screen advanced EVENT→MAP with no relic screen. The IB-003 shape (translation/index ordering mismatch), but here it changed the outcome instead of just the log line.

**Root cause:** FOUND (2026-06-11, via IB-013's run-241 recurrence): `format_event` and the translation numbered the full display list while `choose N` indexes CommunicationMod's enabled-only choice_list. Red Mask's "Don the Mask" option is DISABLED without the Red Mask — shifting the offer to display [1] while the executable list had [0]=offer, [1]=Leave. `choose 1` = Leave, exactly as observed.

**Impact:** Medium this time (~0 cost — run 237, F41 Tomb of Lord Red Mask, gold ended the run unspent), but the same desync on a consequential event (Vampires, Falling, Mind Bloom) would be run-altering. Player blameless — intent and echo agreed.

**Affected runs:** 237 (F41, idx 630-631), 241 (F38 — see IB-013).

**Status:** FIXED (2026-06-11) — see IB-013 for the shared fix (`_event_choice_options()`, enabled-only indexing in both formatter and translation).

**Fix:** Compare event option ordering between `_translate_command()` and CommunicationMod; add a post-choice assertion (gold/relic/HP delta vs the echoed option's stated effect) that flags a mismatch immediately instead of leaving it to audit-time inventory reconciliation.

---

## IB-011: Key acquisition fails silently (Emerald Key)

**What:** `choose Emerald Key` (echo "Emerald") returned an empty `{}` result; no confirmation, no retry; the key was never collected (end-of-run state shows "no keys").

**Root cause:** Unknown. Note: empty `{}` results ALSO follow SUCCESSFUL special-screen picks (run 237: Black Blood idx 263, Snecko idx 524, both acquired), so a guard cannot key on the empty state alone.

**Impact:** Low at A9 with an Act 3 goal (keys unused); FATAL to any Act 4 attempt.

**Affected runs:** 237 (idx 160-161, burning-elite reward).

**Status:** OPEN (known to orchestrator).

**Fix:** Post-hoc possession check after any key/relic special-screen pick — re-poll state and assert the item appears in inventory; retry once if absent.

---

## IB-012: Game drops to main menu mid-run; subsequent commands echo against a dead session

**What:** Run 241 (Silent A9, floor 28 shop): the game left the run and sat at the MAIN MENU while the relay kept answering. Every shop `choose` echoed `[chose: Buy X]` but nothing happened — gold never deducted, state flickered "OUT OF GAME transient". The player diagnosed a "broken shop," tried `key escape` (rejected out of game — but one queued escape executed and opened the Settings panel), and eventually planned to abandon the floor, losing ~178g of intended purchases.

**Root cause:** Unknown for the menu drop itself (no crash dialog; the save was written normally at floor entry — candidates: a stray input reaching the pause menu's Save and Quit, or an internal exception unwinding to menu). The SECONDARY failure is ours: command echoes don't verify the game is still in a run, so buys "succeed" against a dead session.

**Impact:** Medium-FATAL — unrecoverable by the agent alone (no resume verb exists in CommunicationMod; `start` DESTROYS the save). Without orchestrator intervention this ends the run as surely as a death.

**Recovery (worked, run 241):** (1) back up `saves/<CHAR>.autosave` immediately; (2) `scripts/game_mouse.ps1` — hover the main menu's Continue with the real cursor, VERIFY the gold hover-highlight via an OBS projector screenshot (Abandon Run sits one slot below), then click. Save loaded intact (floor 28, 45 HP, 214 gold); player resumed within its next poll.

**Affected runs:** 241 (recovered, ~40 min lost).

**Status:** OPEN (recovery procedure proven; menu-drop cause not yet found). Guard hardening shipped: `start()` no longer treats "cleanly OUT OF GAME + save exists" as a stale save (a crash-to-menu produces exactly that state with a LIVE save) — it now always requires the two-call confirm when a save file exists.

**Fix candidates:** a cmd.py tripwire — when `in_game` flips false while the last known state was mid-run (not GAME_OVER), return a loud `[RUN INTERRUPTED — game at main menu, save likely intact: STOP, do not start(), report to orchestrator]` instead of a normal state echo.

---

## IB-013: Event option indices shift past disabled options (chose relic offer, executed Leave)

**What:** Run 241 floor 38: the formatted event showed the pay-23-gold relic offer at `[1]`; the player sent `choose 1` with that intent; the echo even named the offer — but the game executed **Leave**. Gold untouched, no relic, event gone.

**Root cause:** FOUND, mechanical. `format_event` numbered ALL of `screen_state.options` (disabled included), but CommunicationMod's `choose N` indexes its `choice_list`, which contains only ENABLED options. Any disabled option above the target (here: an offer the player couldn't afford) shifts every later index by one. The command translation made it invisible by reading the same display list — echo said one thing, game did another. **This is also IB-010's mechanism** (Tomb of Lord Red Mask, run 237: option executed ≠ option echoed — that event has conditionally disabled options).

**Impact:** Medium-FATAL — silently converts any event decision into a different one whenever a disabled option is present. Wasted the run-241 relic; IB-010's instance altered gameplay.

**Affected runs:** 241 (relic offer → Leave), 237 (IB-010, Red Mask).

**Status:** FIXED (2026-06-11). Shared source of truth `_event_choice_options()` (enabled options, in order — exactly CommunicationMod's event choice_list). `format_event` numbers only enabled options (`[-] ... (DISABLED — not choosable, has no index)` for the rest) and the command translation indexes the same list. Verified with a synthetic disabled-offer event: display index == executed index. Same lesson as the shop's IB-003: always index against CommunicationMod's REAL choice list, never the raw display array.

---

## IB-014: Boss-chest stale-echo desync (relay answers "Invalid command: choose" against an already-open chest)

**What:** Run 243, floor 17 (Act 1 boss chest after BOSS_REWARD): the chest arrives already open (`chest_open` true), but the relay/formatter pipeline desynced for ~6 commands — stale "Invalid command: choose" echoes while the formatter (pre-c552a85) was simultaneously instructing "choose open / do NOT proceed." The choice list was empty (no `choose` is actually offered on an opened chest), so the player was steered into a stall: `choose open` → invalid echo → wait → repeat.

**Root cause:** Two halves. (1) Formatter half — `state_formatter.py` unconditionally emitted unopened-chest guidance ("choose open / do NOT proceed") even when `chest_open` was set. FIXED in c552a85 (2026-06-11, mid-run-243): the branch now reads `chest_open` and says "use proceed." (2) Echo half — the relay kept returning stale "Invalid command: choose" responses for several commands rather than a fresh state, so the player couldn't see the screen had no choices. OPEN; mechanism not yet isolated (candidates: cached last-error echo in relay.py, or CommunicationMod returning no state delta for rejected commands so the relay re-serves the previous response).

**Impact:** Low this time — ~6 wasted commands and a manual recovery (`wait` → `key confirm` → `wait` → `proceed`), zero game-state loss; the player's raw-read recovery worked. But a stale-echo loop on a screen with a real timer or a consequential default would be run-altering, and the same staleness shape contributed to the IB-008 family's deaths.

**Affected runs:** 243 (floor 17, idx 442-450; player's interface note at idx 452).

**Status:** HALF-FIXED (formatter guidance, c552a85). Echo staleness OPEN.

**Fix:** (1) Isolate why a rejected command can echo stale — the relay should always return the CURRENT state with the rejection, never a cached error. (2) Broader guard worth considering from the same run: the F9 Akabeko forfeit (queued `choose` hit a shifted index after a gold pickup, tool warned, pre-chained `proceed` consumed the retry) shows reward screens lack the acquisition-assert guard IB-011 proposes — extend it: after any `choose` on a reward/chest screen, assert the named item entered inventory before honoring a queued `proceed`.

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
