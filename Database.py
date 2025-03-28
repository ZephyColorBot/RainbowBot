from Armor import HexColor, GetAbsoluteDifference, GetVisualDifference, UpdateItemID, GetArmorType

'''
itemDB = {
    "hexCode": {
        "armorType": [
            "playerUUID",
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

def LoadDatabase(filePath):
    global totalDatabaseItems
    with open(filePath) as file:
        for index, line in enumerate(file):
            line = line.strip()

            if not line:
                continue

            try:
                baseHex, armorType, playerUUID = line.split(" ")
                itemID = armorType.upper()
                playerUUID = playerUUID.upper()
            except Exception as e:
                print(f"Error Loading database line #{index}: '{line}' | {e}")
                continue

            try:
                hexColor = HexColor(baseHex=baseHex)
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

def GetValidItemIDFromItemName(itemName):
    itemID = None
    isArmorType = False
    isValid = False
    if itemName is not None:
        itemID = UpdateItemID(itemName)
        armorType = str(GetArmorType(itemName)).upper().strip().replace(' ', '_')
        if itemID in itemIDToItemCount:
            isValid = True
        elif armorType in itemIDToItemCount:
            isValid = True
            isArmorType = True
            itemID = armorType
        elif itemName.lower().replace("_", "").replace(" ", "").strip() == itemName.lower().replace("_", "").replace(" ", "").strip():
            isValid = True
            isArmorType = True

    return isValid, itemID, isArmorType

def GetMatchingItems(itemID: str, itemHex: HexColor, tolerance: float = 0, isArmorType: bool = False, visualDistance: bool = False):
    matchingItemsList = {}
    matchingItemCount = 0
    for hexCode in itemDB:
        if not (itemID in itemDB[hexCode] or itemID == "any" or isArmorType):
            continue

        tempPlayerList = []
        if visualDistance:
            difference = GetVisualDifference(HexColor(baseHex=hexCode), itemHex)
        else:
            difference = GetAbsoluteDifference(HexColor(baseHex=hexCode), itemHex)

        if difference <= tolerance:
            if itemID in itemDB[hexCode]:
                for player in itemDB[hexCode][itemID]:
                    tempPlayerList.append([itemID, player])

            elif itemID == "any":
                for armorType in itemDB[hexCode]:
                    for player in itemDB[hexCode][armorType]:
                        tempPlayerList.append([armorType, player])

            elif isArmorType:
                for armorType in itemDB[hexCode]:
                    if itemID in armorType:
                        for player in itemDB[hexCode][armorType]:
                            tempPlayerList.append([armorType, player])

            matchingItemsList[hexCode] = [tempPlayerList, difference]
            matchingItemCount += len(tempPlayerList)

    return matchingItemsList, matchingItemCount