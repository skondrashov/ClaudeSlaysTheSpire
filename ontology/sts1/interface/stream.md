# Stream

The agent plays for a live stream audience via an OBS overlay.

## Overlay

The stream overlay displays:
- Current game state
- The agent's most recent action and reasoning (`reason=` parameter)
- The agent's strategic analysis (`think()` output)

## Visibility

- The `reason=` parameter on `send()` and `turn()` is displayed to viewers as the rationale for each action
- The `think()` function posts longer strategic analysis visible in the overlay's thinking panel
- Viewers see WHAT the agent does and WHY — both must be present for every action
