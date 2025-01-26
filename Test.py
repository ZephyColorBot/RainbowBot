from Armor import *

# /armor
# /color - DONE
# /exotic
# /help
# /info
# /mix

# armorSet, colors = CreateArmorSetImage(
#     armorType=ArmorType.RacingHelmet,
#     hexList=[],
#     versionType=VersionType._1_8_9,
#     displayType=DisplayType.Vertical,
#     imageSpacing=20,
#     imageSize=128
# )
#
# if type(armorSet) == list:
#     output_path = "Output/armorSet.webp"
#     armorSet[0].save(
#         output_path,
#         save_all=True,
#         append_images=armorSet[1:],
#         duration=225,
#         loop=0,
#         quality=100,
#         method=3,
#         format="WEBP",
#         lossless=True
#     )
# else:
#     armorSet.show()
#     armorSet.save("Output/armorSet.png", format="PNG", quality=100, method=6, lossless=True)

for itemKey in itemDict:
    item = itemDict[itemKey]
    filePaths = item[0]
    for imagePath in filePaths:
        try:
            if "Leather" in imagePath:
                continue
            image = Image.open(f"Images/{imagePath}")
            image.close()
        except:
            print(f"Missing image for '{itemKey}' - '{imagePath}'")

startHex = "DDE4F0"  # Hex code as an integer
rgbList = ["7fcc19"]
# startHex = "7fcc19"  # Hex code as an integer
# rgbList = ["6699d8", "993333", "4c4c4c", "334cb2", "e5e533", "7fcc19", "4c7f99", "ffffff"]

result = MixHexList(startHex, rgbList)
print(f"Combined Color: #{result}")