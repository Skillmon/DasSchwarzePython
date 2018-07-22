from ..proben import *
from ..held import *

# Meljow initialisieren
meljow = Held("Meljow vom Berg", "Meljow")

## Basiseigenschaften {{{
meljow.eigenschaften.basis = \
        {"mu":13,"kl":15,"in":14,"ch":14,"ff":12,"ge":13,"ko":15,"kk":12}
# }}}

## Zauber {{{
meljow.neuer_zauber("Adamantium Erzstruktur"   ,  2)
meljow.neuer_zauber("Adlerauge Luchsenohr"     ,  5)
meljow.neuer_zauber("Armatrutz"                ,  9)
meljow.neuer_zauber("Attributo"                ,  5)
meljow.neuer_zauber("Balsam Salabunde"         ,  4)
meljow.neuer_zauber("Blick in die Gedanken"    ,  4)
meljow.neuer_zauber("Blitz dich find"          , 13)
meljow.neuer_zauber("Corpofrigo Kälteschock"   ,  5)
meljow.neuer_zauber("Custodosigil Diebesbann"  ,  2)
meljow.neuer_zauber("Eisenrost und Patina"     ,  4)
meljow.neuer_zauber("Flim Flam Funkel"         ,  3)
meljow.neuer_zauber("Fortifex arkane Wand"     ,  4)
meljow.neuer_zauber("Fulminictus Donnerkeil"   , 12)
meljow.neuer_zauber("Gardianum Zauberschild"   ,  6)
meljow.neuer_zauber("Ignifaxius Flammenstrahl" , 11)
meljow.neuer_zauber("Ignisphaero Feuerball"    ,  5)
meljow.neuer_zauber("Invercano Spiegeltrick"   ,  2)
meljow.neuer_zauber("Odem Arcanum"             , 12)
meljow.neuer_zauber("Paralysis starr wie Stein",  4)
meljow.neuer_zauber("Plumbumbarum schwerer Arm",  5)
meljow.neuer_zauber("Psychostabilis"           ,  5)
meljow.neuer_zauber("Respondami"               ,  4)
# }}}
## Talente {{{
meljow.neues_talent("Athletik",               4)
meljow.neues_talent("Klettern",               2)
meljow.neues_talent("Körperbeherrschung",     4)
meljow.neues_talent("Schleichen",             0)
meljow.neues_talent("Schwimmen",              0)
meljow.neues_talent("Selbstbeherrschung",     5)
meljow.neues_talent("Sich Verstecken",        0)
meljow.neues_talent("Singen",                 0)
meljow.neues_talent("Sinnenschärfe",          4)
meljow.neues_talent("Tanzen",                 0)
meljow.neues_talent("Zechen",                 1)
meljow.neues_talent("Reiten",                 3)
meljow.neues_talent("Menschenkenntnis",       5)
meljow.neues_talent("Überreden",              5)
meljow.neues_talent("Betören",                5)
meljow.neues_talent("Etikette",               6)
meljow.neues_talent("Gassenwissen",          -2)
meljow.neues_talent("Lehren",                 3)
meljow.neues_talent("Überzeugen",             2)
meljow.neues_talent("Fährtensuche",           3)
meljow.neues_talent("Orientierung",           5)
meljow.neues_talent("Wildnisleben",           5)
meljow.neues_talent("Götter/Kulte",          10)
meljow.neues_talent("Rechnen",                7)
meljow.neues_talent("Sagen/Legenden",         8)
meljow.neues_talent("Anatomie",              -3)
meljow.neues_talent("Geografie",              5)
meljow.neues_talent("Geschichtswissen",       6)
meljow.neues_talent("Heraldik",               5)
meljow.neues_talent("Kriegskunst",            4)
meljow.neues_talent("Magiekunde",             6)
meljow.neues_talent("Mechanik",               2, fullmatch=True)
meljow.neues_talent("Pflanzenkunde",          2)
meljow.neues_talent("Rechtskunde",            7)
meljow.neues_talent("Staatskunst",            2)
meljow.neues_talent("Sternkunde",             2)
meljow.neues_talent("Tierkunde",              1)
meljow.neues_talent("Heilkunde Wunden",       4)
meljow.neues_talent("Holzbearbeitung",        0)
meljow.neues_talent("Kochen",                 0)
meljow.neues_talent("Lederarbeiten",          2)
meljow.neues_talent("Malen/Zeichnen",         4)
meljow.neues_talent("Schneidern",             0)
meljow.neues_talent("Alchimie",               4)
meljow.neues_talent("Handel",                 2)
meljow.neues_talent("Hauswirtschaft",         1)
meljow.neues_talent("Heilkunde Gift",         2)
meljow.neues_talent("Heilkunde Krankheiten", -3)
# }}}

## globalisieren {{{
meljow.aktiv()
# }}}
