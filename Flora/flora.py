from rollInterface import *
from .flora_tables import *


class Flora(object):
    def __init__(self):
        self.type = ""
        self.habitat = {}
        self.grouping = ""
        self.size = ""
        self.body = {}
        self.leaves = {}
        self.reproduction = {}
        self.diet = {}
        self.sentience = ""
        self.edibility = {}

    def generate(self):
        # Table 1
        self.type = select(type_table)
        # Table 2*
        self._generate_habitat()
        # Table 3
        self.grouping = select(grouping_table[self.type])
        # Table 4
        self.size = select(size_table[self.type])
        # Table 5*
        self._generate_body()
        # Table 6*
        self._generate_leaves()
        # Table 7*
        self._generate_reproduction()
        # Table 8
        self.diet["type"] = select(diet_table[self.type])
        # Table 8a
        self.diet["tropism"] = select(tropism_table[self.type])
        # Table 9*
        self._generate_sentience()
        # Table 10*
        self._generate_edibility()

    def _generate_habitat(self):
        # Table 2
        self.habitat["primary"] = \
            select(habitat_table[self.type], -0.05 * gravity)
        # Table 2a, 2b
        self.habitat["sub"] = {}
        if self.habitat["primary"] == "Aquatic":
            # Table 2a
            self.habitat["sub"]["type"] = select(subhabitat_table["Aquatic"])
        else:
            # Table 2b
            if random() <= 0.10:
                # 10% chance of two subhabitats
                self.habitat["sub"] = roll_twice(subhabitat_table["Other"])
                self.habitat["sub"][0] = {"type": self.habitat["sub"][0]}
                self.habitat["sub"][1] = {"type": self.habitat["sub"][1]}
            else:
                self.habitat["sub"]["type"] = select( \
                    subhabitat_table["Other"])
        # Table 2c
        if type(self.habitat["sub"]) is list:
            self.habitat["sub"][0]["rarity"] = select(rarity_table)
            self.habitat["sub"][1]["rarity"] = select(rarity_table)
        else:
            self.habitat["sub"]["rarity"] = select(rarity_table)

    def _generate_body(self):
        # Table 5
        self.body["main"] = select(body_table[self.type])
        # Table 5a
        self.body["branches"] = select(branches_table[self.type])
        # Table 5b
        self.body["roots"] = select(roots_table[self.type])
        # Table 5c
        self.body["main"] = {"type": self.body["main"], \
                             "surface": select(body_surface_table[self.type])}
        if self.body["branches"] != "None":
            self.body["branches"] = {"type": self.body["branches"], \
                                     "surface": select(body_surface_table[self.type])}
        if self.body["roots"] != "None":
            self.body["roots"] = {"type": self.body["roots"], \
                                  "surface": select(body_surface_table[self.type])}
        # Table 5d
        self.body["main"]["color"] = select(color_table)
        self.body["main"]["pattern"] = select(pattern_table)
        if self.body["branches"] != "None":
            self.body["branches"]["color"] = select(color_table)
            self.body["branches"]["pattern"] = select(pattern_table)

        if self.body["roots"] != "None":
            self.body["roots"]["color"] = select(color_table)
            self.body["roots"]["pattern"] = select(pattern_table)

    def _generate_leaves(self):
        # Table 6
        self.leaves["type"] = select(leaves_table[self.type])
        # Table 6a+
        self.leaves = account_for_two(self.leaves, self.__get_random_leaf_of_type)

    def __get_random_leaf_of_type(self, type):
        leaf = {"type": type}
        # Table 6a
        if self.type == "Fungus":
            leaf["location"] = "Terminal"
        else:
            leaf["location"] = select(leaf_location_table)
        # Table 6b
        leaf["shape"] = select(leaf_shape_table)
        leaf["margin"] = select(leaf_margin_table)
        # Table 6c
        leaf["surface_topside"] = select(leaf_surface_table)
        leaf["surface_underside"] = select(leaf_surface_table)
        # Table 6d
        leaf["venation"] = select(leaf_venation_table)
        leaf["numbers"] = select(leaf_numbers_table)
        leaf["color"] = select(color_table)
        leaf["pattern"] = select(pattern_table)
        return leaf

    def _generate_reproduction(self):
        # Table 7
        self.reproduction["type"] = select(reproduction_table[self.type])
        if "Seeds" not in self.reproduction["type"]:
            return
        # Table 7a
        self.reproduction["seed_type"] = select(seeds_table[self.type])
        # Table 7b
        self.reproduction["seed_dispersal"] = \
            select(seed_dispersal_table[self.reproduction["seed_type"]])
        # Table 7c
        self.reproduction["flower_type"] = \
            select(flower_table[self.reproduction["seed_type"]])
        if self.reproduction["flower_type"] == "None":
            return
        # Table 7d
        self.reproduction["flower_shape"] = select(
            flower_shape_table[self.reproduction["flower_type"]])
        # Table 7e
        self.reproduction["flower_size"] = select(flower_size_table)
        # Table 7f
        self.reproduction["petal_number"] = \
            roll_dice(select(petal_number_table))
        if self.reproduction["petal_number"] > 0:
            self.reproduction["petal_shape"] = select(petal_shape_table)
            # Table 7g
            self.reproduction["petal_surface_inside"] = \
                select(petal_surface_table)
            self.reproduction["petal_surface_outside"] = \
                select(petal_surface_table)
        # Table 7h
        self.reproduction["flower_location"] = select(flower_location_table)
        # Table 7i
        self.reproduction["flower_scent"] = select(flower_scent_table)
        # Table 7j
        modifier = 0
        if self.type == "Woody":
            modifier = 0.15
        self.reproduction["flower_frequency"] = \
            select(flower_frequency_table, modifier)
        # Table 7k
        self.reproduction["flower_color"] = select(flower_color_table)
        # Table 7l
        self.reproduction["flower_stamens"] = select(flower_stamens_table)
        self.reproduction["flower_pistils"] = select(flower_pistils_table)

    def _generate_sentience(self):
        # Table 9
        roll = random() + 0.05 * aura
        if self.diet["tropism"] == "Motile":
            roll += 0.10
        elif self.diet["tropism"] == "Mobile":
            roll += 0.20
        if roll <= sentience_chance[self.diet["type"]]:
            self.sentience = "Non-Sentient"
            return
        # Table 9a
        modifier = 0.05 * aura
        if self.diet["type"] == "Symbiotic":
            modifier += 0.05
        elif self.diet["type"] == "Predaceous":
            modifier += 0.10
        self.sentience = select(sentience_table, modifier)
        if self.sentience == "Hive":
            self.sentience = [self.sentience, select(sentience_table, modifier)]

    def _generate_edibility(self):
        # Table 10
        self.edibility["type"] = select(edibility_table[self.type])
        # Table 10a+
        self.edibility = account_for_two(self.edibility,
                                         self.__get_random_use_of_type)

    def __get_random_use_of_type(self, type):
        # Table 10a
        use = {"type": type}
        if type == "Edible" or type == "Nutritious / Tasty":
            use["preparation"] = \
                select(edible_preparation_table[type])
        # Table 10b+
        if type == "Medicinal":
            # Table 10b
            use["property"] = select(medicinal_properties_table)
            # Table 10c
            use["preparation"] = select(medicinal_preparation_table)
        return use

    def to_string(self):
        formattedOutput = "This %s, %s flora is a %s sized, %s plant.\n" % (
        self.edibility["type"], self.sentience, self.size, self.type)
        if self.edibility["type"] == "Medicinal":
            formattedOutput += "It can be used as %s medicine by creating a %s out of it.\n" % (
            self.edibility["property"], self.edibility["preparation"])
        elif self.edibility["type"] == "Edible":
            formattedOutput += "It can be eaten safely by %s preparation.\n" % (self.edibility["preparation"])
        formattedOutput += "It can primarily be found in a %s environment, and also %sly be found in a %s environment\n" \
                           % (self.habitat["primary"], self.habitat["sub"]["rarity"], self.habitat["sub"]["type"]) + \
                           "It has a %s based diet utilizing %s.\n" % (self.diet["type"], self.diet["tropism"])
        return "GENERAL:\n" + formattedOutput + "BODY:\n" + self._body_to_string() + \
               "LEAVES:\n" + self._leaves_to_string() + "REPRODUCTION:\n" + self._reproduction_to_string()

    def _body_to_string(self):
        formattedOutput = ""
        if self.body["roots"] != "None":
            formattedOutput += "The %s surfaced, %s %s roots have a %s pattern to them. \n" % (
            self.body["roots"]["surface"], self.body["roots"]["color"], self.body["roots"]["type"],
            self.body["roots"]["pattern"])
        else:
            formattedOutput += "The plant has no branches.\n"

        if self.body["main"] != "None":
            formattedOutput += "The %s surfaced, %s %s-like body has a %s pattern to it. \n" % (
            self.body["main"]["surface"], self.body["main"]["color"], self.body["main"]["type"],
            self.body["main"]["pattern"])
        else:
            formattedOutput += "The plant has no main body structure.\n"

        if self.body["branches"] != "None":
            formattedOutput += "The %s surfaced, %s %s branches have a %s growing pattern to them. \n" % (
            self.body["branches"]["surface"], self.body["branches"]["color"], self.body["branches"]["type"],
            self.body["branches"]["pattern"])
        else:
            formattedOutput += "The plant has no roots.\n"
        return formattedOutput

    def _leaves_to_string(self):
        formattedOutput = ""
        if self.leaves != None:
            formattedOutput += "It's %s, %s leaves are %s shaped and grow in %s at the %s of the plant.\n" % (
                self.leaves["color"], self.leaves["type"], self.leaves["shape"], self.leaves["numbers"],
                self.leaves["location"]) + \
                               "They have a %s pattern, a %s topside, and %s underside with a %s margin around the edge of the leaf.\n" \
                               % (
                                   self.leaves["pattern"], self.leaves["surface_topside"],
                                   self.leaves["surface_underside"],
                                   self.leaves["margin"]) + \
                               "The veins in the leaf are of a %s pattern.\n" % (self.leaves["venation"])
        else:
            formattedOutput += "The plant has no leaves.\n"
        return formattedOutput

    def _reproduction_to_string(self):
        formattedOutput = ""
        if self.reproduction["type"] == "Seeds":
            formattedOutput += \
                "The %s, %s %s shaped flowers grow in %s at the %s of the branches.\n" \
                % (
                    self.reproduction["flower_size"], self.reproduction["flower_color"],
                    self.reproduction["flower_shape"],
                    self.reproduction["flower_type"], self.reproduction["flower_location"]) + \
                "They have %s blooming, %s smelling flowers with %s pistils and %s stamens.\n" \
                % (self.reproduction["flower_frequency"], self.reproduction["flower_scent"],
                   self.reproduction["flower_pistils"],
                   self.reproduction["flower_stamens"])

            if self.reproduction["petal_number"] > 0:
                formattedOutput += \
                    "Each flower consists of %s %s shaped petals with a %s inside and %s outside.\n" \
                    % (self.reproduction["petal_number"], self.reproduction["petal_shape"],
                       self.reproduction["petal_surface_inside"], self.reproduction["petal_surface_outside"])

            formattedOutput += "It reproduces with seeds from %s and uses %s to disperse them.\n" % (
                self.reproduction["seed_type"], self.reproduction["seed_dispersal"])
        else:
            formattedOutput += "It has no flowers, so it reproduces through %s" % (self.reproduction["type"])
        return formattedOutput
