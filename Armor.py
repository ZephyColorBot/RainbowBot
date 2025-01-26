import math
import imageio

from PIL import Image, ImageDraw
from typing import Optional
from Constants import *

def CreateColorSquare(colors):
    side = math.ceil(math.sqrt(len(colors)))
    rows = math.ceil(len(colors) / side)
    width = side * 100
    height = rows * 100

    image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    for i, color in enumerate(colors):
        row = i // side
        col = i % side
        x0, y0 = col * 100, row * 100
        x1, y1 = x0 + 99, y0 + 99

        draw.rectangle([x0, y0, x1, y1], fill=tuple(color))

    return image

def GetOverlayImage(imagePath):
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

def GetFixedHex(baseHex):
    if baseHex is None:
        return "000000"
    if type(baseHex) is list:
        baseHex = GetHexFromRGB(baseHex)

    baseHex = baseHex.lower().strip()
    if baseHex in stringToColorTypeDict:
        baseHex = stringToColorTypeDict[baseHex].value[1]

    baseHex = baseHex.upper().replace(',', '')
    baseHex = baseHex.lstrip('#').strip()
    baseHex = baseHex.rjust(6, '0')
    return baseHex

def GetRBGFromHex(baseHex):
    color = list(int(baseHex[i:i+2], 16) for i in (0, 2, 4))
    r = color[0]
    g = color[1]
    b = color[2]
    return [r, g, b]

def GetHexFromRGB(rgb):
    return '%02x%02x%02x' % tuple(rgb)

def CreateArmorSetImage(armorType, hexList, displayType, versionType = VersionType._1_8_9, imageSpacing = 20, imageSize = 128):
    if armorType not in itemDict:
        raise ValueError(f"Invalid armor type '{armorType}'")

    armorType = itemDict[armorType]
    armorImages = armorType[0]

    imageSpacing *= math.ceil(imageSize / 128)

    finalHexList = []
    i = 0
    lastHex = None
    for armorHexes in enumerate(armorType[1]):
        if not armorHexes[1]:
            finalHexList.append(armorHexes[1])
            continue

        i += 1
        if i <= len(hexList):
            finalHexList.append(hexList[i - 1])
            lastHex = hexList[i - 1]
        else:
            if lastHex is not None:
                finalHexList.append(lastHex)
            else:
                finalHexList.append(armorHexes[1])

    # if len(finalHexList) != i:
    #     raise ValueError(f"Invalid number of hex codes for '{armorTypeString}'")

    armorPaths = [f"Images/{image}" for image in armorImages]
    armorImages = [CreateArmorPieceImage(basePath=image, tintColor=finalHexList[i], versionType=versionType, imageSize=imageSize) for i, image in enumerate(armorPaths)]

    croppedImageList = []
    for armorImage in armorImages:
        bbox = armorImage.getbbox()
        if bbox:
            croppedImage = armorImage.crop(bbox)
            croppedImageList.append(croppedImage)

    image = None
    animatedFiles = []
    if displayType == DisplayType.Vertical:
        width = max([image.width for image in croppedImageList])
        height = sum([image.height for image in croppedImageList]) + (len(armorImages) - 1) * imageSpacing

        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        y = 0
        for i, croppedImage in enumerate(croppedImageList):
            x_offset = (width - croppedImage.width) // 2
            image.paste(croppedImage, (x_offset, y), croppedImage)

            tempItemSpacing = imageSpacing
            if "a_" in armorPaths[i].lower():
                animatedFiles.append([croppedImage, armorPaths[i], x_offset, 0, 0, y])

            armorName = armorPaths[i].lower()
            if "helmet" in armorPaths[i].lower() and "leather" not in armorName:
                tempItemSpacing = tempItemSpacing // 2

            y += croppedImage.height + tempItemSpacing

    elif displayType == DisplayType.Horizontal:
        width = sum([image.width for image in croppedImageList]) + (len(armorImages) - 1) * imageSpacing
        height = max([image.height for image in croppedImageList])
        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        x = 0
        for i, croppedImage in enumerate(croppedImageList):
            y_offset = (height - croppedImage.height) // 2
            image.paste(croppedImage, (x, y_offset), croppedImage)

            tempItemSpacing = imageSpacing
            if "a_" in armorPaths[i].lower():
                animatedFiles.append([croppedImage, armorPaths[i], 0, y_offset, x, 0])

            armorName = armorPaths[i].lower()
            if "helmet" in armorPaths[i].lower() and "leather" not in armorName:
                tempItemSpacing = tempItemSpacing // 2

            x += croppedImage.width + tempItemSpacing

    elif displayType == DisplayType.Square:
        num_images = len(croppedImageList)
        grid_size = math.ceil(math.sqrt(num_images))
        max_width = max([image.width for image in croppedImageList])
        max_height = max([image.height for image in croppedImageList])

        square_size = grid_size * max(max_width, max_height) + (grid_size - 1) * imageSpacing
        image = Image.new("RGBA", (square_size, square_size), (0, 0, 0, 0))

        # boot_index = None
        # for i, armorPath in enumerate(armorPaths):
        #     if "boot" in armorPath.lower():
        #         boot_index = i
        #         break

        # total_rows = math.ceil(num_images / grid_size)
        # grid_height = total_rows * (max_height + imageSpacing) - imageSpacing

        for i, croppedImage in enumerate(croppedImageList):
            row = i // grid_size
            col = i % grid_size

            x_offset = col * (max_width + imageSpacing) + (max_width - croppedImage.width) // 2

            # if i == boot_index:
            #     y_offset = grid_height - croppedImage.height
            # else:
            y_offset = row * (max_height + imageSpacing) + (max_height - croppedImage.height) // 2

            image.paste(croppedImage, (x_offset, y_offset), croppedImage)

            if "a_" in armorPaths[i].lower():
                animatedFiles.append([croppedImage, armorPaths[i], x_offset, y_offset, 0, 0])

    if len(animatedFiles) > 0:
        frames = []
        for animatedImage, armorPath, x_offset, y_offset, x, y in animatedFiles:
            reader = imageio.get_reader(armorPath)
            for frame in reader:
                frameImage = Image.fromarray(frame).resize((imageSize, imageSize)).convert("RGBA")
                bbox = frameImage.getbbox()
                if bbox:
                    frameImage = frameImage.crop(bbox)

                baseImage = image.copy()
                baseImage.paste(frameImage, (x_offset, y))
                frames.append(baseImage)

        image = frames

    returnHexList = []
    for baseHex in finalHexList:
        if baseHex == "" or baseHex is None:
            continue
        returnHexList.append(baseHex)

    return image, returnHexList

def GetArmorPiecePath(itemType: ItemType) -> str:
    return f"Images/{itemType}.png"

def GetItemPathResolution(basePath, versionType, imageSize):
    if "Leather" in basePath:
        if str(versionType) not in basePath:
            splitPath = basePath.split("Leather")
            basePath = f"{splitPath[0]}{versionType}Leather{splitPath[1]}"

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
        itemType: Optional[ItemType] = None,
        baseImage: Optional[Image.Image] = None,
        overlayImage: Optional[Image.Image] = None,
        basePath: Optional[str] = None,
        overlayPath: Optional[str] = None,
        tintColor: Optional[any] = None,
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

    if tintColor is None or tintColor == "":
        return baseImage
    elif type(tintColor) == str:
        tintColor = GetRBGFromHex(GetFixedHex(tintColor))

    tintedImage = ApplyColorTint(baseImage=baseImage, overlayColor=tintColor, imageSize=imageSize)

    if overlayImage is not None:
        tintedImage = AddImageOverlay(baseImage=tintedImage, overlayImage=overlayImage, imageSize=imageSize)
    return tintedImage

def AddImageOverlay(
    baseImage: Optional[Image.Image] = None,
    overlayImage: Optional[Image.Image] = None,
    basePath: Optional[str] = None,
    overlayPath: Optional[str] = None,
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
    baseImage: Optional[Image.Image] = None,
    basePath: Optional[str] = None,
    overlayColor: Optional[any] = None,
    imageSize: int = 128
) -> Image.Image:
    if baseImage is None and basePath is None:
        raise ValueError("Either 'baseImage' or 'basePath' must be provided for the base image.")

    if baseImage is None:
        baseImage = Image.open(basePath).resize((imageSize, imageSize)).convert("RGBA")

    if overlayColor is None:
        overlayColor = [160, 101, 64]

    [r, g, b] = overlayColor
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