"""
Credits:
Random Flora Tables v1.1 by Sebastian Romu
https://blog.entorais.world/2016/08/02/random-animals/

"""

# Table 1
skeletal_table = {
    'Endoskeleton': .80,
    'Exoskeleton': .95,
    'Muscoskeleton': 1
}
temperature_table = {
    'Warm Blooded': .45,
    'Cold Blooded': 1
}

# Table 2
habitat_table = {
    'Warm Blooded': {
        'Aquatic': .2,
        'Subterranean': .35,
        'Terrestrial': .79,
        'Avian': 1
    },
    'Cold Blooded': {
        'Aquatic': .4,
        'Subterranean': .5,
        'Terrestrial': .89,
        'Avian': 1
    }
}
# tables 2a, 2b
subhabitat_table = {
    "Aquatic":
        {"Salt-Water": 0.40, "Fresh Water": 0.80, "Brackish": 1},
    "Other":
        {"Desert / Waste": 0.10, "Plains / Savannah": 0.32,
         "Marsh / Swamp / Bog": 0.37, "Forest / Jungle": 0.68,
         "Hills / Scrub": 0.75, "Mountains": 0.85, "Tundra": 1}
}
# table 3
diet = {
    "Carnivore": .30,
    "Omnivore": .55,
    "Herbivore": 1
}
"""
    "Scavenger": .95,
    "Parasitic": .97,
    "Symbiotic": 1
"""

# table 3a
social_type = {
    "Carnivore": {
        "Solitary": .40,
        "Small Group": .80,
        "Medium Group": .95,
        "Large Group": .99,
        "Huge Group": 1
    },
    "Omnivore": {
        "Solitary": .30,
        "Small Group": .75,
        "Medium Group": .90,
        "Large Group": .99,
        "Huge Group": 1

    },
    "Herbivore": {
        "Solitary": .10,
        "Small Group": .40,
        "Medium Group": .75,
        "Large Group": .98,
        "Huge Group": 1
    }
}
"""
    "Parasitic": {
        "Solitary": .3,
        "Small Group": .85,
        "Medium Group": .89,
        "Large Group": .96,
        "Huge Group": 1
    },
    "Symbiotic": {
        "Solitary": .50,
        "Small Group": .85,
        "Medium Group": .98,
        "Large Group": .99,
        "Huge Group": 1
    }
"""
# table 3b
temperament = {
    "Carnivore": {
        "Hostile": .15,
        "Aggressive": .70,
        "Friendly": .80,
        "Wary": .97,
        "Skittish": .99,
        "Oblivious": 1
    },
    "Omnivore": {
        "Hostile": .05,
        "Aggressive": .30,
        "Friendly": .70,
        "Wary": .90,
        "Skittish": .98,
        "Oblivious": 1

    },
    "Herbivore": {
        "Hostile": .02,
        "Aggressive": .08,
        "Friendly": .30,
        "Wary": .50,
        "Skittish": .95,
        "Oblivious": 1

    },
    "Parasitic": {
        "Hostile": .01,
        "Aggressive": .10,
        "Friendly": .12,
        "Wary": .15,
        "Skittish": .40,
        "Oblivious": 1
    },
    "Symbiotic": {
        "Hostile": .05,
        "Aggressive": .30,
        "Friendly": .55,
        "Wary": .70,
        "Skittish": .95,
        "Oblivious": 1
    }
}
# table 3c
territoriality = {
    "Solitary": {
        "Nomadic": .15,
        "Migratory": .30,
        "Range": .60,
        "Hive/Nest/Den": 1
    },
    "Small Group": {
        "Nomadic": .35,
        "Migratory": .50,
        "Range": .75,
        "Hive/Nest/Den": 1
    },
    "Medium Group": {
        "Nomadic": .25,
        "Migratory": .50,
        "Range": .75,
        "Hive/Nest/Den": 1
    },
    "Large Group": {
        "Nomadic": .10,
        "Migratory": .35,
        "Range": .80,
        "Hive/Nest/Den": 1
    },
    "Huge Group": {
        "Nomadic": .05,
        "Migratory": .60,
        "Range": .95,
        "Hive/Nest/Den": 1
    }
}

# Table 4
body_mass = {
    "Warm Blooded": {
        "Endoskeleton": {
            "Huge": .05,
            "Large": .20,
            "Average": .70,
            "Small": .95,
            "Tiny": .98,
            "Miniscule": 1
        },
        "Exoskeleton": {
            "Huge": .03,
            "Large": .25,
            "Average": .45,
            "Small": .70,
            "Tiny": .90,
            "Miniscule": 1
        },
        "Muscoskeleton": {
            "Huge": .01,
            "Large": .20,
            "Average": .50,
            "Small": .70,
            "Tiny": .90,
            "Miniscule": 1
        }
    },
    "Cold Blooded": {
        "Endoskeleton": {
            "Huge": .03,
            "Large": .15,
            "Average": .55,
            "Small": .85,
            "Tiny": .98,
            "Miniscule": 1
        },
        "Exoskeleton": {
            "Huge": .02,
            "Large": .15,
            "Average": .30,
            "Small": .50,
            "Tiny": .80,
            "Miniscule": 1
        },
        "Muscoskeleton": {
            "Huge": .01,
            "Large": .20,
            "Average": .50,
            "Small": .70,
            "Tiny": .90,
            "Miniscule": 1
        }
    }
}
body_mass_kg = {
    "Huge": {"min": 1000, "max": 10000},
    "Large": {"min": 100, "max": 1000},
    "Average": {"min": 10, "max": 100},
    "Small": {"min": .1, "max": 10},
    "Tiny": {"min": .001, "max": .1},
    "Miniscule": {"min": 0, "max": .001}
}
# Table 4a
body_symmetry = {
    "Endoskeleton": {
        "Linear": .97,
        "Radial": .99,
        "Torsional": 1
    },
    "Exoskeleton": {
        "Linear": .80,
        "Radial": .95,
        "Torsional": 1
    },
    "Muscoskeleton": {
        "Linear": .20,
        "Radial": .40,
        "Torsional": 1
    }
}
# Table 4b
body_frame = {
    "Carnivore": {
        "Scant": .10,
        "Light": .50,
        "Average": .80,
        "Heavy": .95,
        "Massive": 1
    },
    "Omnivore": {
        "Scant": .10,
        "Light": .30,
        "Average": .70,
        "Heavy": .90,
        "Massive": 1

    },
    "Herbivore": {
        "Scant": .05,
        "Light": .20,
        "Average": .55,
        "Heavy": .90,
        "Massive": 1
    }
}
# Table 4c
body_shape = {
    "Endoskeleton": {
        "Tubular": .10,
        "Flat": .25,
        "Ovoid": .90,
        "Spherical": .99,
        "Amorphous": 1
    },
    "Exoskeleton": {
        "Tubular": .15,
        "Flat": .45,
        "Ovoid": .85,
        "Spherical": .95,
        "Amorphous": 1
    },
    "Muscoskeleton": {
        "Tubular": .20,
        "Flat": .40,
        "Ovoid": .60,
        "Spherical": .80,
        "Amorphous": 1
    }
}
# Table 4d
body_mass_index = {
    "Tubular": {
        "Scant": 3,
        "Light": 4,
        "Average": 5,
        "Heavy": 6,
        "Massive": 7
    },
    "Flat": {
        "Scant": 6,
        "Light": 8,
        "Average": 10,
        "Heavy": 12,
        "Massive": 14
    },
    "Ovoid": {
        "Scant": 12,
        "Light": 16,
        "Average": 20,
        "Heavy": 24,
        "Massive": 28
    },
    "Spherical": {
        "Scant": 24,
        "Light": 32,
        "Average": 40,
        "Heavy": 48,
        "Massive": 56
    },
    "Amorphous": {
        "Scant": 24,
        "Light": 32,
        "Average": 40,
        "Heavy": 48,
        "Massive": 56
    }
}
# table 5
head = {
    "Endoskeleton": {
        "No Neck": .01,
        "Tiny Neck": .03,
        "Short Neck": .30,
        "Medium Neck": .90,
        "Long Neck": 1
    },
    "Exoskeleton": {
        "No Neck": .20,
        "Tiny Neck": .94,
        "Short Neck": .97,
        "Medium Neck": .99,
        "Long Neck": 1
    },
    "Muscoskeleton": {
        "No Neck": .85,
        "Tiny Neck": .97,
        "Short Neck": .98,
        "Medium Neck": .99,
        "Long Neck": 1
    }
}
neck = {
        "Tiny Neck": {"min" : 0, "max": .10},
        "Short Neck": {"min" :.10, "max": .25},
        "Medium Neck": {"min" :.25, "max": .75},
        "Long Neck": {"min" :.75, "max": 1.5}
}
# table 5a
eyes = {
    "Endoskeleton": {
        "None/Blind": .01,
        "Stalked/Omnidirectional": .02,
        "Inset/Forward": .50,
        "Bulbous/Side": 1
    },
    "Exoskeleton": {
        "None/Blind": .05,
        "Stalked/Omnidirectional": .60,
        "Inset/Forward": .85,
        "Bulbous/Side": 1

    },
    "Muscoskeleton": {
        "None/Blind": .40,
        "Stalked/Omnidirectional": .60,
        "Inset/Forward": .80,
        "Bulbous/Side": 1
    }
}
# table 6
limbs = {
    "Endoskeleton": {
        "0 Limbs": .08,
        "2 Limbs": .14,
        "4 Limbs": .95,
        "6 Limbs": .99,
        "8 Limbs": 1
    },
    "Exoskeleton": {
        "0 Limbs": .05,
        "2 Limbs": .15,
        "4 Limbs": .60,
        "6 Limbs": .90,
        "8 Limbs": 1
    },
    "Muscoskeleton": {
        "0 Limbs": .40,
        "2 Limbs": .60,
        "4 Limbs": .80,
        "6 Limbs": .90,
        "8 Limbs": 1
    }
}
# table 6a
tail = {
    "Endoskeleton": {
        "Tail": .85,
        "No Tail": 1
    },
    "Exoskeleton": {
        "Tail": .1,
        "No Tail": 1
    },
    "Muscoskeleton": {
        "Tail": .2,
        "No Tail": 1
    }
}
# table 6b
flight = {
    "Flight Wings": .45,
    "Wings connected to Limb": .50,
    "Patagia": .95,
    "Other (Parachute, Balloon, Drifter, etc.)": 1
}
# table 6c
swimming = {
    "Webbing": .3,
    "Fins": .85,
    "Other (Jet, Body Twisting, Drifting, etc.)": .95,
    "Can't Swim": 1
}

# table 6d
limb_length = {
    "Carnivore": {
        "Vestigial": .01,
        "Stubby": .15,
        "Short": .35,
        "Medium": .60,
        "Long": 1
    },
    "Omnivore": {
        "Vestigial": .01,
        "Stubby": .25,
        "Short": .50,
        "Medium": .75,
        "Long": 1
    },
    "Herbivore": {
        "Vestigial": .01,
        "Stubby": .20,
        "Short": .60,
        "Medium": .85,
        "Long": 1
    }
}

limb_length_percent = {
    "Vestigial": {
        "min": .01,
        "max": .05
    },
    "Stubby": {
        "min": .05,
        "max": .25
    },
    "Short": {
        "min": .25,
        "max": .50
    },
    "Medium": {
        "min": .50,
        "max": 1
    },
    "Long": {
        "min": 1,
        "max": 1.5
    }
}

# table 6e
appendages = {
    "Endoskeleton": {
        "Carnivore": {
            "Hoof": .10,
            "Pincer": .15,
            "Paw": .96,
            "Prehensile": 1
        },
        "Omnivore": {
            "Hoof": .30,
            "Pincer": .40,
            "Paw": .95,
            "Prehensile": 1
        },
        "Herbivore": {
            "Hoof": .60,
            "Pincer": .65,
            "Paw": .97,
            "Prehensile": 1
        }
    },
    "Exoskeleton": {
        "Carnivore": {
            "Hoof": .30,
            "Pincer": .96,
            "Paw": .97,
            "Prehensile": 1
        },
        "Omnivore": {
            "Hoof": .40,
            "Pincer": .96,
            "Paw": .98,
            "Prehensile": 1
        },
        "Herbivore": {
            "Hoof": .70,
            "Pincer": .96,
            "Paw": .99,
            "Prehensile": 1
        }
    },
    "Muscoskeleton": {
        "Carnivore": {
            "Hoof": .03,
            "Pincer": .12,
            "Paw": .20,
            "Prehensile": 1
        },
        "Omnivore": {
            "Hoof": .02,
            "Pincer": .10,
            "Paw": .20,
            "Prehensile": 1
        },
        "Herbivore": {
            "Hoof": .01,
            "Pincer": .05,
            "Paw": .10,
            "Prehensile": 1
        }

    }
}
# table 7
body_coverage = {
    "Warm Blooded": {
        "Endoskeleton": {
            "Smooth/Slick": .35,
            "Scaly/Pebbled": .40,
            "Hairy/Furry": .90,
            "Feathery": .97,
            "Shelled": 1
        },
        # Exoskeletal creatures always have a shell - The roll is for the outer shell
        "Exoskeleton": {
            "Smooth/Slick": .40,
            "Scaly/Pebbled": .50,
            "Hairy/Furry": .90,
            "Feathery": 1,
            "Shelled": 1.5
        },
        "Muscoskeleton": {
            "Smooth/Slick": .65,
            "Scaly/Pebbled": .70,
            "Hairy/Furry": .85,
            "Feathery": .90,
            "Shelled": 1

        }
    },
    "Cold Blooded": {
        "Endoskeleton": {
            "Smooth/Slick": .40,
            "Scaly/Pebbled": .85,
            "Hairy/Furry": .90,
            "Feathery": .95,
            "Shelled": 1

        },
        # Exoskeletal creatures always have a shell - The roll is for the outer shell
        "Exoskeleton": {
            "Smooth/Slick": .55,
            "Scaly/Pebbled": .65,
            "Hairy/Furry": .95,
            "Feathery": 1,
            "Shelled": 1.5

        },
        "Muscoskeleton": {
            "Smooth/Slick": .70,
            "Scaly/Pebbled": .75,
            "Hairy/Furry": .80,
            # "Feathery": 1.5,
            "Shelled": 1

        }
    }
}
# table 7a
coloration = {
    "Smooth/Slick": {
        "Black": .10,
        "Grey": .23,
        "White": .28,
        "Brown": .38,
        "Red": .46,
        "Orange": .54,
        "Yellow": .64,
        "Green": .80,
        "Blue": .89,
        "Purple": 1
    },
    "Scaly/Pebbled": {
        "Black": .08,
        "Grey": .16,
        "White": .24,
        "Brown": .34,
        "Red": .50,
        "Orange": .56,
        "Yellow": .65,
        "Green": .78,
        "Blue": .89,
        "Purple": 1

    },
    "Hairy/Furry": {
        "Black": .12,
        "Grey": .24,
        "White": .30,
        "Brown": .50,
        "Red": .56,
        "Orange": .70,
        "Yellow": .80,
        "Green": .85,
        "Blue": .92,
        "Purple": 1

    },
    "Feathery": {
        "Black": .11,
        "Grey": .26,
        "White": .33,
        "Brown": .40,
        "Red": .50,
        "Orange": .60,
        "Yellow": .70,
        "Green": .80,
        "Blue": .89,
        "Purple": 1

    },
    "Shelled": {
        "Black": .10,
        "Grey": .20,
        "White": .25,
        "Brown": .31,
        "Red": .39,
        "Orange": .47,
        "Yellow": .57,
        "Green": .67,
        "Blue": .87,
        "Purple": 1
    }
}
# table 7b
pattern = {
    "Mottled": .20,
    "Spots": .40,
    "Stripes": .60,
    "Patches": .74,
    "Ornate": .81,
    "Iridescent": .87,
    "Florescent": .89,
    "Phased": 1
}
# table 8
# table 8a
# table 9
sentience = {
    "Warm Blooded": {
        "Carnivore": {
            "Instinctual": .05,
            "Hive": .06,
            "Animal": .75,
            "Cunning": .99,
            "Sapient": 1
        },
        "Omnivore": {
            "Instinctual": .10,
            "Hive": .11,
            "Animal": .70,
            "Cunning": .98,
            "Sapient": 1

        },
        "Herbivore": {
            "Instinctual": .25,
            "Hive": .26,
            "Animal": .79,
            "Cunning": .99,
            "Sapient": 1

        }
    },
    "Cold Blooded": {
        "Carnivore": {
            "Instinctual": .20,
            "Hive": .22,
            "Animal": .84,
            "Cunning": .98,
            "Sapient": 1
        },
        "Omnivore": {
            "Instinctual": .30,
            "Hive": .33,
            "Animal": .79,
            "Cunning": .99,
            "Sapient": 1

        },
        "Herbivore": {
            "Instinctual": .40,
            "Hive": .42,
            "Animal": .74,
            "Cunning": .99,
            "Sapient": 1

        }

    }
}
# table 9a
sentience_of_hive_mind = {
    "Carnivore": {
        "Instinctual": .50,
        "Animal": .80,
        "Cunning": .99,
        "Sapient": 1
    },
    "Omnivore": {
        "Instinctual": .40,
        "Animal": .70,
        "Cunning": .99,
        "Sapient": 1
    },
    "Herbivore":{
        "Instinctual": .30,
        "Animal": .60,
        "Cunning": .99,
        "Sapient": 1
    }
}
# table 10
reproduction = {
    "Warm Blooded":{
        "Live Birth": .70,
        "Eggs": .77,
        "Brood Eggs": .96,
        "Larvae": 1
    },
    "Cold Blooded":{
        "Live Birth" : .10,
        "Eggs": .60,
        "Brood Eggs": .90,
        "Larvae": 1
    }
}
# table 10c
sexual_type = {
    "Two Sexes":.75,
    "Hermaphrodites": .95,
    "Asexual": 1
}
