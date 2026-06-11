# sts1 ontology map — resolve any game entity to its entry.
#
# slug(name): lowercase, drop ' and ., other non-alphanumeric runs -> '-'.
#   e.g. "Spike Slime (M)" -> spike-slime-m, "Gremlin Nob" -> gremlin-nob.
# A bare name resolves to <category>/slug(name), searching these categories in
# order; a miss retries with a leading "the-" added or removed ("Champ" ->
# the-champ); a name in several categories returns every match:
#   cards enemies bosses relics potions events buffs debuffs encounters rules types characters acts ascension shop
# Upgraded card: "<name>+" -> phenomena/sts1/cards/slug(name)-plus.
# The names below override the slug rule (in-game name doesn't slug to the file).

## aliases (in-game name -> entry)
Ascension N: ascension/aN   (e.g. "Ascension 15" -> ascension/a15)
Centurion + Mystic: encounters/centurion-and-mystic
Chosen + Cultist: encounters/chosen-and-cultist
Gremlin Leader + 2 Gremlins: encounters/gremlin-leader
Reptomancer + 2 Daggers: encounters/reptomancer
The Corrupt Heart: bosses/corrupt-heart
The Transient: enemies/transient

## phenomena (applies-when -> entry)
in combat holding any potion, and at least one of — incoming damage exceeds what the hand can block; a kill may be in reach this turn or next; the fight is an elite or boss; the belt is full.: phenomena/sts1/recognitions/potion-use
