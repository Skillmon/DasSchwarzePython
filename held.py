import xml.etree.ElementTree as ET # xml parsing
from . import ipop
from . import proben
from . import talentlisten as talente

class Zauber(object):# {{{
    def __init__(self,probe,ZfW,name=False):
        self.name = name
        self.probe = probe
        self.ZfW = ZfW
#}}}

class Talent(object):# {{{
    def __init__(self,probe,TaW,name=False):
        self.name = name
        self.probe = probe
        self.TaW = TaW
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
    def zauber(self,name,harder=0):# {{{
        matches = talente.suche.zauber(name)
        if len(matches) == 0:
            print("Zauber '%s' nicht bekannt."%(name))
        elif len(matches) != 1:
            evtl = [ i for i in matches if talente.zauberliste.namen[i] in
                    self.eigenschaften.zauber ]
            if len(evtl) == 0:
                print("Held kennt Zauber '%s' nicht."%(name))
                return False
            elif len(evtl) != 1:
                print("'%s' konnte nicht eindeutig ermittelt werden!"%(name))
                print("Welcher Zauber ist gemeint?")
                for i,m in enumerate(evtl):
                    print("  %d: %s"%(i,talente.zauberliste.namen[m]))
                zz = evtl[ipop.int_input("Nummer: ",len(matches)-1)]
                name = talente.zauberliste.namen[zz]
            else: name = talente.zauberliste.namen[evtl[0]]
        else:
            zz = talente.zauberliste.namen[matches[0]]
            if zz not in self.eigenschaften.zauber:
                print("Held kennt Zauber '%s' nicht."%(name))
                return False
            name = zz
        print("Würfle Probe auf '%s'"%(name))
        skill = self.eigenschaften.zauber[name].ZfW
        stats = self.eigenschaften.basis
        return talente.probe.zauber(name, stats, skill, harder=harder,
                fullmatch=True)
    # }}}
    def probe(self, st, harder=0, skill=0, silent=False, nonstop=False):# {{{
        ret = proben.probe(
                st, harder=harder, skill=skill, silent=silent, nonstop=nonstop,
                stats=self.eigenschaften.basis)
        return ret
    # }}}
    def neues_talent(self,name,TaW,fullmatch=False):# {{{
        if fullmatch:
            if name not in talente.talentliste.namen:
                print("Talent '%s' nicht bekannt."%(name))
                return False
            entry = talente.talentliste.namen.index(name)
        else:
            matches = talente.suche.talent(name)
            if len(matches) == 0:
                print("Talent '%s' nicht bekannt."%(name))
                return False
            elif len(matches) != 1:
                print("'%s' konnte nicht eindeutig ermittelt werden!"%(name))
                print("Welches Talent ist gemeint?")
                for i,m in enumerate(matches):
                    print("  %d: %s"%(i,talente.talentliste.namen[m]))
                entry = matches[ipop.int_input("Nummer: ",len(matches)-1)]
            else: entry = matches[0]
        name = talente.talentliste.namen[entry]
        if name in self.eigenschaften.talente:
            print("Talent bereits bekannt.")
            return False
        probe = talente.talentliste.proben[entry]
        self.eigenschaften.talente[name] = Talent(probe, TaW, name=name)
        return True
    # }}}
    def neuer_zauber(self,name,ZfW,fullmatch=False):# {{{
        if fullmatch:
            if name not in talente.zauberliste.namen:
                print("Talent '%s' nicht bekannt."%(name))
                return False
            entry = talente.zauberliste.namen.index(name)
        else:
            matches = talente.suche.zauber(name)
            if len(matches) == 0:
                print("Zauber '%s' nicht bekannt."%(name))
                return False
            elif len(matches) != 1:
                print("'%s' konnte nicht eindeutig ermittelt werden!"%(name))
                print("Welcher Zauber ist gemeint?")
                for i,m in enumerate(matches):
                    print("  %d: %s"%(i,talente.zauberliste.namen[m]))
                entry = matches[ipop.int_input("Nummer: ",len(matches)-1)]
            else: entry = matches[0]
        name = talente.zauberliste.namen[entry]
        if name in self.eigenschaften.zauber:
            print("Zauber bereits bekannt.")
            return False
        probe = talente.zauberliste.proben[entry]
        self.eigenschaften.zauber[name] = Zauber(probe, ZfW, name=name)
        return True
    # }}}
    def liste_talente(self):# {{{
        l = 0
        for k, v in self.eigenschaften.talente.items():
            l = max(l,len(k))
        for k, v in self.eigenschaften.talente.items():
            print(k,end="")
            for i in range(l - len(k)):
                print(" ",end="")
            print("  ",end="")
            print("%2d"%(v.ZfW))
    # }}}
    def liste_zauber(self):# {{{
        l = 0
        for k, v in self.eigenschaften.zauber.items():
            l = max(l,len(k))
        for k, v in self.eigenschaften.zauber.items():
            print(k,end="")
            for i in range(l - len(k)):
                print(" ",end="")
            print("  ",end="")
            print("%2d"%(v.ZfW))
    # }}}
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
