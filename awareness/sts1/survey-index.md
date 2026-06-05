# sts1 ontology map — resolve any game entity to its entry.
#
# slug(name): lowercase, drop ' and ., other non-alphanumeric runs -> '-'.
#   e.g. "Spike Slime (M)" -> spike-slime-m, "Gremlin Nob" -> gremlin-nob.
# To recall a bare name, search these categories in order for <category>/slug(name):
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
Louse: enemies/red-louse | enemies/green-louse   (ambiguous — pull both)
