"""
Credits:
Random Flora Tables v1.1 by Sebastian Romu
https://entorais.wordpress.com/2016/08/02/random-plants/

"""
# Table 1
type_table = {"Woody": 0.30, "Herbaceous": 0.85, "Algae": 0.90, "Fungus": 1}
# Table 2
habitat_table = {"Woody":
        {"Aquatic": 0.05, "Sub-Terrestrial": 0.10, "Terrestrial": 0.99, "Avian": 1},
        "Herbaceous":
        {"Aquatic": 0.35, "Sub-Terrestrial": 0.40, "Terrestrial": 0.99, "Avian": 1},
        "Algae":
        {"Aquatic": 0.80, "Sub-Terrestrial": 0.90, "Terrestrial": 0.98, "Avian": 1},
        "Fungus":
        {"Aquatic": 0.10, "Sub-Terrestrial": 0.40, "Terrestrial": 0.99, "Avian": 1} }
# Table 2a, 2b
subhabitat_table = {"Aquatic":
        {"Salt-Water": 0.30, "Fresh Water": 0.90, "Brackish": 1},
        "Other":
        {"Desert / Waste": 0.10, "Plains / Savannah": 0.40,
        "Marsh / Swamp / Bog": 0.50, "Forest / Jungle": 0.80,
        "Hills / Scrub": 0.90, "Mountains": 0.95, "Tundra": 1} }
# Table 2c
rarity_table = {"Very Common": 0.15, "Common": 0.50, "Uncommon": 0.80,
        "Rare": 0.94, "Very Rare": 0.99, "Unique": 1}
# Table 3
grouping_table = {"Woody":
        {"Solitary": 0.20, "Small Patch": 0.40, "Medium Patch": 0.80, "Large Patch": 1},
        "Herbaceous":
        {"Solitary": 0.30, "Small Patch": 0.50, "Medium Patch": 0.90, "Large Patch": 1},
        "Algae":
        {"Solitary": 0.25, "Small Patch": 0.70, "Medium Patch": 0.95, "Large Patch": 1} }
grouping_table["Fungus"] = grouping_table["Algae"]
# Table 4
size_table = {"Woody":
        {"Huge": 0.15, "Large": 0.45, "Average": 0.80, "Small": 0.98, "Tiny": 1},
        "Herbaceous":
        {"Huge": 0.10, "Large": 0.20, "Average": 0.70, "Small": 0.95, "Tiny": 1},
        "Algae":
        {"Huge": 0.02, "Large": 0.15, "Average": 0.65, "Small": 0.85, "Tiny": 1},
        "Fungus":
        {"Huge": 0.01, "Large": 0.10, "Average": 0.30, "Small": 0.60, "Tiny": 1} }
# Table 5
body_table = {"Woody":
        {"Colonial Mass": 0.02, "Creeper / Vine": 0.20, "Stem / Trunk": 0.70, 
        "Multiple Stems / Trunks": 0.99, "Roll Twice": 1},
        "Herbaceous":
        {"Colonial Mass": 0.03, "Creeper / Vine": 0.35, "Stem / Trunk": 0.70, 
        "Multiple Stems / Trunks": 0.98, "Roll Twice": 1},
        "Algae":
        {"Colonial Mass": 0.70, "Creeper / Vine": 0.75, "Stem / Trunk": 0.85, 
        "Multiple Stems / Trunks": 0.99, "Roll Twice": 1},
        "Fungus":
        {"Colonial Mass": 0.20, "Creeper / Vine": 0.40, "Stem / Trunk": 0.70, 
        "Multiple Stems / Trunks": 0.99, "Roll Twice": 1} }
# Table 5a
branches_table = {"Woody":
        {"Radial": 0.55, "Ordered": 0.75, "Random": 0.99, "None": 1},
        "Herbaceous":
        {"Radial": 0.45, "Ordered": 0.50, "Random": 0.85, "None": 1},
        "Algae":
        {"Radial": 0.25, "Ordered": 0.60, "Random": 0.90, "None": 1},
        "Fungus":
        {"Radial": 0.02, "Ordered": 0.05, "Random": 0.15, "None": 1} }
# Table 5b
roots_table = {"Woody":
        {"Tap": 0.35, "Tubers": 0.37, "Fibrous": 0.84, "Advantageous": 0.93,
        "Bulb": 0.95, "Rhizoid": 0.99, "None": 1},
        "Herbaceous":
        {"Tap": 0.35, "Tubers": 0.45, "Fibrous": 0.73, "Advantageous": 0.77,
        "Bulb": 0.90, "Rhizoid": 0.99, "None": 1},
        "Algae":
        {"Tap": 0.01, "Tubers": 0.02, "Fibrous": 0.04, "Advantageous": 0.15,
        "Bulb": 0.19, "Rhizoid": 0.50, "None": 1},
        "Fungus":
        {"Tap": 0.03, "Tubers": 0.09, "Fibrous": 0.15, "Advantageous": 0.20,
        "Bulb": 0.30, "Rhizoid": 0.90, "None": 1} }
# Table 5c
body_surface_table = {"Woody":
        {"Smooth": 0.30, "Waxy": 0.40, "Rough": 0.70, "Scaly": 0.84,
        "Flaky": 0.97, "Other": 0.99, "Roll Twice": 1},
        "Herbaceous":
        {"Smooth": 0.59, "Waxy": 0.79, "Rough": 0.85, "Scaly": 0.90,
        "Flaky": 0.94, "Other": 0.99, "Roll Twice": 1},
        "Algae":
        {"Smooth": 0.65, "Waxy": 0.70, "Rough": 0.75, "Scaly": 0.82,
        "Flaky": 0.90, "Other": 0.99, "Roll Twice": 1} }
body_surface_table["Fungus"] = body_surface_table["Algae"]
# Table 5d and 6e
color_table = {"Red": 0.05, "Orange": 0.10, "Yellow": 0.20, "Green": 0.45,
        "Blue": 0.50, "Violet": 0.55, "Black": 0.60, "Grey": 0.65,
        "White": 0.70, "Brown": 0.80, "Silver": 0.85, "Copper": 0.90,
        "Gold": 0.95, "Roll Twice": 1}
pattern_table = {"Spotted": 0.10, "Mottled": 0.20, "Patches": 0.25,
        "Stripes": 0.25, "Solid": 0.60, "Phases": 0.75, "Translucent": 0.80,
        "Iridescent": 0.85, "Luminescent": 0.90, "Blushed": 0.95, "Roll Twice": 1}
# Table 6
leaves_table = {"Woody":
        {"Broad": 0.55, "Needles": 0.70, "Compound": 0.94, "Blades": 0.97,
        "Scales": 0.98, "Roll Twice": 0.99, "None": 1},
        "Herbaceous":
        {"Broad": 0.45, "Needles": 0.50, "Compound": 0.85, "Blades": 0.97,
        "Scales": 0.98, "Roll Twice": 0.99, "None": 1},
        "Algae":
        {"Broad": 0.02, "Needles": 0.03, "Compound": 0.10, "Blades": 0.11,
        "Scales": 0.15, "Roll Twice": 0.30, "None": 1},
        "Fungus":
        {"Broad": 0.25, "Needles": 0.50, "Compound": 0.60, "Blades": 0.80,
        "Scales": 0.90, "Roll Twice": 0.95, "None": 1} }
# Table 6a
leaf_location_table = {"Terminal": 0.30, "Branch Points": 0.50,
        "Random Interval": 0.70, "Regular Interval": 0.90,
        "Stem / Trunk": 0.98, "Roll Twice": 1}
# Table 6b
leaf_shape_table = {"Acicular": 0.03, "Subulate": 0.06, "Lanceolate": 0.10,
        "Linear": 0.14, "Falcate": 0.17, "Spear-Shaped": 0.21, "Hastate": 0.25,
        "Deltoid": 0.28, "Rhomboid": 0.32, "Cuneate": 0.35, "Cordate": 0.39,
        "Obcordate": 0.43, "Ovate": 0.47, "Obovate": 0.51, "Acuminate": 0.56,
        "Aristate": 0.58, "Orbicular": 0.61, "Obtuse": 0.64, "Elliptic": 0.67,
        "Reniform": 0.70, "Spatulate": 0.72, "Truncate": 0.75,
        "Flabellate": 0.78, "Lobed": 0.81, "Pinnatisect": 0.83,
        "Poly-Foliate": 0.87, "Palmate": 0.92, "Pedate": 0.96, "Digitate": 0.98,
        "Roll Twice": 1}

leaf_margin_table = {"Smooth": 0.15, "Sinuate": 0.30, "Undulate": 0.40,
        "Spiny": 0.45,
        "Lobate": 0.55, "Crenate": 0.60, "Dentate": 0.70, "Denticulate": 0.75,
        "Serate": 0.85, "Serrulate": 0.90, "Ciliate": 0.95, "Roll Twice": 1}
# Table 6c
leaf_surface_table = {"Smooth": 0.25, "Waxy": 0.40, "Scaly": 0.55, "Hairy": 0.65,
        "Velvety": 0.80, "Dusty": 0.90, "Sticky": 0.96, "Roll Twice": 1}
# Table 6d
leaf_venation_table = {"Arcuate": 0.10, "Cross-Venulate": 0.20,
        "Dichotomous": 0.30, "Longitudinal": 0.45, "Palmate": 0.60,
        "Parallel": 0.70, "Pinnate": 0.80, "Reticulate": 0.90, "None": 0.99,
        "Roll Twice": 1 }
leaf_numbers_table = {"Singles": 0.20, "Pairs": 0.40, "Whorls": 0.60,
        "Clusters": 0.95, "Roll Twice": 1}
# Table 7
reproduction_table = {"Woody":
        {"Seeds": 0.80, "Suckers": 0.92, "Budding / Fragmentation": 0.98,
        "Other": 1},
        "Herbaceous":
        {"Seeds": 0.63, "Suckers": 0.85, "Budding / Fragmentation": 0.98,
        "Other": 1},
        "Algae":
        {"Seeds": 0.02, "Suckers": 0.06, "Budding / Fragmentation": 0.90,
        "Other": 1},
        "Fungus":
        {"Seeds": 0.89, "Suckers": 0.95, "Budding / Fragmentation": 0.98,
        "Other": 1} }
# Table 7a
seeds_table = {"Woody":
        {"Grain": 0.05, "Nut": 0.50, "Fruit": 0.94, "Spore": 0.99, "Other": 1},
        "Herbaceous":
        {"Grain": 0.40, "Nut": 0.45, "Fruit": 0.80, "Spore": 0.99, "Other": 1},
        "Algae":
        {"Grain": 0.02, "Nut": 0.04, "Fruit": 0.06, "Spore": 0.90, "Other": 1} }
seeds_table["Fungus"] = seeds_table["Algae"]
# Table 7b (This table is incomplete)
seed_dispersal_table = {"Grain":
        {"Animal": 0.20, "Wind": 0.40, "Water": 0.60, "Gravity": 0.98, "Other": 1},
        "Nut":
        {"Animal": 0.45, "Wind": 0.53, "Water": 0.60, "Gravity": 0.98, "Other": 1},
        "Fruit":
        {"Animal": 0.60, "Wind": 0.65, "Water": 0.85, "Gravity": 0.98, "Other": 1},
        "Spore":
        {"Animal": 0.40, "Wind": 0.83, "Water": 0.90, "Gravity": 0.98, "Other": 1},
        "Other": {"Other": 1} # Missing is source doc
        }
# Table 7c
flower_table = {"Grain":
        {"None": 0.02, "Single": 0.05, "Pairs": 0.10, "Bunches": 0.30,
        "Compound": 0.50, "Spray": 0.90, "Other": 1},
        "Nut":
        {"None": 0.02, "Single": 0.40, "Pairs": 0.60, "Bunches": 0.80,
        "Compound": 0.90, "Spray": 0.95, "Other": 1},
        "Fruit":
        {"None": 0.03, "Single": 0.30, "Pairs": 0.60, "Bunches": 0.70,
        "Compound": 0.80, "Spray": 0.90, "Other": 1},
        "Spore":
        {"None": 0.40, "Single": 0.50, "Pairs": 0.60, "Bunches": 0.70,
        "Compound": 0.80, "Spray": 0.90, "Other": 1},
        "Other":
        {"None": 0.10, "Single": 0.20, "Pairs": 0.30, "Bunches": 0.50,
        "Compound": 0.70, "Spray": 0.90, "Other": 1} }
# Table 7d
flower_shape_table = {"Single":
        {"Funnel": 0.18, "Spike": 0.20, "Disc": 0.40, "Cone": 0.60,
        "Bell": 0.85, "Sphere": 0.90, "Complex": 1},
        "Pairs":
        {"Funnel": 0.20, "Spike": 0.25, "Disc": 0.00, "Cone": 0.45,
        "Bell": 0.80, "Sphere": 0.90, "Complex": 1},
        "Bunches":
        {"Funnel": 0.10, "Spike": 0.30, "Disc": 0.00, "Cone": 0.70,
        "Bell": 0.90, "Sphere": 0.95, "Complex": 1},
        "Compound":
        {"Funnel": 0.03, "Spike": 0.25, "Disc": 0.00, "Cone": 0.70,
        "Bell": 0.80, "Sphere": 0.95, "Complex": 1},
        "Spray":
        {"Funnel": 0.10, "Spike": 0.15, "Disc": 0.00, "Cone": 0.40,
        "Bell": 0.80, "Sphere": 0.90, "Complex": 1},
        "Other":
        {"Funnel": 0.15, "Spike": 0.30, "Disc": 0.00, "Cone": 0.60,
        "Bell": 0.75, "Sphere": 0.90, "Complex": 1} }
# Table 7e
flower_size_table = \
        {"Tiny": 0.10, "Small": 0.40, "Average": 0.80, "Large": 0.95, "Huge": 1}
# Table 7f
petal_shape_table = {"Round": 0.10, "Curly": 0.25, "Wavy": 0.40,
        "Toothed": 0.50, "Oval": 0.65, "Blade": 0.80, "Thread": 0.85,
        "Feathery": 0.90, "Roll Twice": 1}
petal_number_table = \
        {"None": 0.10, "1d6": 0.30, "3d4": 0.60, "4d6": 0.90,"5d20": 1}
# Table 7g (Change "Other / Roll Twice" to just "Roll Twice")
petal_surface_table = {"Smooth": 0.15, "Waxy": 0.30, "Veined": 0.40,
        "Scaly": 0.45, "Hairy": 0.60, "Velvety": 0.80, "Dusty": 0.90,
        "Sticky": 0.96, "Twice Roll": 1}
# Table 7h
flower_location_table = {"Terminal": 0.30, "Branch Points": 0.50,
        "Random Interval": 0.70, "Regular Interval": 0.90,
        "Stem / Trunk": 0.98, "Roll Twice": 1}
# Table 7i
flower_scent_table = {"None": 0.10, "Sweet": 0.60, "Musky": 0.80,
        "Foul": 0.95, "Other / Specific": 1}
# Table 7j
flower_frequency_table = {"Annual": 0.40, "Poly-Annual": 0.60, 
        "Perennial": 0.90, "Other": 1}
# Table 7k
flower_color_table = {"Red": 0.10, "Orange": 0.20, "Yellow": 0.30, "Green": 0.40,
        "Blue": 0.50, "Violet": 0.60, "Black": 0.62, "Grey": 0.65,
        "White": 0.75, "Brown": 0.80, "Silver": 0.85, "Copper": 0.90,
        "Gold": 0.95, "Roll Twice": 1}
flower_pattern_table = {"Spotted": 0.08, "Mottled": 0.13, "Patches": 0.20,
        "Stripes": 0.30, "Solid": 0.50, "Phases": 0.55, "Translucent": 0.60,
        "Iridescent": 0.65, "Luminescent": 0.70, "Blushed": 0.84,
        "Mimicry": 0.89, "Night Blooming": 0.92, "Night Closing": 0.95,
        "Roll Twice": 1}
# Table 7l
flower_stamens_table = {"0": 0.10, "1-3": 0.30, "4-9": 0.70, "10+": 1}
flower_pistils_table = {"0": 0.20, "1": 0.40, "2-4": 0.75, "5+": 1}
# Table 8 (change made: Re-roll twice removed 'Re-roll Twice' keep 'Other')
diet_table = {"Woody":
        {"Photo/Chemo-synthetic": 0.89, "Predaceous": 0.90, "Decay": 0.95,
        "Parasitic": 0.98, "Symbiotic": 0.99, "Other": 1},
        "Herbaceous":
        {"Photo/Chemo-synthetic": 0.85, "Predaceous": 0.87, "Decay": 0.93,
        "Parasitic": 0.96, "Symbiotic": 0.98, "Other": 1},
        "Algae":
        {"Photo/Chemo-synthetic": 0.92, "Predaceous": 0.93, "Decay": 0.94,
        "Parasitic": 0.95, "Symbiotic": 0.99, "Other": 1},
        "Fungus":
        {"Photo/Chemo-synthetic": 0.05, "Predaceous": 0.08, "Decay": 0.90,
        "Parasitic": 0.94, "Symbiotic": 0.98, "Other": 1}
        # Change made above to ^^^^ 0.99 to 0.98
        }
# Table 8a
tropism_table = {"Woody":
        {"None": 0.02, "Gravity": 0.55, "Light": 0.83, "Heat": 0.87,
        "Touch": 0.97, "Motile": 0.98, "Mobile": 0.99, "Roll Twice": 1},
        "Herbaceous":
        {"None": 0.05, "Gravity": 0.40, "Light": 0.82, "Heat": 0.87,
        "Touch": 0.97, "Motile": 0.98, "Mobile": 0.99, "Roll Twice": 1},
        "Algae":
        {"None": 0.20, "Gravity": 0.35, "Light": 0.60, "Heat": 0.85,
        "Touch": 0.90, "Motile": 0.94, "Mobile": 0.98, "Roll Twice": 1},
        "Fungus":
        {"None": 0.30, "Gravity": 0.70, "Light": 0.80, "Heat": 0.90,
        "Touch": 0.96, "Motile": 0.98, "Mobile": 0.99, "Roll Twice": 1} }
# Table 9
sentience_chance = {"Photo/Chemo-synthetic": 0.99, "Predaceous": 0.97,
        "Decay": 0.99, "Parasitic": 0.98, "Symbiotic": 0.98, "Other": 0.97 }
# Table 9a
sentience_table = {"Instinctual": 0.75, "Hive": 0.79, "Animal": 0.89,
        "Cunning Animal": 0.99, "Sapient": 1}
# Table 10 (Modified table: "Medicinal / Other" to "Medicinal")
edibility_table = {"Woody":
        {"Non-Edible": 0.40, "Edible": 0.65, "Nutritious / Tasty": 0.80,
        "Medicinal": 0.99, "Roll Twice": 1},
        "Herbaceous":
        {"Non-Edible": 0.15, "Edible": 0.45, "Nutritious / Tasty": 0.60,
        "Medicinal": 0.99, "Roll Twice": 1},
        "Algae":
        {"Non-Edible": 0.60, "Edible": 0.85, "Nutritious / Tasty": 0.90,
        "Medicinal": 0.99, "Roll Twice": 1},
        "Fungus":
        {"Non-Edible": 0.30, "Edible": 0.60, "Nutritious / Tasty": 0.86,
        "Medicinal": 0.99, "Roll Twice": 1} }
# Table 10a
edible_preparation_table = {"Edible":
        {"Raw": 0.15, "Roasted": 0.30, "Boiled": 0.50, "Ground": 0.60,
        "Steeped": 0.75, "Blanched": 0.85, "Dried": 1},
        "Nutritious / Tasty":
        {"Raw": 0.30, "Roasted": 0.45, "Boiled": 0.55, "Ground": 0.65,
        "Steeped": 0.75, "Blanched": 0.80, "Dried": 1} }
# Table 10b
medicinal_properties_table = {'Abortifacient': 0.0, 'Acrid': 0.01,
        'Adjuvant': 0.02, 'Alterative': 0.03, 'Analgesic': 0.04, 'Anaphrodisiac': 0.05, 'Anesthetic': 0.06, 'Anodyne': 0.07, 'Anthelmintic': 0.08, 'Antibiotic': 0.09, 'Anticoagulant': 0.1, 'Antiemetic': 0.11, 'Antifungal': 0.12, 'Antihydrotic': 0.13, 'Antilithic': 0.14, 'Antinauseant': 0.15, 'Antiperodic': 0.16, 'Antiphlogistic': 0.17, 'Antipyretic': 0.18, 'Antiscorbutic': 0.19, 'Antiscrufulous': 0.2, 'Antiseptic': 0.21, 'Antispasmodic': 0.22, 'Antitussive': 0.23, 'Aperient': 0.24, 'Aphrodisiac': 0.25, 'Appetizer': 0.26, 'Aromatic': 0.27, 'Astringent': 0.28, 'Balsam': 0.29, 'Bitter': 0.3, 'Bitter tonic.': 0.31, 'Calmative': 0.32, 'Cardiac': 0.33, 'Carminative.': 0.34, 'Cathartic': 0.35, 'Caustic': 0.36, 'Cholagogue': 0.37, 'Coagulant': 0.38, 'Colourant': 0.39, 'Counterirritant': 0.4, 'Demulcent': 0.41, 'Deodourant': 0.42, 'Depressant': 0.43, 'Depurative': 0.44, 'Detergent': 0.45, 'Diaphoretic': 0.46, 'Digestive': 0.47, 'Disinfectant': 0.48, 'Diuretic': 0.49, 'Dye': 0.5, 'Emetic': 0.51, 'Emmenagogue': 0.52, 'Emollient': 0.53, 'Errihine': 0.54, 'Euphoriant': 0.55, 'Expectorant': 0.56, 'Febrifuge': 0.57, 'Fungicide': 0.58, 'Galactagogue': 0.59, 'Glue': 0.6, 'Haemostatic': 0.61, 'Hallucinogen': 0.62, 'Hepatic': 0.63, 'Hydragogue': 0.64, 'Hypnotic': 0.65, 'Insecticide': 0.66, 'Irritant': 0.67, 'Laxative': 0.68, 'Mucilaginous': 0.69, 'Mystical / Other': 0.7, 'Narcotic': 0.71, 'Nauseant': 0.72, 'Nephretic': 0.73, 'Nervine': 0.74, 'Oil': 0.75, 'Oxytocic': 0.76, 'Pectoral': 0.77, 'Poison': 0.78, 'Purgative': 0.79, 'Refridgerant': 0.8, 'Restorative': 0.81, 'Rubefacient': 0.82, 'Sedative': 0.83, 'Sialagogue': 0.84, 'Soporific': 0.85, 'Specific': 0.86, 'Stimulant': 0.87, 'Stomachic': 0.88, 'Vasodilator': 0.89, 'Vermicide': 0.9, 'Vermifuge': 0.91, 'Vesicant': 0.92, 'Vulnerary': 0.93, 'Wax': 0.94, "Mystical / Other": 0.95, "Roll Twice": 1 }
# Table 10c
medicinal_preparation_table = {"Bathing in": 0.05, "Cold Compressing": 0.10,
        "Cold Extracting": 0.15, "Crushing": 0.20, "Decocting": 0.25,
        "using the Essence of": 0.28, "Fomentating": 0.35, "Grating": 0.38, "Grinding": 0.45,
        "Infusing": 0.51, "Juicing": 0.55, "creating an Ointment from": 0.60, "Poulticing": 0.65,
        "creating a Powder from": 0.73, "Rubbing": 0.76, "creating a Syrup from": 0.80, "creating a Tincture from": 0.85,
        "Smoking": 0.89, "Washing with": 0.93, "Eating": 1}