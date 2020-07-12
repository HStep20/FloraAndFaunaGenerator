# Use a dictionary to determine outcome of dice roll
# scale of 1-10 on gravity. 5=earth, each point up or down is 10% change
# Scale of 1-10 how lush. 1=asteroid/moon, 5=earth, 10=lushest boi
from Flora import Flora
import tkinter


flora = Flora()
def newFlora():
    flora = Flora() # not overwriting flora
    flora.printAttributes()


def addFloraToWindow():
    flora.floraKind + "\n" + flora.primHab + "\n" + flora.aquaHab + "\n" + flora.subHab + "\n" + flora.rare + "\n" + flora.group + "\n" + flora.sized + "\n" + flora.floraBody + "\n" + flora.floraBranches + "\n" + flora.floraRoots + "\n" + flora.floraCoverage + "\n" + flora.floraColor + "\n" + flora.floraPattern + "\n" + flora.leafType + "\n" + flora.leafLoc + "\n" + flora.leafShapes + "\n" + flora.leafMargins + "\n" + flora.leafSurfaced + "\n" + flora.leafVenat + "\n" + flora.leafNumbers + "\n" + flora.leafColors + "\n" + flora.leafPatterns + "\n" + flora.reproductions + "\n" + flora.seed + "\n" + flora.dispersal + "\n" + flora.flower + "\n" + flora.flowerShaping + "\n" + flora.flowerSizing + "\n" + flora.petalShap + "\n" + flora.petalNum + "\n" + flora.petalSurf + "\n" + flora.flowerLoc + "\n" + flora.flowerFreq + "\n" + flora.flowerSmell + "\n" + flora.flowerColors + "\n" + flora.flowerPatterns + "\n" + flora.stamen + "\n" + flora.pistil + "\n" + flora.dietTypes + "\n" + flora.tropisms + "\n" + flora.sentiences + "\n" + flora.sentienceTypes + "\n" + flora.edibilities + "\n" + flora.edibilitiesPrep
    return
def printFloraAttribute():
    print(flora.edibilities) #not doing new flora, instead old flora.
    print(flora.edibilitiesPrep)

root = tkinter.Tk()

topFrame = tkinter.Frame(root)
topFrame.pack()
botFrame = tkinter.Frame(root)
botFrame.pack(side=tkinter.BOTTOM)

floraButton = tkinter.Button(topFrame, text="Create Flora", command=newFlora)
faunaButton = tkinter.Button(topFrame, text="Create Fauna", command=printFloraAttribute)
outputText = tkinter.Label(botFrame, text="This is test Text")

floraButton.pack(side=tkinter.LEFT)
faunaButton.pack(side=tkinter.RIGHT)
outputText.pack()

root.mainloop()
