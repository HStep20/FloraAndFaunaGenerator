from .fauna_tables import *
from rollInterface import *
import random


class Fauna(object):
    rounding = 2
    def __init__(self):
        self.skeleton = ""
        self.body_temperature = ""
        self.habitat = {}
        self.diet = ""
        self.social_type = ""
        self.temperament = ""
        self.territoriality = ""
        self.body_physical = {}
        self.body_features = {}
        self.body_appearance = {}
        self.sentience = {}
        self.reproduction = {}

    def generate(self):
        self.skeleton = select(skeletal_table)
        self._generate_body_temperature()
        self._generate_habitat()
        self.diet = select(diet)
        self.social_type = select(social_type[self.diet])
        self.temperament = select(temperament[self.diet])
        self.territoriality = select(territoriality[self.social_type])
        self._generate_physical_body()
        self._generate_body_features()
        self._generate_body_appearance()
        self._generate_sentience()
        self._generate_reproduction()

    def _generate_body_temperature(self):
        if self.skeleton == "Exoskeleton":
            self.body_temperature = select(temperature_table, .30)
            return
        elif self.skeleton == "Muscoskeleton":
            self.body_temperature = select(temperature_table, .20)
            return
        self.body_temperature = select(temperature_table)

    def _generate_habitat(self):
        self.habitat["primary"] = select(habitat_table[self.body_temperature], -0.05 * gravity)
        if self.habitat["primary"] == "Aquatic":
            self.habitat["sub"] = select(subhabitat_table["Aquatic"])
        else:
            self.habitat["sub"] = select(subhabitat_table["Other"])

    def _generate_physical_body(self):
        self.body_physical["mass"] = select(body_mass[self.body_temperature][self.skeleton])
        if self.body_physical["mass"] == "Tiny" or self.body_physical["mass"] == "Miniscule":
            self.rounding = 4
        self.body_physical["massKG"] = \
            round(random.uniform(body_mass_kg[self.body_physical["mass"]]["min"],
                                 body_mass_kg[self.body_physical["mass"]]["max"]), self.rounding)
        self.body_physical["symmetry"] = select(body_symmetry[self.skeleton])
        self.body_physical["frame"] = select(body_frame[self.diet])
        self.body_physical["shape"] = select(body_shape[self.skeleton])
        self.body_physical["bmi"] = body_mass_index[self.body_physical["shape"]][self.body_physical["frame"]]
        self.body_physical["body_length"] = round(
            (int(self.body_physical["massKG"]) / self.body_physical["bmi"]) ** (1 / 3), self.rounding)

    def _generate_body_features(self):
        self.body_features["neck"] = select(head[self.skeleton])
        if self.body_features["neck"] != "No Neck":
            self.body_features["neck_length_percent"] = \
                round(random.uniform(neck[self.body_features["neck"]]["min"],
                                     neck[self.body_features["neck"]]["max"]), self.rounding)
            self.body_features["neck_length"] = \
                round((self.body_physical["body_length"] * self.body_features["neck_length_percent"]), self.rounding)
        self.body_features["eyes"] = select(eyes[self.skeleton])
        self.body_features["limbs"] = select(limbs[self.skeleton])
        self.body_features["tail"] = select(tail[self.skeleton])
        if self.habitat == "Aquatic":
            self.body_features["flight"] = select(flight)
        elif self.habitat == "Avian":
            self.body_features["swimming"] = select(swimming)
        self.body_features["limb_length"] = select(limb_length[self.diet])
        self.body_features["limb_length_meters"] = \
            round(
                (random.uniform(limb_length_percent[self.body_features["limb_length"]]["min"],
                                limb_length_percent[self.body_features["limb_length"]]["max"])
                  * self.body_physical["body_length"])
                , self.rounding)
        self.body_features["appendages"] = select(appendages[self.skeleton][self.diet])

    def _generate_body_appearance(self):
        self.body_appearance["coverage"] = select(body_coverage[self.body_temperature][self.skeleton])
        self.body_appearance["coloration"] = select(coloration[self.body_appearance["coverage"]])
        self.body_appearance["pattern"] = select(pattern)

    def _generate_sentience(self):
        self.sentience["sentience"] = select(sentience[self.body_temperature][self.diet])
        if self.sentience == "Hive":
            self.sentience["hivemind"] = select(sentience_of_hive_mind[self.diet][self.sentience["sentience"]])

    def _generate_reproduction(self):
        self.reproduction["sexual_type"] = select(sexual_type)
        self.reproduction["reproduction_style"] = select(reproduction[self.body_temperature])

    def __str__(self):
        # todo - add neck part, if nex exists. Add tail part if tail exists, hivemind sentient, if it exists
        return \
                "'name' is a %s %s with a %s which can often be found living in a %s habitat, and occasionally found in %s.\n" \
                %(self.body_temperature, self.diet, self.skeleton, self.habitat["primary"], self.habitat["sub"]) + \
                "These %s minded, %s animals live a %s lifestyle, and are often %s towards other animals.\n" \
                %(self.sentience["sentience"], self.social_type, self.territoriality, self.temperament) + \
                "They are %s beasts, often measuring %s meters on average and weighing in at %s kilograms.\n"\
                %(self.body_physical["mass"],  self.body_physical["body_length"], self.body_physical["massKG"]) + \
                "It's %s framed, %s shaped body has a %s symmetry to it.\n"\
                % (self.body_physical["frame"], self.body_physical["shape"], self.body_physical["symmetry"]) + \
                "They have %s styled eyes on their head, with a %s reaching %s meters on average.\n"\
                % (self.body_features["eyes"], self.body_features["neck"], self.body_features["neck_length"]) + \
                "They have %s %s %s styled appendages which average at %s meters long.\n" \
                % (self.body_features["limbs"], self.body_features["limb_length"], self.body_features["appendages"], self.body_features["limb_length_meters"]) + \
                "They have a %s, %s body with a %s coverage.\n"\
                % (self.body_appearance["coloration"], self.body_appearance["pattern"], self.body_appearance["coverage"]) + \
                "Their mating preference is %s and they reproduce via %s\n"\
                % (self.reproduction["sexual_type"], self.reproduction["reproduction_style"])