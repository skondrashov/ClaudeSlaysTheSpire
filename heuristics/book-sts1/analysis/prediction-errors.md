# Prediction Errors

The player fills out combat plans with predictions. The run log has both the decision (with reasoning) and the result (actual state). Compare them.

Prediction errors reveal broken mental models. They are Priority 1 because they're upstream of strategy — if the model of the game is wrong, strategy built on it will be wrong too.

## What to Look For

- **Damage miscalculations**: Predicted taking 5 but took 15
- **Kill miscalculations**: Predicted killing enemy but it survived
- **Mechanic misunderstandings**: Didn't know an enemy does X, didn't know a card exhausts
- **Missing information**: Player said "I don't know what this does"

## What to Do

For each prediction error: fix [[layer:heuristics, analysis/ontology]] if facts are wrong, update [[layer:heuristics, analysis/heuristics]] if strategy was wrong.
