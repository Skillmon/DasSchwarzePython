import xml.etree.ElementTree as ET # xml parsing
from . import proben
from . import talentlisten

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
        if name not in self.eigenschaften.zauber:
            print("Zauber '%s' nicht bekannt."%(name))
            return False
        zz = self.eigenschaften.zauber[name]
        self.aktiv()# stats für das proben modul setzen
        return proben.probe(zz.probe, harder=harder, skill=zz.ZfW)
    # }}}
    def neuer_zauber(self,name,ZfW):# {{{
        if name not in talentlisten.Zauberliste:
            print("Zauber '%s' nicht bekannt."%(name))
            return False
        zz = talentlisten.Zauberliste[name]
        self.eigenschaften.zauber[name] = Zauber(zz, ZfW, name=name)
        return True
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
