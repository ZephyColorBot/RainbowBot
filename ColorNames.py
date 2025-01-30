import json

colorData = {}

def LoadColorNames():
    with open("ColorNames.json", "r") as file:
        global colorData
        colorData = json.load(file)

def GetNearestColorName(hexCode: str):
    lowestDistance = 9999999999999999999
    nearestColor = ""
    if hexCode in colorData:
        return colorData[hexCode]
    for colorHex in colorData:
        distance = (int(hexCode[0:2], 16) - int(colorHex[0:2], 16)) ** 2 + (int(hexCode[2:4], 16) - int(colorHex[2:4], 16)) ** 2 + (int(hexCode[4:6], 16) - int(colorHex[4:6], 16)) ** 2
        if distance < lowestDistance:
            colorName = colorData[colorHex]
            lowestDistance = distance
            nearestColor = colorName

    return nearestColor