from random import random, randint
from Flora import *

# ----------------------- Globals ----------------------------------------------

gravity = 0  # Planetary Gravity Index
aura = 0  # Planetary Aura Index


# ------------------------ Functions -------------------------------------------

def select(table, modifier=0, allow_row_twice=True):
    roll = random() + modifier
    if roll > 1.0:
        roll = 1.0
    for tag in sorted(table, key=table.get):
        # sort table able by weights
        if roll <= table[tag]:
            if allow_row_twice and tag == "Roll Twice":
                return roll_twice(table, modifier)
            return tag
    print("Error: No value less than or equal to " + str(roll))


def add_without_repeat(tag, additional_tag):
    if additional_tag != tag:
        # both rolled subhabitats aren't the same
        return [tag, additional_tag]
    return tag


def roll_twice(table, modifier=0):
    output = ["Roll Twice", "Roll Twice"]
    # Reroll if land on roll twice
    while output[0] == "Roll Twice":
        output[0] = select(table, allow_row_twice=False)
    while output[1] == "Roll Twice" or output[1] == output[0]:
        output[1] = select(table, allow_row_twice=False)
    return output


def account_for_two(tag, generate):
    # self.leaves["type"] = select(leaves_table[self.type])
    if type(tag["type"]) is list:
        tag = [{"type": tag["type"][0]}, {"type": tag["type"][1]}]
    elif tag["type"] == "None":
        return
    if type(tag) is list:
        tag[0] = generate(tag[0]["type"])
        tag[1] = generate(tag[1]["type"])
    else:
        tag = generate(tag["type"])
    return tag


def roll_dice(roll):
    if roll == "None":
        return 0
    # Remove all whitespace
    roll = "".join(roll.split())
    sum = 0
    for n in roll.split("+"):
        arg = n.split('d')
        if len(arg) == 1:
            sum += int(arg[0])
        elif len(arg) == 2:
            number_of_rolls = int(arg[0])
            die_type = int(arg[1])
            for i in range(0, number_of_rolls):
                sum += randint(1, die_type)
    return sum