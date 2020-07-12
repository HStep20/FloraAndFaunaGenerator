import random


def diceRoll(self):
    roll = random.randint(0, 9) + (random.randint(0, 9) * 10) + 1
    if roll > 100:
        return 100
    elif roll < 1:
        return 1
    else:
        return roll


def multiDiceRoll(self, x, diceFaces):
    num = 0
    for i in range(0, x):
        num = num + random.randint(1, diceFaces)
    return num

def lineBreak(self, text):
    print("==============================")
    print("         " +text)
    print("==============================")

class Flora:
    # Flora Info Vars
    floraKind = "nothin"
    primHab = "nada"
    aquaHab = "get gud"
    subHab = "non"
    rare = "meybe rare"
    group = "lonely"
    sized = "big ol one"

    # Body Vars
    floraBody = "nothin"
    floraBranches = "nada"
    floraRoots = "get gud"
    floraCoverage = "spotty"
    floraColor = "I am the night"
    floraPattern = "shallan"

    # leaf Vars
    leafType = "None"
    leafLoc = "No leaves"
    leafShapes = "No leaves"
    leafMargins = "No leaves"
    leafSurfaced = "No leaves"
    leafVenat = "No leaves"
    leafNumbers = "No leaves"
    leafColors = "No leaves"
    leafPatterns = "No Leaves"
#Reproduction Vars
    reproductions = "str"
    seed = "str"
    dispersal = "str"
    flower = "No Flowers"
    flowerShaping = "No Flowers"
    flowerSizing = "No Flowers"
    petalShap = "No Petals"
    petalNum = "No Petals"
    petalSurf = "No Petals"
    flowerLoc = "No Flowers"
    flowerFreq = "No Flowers"
    flowerSmell = "No Flowers"
    flowerColors = "No Flowers"
    flowerPatterns = "No Flowers"
    stamen = "No Flowers"
    pistil = "No Flowers"
#Diet Vars
    dietTypes = "Photosynthetic"
    tropisms = "Gravity"
#Sentience vars
    sentiences = "Not Sentient"
    sentienceTypes = "Not Sentient"
#Edibility Vars
    edibilities = "Not Edible"
    edibilitiesPrep = "Not Edible"



    def __init__(self):
        self.floraKind = self.floraType()
        self.primHab = self.primaryHabitat()
        self.aquaHab = self.aquaticSubHab()
        self.subHab = self.otherSubHab()
        self.rare = self.rarity()
        self.group = self.grouping()
        self.sized = self.size()
        self.floraBody = self.body()
        self.floraBranches = self.branches()
        self.floraRoots = self.roots()
        self.floraCoverage = self.coverage()
        self.floraColor = self.color()
        self.floraPattern = self.pattern()
        self.leafType = self.leaves()
        if self.leafType != 'None':
            self.leafLoc = self.leafLocation()
            self.leafShapes = self.leafShape()
            self.leafMargins = self.leafMargin()
            self.leafSurfaced = self.leafSurface()
            self.leafVenat = self.leafVenation()
            self.leafNumbers = self.leafNum()
            self.leafColors = self.leafColor()
            self.leafPatterns = self.leafPattern()
        self.reproductions = self.reproduction()
        self.seed = self.seeds()
        self.dispersal = self.primaryDispersal()
        self.flower = self.flowertype()
        if self.flower != "None":
            self.flowerShaping = self.flowerShape()
            self.flowerSizing = self.flowerSize()
            self.petalNum = self.petalNumber()
            if self.petalNum != "No Petals":
                self.petalShap = self.petalShape()
                self.petalSurf = self.petalSurface()
            self.flowerLoc = self.flowerLocation()
            self.flowerSmell = self.flowerScent()
            self.flowerFreq = self.flowerFrequency()
            self.flowerColors = self.flowerColor()
            self.flowerPatterns = self.flowerPattern()
            self.stamen = self.stamens()
            self.pistil = self.pistils()
            self.dietTypes = self.dietType()
            self.tropisms = self.tropism()
            # Sentience vars
            self.sentiences =self.sentience()
            if self.sentiences == "Sentient":
                self.sentienceTypes = self.sentienceType()
            # Edibility Vars
            self.edibilities =self.edibility()
            if (self.edibilities == "Edible") or (self.edibilities == "Nutritious/Tasty"):
               self.edibilitiesPrep = self.edibilityPrep()

        return

    def printAttributes(self):
        lineBreak(self, "Base Traits")
        print(self.floraKind)
        print(self.primHab)
        print(self.aquaHab)
        print(self.subHab)
        print(self.rare)
        print(self.group)
        print(self.sized)
        lineBreak(self, "Flora Body")
        print(self.floraBody)
        print(self.floraBranches)
        print(self.floraRoots)
        print(self.floraCoverage)
        print(self.floraColor)
        print(self.floraPattern)
        lineBreak(self,"Leaf Info")
        print(self.leafType)
        print(self.leafLoc)
        print(self.leafShapes)
        print(self.leafMargins)
        print(self.leafSurfaced)
        print(self.leafVenat)
        print(self.leafNumbers)
        print(self.leafColors)
        lineBreak(self,"Reproduction")
        print(self.reproductions)
        print(self.dispersal)
        print(self.flower)
        print(self.flowerShaping)
        print(self.flowerSizing)
        print(self.petalShap)
        print(self.petalNum)
        print(self.petalSurf)
        print(self.flowerLoc)
        print(self.flowerSmell)
        print(self.flowerFreq)
        print(self.flowerColors)
        print(self.flowerPatterns)
        print(self.stamen)
        print(self.pistil)
        lineBreak(self,"Diet")
        print(self.dietTypes)
        print(self.tropisms)
        lineBreak(self,"Sentience")
        print(self.sentiences)
        print(self.sentienceTypes)
        lineBreak(self,"Edibility")
        print(self.edibilities)
        print(self.edibilitiesPrep)


    # General info Stuff
    def floraType(self):
        num = diceRoll(self)
        floraTypes = {'Woody': [1, 30], 'Herbaceous': [31, 85], 'Algae': [86, 90], 'Fungus': [91, 100]}
        for t, (start, end) in floraTypes.items():
            if start <= num <= end: return t

    def primaryHabitat(self):
        num = diceRoll(self)

        # TODO: factor in gravity to roll
        if self.floraKind == 'Woody':
            primaryHabitatList = {'Aquatic': [0, 5], 'Sub-Terrestrial': [6, 10], 'Terrestrial': [11, 98],
                                  'Avian': [99, 100]}
        elif self.floraKind == 'Herbaceous':
            primaryHabitatList = {'Aquatic': [0, 35], 'Sub-Terrestrial': [36, 40], 'Terrestrial': [41, 98],
                                  'Avian': [99, 100]}
        elif self.floraKind == 'Algae':
            primaryHabitatList = {'Aquatic': [0, 80], 'Sub-Terrestrial': [81, 90], 'Terrestrial': [91, 98],
                                  'Avian': [99, 100]}
        elif self.floraKind == 'Fungus':
            primaryHabitatList = {'Aquatic': [0, 10], 'Sub-Terrestrial': [11, 40], 'Terrestrial': [41, 98],
                                  'Avian': [99, 100]}
        for t, (start, end) in primaryHabitatList.items():
            if start <= num <= end: return t

    def aquaticSubHab(self):
        if self.primHab == 'Aquatic':
            num = diceRoll(self)
            aquaHab = {'Salt Water': [0, 30], 'Fresh Water': [31, 90], 'Brackish': [91, 100]}
            for t, (start, end) in aquaHab.items():
                if start <= num <= end: return t
        return "Non-Aquatic"

    def otherSubHab(self):
        num = diceRoll(self)
        secondSubHab = {'Desert/Waste': [1, 10], 'Plains/Savannah': [11, 40], 'Marsh/Swamp': [41, 50],
                        'Forest/Jungle': [51, 80], 'Hills/Scrubland': [81, 90], 'Mountains': [91, 100]}
        for t, (start, end) in secondSubHab.items():
            if start <= num <= end: return t

    def rarity(self):
        num = diceRoll(self)
        rarities = {'Very Common': [1, 15], 'Common': [16, 50], 'Uncommon': [51, 80], 'Rare': [81, 94],
                    'Very Rare': [95, 98], 'Unique': [99, 100]}
        for t, (start, end) in rarities.items():
            if start <= num <= end: return t

    def grouping(self):
        num = diceRoll(self)
        if self.floraKind == 'Woody':
            grouping = {'Solitary (1-2)': [0, 20], 'Small Patch (1-12)': [21, 40], 'Medium Patch (12-120)': [41, 80],
                        'Large Patch (100+)': [91, 100]}
        elif self.floraKind == 'Herbaceous':
            grouping = {'Solitary (1-2)': [0, 30], 'Small Patch (1-12)': [31, 50], 'Medium Patch (12-120)': [51, 90],
                        'Large Patch (100+)': [91, 100]}
        elif self.floraKind == 'Algae':
            grouping = {'Solitary (1-2)': [0, 25], 'Small Patch (1-12)': [26, 70], 'Medium Patch (12-120)': [71, 95],
                        'Large Patch (100+)': [96, 100]}
        elif self.floraKind == 'Fungus':
            grouping = {'Solitary (1-2)': [0, 25], 'Small Patch (1-12)': [26, 70], 'Medium Patch (12-120)': [71, 95],
                        'Large Patch (100+)': [96, 100]}
        for t, (start, end) in grouping.items():
            if start <= num <= end: return t

    def size(self):
        num = diceRoll(self)
        if self.floraKind == 'Woody':
            size = {'Huge (>10m)': [1, 15], 'Large (1-10m)': [16, 45], 'Average (25cm-1m)': [46, 80],
                    'Small (5cm-25cm)': [81, 98], 'Tiny (<5cm)': [99, 100]}
        elif self.floraKind == 'Herbaceous':
            size = {'Huge (>10m)': [1, 10], 'Large (1-10m)': [11, 20], 'Average (25cm-1m)': [21, 70],
                    'Small (5cm-25cm)': [71, 95], 'Tiny (<5cm)': [96, 100]}
        elif self.floraKind == 'Algae':
            size = {'Huge (>10m)': [1, 2], 'Large (1-10m)': [3, 15], 'Average (25cm-1m)': [16, 65],
                    'Small (5cm-25cm)': [66, 85], 'Tiny (<5cm)': [86, 100]}
        elif self.floraKind == 'Fungus':
            size = {'Huge (>10m)': [1, 2], 'Large (1-10m)': [3, 11], 'Average (25cm-1m)': [12, 31],
                    'Small (5cm-25cm)': [32, 60], 'Tiny (<5cm)': [61, 100]}
        for t, (start, end) in size.items():
            if start <= num <= end: return t

    # Body Stuff
    def body(self):
        num = diceRoll(self)

        if self.floraKind == 'Woody':
            body = {'Colonial Mass': [1, 2], 'Creeper/Vine': [3, 20], 'Stem/Trunk': [21, 70],
                    'Multiple Stems/Trunks': [70, 100]}
        elif self.floraKind == 'Herbaceous':
            body = {'Colonial Mass': [1, 3], 'Creeper/Vine': [4, 35], 'Stem/Trunk': [36, 70],
                    'Multiple Stems/Trunks': [71, 100]}
        elif self.floraKind == 'Algae':
            body = {'Colonial Mass': [1, 70], 'Creeper/Vine': [71, 75], 'Stem/Trunk': [76, 85],
                    'Multiple Stems/Trunks': [86, 100]}
        elif self.floraKind == 'Fungus':
            body = {'Colonial Mass': [1, 20], 'Creeper/Vine': [21, 30], 'Stem/Trunk': [31, 70],
                    'Multiple Stems/Trunks': [71, 100]}

        for t, (start, end) in body.items():
            if start <= num <= end: return t

    def branches(self):
        num = diceRoll(self)
        if self.floraKind == 'Woody':
            branches = {'Radial': [1, 55], 'Ordered': [56, 75], 'Random': [76, 98], 'No Branches': [99, 100]}
        elif self.floraKind == 'Herbaceous':
            branches = {'Radial': [1, 45], 'Ordered': [46, 50], 'Random': [51, 85], 'No Branches': [86, 100]}
        elif self.floraKind == 'Algae':
            branches = {'Radial': [1, 25], 'Ordered': [26, 60], 'Random': [61, 90], 'No Branches': [91, 100]}
        elif self.floraKind == 'Fungus':
            branches = {'Radial': [1, 2], 'Ordered': [3, 5], 'Random': [6, 15], 'No Branches': [16, 100]}

        for t, (start, end) in branches.items():
            if start <= num <= end: return t

    def roots(self):
        num = diceRoll(self)
        if self.floraKind == 'Woody':
            roots = {'Tap': [1, 35], 'Tubers': [36, 37], 'Fibrous': [38, 84], 'Advantageous': [85, 93],
                     'Bulbous': [94, 95], 'Rhizoid': [96, 98], 'None': [99, 100]}
        elif self.floraKind == 'Herbaceous':
            roots = {'Tap': [1, 35], 'Tubers': [36, 45], 'Fibrous': [46, 63], 'Advantageous': [64, 77],
                     'Bulbous': [91, 99], 'Rhizoid': [91, 98], 'None': [99, 100]}
        elif self.floraKind == 'Algae':
            roots = {'Tap': [1, 2], 'Tubers': [3, 4], 'Fibrous': [5, 6], 'Advantageous': [7, 17], 'Bulbous': [18, 30],
                     'Rhizoid': [31, 50], 'None': [51, 100]}
        elif self.floraKind == 'Fungus':
            roots = {'Tap': [1, 3], 'Tubers': [4, 9], 'Fibrous': [10, 15], 'Advantageous': [16, 20],
                     'Bulbous': [21, 30], 'Rhizoid': [31, 90], 'None': [91, 100]}

        for t, (start, end) in roots.items():
            if start <= num <= end: return t

    def coverage(self):
        num = diceRoll(self)
        if self.floraKind == 'Woody':
            cover = {'Smooth': [0, 30], 'Waxy': [31, 40], 'Rough': [41, 70], 'Scaly': [71, 84], 'Flaky': [85, 97],
                     'Other': [98, 100]}
        elif self.floraKind == 'Herbaceous':
            cover = {'Smooth': [0, 59], 'Waxy': [60, 79], 'Rough': [80, 85], 'Scaly': [86, 90], 'Flaky': [91, 94],
                     'Other': [95, 100]}
        elif self.floraKind == 'Algae':
            cover = {'Smooth': [0, 65], 'Waxy': [65, 70], 'Rough': [71, 75], 'Scaly': [76, 82], 'Flaky': [83, 90],
                     'Other': [91, 100]}
        elif self.floraKind == 'Fungus':
            cover = {'Smooth': [0, 65], 'Waxy': [65, 70], 'Rough': [71, 75], 'Scaly': [76, 82], 'Flaky': [83, 90],
                     'Other': [91, 100]}

        for t, (start, end) in cover.items():
            if start <= num <= end: return t

    def color(self):
        num = diceRoll(self)
        color = {'Red': [1, 5], 'Orange': [7, 10], 'Yellow': [11, 20], 'Green': [21, 45], 'Blue': [46, 50],
                 'Violet': [51, 55], 'Black': [56, 60], 'Gray': [61, 65], 'White': [66, 70], 'Brown': [71, 80],
                 'Silver': [81, 85], 'Copper': [86, 90], 'Gold': [91, 95], 'Green': [96, 100]}
        for t, (start, end) in color.items():
            if start <= num <= end: return t

    def pattern(self):
        num = diceRoll(self)
        pattern = {'Spotted': [1, 10], 'Mottled': [11, 20], 'Patches': [21, 25], 'Strips': [26, 40], 'Solid': [41, 60],
                   'Phases': [61, 75], 'Translucent': [76, 80], 'Iridescent': [81, 85], 'Luminescent': [86, 90],
                   'Blushed': [91, 95], 'Solid': [96, 100]}
        for t, (start, end) in pattern.items():
            if start <= num <= end: return t

    # Leaves Stuff
    def leaves(self):
        num = diceRoll(self)

        if self.floraKind == 'Woody':
            leaves = {'Broad': [1, 55], 'Needles': [56, 70], 'Compound': [71, 94], 'Blades': [95, 96],
                      'Scales': [97, 98], 'None': [99, 100]}
        elif self.floraKind == 'Herbaceous':
            leaves = {'Broad': [1, 45], 'Needles': [46, 50], 'Compound': [51, 85], 'Blades': [86, 96],
                      'Scales': [97, 98], 'None': [99, 100]}
        elif self.floraKind == 'Algae':
            leaves = {'Broad': [1, 2], 'Needles': [3, 4], 'Compound': [4, 10], 'Blades': [11, 12], 'Scales': [13, 16],
                      'None': [16, 100]}
        elif self.floraKind == 'Fungus':
            leaves = {'Broad': [1, 25], 'Needles': [26, 50], 'Compound': [51, 60], 'Blades': [61, 80],
                      'Scales': [81, 90], 'None': [91, 100]}
        for t, (start, end) in leaves.items():
            if start <= num <= end: return t

    def leafLocation(self):
        num = diceRoll(self)
        leafLocation = {'Terminal': [1, 30], 'Branch Points': [31, 50], 'Random Interval': [51, 70],
                        'Regular Inverval': [71, 90], 'Stem/Trunk': [91, 100]}
        for t, (start, end) in leafLocation.items():
            if start <= num <= end: return t

    def leafShape(self):
        num = diceRoll(self)
        leafShape = {'Acicular (Needle-shaped)': [1, 3], 'Subulate (Awl shaped)': [4, 6],
                     'Lanceolate (Pointed at both ends)': [7, 10], 'Linear (Parallel margins,elongate)': [11, 14],
                     'Falcate (Sickle-shaped)': [15, 17], 'Spear-Shaped (Pointed barbed base)': [18, 21],
                     'Hastate (Triangular with basal lobes)': [22, 25], 'Deltoid (Triangular)': [26, 28],
                     'Rhomboid (Diamond-shaped)': [29, 32], 'Cuneate (Wedge-shaped, accute base)': [33, 35],
                     'Cordate (Heart shaped, stem in cleft)': [36, 39],
                     'Obcordate (Heart-shaped, stem at point)': [40, 43],
                     'Ovate (Egg-shaped, wide at base)': [44, 47], 'Obovate (Egg-shaped, narrow at base)': [48, 51],
                     'Acuminate (Taper to long point)': [52, 56], 'Aristate (With spine-like tip)': [56, 58],
                     'Orbicular (Circular)': [59, 61],
                     'Obtuse (Bluntly tipped)': [62, 64],
                     'Elliptic (Oval-shaped, small or no point)': [65, 67], 'Reniform (Kidney-shaped)': [68, 70],
                     'Spatulate (Spoon shaped)': [70, 72], 'Truncate (Squared off apex)': [73, 75],
                     'Flabellate (Fan-shaped)': [76, 78],
                     'Lobed (Deeply indented margins)': [79, 81], 'Pinnatisect (Deep opposite lobing)': [82, 83],
                     'Poly-Foliate (2-7 leaflets)': [84, 87],
                     'Palmate (Hand-like)': [88, 92], 'Pedate (Palmate divided lateral lobes)': [93, 96],
                     'Digitate (Finger-like lobes)': [97, 100], }
        for t, (start, end) in leafShape.items():
            if start <= num <= end: return t

    def leafMargin(self):
        num = diceRoll(self)
        leafMargins = {'Smooth': [1, 15], 'Sinuate': [16, 30], 'Undulate': [31, 40], 'Spiny': [41, 45],
                       'Lobate': [46, 55], 'Crenate': [56, 60],
                       'Dentate': [61, 70], 'Denticulate': [71, 75], 'Serate': [76, 85], 'Serrulate': [86, 90],
                       'Ciliate': [91, 95], 'Smooth': [96, 100]}
        for t, (start, end) in leafMargins.items():
            if start <= num <= end: return t

    def leafSurface(self):
        num = diceRoll(self)
        leafSurface = {'Smooth': [1, 25], 'Waxy': [26, 40], 'Scaly': [41, 55], 'Hairy': [56, 65], 'Velvety': [66, 80],
                       'Dusty': [81, 90], 'Sticky': [91, 100]}
        for t, (start, end) in leafSurface.items():
            if start <= num <= end: return t

    def leafVenation(self):
        num = diceRoll(self)
        leafVenations = {'Arcuate (Secondary veins bending toward apex)': [1, 10],
                         'Cross-Venulate (Small veins connecting secondary veins)': [11, 20],
                         'Dichotomous (Veins branching in symmetric pairs)': [21, 30],
                         'Longitudinal (Veins aligned mostly along axis of leaf)': [31, 45],
                         'Palmate (Several primary veins diverging from a point)': [46, 60],
                         'Parallel (Veins arranged axially, not intersecting)': [61, 70],
                         'Pinnate (secondary veins paired oppositely)': [71, 80],
                         'Reticulate (Smaller veins forming a network)': [81, 90], 'None': [91, 100]}
        for t, (start, end) in leafVenations.items():
            if start <= num <= end: return t

    def leafNum(self):
        num = diceRoll(self)
        leafNumbers = {'Single': [1, 20], 'Pairs': [21, 40], 'Whorls (3-5)': [41, 60], 'Clusters (6+)': [61, 100]}
        for t, (start, end) in leafNumbers.items():
            if start <= num <= end: return t

    def leafColor(self):
        num = diceRoll(self)
        color = {'Red': [1, 5], 'Orange': [7, 10], 'Yellow': [11, 20], 'Green': [21, 45], 'Blue': [46, 50],
                 'Violet': [51, 55], 'Black': [56, 60], 'Gray': [61, 65], 'White': [66, 70], 'Brown': [71, 80],
                 'Silver': [81, 85], 'Copper': [86, 90], 'Gold': [91, 95], 'Green': [96, 100]}
        for t, (start, end) in color.items():
            if start <= num <= end: return t

    def leafPattern(self):
        num = diceRoll(self)
        pattern = {'Spotted': [1, 10], 'Mottled': [11, 20], 'Patches': [21, 25], 'Strips': [26, 40], 'Solid': [41, 60],
                   'Phases': [61, 75], 'Translucent': [76, 80], 'Iridescent': [81, 85], 'Luminescent': [86, 90],
                   'Blushed': [91, 95], 'Solid': [96, 100]}
        for t, (start, end) in pattern.items():
            if start <= num <= end: return t
        # Reproduction Stuff

    # Flower/Seed Stuff
    def reproduction(self):
        num = diceRoll(self)

        if self.floraKind == 'Woody':
            reproduction = {'Seeds': [1, 80], 'Suckers': [81, 92], 'Budding/Fragmentation': [93, 98],
                            'Other means': [99, 100]}
        elif self.floraKind == 'Herbaceous':
            reproduction = {'Seeds': [1, 63], 'Suckers': [64, 85], 'Budding/Fragmentation': [86, 98],
                            'Other means': [99, 100]}
        elif self.floraKind == 'Algae':
            reproduction = {'Seeds': [1, 2], 'Suckers': [3, 6], 'Budding/Fragmentation': [7, 90],
                            'Other means': [91, 100]}
        elif self.floraKind == 'Fungus':
            reproduction = {'Seeds': [1, 89], 'Suckers': [90, 95], 'Budding/Fragmentation': [96, 98],
                            'Other means': [99, 100]}
        for t, (start, end) in reproduction.items():
            if start <= num <= end: return t

    def seeds(self):
        num = diceRoll(self)

        if self.floraKind == 'Woody':
            seeds = {'Grain': [1, 5], 'Nut': [6, 50], 'Fruit': [51, 94], 'Spore': [95, 98], 'Other': [99, 100]}
        elif self.floraKind == 'Herbaceous':
            seeds = {'Grain': [1, 40], 'Nut': [41, 45], 'Fruit': [46, 80], 'Spore': [81, 98], 'Other': [99, 100]}
        elif self.floraKind == 'Algae':
            seeds = {'Grain': [1, 2], 'Nut': [3, 4], 'Fruit': [5, 6], 'Spore': [7, 90], 'Other': [91, 100]}
        elif self.floraKind == 'Fungus':
            seeds = {'Grain': [1, 2], 'Nut': [3, 4], 'Fruit': [5, 6], 'Spore': [7, 90], 'Other': [91, 100]}
        for t, (start, end) in seeds.items():
            if start <= num <= end: return t

    def primaryDispersal(self):
        num = diceRoll(self)

        if self.seed == 'Grain':
            dispersal = {'Animal': [1, 20], 'Wind': [21, 40], 'Water': [41, 60], 'Gravity': [61, 98],
                         'Other': [99, 100]}
        elif self.seed == 'Nut':
            dispersal = {'Animal': [1, 45], 'Wind': [46, 53], 'Water': [54, 60], 'Gravity': [61, 98],
                         'Other': [99, 100]}
        elif self.seed == 'Fruit':
            dispersal = {'Animal': [1, 60], 'Wind': [61, 65], 'Water': [66, 85], 'Gravity': [86, 98],
                         'Other': [99, 100]}
        elif self.seed == 'Spore':
            dispersal = {'Animal': [1, 40], 'Wind': [41, 83], 'Water': [84, 90], 'Gravity': [91, 98],
                         'Other': [99, 100]}
        elif self.seed == 'Other':
            dispersal = {'Animal': [1, 40], 'Wind': [41, 83], 'Water': [84, 90], 'Gravity': [91, 98],
                         'Other': [99, 100]}

        for t, (start, end) in dispersal.items():
            if start <= num <= end: return t

    def flowertype(self):
        num = diceRoll(self)

        if self.seed == 'Grain':
            flower = {'None': [1, 2], 'Single': [3, 5], 'Pairs': [6, 1], 'Bunches': [11, 30], 'Compound': [31, 50],
                      'Spray': [51, 90], 'Other': [91, 100]}
        elif self.seed == 'Nut':
            flower = {'None': [1, 2], 'Single': [3, 40], 'Pairs': [41, 60], 'Bunches': [61, 80], 'Compound': [81, 90],
                      'Spray': [91, 95],
                      'Other': [96, 100]}
        elif self.seed == 'Fruit':
            flower = {'None': [1, 3], 'Single': [4, 30], 'Pairs': [31, 60], 'Bunches': [61, 70], 'Compound': [71, 80],
                      'Spray': [81, 90],
                      'Other': [91, 100]}
        elif self.seed == 'Spore':
            flower = {'None': [1, 40], 'Single': [41, 50], 'Pairs': [51, 60], 'Bunches': [61, 70], 'Compound': [71, 80],
                      'Spray': [81, 90],
                      'Other': [91, 100]}
        elif self.seed == 'Other':
            flower = {'None': [1, 10], 'Single': [11, 20], 'Pairs': [21, 30], 'Bunches': [31, 50], 'Compound': [51, 70],
                      'Spray': [71, 90],
                      'Other': [91, 100]}

        for t, (start, end) in flower.items():
            if start <= num <= end: return t

    def flowerShape(self):
        num = diceRoll(self)
        if self.flower == "Single":
            flowerShape = {'Funnel': [1, 18], 'Spike': [19, 20], 'Disc': [21, 40], 'Cone': [41, 60], 'Bell': [61, 85],
                           'Sphere': [86, 90], 'Complex': [91, 100]}
        elif self.flower == "Pairs":
            flowerShape = {'Funnel': [1, 20], 'Spike': [21, 25], 'Disc': [26, 30], 'Cone': [31, 45], 'Bell': [46, 80],
                           'Sphere': [81, 90],
                           'Complex': [91, 100]}
        elif self.flower == "Bunches":
            flowerShape = {'Funnel': [1, 10], 'Spike': [11, 30], 'Disc': [31, 50], 'Cone': [51, 70], 'Bell': [71, 90],
                           'Sphere': [91, 95],
                           'Complex': [96, 100]}
        elif self.flower == "Compound":
            flowerShape = {'Funnel': [1, 3], 'Spike': [4, 25], 'Disc': [26, 50], 'Cone': [51, 70], 'Bell': [71, 80],
                           'Sphere': [81, 95],
                           'Complex': [96, 100]}
        elif self.flower == "Spray":
            flowerShape = {'Funnel': [1, 10], 'Spike': [11, 15], 'Disc': [16, 25], 'Cone': [26, 40], 'Bell': [41, 80],
                           'Sphere': [81, 90],
                           'Complex': [91, 100]}
        elif self.flower == "Other":
            flowerShape = {'Funnel': [1, 15], 'Spike': [16, 30], 'Disc': [31, 45], 'Cone': [46, 60], 'Bell': [61, 75],
                           'Sphere': [76, 90],
                           'Complex': [91, 100]}

        for t, (start, end) in flowerShape.items():
            if start <= num <= end: return t

    def flowerSize(self):
        num = diceRoll(self)
        flowerSize = {'Tiny (<5mm)': [1, 10], 'Small (5-10mm)': [11, 40], 'Average (1-5cm)': [41, 80],
                      'Large (5-10cm)': [81, 95], 'Huge (>10cm)': [96, 100]}
        for t, (start, end) in flowerSize.items():
            if start <= num <= end: return t

    def petalShape(self):
        num = diceRoll(self)
        shapes = {'Round': [1, 10], 'Curly': [11, 25], 'Wavy': [26, 40], 'Toothed': [41, 50], 'Oval': [51, 65],
                  'Blade': [66, 80], 'Thread': [81, 85], 'Feathery': [86, 100]}
        for t, (start, end) in shapes.items():
            if start <= num <= end: return t

    def petalNumber(self):
        num = diceRoll(self)
        numbers = {'No Petals': [1, 10], multiDiceRoll(self, 1, 6): [11, 30], multiDiceRoll(self, 3, 4): [31, 60],
                   multiDiceRoll(self, 4, 6): [61, 90], multiDiceRoll(self, 5, 20): [91, 100]}
        for t, (start, end) in numbers.items():
            if start <= num <= end: return t

    def petalSurface(self):
        num = diceRoll(self)
        petalSurface = {'Smooth': [1, 15], 'Waxy': [16, 30], 'Scaly': [31, 40], 'Hairy': [41, 45], 'Velvety': [46, 60],
                        'Dusty': [61, 80], 'Sticky': [81, 89], 'Veined': [90, 100]}
        for t, (start, end) in petalSurface.items():
            if start <= num <= end: return t

    def flowerLocation(self):
        num = diceRoll(self)
        flowerLoc = {'Terminal': [1, 30], 'Branch Points': [31, 50], 'Random Interval': [51, 70],
                     'Regular Inverval': [71, 90], 'Stem/Trunk': [91, 100]}
        for t, (start, end) in flowerLoc.items():
            if start <= num <= end: return t

    def flowerScent(self):
        num = diceRoll(self)
        flowerScent = {'None': [1, 10], 'Sweet': [11, 60], 'Musky': [61, 80], 'Foul': [81, 95], 'Other': [96, 100]}
        for t, (start, end) in flowerScent.items():
            if start <= num <= end: return t

    def flowerFrequency(self):
        num = diceRoll(self)
        flowerFreq = {'Annual (Once)': [1, 40], 'Poly-Annual (2-7 Years)': [41, 60], 'Perennial (Yearly)': [61, 90],
                      'Other': [91, 100]}
        for t, (start, end) in flowerFreq.items():
            if start <= num <= end: return t

    def flowerColor(self):
        num = diceRoll(self)
        color = {'Red': [1, 5], 'Orange': [7, 10], 'Yellow': [11, 20], 'Green': [21, 45], 'Blue': [46, 50],
                 'Violet': [51, 55], 'Black': [56, 60], 'Gray': [61, 65], 'White': [66, 70], 'Brown': [71, 80],
                 'Silver': [81, 85], 'Copper': [86, 90], 'Gold': [91, 95], 'Green': [96, 100]}
        for t, (start, end) in color.items():
            if start <= num <= end: return t

    def flowerPattern(self):
        num = diceRoll(self)
        flowerPatter = {'Spotted': [1,8 ], 'Mottled': [9,13 ], 'Patches': [14,20 ], 'Stripes': [21,30 ], 'Solid': [31,50 ],
                        'Phases': [51,55 ], 'Translucent': [56,60 ], 'Iridescent': [61,65 ], 'Luminescent': [66,70 ], 'Blushed': [71,80 ],
                        'Mimicry': [85,89 ], 'Night Blooming': [90,95 ], 'Night Closing': [96,100 ]}
        for t, (start, end) in flowerPatter.items():
            if start <= num <= end: return t

    def stamens(self):
        num = diceRoll(self)
        stamens = {'None':[1,10],'1-3':[11,30],'4-9':[31,70],'10+':[71,100]}
        for t, (start, end) in stamens.items():
            if start <= num <= end: return t

        # Flora Survival Stuff

    def pistils(self):
        num = diceRoll(self)
        pistils = {'None':[1,20],'1':[21,40],'2-4':[41,75],'5+':[76,100]}
        for t, (start, end) in pistils.items():
            if start <= num <= end: return t

        # Sentience

    def dietType(self):
        num = diceRoll(self)

        if self.floraKind == 'Woody':
             dietType = {'Photosynthetic / Chemosynthetic':[1,89],'Predaceous':[90,91],'Decay':[92,96],'Parasitic':[97,98],'Symbiotic':[99,100]}
        elif self.floraKind == 'Herbaceous':
            dietType = {'Photosynthetic / Chemosynthetic': [1,85 ], 'Predaceous': [86,87 ], 'Decay': [88,93 ], 'Parasitic': [94,97 ],
                        'Symbiotic': [98,100 ]}
        elif self.floraKind == 'Algae':
            dietType = {'Photosynthetic / Chemosynthetic': [1,90 ], 'Predaceous': [91,92 ], 'Decay': [93,94 ], 'Parasitic': [95,98 ],
                        'Symbiotic': [99,100 ]}
        elif self.floraKind == 'Fungus':
            dietType = {'Photosynthetic / Chemosynthetic': [1,5 ], 'Predaceous': [6,8 ], 'Decay': [9,90 ], 'Parasitic': [95,98 ],
                        'Symbiotic': [99,100 ]}
        for t, (start, end) in dietType.items():
            if start <= num <= end: return t

    def tropism(self):
        num = diceRoll(self)

        if self.floraKind == 'Woody':
            tropism = {'None':[1,2],'Gravity':[3,55],'Light':[56,83],'Heat':[84,87],'Touch':[88,96],'Motile':[97,98],'Mobile':[99,100]}
        elif self.floraKind == 'Herbaceous':
            tropism = {'None': [1,5 ], 'Gravity': [6,40 ], 'Light': [41,82 ], 'Heat': [83,87 ], 'Touch': [88,96 ], 'Motile': [97,98 ],
                       'Mobile': [99,100 ]}
        elif self.floraKind == 'Algae':
            tropism = {'None': [1,20 ], 'Gravity': [21,35 ], 'Light': [36,70 ], 'Heat': [71,85 ], 'Touch': [86,90 ], 'Motile': [91,95 ],
                       'Mobile': [96,100 ]}
        elif self.floraKind == 'Fungus':
            tropism = {'None': [1,30 ], 'Gravity': [31,70 ], 'Light': [71,80 ], 'Heat': [81,90 ], 'Touch': [91,96 ], 'Motile': [97,98 ],
                       'Mobile': [99,100 ]}
        for t, (start, end) in tropism.items():
            if start <= num <= end: return t

    def sentience(self):
        num = diceRoll(self)

        sentience = {'Non-Sentient':[1,98],'Sentient':[99,100]}
        for t, (start, end) in sentience.items():
            if start <= num <= end: return t

    def sentienceType(self):
        num = diceRoll(self)
        sentType = {'Instinctual':[1,75],'Hive':[76,79],'Animal':[80,89],'Cunning Animal':[90,98],'Sapient':[99,100]}
        for t, (start, end) in sentType.items():
            if start <= num <= end: return t

        # Flora Uses

    def edibility(self):
        num = diceRoll(self)

        if self.floraKind == 'Woody':
            edibility= {'Non-Edible':[1,40],'Edible':[41,65],'Nutritious/Tasty':[66,80],'Medicinal/Other':[81,100]}
        elif self.floraKind == 'Herbaceous':
            edibility = {'Non-Edible': [1,15 ], 'Edible': [16,45 ], 'Nutritious/Tasty': [46,60 ], 'Medicinal/Other': [61,100 ]}
        elif self.floraKind == 'Algae':
            edibility = {'Non-Edible': [1,60 ], 'Edible': [61,85 ], 'Nutritious/Tasty': [86,90 ], 'Medicinal/Other': [91,100 ]}
        elif self.floraKind == 'Fungus':
            edibility = {'Non-Edible': [1,30 ], 'Edible': [31,60 ], 'Nutritious/Tasty': [61,86 ], 'Medicinal/Other': [85,100 ]}
        for t, (start, end) in edibility.items():
            if start <= num <= end: return t

    def edibilityPrep(self):
        num = diceRoll(self)
        if self.edibilities == "Edible":
            prep= {'Raw':[1,15],'Roasted':[16,30],'Boiled':[31,50],'Ground':[51,60],'Steeped':[61,75],'Blanched':[76,85],'Dried':[86,100]}
        elif self.edibilities == "Nutritious/Tasty":
            prep = {'Raw': [1,30 ], 'Roasted': [31,45 ], 'Boiled': [46,55 ], 'Ground': [56,65 ], 'Steeped': [66,75 ], 'Blanched': [76,80 ],
                    'Dried': [81,100 ]}
        for t, (start, end) in prep.items():
            if start <= num <= end: return t

    def medicinalProperties(self):
        # Random number of rolls
        #Write a regex to parse it for you
        #mult roll times two, and give each
        num = diceRoll(self)
        medProp= {}
        for t, (start, end) in medProp.items():
            if start <= num <= end: return t

    def medicinalPrep(self):
        # number of rolls based on properties for each type
        num = diceRoll(self)
        medPrep= {}
        for t, (start, end) in medPrep.items():
            if start <= num <= end: return t
