import re

from Constants import longestArmorType
from Armor import ArmorType, HexColor, GetAbsoluteDifference

'''
itemDB = {
    "hexCode": {
        "armorType": [
            "playerUUID"
        ]
    }
}
'''
playerUUIDToItemList = {}
itemDB = {}
hexCodeToItemCount = {}
itemIDToItemCount = {}
totalDatabaseItems = 0

def GetArmorType(itemString: str):
    itemString = itemString.replace("_", " ")
    armorTypeSplit = re.split('', itemString)

    currentWord = ""
    for i, letter in enumerate(armorTypeSplit):
        if i > longestArmorType:
            break

        letter = letter.lower().strip()
        currentWord += letter
        for armor in ArmorType.__members__:
            if currentWord == armor.lower():
                return ArmorType[armor]
    return None

helmetNames = sorted(["helmet", "helm"], key=len, reverse=True)
chestplateNames = sorted(["chestplate", "chest", "cp"], key=len, reverse=True)
leggingsNames = sorted(["leggings", "legging", "legs", "leg", "pant", "pants"], key=len, reverse=True)
bootsNames = sorted(["boots", "boot"], key=len, reverse=True)
def UpdateItemID(itemString: str):
    doPrint = False

    armorType = GetArmorType(itemString)
    if doPrint:
        print(f"1 {itemString} - {armorType}")
    if armorType is None:
        return None

    itemString = itemString.lower().replace("_", " ").strip()
    armorTypeName = armorType.value.lower()
    for name in helmetNames + chestplateNames + leggingsNames + bootsNames:
        armorTypeName = armorTypeName.replace(name, "").strip()

    if doPrint:
        print(f"2 {itemString} - {armorTypeName}")

    itemType = itemString.replace(armorTypeName, "").strip()
    if doPrint:
        print(f"3 {itemString} - {armorTypeName} - {itemType}")

    if itemType in helmetNames:
        itemType = "helmet"
    elif itemType in chestplateNames:
        itemType = "chestplate"
    elif itemType in leggingsNames:
        itemType = "leggings"
    elif itemType in bootsNames:
        itemType = "boots"
    else:
        itemType = ""

    return f"{armorTypeName} {itemType}".strip().replace(" ", "_").upper()

def LoadDatabase(filePath):
    global totalDatabaseItems
    with open(filePath) as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            baseHex, armorType, playerUUID = line.split(" ")
            itemID = armorType.upper()
            playerUUID = playerUUID.upper()
            # itemID = UpdateItemID(armorType)
            # if itemID is None:
            #     print(f"Error: Invalid itemID '{armorType}'")

            hexColor = None
            try:
                hexColor = HexColor(hex=baseHex)
            except Exception as e:
                print(f"Error: {e}")
                continue

            if hexColor is None:
                continue

            hexCode = hexColor.GetHexCode()
            if hexCode not in itemDB:
                itemDB[hexCode] = {}

            if hexCode not in hexCodeToItemCount:
                hexCodeToItemCount[hexCode] = 1
            else:
                hexCodeToItemCount[hexCode] += 1

            if itemID not in itemIDToItemCount:
                itemIDToItemCount[itemID] = 1
            else:
                itemIDToItemCount[itemID] += 1

            if itemID not in itemDB[hexCode]:
                itemDB[hexCode][itemID] = []

            if playerUUID not in playerUUIDToItemList:
                playerUUIDToItemList[playerUUID] = []
            playerUUIDToItemList[playerUUID].append([itemID, hexCode])

            itemDB[hexCode][itemID].append(playerUUID)
            totalDatabaseItems += 1

def GetDatabasePlayers(itemID: str = None, itemHex: str = None, isArmorType: bool = False):
    itemID = itemID.upper() if itemID is not None else None
    itemHex = itemHex.upper() if itemHex is not None else None

    playerItems = {}
    itemList = []
    if itemHex is not None:
        if itemHex in itemDB:
            if itemID is not None:
                if itemID in itemDB[itemHex]:
                    itemList.append([itemHex, itemID])
                elif isArmorType:
                    for armorType in itemDB[itemHex]:
                        if itemID in armorType:
                            itemList.append([itemHex, armorType])
            else:
                for itemID in itemDB[itemHex]:
                    itemList.append([itemHex, itemID])

    elif itemID is not None:
        for hexCode in itemDB:
            if itemID in itemDB[hexCode]:
                itemList.append([hexCode, itemID])
            elif isArmorType:
                for armorType in itemDB[hexCode]:
                    if itemID in armorType:
                        itemList.append([hexCode, armorType])

    for itemList in itemList:
        hexCode, itemID = itemList
        for player in itemDB[hexCode][itemID]:
            if player not in playerItems:
                playerItems[player] = []
            playerItems[player].append([itemID, hexCode])

    return playerItems

def GetItemCount(itemID: str = None, itemHex: str = None, isArmorType: bool = False):
    itemID = itemID.upper() if itemID is not None else None
    itemHex = itemHex.upper() if itemHex is not None else None

    if itemHex is not None:
        if itemHex in hexCodeToItemCount:
            if itemID is not None:
                if itemID in itemDB[itemHex]:
                    return len(itemDB[itemHex][itemID])
                elif isArmorType:
                    totalItems = 0
                    for armorType in itemDB[itemHex]:
                        if itemID in armorType:
                            totalItems += len(itemDB[itemHex][armorType])

                    return totalItems
            else:
                return hexCodeToItemCount.get(itemHex, 0)

    elif itemID is not None:
        if isArmorType:
            totalItems = 0
            for hexCode in itemDB:
                for armorType in itemDB[hexCode]:
                    if itemID in armorType:
                        totalItems += len(itemDB[hexCode][armorType])
            return totalItems
        return itemIDToItemCount.get(itemID, 0)

    return 0

def GetMatchingItems(itemID: str, itemHex: HexColor, tolerance: int = 0):
    matchingItemsList = {}
    matchingItemCount = 0
    for hexCode in itemDB:
        if itemID in itemDB[hexCode]:
            difference = GetAbsoluteDifference(HexColor(hex=hexCode), itemHex)
            if difference <= tolerance:
                playerList = itemDB[hexCode][itemID]
                matchingItemsList[hexCode] = [playerList, difference]
                matchingItemCount += len(playerList)

    return matchingItemsList, matchingItemCount

# LoadDatabase("Combined-S.html")

# print(GetDatabasePlayers(itemID="LAPIS_CHEST", itemHex="211A1B"))
# print(GetDatabasePlayers(itemID="LAPIS_CHEST"))
# print(GetDatabasePlayers(itemHex="211A1B"))

# print(GetItemCount(itemID="LAPIS_CHEST", itemHex="211A1B"))
# print(GetItemCount(itemID="LAPIS_CHEST"))
# print(GetItemCount(itemHex="211A1B"))

# print(3, GetArmorType("LAPIS_CHEST"))
# print(3, GetArmorType("LAPIS CHEST"))
# print(3, GetArmorType("LAPIS_CP"))
# print(3, GetArmorType("LAPISchestplate"))
# print(3, GetArmorType("anglerlegs"))
# print(3, GetArmorType("lapisboots"))
# print(3, GetArmorType("lapis_helmet"))

# print(3, UpdateItemID("LAPIS_CHEST"))
# print(3, UpdateItemID("LAPIS CHEST"))
# print(3, UpdateItemID("LAPIS_CP"))
# print(3, UpdateItemID("LAPISchestplate"))
# print(3, UpdateItemID("anglerlegs"))
# print(3, UpdateItemID("lapisboots"))
# print(3, UpdateItemID("OBSIDIAN_CHESTPLATE"))
# print(3, UpdateItemID("CREEPER_LEGGINGS"))
# print(3, UpdateItemID("ZOMBIE_SOLDIER_CHESTPLATE"))
# print(3, UpdateItemID("RANCHERS_BOOTS"))
# print(3, UpdateItemID("MAGMAHELMET"))
# print(3, UpdateItemID("MAGMA_HELMET"))
# print(3, UpdateItemID("FARMER_BOOTS"))
# print(3, UpdateItemID("STEREO_PANTS"))
# print(3, UpdateItemID("STARRED_SHADOW_ASSASSIN_BOOTS"))
# print(3, UpdateItemID("FARM_SUIT_HELMET"))
# print(3, UpdateItemID("CHEAP_TUXEDO_BOOTS"))
# print(3, UpdateItemID("GOLDOR_BOOTS"))
# print(3, UpdateItemID("CHEAP_TUXEDO_LEGS"))
# print(3, UpdateItemID("CHEAP_TUXEDO_CHEST"))
# print(3, UpdateItemID("FANCY_TUXEDO_LEGS"))
# print(3, UpdateItemID("FANCY_TUXEDO_BOOTS"))
# print(3, UpdateItemID("FANCY_TUXEDO_CHEST"))
# print(3, UpdateItemID("GOLDOR_LEGS"))
# print(3, UpdateItemID("PACK"))

# print(4, len(GetDatabasePlayers(itemHex="7fcc19", itemID="young", isArmorType=True)))
# print(4, GetItemCount(itemHex="7fcc19", itemID="young", isArmorType=True))