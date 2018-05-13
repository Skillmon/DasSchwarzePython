import xml.etree.ElementTree as ET # xml parsing
import re
from . import ipop
from . import proben
from . import talentlisten as talente

class Zauber(object):# {{{
    def __init__(self,probe,ZfW,name=False):
        self.name  = name
        self.probe = probe
        self.skill = ZfW
#}}}

class Talent(object):# {{{
    def __init__(self,probe,TaW,name=False):
        self.name  = name
        self.probe = probe
        self.skill = TaW
#}}}

class Held(object):# {{{
    def __init__(self):# {{{
        self.eigenschaften = self.Eigenschaften()
    # }}}
    class Eigenschaften(object):# {{{
        def __init__(self):
            self.basis = {
                    "mu":0,"kl":0,"in":0,"ch":0,"ff":0,"ge":0,"ko":0,"kk":0 }
            self.zauber = {}
            self.talente = {}
    # }}}
    def zauber(self, name, harder=0):# {{{
        return self._skill_probe(name, talente.suche.zauber,
                talente.zauberliste.namen, self.eigenschaften.zauber, "Welcher",
                "Zauber", talente.probe.zauber, harder=harder)
    # }}}
    def talent(self, name, harder=0):# {{{
        return self._skill_probe(name, talente.suche.talent,
                talente.talentliste.namen, self.eigenschaften.talente,
                "Welches", "Talent", talente.probe.talent, harder=harder)
    # }}}
    def _skill_probe(self, name, suche, talentliste, bekannt, welchers,# {{{
            talauber, probe, harder=0):
        matches = suche(name)
        if len(matches) == 0:
            print(talauber + " '%s' nicht bekannt."%(name))
        elif len(matches) != 1:
            evtl = [ i for i in matches if talentliste[i] in bekannt ]
            if len(evtl) == 0:
                print("Held kennt "+talauber+" '%s' nicht."%(name))
                return False
            elif len(evtl) != 1:
                print("'%s' konnte nicht eindeutig ermittelt werden!"%(name))
                print(welchers+" "+talauber+" ist gemeint?")
                name = ipop.choice_from_list(evtl, print_list=talentliste,
                        out_list=talentliste)
            else: name = talentliste[evtl[0]]
        else:
            zz = talentliste[matches[0]]
            if zz not in bekannt:
                print("Held kennt "+talauber+" '%s' nicht."%(name))
                return False
            name = zz
        print("Würfle Probe auf '%s'"%(name))
        skill = bekannt[name].skill
        stats = self.eigenschaften.basis
        return probe(name, stats, skill, harder=harder, fullmatch=True)
    # }}}
    def probe(self, st, harder=0, skill=0, silent=False, nonstop=False):# {{{
        ret = proben.probe(
                st, harder=harder, skill=skill, silent=silent, nonstop=nonstop,
                stats=self.eigenschaften.basis)
        return ret
    # }}}
    def neues_talent(self, name, TaW, fullmatch=False):# {{{
        return self._neuer_skill(name, TaW, talente.suche.talent,
                talente.talentliste, self.eigenschaften.talente, "Welches",
                "Talent", Talent, fullmatch=fullmatch)
    # }}}
    def neuer_zauber(self, name, ZfW, fullmatch=False):# {{{
        return self._neuer_skill(name, ZfW, talente.suche.zauber,
                talente.zauberliste, self.eigenschaften.zauber, "Welcher",
                "Zauber", Zauber, fullmatch=fullmatch)
    # }}}
    def _neuer_skill(self, name, skill, suche, talentliste, bekannt,# {{{
            welchers, talauber, Talauber, fullmatch=False):
        if fullmatch:
            if name not in talentliste.namen:
                print(talauber+" '%s' nicht bekannt."%(name))
                return False
            entry = talentliste.namen.index(name)
        else:
            matches = suche(name)
            if len(matches) == 0:
                print(talauber+" '%s' nicht bekannt."%(name))
                return False
            elif len(matches) != 1:
                print("'%s' koonte nicht eindeutig ermittelt werden!"%(name))
                print(welchers+" "+talauber+" ist gemeint?")
                entry = ipop.choice_from_list(matches,
                        print_list=talentliste.namen)
            else: entry = matches[0]
        name = talentliste.namen[entry]
        if name in bekannt:
            print(talauber+" bereits bekannt.")
            return False
        probe = talentliste.proben[entry]
        bekannt[name] = Talauber(probe, skill, name=name)
        return True
    # }}}
    def liste_talente(self, name=False, probe=False):# {{{
        return self._liste_skills(self.eigenschaften.talente, name=name,
                probe=probe)
    # }}}
    def liste_zauber(self, name=False, probe=False):# {{{
        return self._liste_skills(self.eigenschaften.zauber, name=name,
                probe=probe)
    # }}}
    def _liste_skills(self, liste, name=False, probe=False):# {{{
        l = 0
        if name: pattern = re.compile(".*" + name + ".*",re.I)
        for k, v in liste.items():
            if name and re.search(pattern, k) == None: continue
            l = max(l,len(k))
        for k, v in liste.items():
            if name and re.search(pattern, k) == None: continue
            print(k,end="")
            for i in range(l - len(k)):
                print(" ",end="")
            print("  ",end="")
            print("%2d"%(v.skill),end="")
            if probe:
                print("    ",end="")
                print(v.probe,end="")
            print("")
    # }}}
    def chance_zauber(self,name,harder=0):
        return self._chance(name, talente.suche.zauber,
                talente.zauberliste, self.eigenschaften.zauber, "Welcher",
                "Zauber", harder=harder)
    def chance_talent(self,name,harder=0):
        return self._chance(name, talente.suche.talent,
                talente.talentliste, self.eigenschaften.talente, "Welches",
                "Talent", harder=harder)
    def _chance(self, name, suche, talentliste, bekannt,
            welchers, talauber, harder=0):
        matches = suche(name)
        if len(matches) == 0:
            print(talauber + " '%s' nicht bekannt."%(name))
            return False
        elif len(matches) != 1:
            evtl = [ i for i in matches if talentliste.namen[i] in bekannt ]
            if len(evtl) == 0:
                print("Held kennt "+talauber+" '%s' nicht."%(name))
                return False
            elif len(evtl) != 1:
                print("'%s' konnte nicht eindeutig ermittelt werden!"%(name))
                print(welchers+" "+talauber+" ist gemeint?")
                name = ipop.choice_from_list(evtl, print_list=talentliste.namen,
                        out_list=talentliste.namen)
            else: name = talentliste.namen[evtl[0]]
        else:
            zz = talentliste.namen[matches[0]]
            if zz not in bekannt:
                print("Held kennt "+talauber+" '%s' nicht."%(name))
                return False
            name = zz
        print("Ermittle Wahrscheinlichkeit von '%s'"%(name))
        skill = bekannt[name].skill
        stats = self.eigenschaften.basis
        probe = talente.probe.proben_eigenschaften(name, talentliste,
                fullmatch=True)
        if probe:
            harder = harder + probe[1]
            probe = probe[0]
        else: return False
        return proben.chance(probe[0], probe[1], probe[2],
                harder=harder, skill=skill, stats=stats)
    def aktiv(self):# {{{
        """Setzt die momentan vom Submodule 'proben' verwendeten stats auf die
        Basiseigenschaften des momentanen Helden"""
        proben.set_stats(self.eigenschaften.basis)
    # }}}
    def held_von_helden_xml(self,infile):# {{{
        traits  = {}
        talents = {}
        fights  = {}
        spells  = {}
        tree    = ET.parse(infile)
        root    = tree.getroot()
        for trait in root.iter('eigenschaft'):
            traits[trait.attrib['name']] = int(trait.attrib['value'])
        for talent in root.iter('talent'):
            talents[talent.attrib['name']] = int(talent.attrib['value'])
        # for fight in root.iter('kampfwerte'):
            # fights[fight.attrib['name']] = int(fight.attrib['value'])
        spellslist = root[0].find('zauberliste')
        spe
        talents = hero.getElementsByTagName('talent')
        fights  = hero.getElementsByTagName('kampfwerte')
        spells  = hero.getElementsByTagName('zauber')
        return [hero,traits,talents,fights,spells]
    # }}}
# }}}
