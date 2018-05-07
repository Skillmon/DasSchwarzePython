from .proben import *
from .held import *

# Meljow initialisieren
meljow = Held()

## Basiseigenschaften {{{
meljow.eigenschaften.basis = \
        {"mu":13,"kl":14,"in":13,"ch":14,"ff":12,"ge":13,"ko":13,"kk":12}
# }}}

## Zauber {{{
meljow.neuer_zauber("Adamantium Erzstruktur"   ,  2)
meljow.neuer_zauber("Adlerauge Luchsenohr"     ,  5)
meljow.neuer_zauber("Armatrutz"                ,  9)
meljow.neuer_zauber("Attributo"                ,  5)
meljow.neuer_zauber("Balsam Salabunde"         ,  4)
meljow.neuer_zauber("Blick in die Gedanken"    ,  3)
meljow.neuer_zauber("Blitz dich find"          , 13)
meljow.neuer_zauber("Corpofrigo Kälteschock"   ,  5)
meljow.neuer_zauber("Custodosigil Diebesbann"  ,  2)
meljow.neuer_zauber("Eisenrost und Patina"     ,  3)
meljow.neuer_zauber("Flim Flam Funkel"         ,  3)
meljow.neuer_zauber("Fortifex arkane Wand"     ,  4)
meljow.neuer_zauber("Fulminictus Donnerkeil"   , 11)
meljow.neuer_zauber("Gardianum Zauberschild"   ,  6)
meljow.neuer_zauber("Ignifaxius Flammenstrahl" , 10)
meljow.neuer_zauber("Ignisphaero Feuerball"    ,  4)
meljow.neuer_zauber("Invercano Spiegeltrick"   ,  2)
meljow.neuer_zauber("Odem Arcanum"             , 12)
meljow.neuer_zauber("Paralysis starr wie Stein",  3)
meljow.neuer_zauber("Plumbumbarum schwerer Arm",  5)
meljow.neuer_zauber("Psychostabilis"           ,  5)
meljow.neuer_zauber("Respondami"               ,  3)
# }}}

## globalisieren {{{
meljow.aktiv()
# }}}
