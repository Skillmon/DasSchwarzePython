import xml.etree.ElementTree as ET # xml parsing

class zauber(object):
    def __init__(self,name,probe,taw):
        name = name
        probe = probe
        taw = taw
class Held(object):
    def __init__(self):
        self.eigenschaften.stats = {
                "mu":0,"kl":0,"in":0,"ch":0,"ff":0,"ge":0,"ko":0,"kk":0 }
        self.eigenschaften.zauber = {}

    class eigenschaften(object):
        def __init__(self):
            stats = {
                    "mu":0,"kl":0,"in":0,"ch":0,"ff":0,"ge":0,"ko":0,"kk":0 }
            zauber
    def self.zauber(

    def held_von_helden_xml(self,infile):
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
