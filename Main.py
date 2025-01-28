import re
import discord

from discord.ext import commands
from discord import app_commands
from Armor import *

# TODO: off pure checker command

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

        try:
            synced = await self.tree.sync()
            print(f'Synced {synced} commands')
        except Exception as e:
            print(f'Failed to sync commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'hello':
            await message.channel.send('Hello!')

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix='/', intents=intents)

shape_choices = [
    app_commands.Choice(name="Vertical", value="Vertical"),
    app_commands.Choice(name="Horizontal", value="Horizontal"),
    app_commands.Choice(name="Square", value="Square"),
]
armor_version_choices = [
    app_commands.Choice(name="1.8.9", value="1.8.9"),
    app_commands.Choice(name="1.14+", value="1.14+")
]

async def armor_type_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=str(option), value=str(option))
        for option in itemDict if current.lower() in str(option).lower()
    ][:25]
async def armor_color_type_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=str(option.value[0]), value=str(option.value[0]))
        for option in list(Color) if current.lower() in str(option.value[0]).lower()
    ][:25]

colorCommandDescription = 'Generate hex code images.'
colorCommandColorsDescription = 'Enter a list of hex codes separated by spaces (e.g., #334CB2 #191919)'

armorCommandDescription = 'Displays an armor set with the given hex color(s).'
armorCommandColorsDescription = 'Enter a list of hex codes separated by spaces (e.g., #334CB2 #191919)'
armorCommandArmorDescription = 'Enter the armor type. (e.g., Superior, Young Baby)'
armorCommandShapeDescription = 'Enter the armor shape. (e.g., Vertical, Horizontal, Square)'
armorCommandVersionDescription = 'Enter the armor version. (e.g., 1.8.9, 1.14+)'

exoticCommandDescription = 'Checks the type of a given hex.'
exoticCommandColorDescription = 'Enter a hex code.'

mixCommandDescription = 'Mixes the given hexes and displays the result.'
mixCommandColorsDescription = 'Enter a list of hex codes, they will be combined one by one. (Same as crafting after each dye)'
mixCommandCraftingSequence1Description = 'Enter a list of hex codes, they will be combined in one crafting step.'
mixCommandCraftingSequence2Description = 'Enter a list of hex codes, they will be combined in two crafting steps.'
mixCommandCraftingSequence3Description = 'Enter a list of hex codes, they will be combined in three crafting steps.'
mixCommandOutputArmorDescription = 'Enter the armor type. (e.g., Superior, Young Baby)'
mixCommandOutputShapeDescription = 'Enter the armor shape. (e.g., Vertical, Horizontal, Square)'
mixCommandOutputVersionDescription = 'Enter the armor version. (e.g., 1.8.9, 1.14+)'

helpCommandDescription = 'Displays information about the bot.'

hexDifferenceCommandDescription = 'Displays the absolute and euclidian difference between two hexes.'
hexDifferenceCommandColor1Description = 'Enter the first hex code.'
hexDifferenceCommandColor2Description = 'Enter the second hex code.'

@client.tree.command(name='color', description=colorCommandDescription, extras={"contexts": [0, 1, 2], "integration_types": [0, 1]})
@app_commands.describe(colors=colorCommandColorsDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColor(interaction, colors: str):
    originalHexList = re.split(r'(\s)', colors)
    originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]

    colorList = []
    colorString = ""
    for baseHex in originalHexList:
        hexColor = HexColor(baseHex)
        colorList.append(hexColor)

        if colorString != "":
            colorString += ", "
        colorString += f"#{hexColor.GetHexCode()}"

    buffer = io.BytesIO()
    image = CreateColorSquare(colorList)
    image.save(buffer, "PNG")
    buffer.seek(0)

    discordFile = discord.File(buffer, filename="colorSquare.png")
    await interaction.response.send_message(f"**{colorString}**", file=discordFile)
@client.tree.command(name='colour', description=colorCommandDescription)
@app_commands.describe(colors=colorCommandColorsDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColour(interaction: discord.Interaction, colors: str):
    await displayColor.callback(interaction, colors)

@client.tree.command(name='armor', description=armorCommandDescription)
@app_commands.choices(shape=shape_choices, version=armor_version_choices)
@app_commands.autocomplete(armor=armor_type_autocomplete, colors=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    colors=armorCommandColorsDescription,
    armor=armorCommandArmorDescription,
    shape=armorCommandShapeDescription,
    version=armorCommandVersionDescription
)
async def displayArmor(interaction, colors: str = None, armor: str = None, shape: str = None, version: str = None):
    if colors is None and armor is None:
        await interaction.response.send_message("Please provide at least one hex code or armor type.")
        return

    if colors is None:
        colors = []
    if armor is None:
        armor = "Full Set"
    if shape is None:
        shape = "Vertical"
    if version is None:
        version = "1.8.9"

    if type(armor) == str:
        armor = armor.lower().replace(' ', '').strip()
    if type(shape) == str:
        shape = shape.lower().replace(' ', '').strip()
    if type(version) == str:
        version = version.lower().replace(' ', '').strip()

    if armor not in stringToArmorTypeDict:
        await interaction.response.send_message(f"Invalid armor type '{armor}'")
        return
    if shape not in stringToShapeTypeDict:
        await interaction.response.send_message(f"Invalid shape type '{shape}'")
        return
    if version not in stringToVersionTypeDict:
        await interaction.response.send_message(f"Invalid version type '{version}'")
        return

    armorEnum = stringToArmorTypeDict[armor]
    shapeEnum = stringToShapeTypeDict[shape]
    versionEnum = stringToVersionTypeDict[version]

    colorList = []
    colorString = ""
    if type(colors) == str:
        originalHexList = re.split(r'(\s)', colors)
        originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]

        for baseHex in originalHexList:
            colorList.append(HexColor(baseHex))

    buffer, filePath, colors = GetCombinedArmorSetBuffer(
        armorType=armorEnum,
        hexList=colorList,
        versionType=versionEnum,
        shapeType=shapeEnum,
        imageSpacing=20,
        imageSize=128
    )
    for baseHex in colors:
        if colorString != "":
            colorString += ", "
        colorString += f"#{baseHex.GetHexCode()}"

    discordFile = discord.File(buffer, filename=filePath)
    await interaction.response.send_message(f"**{colorString}**", file=discordFile)
@client.tree.command(name='armour', description=armorCommandDescription)
@app_commands.choices(shape=shape_choices, version=armor_version_choices)
@app_commands.autocomplete(armor=armor_type_autocomplete, colors=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    colors=armorCommandColorsDescription,
    armor=armorCommandArmorDescription,
    shape=armorCommandShapeDescription,
    version=armorCommandVersionDescription
)
async def displayArmour(interaction, colors: str = None, armor: str = None, shape: str = None, version: str = None):
    await displayArmor.callback(interaction, colors, armor, shape, version)

@client.tree.command(name='advancedmix', description=mixCommandColorsDescription)
@app_commands.choices(outputshape=shape_choices, outputversion=armor_version_choices)
@app_commands.autocomplete(craftingsequence1=armor_color_type_autocomplete, craftingsequence2=armor_color_type_autocomplete, craftingsequence3=armor_color_type_autocomplete, outputarmor=armor_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    craftingsequence1=mixCommandCraftingSequence1Description,
    craftingsequence2=mixCommandCraftingSequence2Description,
    craftingsequence3=mixCommandCraftingSequence3Description,
    outputarmor=mixCommandOutputArmorDescription,
    outputshape=mixCommandOutputShapeDescription,
    outputversion=mixCommandOutputVersionDescription
)
async def displayAdvancedMix(
        interaction: discord.Interaction,
        craftingsequence1: str,
        craftingsequence2: str = None,
        craftingsequence3: str = None,
        outputarmor: str = None,
        outputshape: str = None,
        outputversion: str = None):
    await displayMix(interaction, None, craftingsequence1, craftingsequence2, craftingsequence3, outputarmor, outputshape, outputversion)

@client.tree.command(name='mix', description=mixCommandColorsDescription)
@app_commands.choices(outputshape=shape_choices, outputversion=armor_version_choices)
@app_commands.autocomplete(colors=armor_color_type_autocomplete, outputarmor=armor_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    colors=mixCommandColorsDescription,
    outputarmor=mixCommandOutputArmorDescription,
    outputshape=mixCommandOutputShapeDescription,
    outputversion=mixCommandOutputVersionDescription
)
async def displaySimpleMix(
        interaction: discord.Interaction,
        colors: str,
        outputarmor: str = None,
        outputshape: str = None,
        outputversion: str = None):
    await displayMix(interaction, colors, None, None, None, outputarmor, outputshape, outputversion)

async def displayMix(
        interaction: discord.Interaction,
        colors: str = None,
        craftingsequence1: str = None,
        craftingsequence2: str = None,
        craftingsequence3: str = None,
        outputarmor: str = None,
        outputshape: str = None,
        outputversion: str = None
):
    if colors is None and craftingsequence1 is None and craftingsequence2 is None and craftingsequence3 is None:
        await interaction.response.send_message("Please provide at least two hex codes to mix.")
        return

    if craftingsequence1 is None and (craftingsequence2 is not None or craftingsequence3 is not None):
        raise ValueError("Error: Cannot complete step 2 or 3 without step 1.")
    if craftingsequence2 is None and craftingsequence3 is not None:
        raise ValueError("Error: Cannot complete step 3 without step 2.")

    if colors is not None and (craftingsequence1 is not None or craftingsequence2 is not None or craftingsequence3 is not None):
        raise ValueError("Error: Cannot combine colors with crafting sequences.")

    inputColorList = []
    finalHex = None
    colorString = ""
    if colors is None:
        if craftingsequence1 is not None:
            colorSplit = re.split(r'(\s)', craftingsequence1)
            inputColorList += [[x for i, x in enumerate(colorSplit) if i % 2 == 0]]

            if craftingsequence2 is not None:
                colorSplit = re.split(r'(\s)', craftingsequence2)
                inputColorList += [[x for i, x in enumerate(colorSplit) if i % 2 == 0]]

                if craftingsequence3 is not None:
                    colorSplit = re.split(r'(\s)', craftingsequence3)
                    inputColorList += [[x for i, x in enumerate(colorSplit) if i % 2 == 0]]

        i = -1
        for colorList in inputColorList:
            i += 1
            if colorString != "":
                colorString += "\n"
            colorString += f"__Step {i+1}:__ "

            hexColorList = []
            tempColorString = ""
            for baseHex in colorList:
                hexColor = HexColor(baseHex)
                hexColorList.append(hexColor)

                if tempColorString != "":
                    tempColorString += " + "
                tempColorString += f"#{hexColor.GetHexCode()}"

            colorString += tempColorString

            if finalHex is None:
                finalHex = MixHexColorList(hexColorList[0], hexColorList[1:])
            else:
                finalHex = MixHexColorList(finalHex, hexColorList)
    else:
        colorSplit = re.split(r'(\s)', colors)
        inputColorList += [[x for i, x in enumerate(colorSplit) if i % 2 == 0]]

        for colorList in inputColorList:
            hexList = []
            for baseHex in colorList:
                hexColor = HexColor(baseHex)
                hexList.append(hexColor)

            for baseHex in hexList:
                if colorString != "":
                    colorString += " + "
                colorString += f"#{baseHex.GetHexCode()}"

                if finalHex is None:
                    finalHex = baseHex
                else:
                    finalHex = MixHexColorList(finalHex, [baseHex])

    colorString += f" = #{finalHex.GetHexCode()}"
    if outputarmor is not None or outputshape is not None or outputversion is not None:
        if outputarmor is None:
            outputarmor = "Full Set"
        if outputshape is None:
            outputshape = "Vertical"
        if outputversion is None:
            outputversion = "1.8.9"

        if type(outputarmor) == str:
            outputarmor = outputarmor.lower().replace(' ', '').strip()
        if type(outputshape) == str:
            outputshape = outputshape.lower().replace(' ', '').strip()
        if type(outputversion) == str:
            outputversion = outputversion.lower().replace(' ', '').strip()

        if outputarmor not in stringToArmorTypeDict:
            await interaction.response.send_message(f"Invalid armor type '{outputarmor}'")
            return
        if outputshape not in stringToShapeTypeDict:
            await interaction.response.send_message(f"Invalid shape type '{outputshape}'")
            return
        if outputversion not in stringToVersionTypeDict:
            await interaction.response.send_message(f"Invalid version type '{outputversion}'")
            return

        armorEnum = stringToArmorTypeDict[outputarmor]
        shapeEnum = stringToShapeTypeDict[outputshape]
        versionEnum = stringToVersionTypeDict[outputversion]

        buffer, filePath, colors = GetCombinedArmorSetBuffer(
            armorType=armorEnum,
            hexList=[finalHex.GetRGBList()],
            versionType=versionEnum,
            shapeType=shapeEnum,
            imageSpacing=20,
            imageSize=128
        )
    else:
        filePath = "colorSquare.png"
        buffer = io.BytesIO()
        image = CreateColorSquare([finalHex])
        image.save(buffer, "PNG")
        buffer.seek(0)

    discordFile = discord.File(buffer, filename=filePath)
    await interaction.response.send_message(f"**{colorString}**", file=discordFile)

@client.tree.command(name='help', description=helpCommandDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def helpCommand(interaction):
    embed = discord.Embed(
        title = "Rainbow",
        description = "A useful bot for your exotics needs.",
        color = discord.Color(0x7FCC19)
    )
    embed.add_field(name = "", value = "", inline = False)

    embed.add_field(
        name = "/help",
        value = "Displays this message.",
        inline = False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name = "/armor <[[<hexes>], [<armor>]]> [<shape>] [<version>]",
        value = "Displays an armor set with the given hex color(s).\n-# Optional Armor Type and Shape Type.\n-# Aliases: /armour",
        inline = False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name = "/color <hexes>",
        value = "Displays the given hex color(s).\n-# Aliases: /colour",
        inline = False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name = "/exotic <hex>",
        value = "Checks the type of a given hex.\n-# Aliases: /fairy, /crystal",
        inline = False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name = "/mix <hexes>",
        value = "Mixes the given hexes and displays the result.",
        inline = False
    )
    embed.add_field(name="", value="", inline=False)

    embed.set_footer(text="Made by zeph.y", icon_url="https://cdn.discordapp.com/avatars/1000919610251558993/7c7d0e2f2d831a5241b9053fd0ca6fd1.webp")
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed)

@client.tree.command(name='exotic', description=exoticCommandDescription)
@app_commands.describe(color=exoticCommandColorDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColorStatusExotic(interaction, color: str):
    hexColor = HexColor(color)
    statusString, explanationString = GetColorStatusText(hexColor)

    embed = discord.Embed(
        title = f"__**#{hexColor.GetHexCode()}**__ is {statusString}.",
        description = f"{explanationString}",
        color = discord.Color(int(f"0x{hexColor.GetHexCode()}", 16))
    )
    embed.add_field(name = "", value = "", inline = False)

    embed.set_image(url=f"https://blargbot.xyz/color/{hexColor.GetHexCode()}")
    embed.set_footer(text="Made by zeph.y", icon_url="https://cdn.discordapp.com/avatars/1000919610251558993/7c7d0e2f2d831a5241b9053fd0ca6fd1.webp")
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed)
@client.tree.command(name='crystal', description=exoticCommandDescription)
@app_commands.describe(color=exoticCommandColorDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColorStatusCrystal(interaction, color: str):
    await displayColorStatusExotic.callback(interaction, color)
@client.tree.command(name='fairy', description=exoticCommandDescription)
@app_commands.describe(color=exoticCommandColorDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColorStatusCrystal(interaction, color: str):
    await displayColorStatusExotic.callback(interaction, color)

@client.tree.command(name='comparearmor', description=colorCommandDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayCompareArmor(
        interaction,
        armorcolor1: str,
        armorcolor2: str,
        armorcolor3: str = None,
        armorcolor4: str = None,
        armorcolor5: str = None,
        armortype1: str = None,
        armortype2: str = None,
        armortype3: str = None,
        armortype4: str = None,
        armortype5: str = None,
        shape: str = None,
        version: str = None
):
    inputArmorColorListList = [armorcolor1, armorcolor2, armorcolor3, armorcolor4, armorcolor5]
    inputArmorTypeList = [armortype1, armortype2, armortype3, armortype4, armortype5]

    if shape is None:
        shape = "Vertical"
    if version is None:
        version = "1.8.9"

    if type(shape) == str:
        shape = shape.lower().replace(' ', '').strip()
    if type(version) == str:
        version = version.lower().replace(' ', '').strip()

    if shape not in stringToShapeTypeDict:
        await interaction.response.send_message(f"Invalid shape type '{shape}'")
        return
    if version not in stringToVersionTypeDict:
        await interaction.response.send_message(f"Invalid version type '{version}'")
        return

    shapeEnum = stringToShapeTypeDict[shape]
    versionEnum = stringToVersionTypeDict[version]

    finalImageList = []
    for i in range(5):
        if inputArmorColorListList[i] is None and inputArmorTypeList[i] is None:
            continue

        hexList = []
        if inputArmorColorListList[i] is not None:
            colorSplit = re.split(r'(\s)', inputArmorColorListList[i])
            colorSplit = [x for i, x in enumerate(colorSplit) if i % 2 == 0]

            for baseHex in colorSplit:
                hexList.append(HexColor(baseHex))

        if inputArmorTypeList[i] is None:
            armorEnum = ArmorType.FullSet
        elif inputArmorTypeList[i] in stringToArmorTypeDict:
            armorEnum = stringToArmorTypeDict[inputArmorTypeList[i].lower().replace(' ', '').strip()]
        else:
            await interaction.response.send_message(f"Invalid armor type '{inputArmorTypeList[i]}'")
            return

        ! TODO: make this work on horizontal

        buffer, filePath, colors = GetCombinedArmorSetBuffer(
            armorType=armorEnum,
            hexList=hexList,
            versionType=versionEnum,
            shapeType=shapeEnum,
            imageSpacing=20,
            imageSize=128
        )
        finalImageList.append((buffer, filePath, colors))

    if len(finalImageList) == 0:
        await interaction.response.send_message("Please provide at least one armor color or armor type.")
        return

    resultImage = Image.new(mode='RGBA', size=(0, 0), color=(0, 0, 0, 0))
    armorSpacing = 20
    for i, imageData in enumerate(finalImageList):
        buffer, filePath, colors = imageData

        if i != 0:
            resultImage = MergeImagesHorizontal(resultImage, Image.new(mode='RGBA', size=(armorSpacing, 0), color=(0, 0, 0, 0)))
        resultImage = MergeImagesHorizontal(resultImage, Image.open(buffer))

    buffer = io.BytesIO()
    resultImage.save(buffer, "PNG")
    buffer.seek(0)

    discordFile = discord.File(buffer, filename=f"armorComparison.png")
    await interaction.response.send_message(file=discordFile)

@client.tree.command(name='hexdifference', description=hexDifferenceCommandDescription)
@app_commands.describe(color1=hexDifferenceCommandColor1Description, color2=hexDifferenceCommandColor2Description)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayHexDifference(interaction, color1: str, color2: str):
    hexColor1 = HexColor(color1)
    hexColor2 = HexColor(color2)

    hex1 = hexColor1.GetHexCode()
    hex2 = hexColor2.GetHexCode()
    rgb1 = hexColor1.GetRGBList()
    rgb2 = hexColor2.GetRGBList()

    absoluteDifference, eulerDistance = GetHexDifference(hexColor1, hexColor2)
    absoluteDifferenceString = f"{absoluteDifference}"
    eulerDistanceString = f"{eulerDistance:.2f}"

    explanationString = f"**{color1}** ({rgb1}) and **{color2}** ({rgb2}) have an absolute difference of **{absoluteDifferenceString}** and an Euler distance of **{eulerDistanceString}**."

    colorSquare = CreateColorSquare([hexColor1, hexColor2])
    buffer = io.BytesIO()
    colorSquare.save(buffer, "PNG")
    buffer.seek(0)
    discordFile = discord.File(buffer, filename="colorSquare.png")

    embed = discord.Embed(
        title = f"__**#{hex1} vs. {hex2}**__",
        description = f"{explanationString}",
        color = discord.Color(int(f"0x{hex1}", 16))
    )
    embed.add_field(name = "", value = "", inline = False)

    embed.set_image(url=f"attachment://colorSquare.png")
    embed.set_footer(text="Made by zeph.y", icon_url="https://cdn.discordapp.com/avatars/1000919610251558993/7c7d0e2f2d831a5241b9053fd0ca6fd1.webp")
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed, file=discordFile)

with open('BotToken') as file:
    client.run(file.read().strip())