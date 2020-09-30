"""
Instead of rewriting my original one from scratch, I refactored and expanded https://github.com/cutecprog's version.
I broke up the RollInterface, and the Flora into individual classes.
I've also added a ToString method in the Flora class to output  human readable output text to the generator.
I'm in the process of adding the FaunaTables, and the Fauna Class as well as Fungus Tables and Fungus Class.
"""

from Flora.flora import *
from Fauna.fauna import *

def main():
    #print(createFlora())
    createFauna()



def createFlora():
    newPlant = Flora()
    newPlant.generate()
    return newPlant

def createFauna():
    newAnimal = Fauna()
    newAnimal.generate()
    pprint(vars(newAnimal))
    print(newAnimal)

if __name__ == "__main__":
    # execute only if run as a script
    from pprint import pprint
    main()
