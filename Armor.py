import re
import io
import math
import imageio
import numpy as np

from PIL import Image, ImageDraw
from Constants import *

class HexColor:
    hexCode: str = None
    RGBList: list[int] = None

    def __str__(self):
        return f"Hex: {self.hexCode}, RGB: {self.RGBList}"

    def __init__(self, baseHex: str = None, rgb: list = None):
        if (baseHex is None or not baseHex) and (rgb is None or not rgb):
            raise ValueError("Hex code or RGB list must be set.")

        if baseHex == "empty" or baseHex == "blank" or baseHex == "none":
            self.hexCode = "Blank"
            self.RGBList = [0, 0, 0]
            return

        if baseHex is not None:
            if type(baseHex) is not str:
                raise ValueError("Hex code must be a string.")
            self.hexCode = self.GetFixedHex(baseHex)
        if rgb is not None:
            if type(rgb) is not list:
                raise ValueError("RGB list must be a list.")
            if len(rgb) != 3:
                raise ValueError("RGB list must have 3 values.")
            self.RGBList = rgb

        if self.hexCode is None:
            self.hexCode = self.GetHexFromRGB(self.RGBList)
        if self.RGBList is None:
            self.RGBList = self.GetRBGFromHex(self.hexCode)

    def GetHexCode(self):
        if self.hexCode is None and self.RGBList is None:
            raise ValueError("Hex code or RGB list must be set.")

        if self.hexCode is not None:
            return self.hexCode
        return self.GetHexFromRGB(self.RGBList)
    def GetRGBList(self):
        return self.RGBList
    def GetRGBInt(self):
        return self.RGBList[0] << 16 | self.RGBList[1] << 8 | self.RGBList[2]

    def GetFixedHex(self):
        if self.hexCode is None and self.RGBList is None:
            raise ValueError("Hex code or RGB list must be set.")

        if self.hexCode is not None:
            return self.GetFixedHex(self.hexCode)
        if self.RGBList is not None:
            return self.GetHexFromRGB(self.RGBList)

    @staticmethod
    def GetFixedHex(hexCode: str|list[int]):
        if hexCode is None:
            raise ValueError("Hex code must be set.")

        if type(hexCode) is list:
            hexCode = HexColor.GetHexFromRGB(hexCode)

        hexCode = hexCode.lower().strip()
        if hexCode in stringToColorDict:
            hexCode = stringToColorDict[hexCode].value[1]

        hexCode = hexCode.upper().replace(',', '')
        hexCode = hexCode.lstrip('#').strip()
        hexCode = hexCode.rjust(6, '0')
        return hexCode

    @staticmethod
    def GetRBGFromHex(hexCode: str):
        if hexCode is None:
            raise ValueError("Hex code must be set.")
        if type(hexCode) is not str:
            raise ValueError("Hex code must be a string.")

        return list(int(hexCode[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def GetHexFromRGB(rgb: list[int]):
        if rgb is None:
            raise ValueError("RGB list must be set.")
        if type(rgb) is not list:
            raise ValueError("RGB list must be a list.")

        hexString = '%02x%02x%02x' % tuple(rgb)
        return hexString.upper()

    @staticmethod
    def GetIntFromRGB(rgb: list[int]):
        if rgb is None:
            raise ValueError("RGB list must be set.")
        if type(rgb) is not list:
            raise ValueError("RGB list must be a list.")

        return rgb[0] << 16 | rgb[1] << 8 | rgb[2]

def CreateColorSquare(
    hexColorList: list[HexColor],
    imageSize: int = 128,
    maxColumns: int = -1,
    maxRows: int = -1
):
    total = len(hexColorList)
    if maxColumns == -1 and maxRows == -1:
        columns = math.ceil(math.sqrt(total))
        rows = math.ceil(total / columns)
    elif maxColumns != -1 and maxRows == -1:
        columns = maxColumns
        rows = math.ceil(total / columns)
    elif maxColumns == -1 and maxRows != -1:
        rows = maxRows
        columns = math.ceil(total / rows)
    else:
        columns = maxColumns
        rows = maxRows
        max_cells = columns * rows
        hexColorList = hexColorList[:max_cells]

    width = columns * imageSize
    height = rows * imageSize

    image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    for i, color in enumerate(hexColorList):
        row = i // columns
        col = i % columns
        if row >= rows:
            break
        x0, y0 = col * imageSize, row * imageSize
        x1, y1 = x0 + imageSize - 1, y0 + imageSize - 1

        if color.hexCode == "Blank":
            draw.rectangle((x0, y0, x1, y1), fill=(0, 0, 0, 0))
            continue
        draw.rectangle((x0, y0, x1, y1), fill=tuple(color.GetRGBList()))

    return image

def GetOverlayImage(
        imagePath: str
):
    if imagePath is None:
        return None

    if "/" in imagePath:
        imagePath = imagePath.split("/")[-1]

    if imagePath == "LeatherHelmet.png":
        return "Images/LeatherHelmetOverlay.png"

    # elif imagePath == "LeatherChestplate.png":
    #     return "Images/LeatherChestplateOverlay.png"

    elif imagePath == "LeatherLeggings.png":
        return "Images/LeatherLeggingsOverlay.png"

    elif imagePath == "LeatherBoots.png":
        return "Images/LeatherBootsOverlay.png"

    return None

def CreateArmorSetImage(
        armorType: ArmorType,
        hexList: list[HexColor],
        shapeType: ShapeType = ShapeType.Vertical,
        versionType: VersionType = VersionType._1_8_9,
        imageSpacing = 20,
        imageSize = 128
):
    if armorType not in itemDict:
        raise ValueError(f"Invalid armor type '{armorType}'")

    armorType = itemDict[armorType]
    armorImages = armorType[0]

    imageSpacing *= math.ceil(imageSize / 128)

    finalHexColorList = []
    i = 0
    lastHex = None
    for armorHexes in enumerate(armorType[1]):
        armorHex = armorHexes[1].strip()
        if not armorHex or armorHex == "":
            finalHexColorList.append(None)
            continue

        i += 1
        if i <= len(hexList):
            finalHexColorList.append(hexList[i - 1])
            lastHex = hexList[i - 1]
        else:
            if lastHex is not None:
                finalHexColorList.append(lastHex)
            else:
                finalHexColorList.append(HexColor(baseHex=armorHex))

    armorPaths = [f"Images/{image}" for image in armorImages]

    armorImages = []
    for j, basePath in enumerate(armorPaths):
        if finalHexColorList[j] is not None:
            if finalHexColorList[j].hexCode == "Blank":
                basePath = basePath.replace("Leather", "EmptyImage")

        armorImages.append(CreateArmorPieceImage(basePath=basePath, overlayColor=finalHexColorList[j], versionType=versionType, imageSize=imageSize))

    croppedImageList = []
    for armorImage in armorImages:
        bbox = armorImage.getbbox()
        if bbox:
            croppedImage = armorImage.crop(bbox)
            croppedImageList.append(croppedImage)

    heightOffset = 0
    disallowedNames = ["leather", "angler", "chainmail", "gold", "iron", "diamond"]
    for i, croppedImage in enumerate(croppedImageList):
        armorName = armorPaths[i].lower()
        if "helmet" in armorName and not any(item in armorName for item in disallowedNames):
            heightOffset = imageSpacing // 2
            break

    image = None
    animatedFiles = []
    if shapeType == ShapeType.Vertical:
        width = max([image.width for image in croppedImageList])
        height = sum([image.height for image in croppedImageList]) + (len(armorImages) - 1) * imageSpacing

        image = Image.new("RGBA", (width, height - heightOffset), (0, 0, 0, 0))

        y = 0
        for i, croppedImage in enumerate(croppedImageList):
            x_offset = (width - croppedImage.width) // 2
            image.paste(croppedImage, (x_offset, y), croppedImage)

            if "a_" in armorPaths[i].lower():
                animatedFiles.append([croppedImage, armorPaths[i], x_offset, 0, 0, y])

            tempItemSpacing = imageSpacing
            armorName = armorPaths[i].lower()
            if "helmet" in armorName and not any(item in armorName for item in disallowedNames):
                tempItemSpacing = imageSpacing // 2

            y += croppedImage.height + tempItemSpacing

    elif shapeType == ShapeType.Horizontal:
        width = sum([image.width for image in croppedImageList]) + (len(armorImages)) * imageSpacing
        height = max([image.height for image in croppedImageList])
        image = Image.new("RGBA", (width - heightOffset, height), (0, 0, 0, 0))

        x = 0
        for i, croppedImage in enumerate(croppedImageList):
            y_offset = (height - croppedImage.height) // 2
            image.paste(croppedImage, (x, y_offset), croppedImage)

            if "a_" in armorPaths[i].lower():
                animatedFiles.append([croppedImage, armorPaths[i], 0, y_offset, x, 0])

            # tempItemSpacing = imageSpacing
            # armorName = armorPaths[i].lower()
            # if "helmet" in armorName and not any(item in armorName for item in disallowedNames):
            #     tempItemSpacing = imageSpacing // 2

            x += croppedImage.width + imageSpacing

    elif shapeType == ShapeType.Square:
        num_images = len(croppedImageList)
        grid_size = math.ceil(math.sqrt(num_images))
        max_width = max([image.width for image in croppedImageList])
        max_height = max([image.height for image in croppedImageList])

        square_size = grid_size * max(max_width, max_height) + (grid_size - 1) * imageSpacing
        image = Image.new("RGBA", (square_size, square_size), (0, 0, 0, 0))

        for i, croppedImage in enumerate(croppedImageList):
            row = i // grid_size
            col = i % grid_size

            x_offset = col * (max_width + imageSpacing) + (max_width - croppedImage.width) // 2
            y_offset = row * (max_height + imageSpacing) + (max_height - croppedImage.height) // 2

            image.paste(croppedImage, (x_offset, y_offset), croppedImage)

            if "a_" in armorPaths[i].lower():
                animatedFiles.append([croppedImage, armorPaths[i], x_offset, y_offset, 0, 0])

    animatedDuration = 0
    if len(animatedFiles) > 0:
        frames = []
        for animatedImage, armorPath, x_offset, y_offset, x, y in animatedFiles:
            reader = imageio.get_reader(armorPath)
            i = -1
            for frame in reader:
                i += 1
                frameMeta = reader.get_meta_data(index=i)
                frameDuration = frameMeta.get("duration", 0)
                animatedDuration += frameDuration

                frameImage = Image.fromarray(frame).resize((imageSize, imageSize)).convert("RGBA")
                bbox = frameImage.getbbox()
                if bbox:
                    frameImage = frameImage.crop(bbox)

                baseImage = image.copy()
                baseImage.paste(frameImage, (x_offset, y))
                frames.append(baseImage)

        image = frames

    returnHexList = []
    for baseHex in finalHexColorList:
        if baseHex == "" or baseHex is None:
            continue
        returnHexList.append(baseHex)

    return image, returnHexList, animatedDuration

def GetArmorPiecePath(itemType: ItemType) -> str:
    return f"Images/{itemType}.png"

def GetItemPathResolution(basePath, versionType, imageSize):
    validSplits = ["Leather", "EmptyImage"]
    for split in validSplits:
        if split in basePath:
            if str(versionType) not in basePath:
                splitPath = basePath.split(split)
                basePath = f"{splitPath[0]}{versionType}{split}{splitPath[1]}"

            if "128x" not in basePath and "256x" not in basePath:
                targetSize = "256x"
                if imageSize == 128:
                    targetSize = "128x"
                elif imageSize == 256:
                    targetSize = "256x"

                splitPath = basePath.split("/")
                basePath = f"{splitPath[0]}/{targetSize}{splitPath[1]}"

    return basePath

def CreateArmorPieceImage(
        itemType: ItemType = None,
        baseImage: Image.Image = None,
        overlayImage: Image.Image = None,
        basePath: str = None,
        overlayPath: str = None,
        overlayColor: HexColor|str = None,
        imageSize: int = 128,
        versionType: VersionType = VersionType._1_8_9
) -> Image.Image:
    if itemType is not None:
        basePath = GetArmorPiecePath(itemType)
        overlayPath = GetOverlayImage(basePath)

    if baseImage is None and basePath is None:
        raise ValueError("Either 'baseImage' or 'basePath' must be provided for the base image.")
    if overlayImage is None and overlayPath is None:
        overlayPath = GetOverlayImage(basePath)

    if basePath is not None:
        basePath = GetItemPathResolution(basePath, versionType, imageSize)
    if overlayPath is not None:
        overlayPath = GetItemPathResolution(overlayPath, versionType, imageSize)

    if baseImage is None:
        baseImage = Image.open(basePath).resize((imageSize, imageSize)).convert("RGBA")
    if overlayImage is None and overlayPath is not None:
        overlayImage = Image.open(overlayPath).resize((imageSize, imageSize)).convert("RGBA")

    if overlayColor is None or not overlayColor:
        return baseImage
    # elif type(overlayColor) == str:
    #     tintColor = GetRBGFromHex(GetFixedHex(tintColor))

    tintedImage = ApplyColorTint(baseImage=baseImage, overlayColor=overlayColor, imageSize=imageSize)

    if overlayImage is not None:
        tintedImage = AddImageOverlay(baseImage=tintedImage, overlayImage=overlayImage, imageSize=imageSize)
    return tintedImage

def AddImageOverlay(
    baseImage: Image.Image = None,
    overlayImage: Image.Image = None,
    basePath: str = None,
    overlayPath: str = None,
    imageSize: int = 128
) -> Image.Image:
    if baseImage is None and basePath is None:
        raise ValueError("Either 'baseImage' or 'basePath' must be provided for the base image.")
    if overlayImage is None and overlayPath is None:
        raise ValueError("Either 'overlayImage' or 'overlayPath' must be provided for the overlay image.")

    if baseImage is None:
        baseImage = Image.open(basePath).resize((imageSize, imageSize)).convert("RGBA")
    if overlayImage is None:
        overlayImage = Image.open(overlayPath).resize((imageSize, imageSize)).convert("RGBA")

    tempImage = Image.new("RGBA", baseImage.size, (0, 0, 0, 0))
    tempImage.paste(overlayImage, (0, 0), mask=overlayImage)

    result_image = Image.alpha_composite(baseImage, tempImage)

    return result_image

def ApplyColorTint(
    baseImage: Image.Image = None,
    basePath: str = None,
    overlayColor: HexColor = None,
    imageSize: int = 128
) -> Image.Image:
    if baseImage is None and basePath is None:
        raise ValueError("Either 'baseImage' or 'basePath' must be provided for the base image.")

    if baseImage is None:
        baseImage = Image.open(basePath).resize((imageSize, imageSize)).convert("RGBA")

    if overlayColor is None:
        overlayColor = HexColor("FFFFFF")

    [r, g, b] = overlayColor.GetRGBList()
    tintImage = Image.new("RGBA", baseImage.size, (r, g, b, 255))

    tinted = Image.new("RGBA", baseImage.size)
    for x in range(baseImage.width):
        for y in range(baseImage.height):
            orig_r, orig_g, orig_b, orig_a = baseImage.getpixel((x, y))
            tint_r, tint_g, tint_b, _ = tintImage.getpixel((x, y))
            new_r = int((orig_r * tint_r) / 255)
            new_g = int((orig_g * tint_g) / 255)
            new_b = int((orig_b * tint_b) / 255)
            tinted.putpixel((x, y), (new_r, new_g, new_b, orig_a))

    return tinted

# def MixHexList(startHex, hexList):
#     startRGB = GetRBGFromHex(startHex)
#     rgbList = []
#     for baseHex in hexList:
#         rgb = GetRBGFromHex(baseHex)
#         rgbList.append(rgb)
#     result = MixRGBList(startRGB, rgbList)
#     return GetHexFromRGB(result)
def MixHexColorList(startHexColor, hexColorList):
    startRGB = startHexColor.GetRGBList()
    rgbList = []
    for hexColor in hexColorList:
        rgbList.append(hexColor.GetRGBList())
    result = MixRGBList(startRGB, rgbList)
    return HexColor(rgb=result)
def MixRGBList(startRGB, rgbList):
    if len(rgbList) > 8:
        colorList = rgbList[:8]
        remainingList = rgbList[8:]
        startRGB = MixRGBList(startRGB, colorList)
        return MixRGBList(startRGB, remainingList)

    redSum = greenSum = blueSum = 0
    maxSum = 0
    itemCount = 0

    redSum += startRGB[0]
    greenSum += startRGB[1]
    blueSum += startRGB[2]
    maxSum += max(startRGB)
    itemCount += 1

    for rgb in rgbList:
        red, green, blue = rgb
        redSum += red
        greenSum += green
        blueSum += blue
        maxSum += max(rgb)
        itemCount += 1

    redAverage = int(np.float32(redSum) / np.float32(itemCount))
    greenAverage = int(np.float32(greenSum) / np.float32(itemCount))
    blueAverage = int(np.float32(blueSum) / np.float32(itemCount))

    overall = np.float32(maxSum) / np.float32(itemCount)
    maxRGB = max(redAverage, greenAverage, blueAverage)
    base = np.float32(overall) / np.float32(maxRGB)

    red = int(redAverage * base)
    green = int(greenAverage * base)
    blue = int(blueAverage * base)

    return [red, green, blue]

def GetCombinedArmorSetBuffer(armorType, hexList, shapeType, versionType = VersionType._1_8_9, imageSpacing = 20, imageSize = 128):
    armorSet, colors, duration = CreateArmorSetImage(
        armorType=armorType,
        hexList=hexList,
        versionType=versionType,
        shapeType=shapeType,
        imageSpacing=imageSpacing,
        imageSize=imageSize
    )
    if duration > 0:
        duration = int(duration / 1000)

    buffer = io.BytesIO()
    filePath = "armorSet.png"
    if type(armorSet) == list:
        filePath = "armorSet.webp"
        armorSet[0].save(
            buffer,
            save_all=True,
            append_images=armorSet[1:],
            duration=duration,
            loop=0,
            quality=100,
            method=3,
            format="WEBP",
            lossless=True
        )
    else:
        armorSet.save(
            buffer,
            format="PNG",
            quality=100,
            # method=3,
            lossless=True
        )

    buffer.seek(0)
    return buffer, filePath, colors

def GetColorStatusType(baseHex):
    if baseHex in stringToColorDict:
        matchingTypes = set()
        for name, color in Color.__members__.items():
            if color.value[1] == baseHex:
                matchingTypes.add(color.value[2])

        matchingTypes = list(matchingTypes)

        validTypes = [
            ColorType.PureDye,
            ColorType.TrueDye,
            ColorType.Crystal,
            ColorType.Armor,
            ColorType.HypixelDye,
            ColorType.Bleached,
        ]

        if any(item in matchingTypes for item in validTypes):
            return matchingTypes
        elif ColorType.Fairy in matchingTypes:
            fairyData = allFairyHexes[stringToColorDict[baseHex]]
            return matchingTypes, fairyData

    return [ColorType._None]

def GetColorStatusText(hexColor):
    if hexColor is  None:
        raise ValueError("Hex color is not set.")

    typeString = ""
    explanationString = ""

    fixedHex = hexColor.GetHexCode()
    colorStatus = GetColorStatusType(fixedHex)

    if type(colorStatus) == tuple:
        colorType = colorStatus[0][0]
        if colorType == ColorType.Fairy:
            fairyList = colorStatus[1][0]
            ogFairyList = colorStatus[1][1]

            if len(fairyList) > 0:
                typeString = "Fairy"

                explanationString += "**Fairy** when applied to "
                if fairyList == ["All"]:
                    explanationString += "any armor piece."
                else:
                    explanationString += "the following pieces: "
                    for i, armorPiece in enumerate(fairyList):
                        if i == 0:
                            explanationString += f"**{armorPiece}**"
                            continue
                        explanationString += f", **{armorPiece}**"

            if len(ogFairyList) > 0:
                if len(fairyList) > 0:
                    typeString += " or OG Fairy"
                    explanationString += "\n"
                else:
                    typeString = "OG Fairy"

                explanationString += "**OG Fairy** when applied to "
                if ogFairyList == ["All"]:
                    explanationString += "any armor piece."
                else:
                    explanationString += "the following pieces: "
                    for i, armorPiece in enumerate(ogFairyList):
                        if i == 0:
                            explanationString += f"**{armorPiece}**"
                            continue
                        explanationString += f", **{armorPiece}**"

    else:
        typeString = "likely exotic"
        if ColorType.Armor in colorStatus:
            matchingArmorString = ""
            for name, color in Color.__members__.items():
                if color.value[1] == fixedHex and color.value[2] == ColorType.Armor:
                    if matchingArmorString:
                        matchingArmorString += ", "

                    matchingArmorString += f"{color.value[0]}"
                    if not any(item in name for item in ["Helmet", "Chestplate", "Leggings", "Boots"]):
                        matchingArmorString += " Armor"

            if ColorType.PureDye in colorStatus:
                typeString = "a pure color"
                explanationString = f"It is likely **exotic** unless it's applied to any of the following armors:\n**{matchingArmorString}**"
            else:
                typeString = "likely exotic"
                explanationString += f"Unless it's applied to any of the following armors:\n**{matchingArmorString}**"

        elif ColorType.PureDye in colorStatus:
            typeString = "a pure color"

        elif ColorType.TrueDye in colorStatus:
            typeString = "a true color"

        elif ColorType.Crystal in colorStatus:
            typeString = "Crystal dyed"

        elif ColorType.Bleached in colorStatus:
            typeString = "Bleached"

        elif ColorType.HypixelDye in colorStatus:
            colorEnum = stringToColorDict[fixedHex]
            typeString = f"{colorEnum.value[0]} dyed"

    return typeString, explanationString

def MergeImagesHorizontal(*images: Image.Image):
    total_width = sum(image.size[0] for image in images)
    max_height = max(image.size[1] for image in images)

    result = Image.new(mode='RGBA', size=(total_width, max_height), color=(0, 0, 0, 0))
    x_offset = 0

    for image in images:
        width, height = image.size
        result.paste(im=image, box=(x_offset, max_height - height))
        x_offset += width

    return result

def MergeImagesVertical(image1: Image.Image, image2: Image.Image):
    (width1, height1) = image1.size
    (width2, height2) = image2.size

    resultWidth = max(width1, width2)
    resultHeight = height1 + height2

    result = Image.new(mode='RGBA', size=(resultWidth, resultHeight), color=(0, 0, 0, 0))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(0, height1))

    return result

def RGBToXYZ(rgbInt: int):
    rgb = [
        ((rgbInt >> 16) & 0xFF) / 255.0,
        ((rgbInt >> 8) & 0xFF) / 255.0,
        (rgbInt & 0xFF) / 255.0
    ]

    for i in range(len(rgb)):
        value = rgb[i]
        if value <= 0.04045:
            rgb[i] = value / 12.92
        else:
            rgb[i] = math.pow((value + 0.055) / 1.055, 2.4)

    xyzFactors = [
        0.4124, 0.3576, 0.1805,
        0.2126, 0.7152, 0.0722,
        0.0193, 0.1192, 0.9505
    ]

    def DotProduct(factors: list[float], offset: int, rgbList: list[float]):
        return sum(factors[offset + j] * rgbList[j] for j in range(3))

    return [
        DotProduct(xyzFactors, 0, rgb),
        DotProduct(xyzFactors, 3, rgb),
        DotProduct(xyzFactors, 6, rgb)
    ]

def XYZToCielab(x: float, y: float, z: float):
    refX, refY, refZ = 0.95047, 1.0, 1.08883
    x /= refX
    y /= refY
    z /= refZ

    def ConvertToLab(t: float):
        if t > 0.008856:
            return math.pow(t, 1.0 / 3.0)
        return 7.787 * t + 16.0

    return [
        116.0 * ConvertToLab(y) - 16.0,
        500.0 * (ConvertToLab(x) - ConvertToLab(y)),
        200.0 * (ConvertToLab(y) - ConvertToLab(z))
    ]

def RGBIntToCielab(rgbInt: int):
    xyz = RGBToXYZ(rgbInt)
    return XYZToCielab(xyz[0], xyz[1], xyz[2])

def HexColorToCielab(hexColor: HexColor):
    return RGBIntToCielab(hexColor.GetRGBInt())

def GetVisualDifference(hexColor1: HexColor, hexColor2: HexColor):
    targetLab = HexColorToCielab(hexColor1)
    pieceLab = HexColorToCielab(hexColor2)

    return math.sqrt(sum((targetLab[i] - pieceLab[i]) ** 2 for i in range(3)))

def GetAbsoluteDifference(hexColor1: HexColor, hexColor2: HexColor):
    rgb1 = hexColor1.GetRGBList()
    rgb2 = hexColor2.GetRGBList()

    redDifference = abs(rgb1[0] - rgb2[0])
    greenDifference = abs(rgb1[1] - rgb2[1])
    blueDifference = abs(rgb1[2] - rgb2[2])

    absoluteDifference = redDifference + greenDifference + blueDifference
    return absoluteDifference

def GetHexDifference(hexColor1: HexColor, hexColor2: HexColor):
    absoluteDifference = GetAbsoluteDifference(hexColor1, hexColor2)
    visualDifference = GetVisualDifference(hexColor1, hexColor2)

    return absoluteDifference, visualDifference

def GetArmorType(itemString: str):
    itemString = itemString.replace("_", " ")
    armorTypeSplit = re.split('', itemString)

    currentWord = ""
    if len(armorTypeSplit) > 100:
        return None

    for i, letter in enumerate(armorTypeSplit):
        letter = letter.lower().strip()
        currentWord += letter
        for armor in ArmorType.__members__:
            if currentWord == armor.lower():
                return ArmorType[armor]
    return None

helmetNames = sorted(["helmet", "helm"], key=len, reverse=True)
chestplateNames = sorted(["chestplate", "chest", "cp"], key=len, reverse=True)
leggingsNames = sorted(["leggings", "legging", "legs", "leg", "pants", "pant"], key=len, reverse=True)
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

    if doPrint:
        print(f"2 {itemString} - {armorTypeName}")

    for name in helmetNames + chestplateNames + leggingsNames + bootsNames:
        armorTypeName = armorTypeName.replace(name, "").strip()

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

def MinMaxHexInt(hexInt: int):
    return min(max(hexInt, 0), 16777215)