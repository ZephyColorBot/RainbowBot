import aiohttp
import discord

from discord.ext import commands
from discord import app_commands
from Database.Database import *
from openai import OpenAI
from ColorNames import *
from Armor import *

avatarLink = "https://cdn.discordapp.com/avatars/1000919610251558993/7c7d0e2f2d831a5241b9053fd0ca6fd1.webp"
footerText = "Made by zeph.y"
allowedDatabaseUsers = [
    263058850234499072 # me
]

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

        try:
            synced = await self.tree.sync()
            print(f'Synced {len(synced)} - {synced} commands')
        except Exception as e:
            print(f'Failed to sync commands: {e}')

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix='/', intents=intents)

# armorTypeHandPickedChoices = [
#     app_commands.Choice(name="Full Set", value="FullSet"),
#     app_commands.Choice(name="Baby Superior", value="BabySuperior"),
#     app_commands.Choice(name="Baby Young", value="BabyYoung"),
#     app_commands.Choice(name="Baby Wise", value="BabyWise"),
#     app_commands.Choice(name="Baby Unstable", value="BabyUnstable"),
#     app_commands.Choice(name="Baby Protector", value="BabyProtector"),
#     app_commands.Choice(name="Baby Strong", value="BabyStrong"),
#     app_commands.Choice(name="Baby Old", value="BabyOld"),
#     app_commands.Choice(name="Baby Holy", value="BabyHoly"),
#     app_commands.Choice(name="Angler", value="Angler"),
#     app_commands.Choice(name="Lapis", value="Lapis"),
#     app_commands.Choice(name="Biohazard", value="Biohazard"),
#     app_commands.Choice(name="Leaflet", value="Leaflet"),
#     app_commands.Choice(name="Tarantula", value="Tarantula"),
#     app_commands.Choice(name="Tuxedo", value="Tuxedo"),
#     app_commands.Choice(name="Spooky", value="Spooky"),
#     app_commands.Choice(name="Bat", value="Bat"),
#     app_commands.Choice(name="Blaze", value="Blaze"),
#     app_commands.Choice(name="Frozen Blaze", value="FrozenBlaze"),
#     app_commands.Choice(name="Pack", value="Pack"),
#     app_commands.Choice(name="Sponge", value="Sponge"),
#     app_commands.Choice(name="Necron Celestial", value="NecronCelestial"),
#     app_commands.Choice(name="Storm Celestial", value="StormCelestial"),
#     app_commands.Choice(name="Maxor Celestial", value="MaxorCelestial"),
#     app_commands.Choice(name="Goldor Celestial", value="GoldorCelestial"),
# ]
# colorHandPickedChoices = [
#     app_commands.Choice(name="Red", value="Red"),
#     app_commands.Choice(name="Orange", value="Orange"),
#     app_commands.Choice(name="Yellow", value="Yellow"),
#     app_commands.Choice(name="Lime", value="Lime"),
#     app_commands.Choice(name="Dark Green", value="DarkGreen"),
#     app_commands.Choice(name="Light Blue", value="LightBlue"),
#     app_commands.Choice(name="Cyan", value="Cyan"),
#     app_commands.Choice(name="Dark Blue", value="DarkBlue"),
#     app_commands.Choice(name="Pink", value="Pink"),
#     app_commands.Choice(name="Magenta", value="Magenta"),
#     app_commands.Choice(name="Purple", value="Purple"),
#     app_commands.Choice(name="Brown", value="Brown"),
#     app_commands.Choice(name="Light Grey", value="LightGrey"),
#     app_commands.Choice(name="Dark Grey", value="DarkGrey"),
#     app_commands.Choice(name="White", value="White"),
#     app_commands.Choice(name="Black", value="Black"),
#     app_commands.Choice(name="Mint", value="Mint"),
#     app_commands.Choice(name="Maroon", value="Maroon"),
#     app_commands.Choice(name="Navy", value="Navy"),
#     app_commands.Choice(name="Ice", value="Ice"),
#     app_commands.Choice(name="Gold", value="Gold"),
#     app_commands.Choice(name="Young", value="Young"),
#     app_commands.Choice(name="Unstable", value="Unstable"),
#     app_commands.Choice(name="Protector", value="Protector"),
#     app_commands.Choice(name="Wise", value="Wise")
# ]

shapeChoices = [
    app_commands.Choice(name="Vertical", value="Vertical"),
    app_commands.Choice(name="Horizontal", value="Horizontal"),
    app_commands.Choice(name="Square", value="Square"),
]
normalShapeChoices = [
    app_commands.Choice(name="Vertical", value="Vertical"),
    app_commands.Choice(name="Horizontal", value="Horizontal"),
]
armorVersionChoices = [
    app_commands.Choice(name="1.8.9", value="1.8.9"),
    app_commands.Choice(name="1.14+", value="1.14+")
]

'''
Auto complete for some reason makes discord not allow up arrow command resending.
'''

# async def armor_type_autocomplete(interaction: discord.Interaction, current: str):
#     return [
#         app_commands.Choice(name=str(option), value=str(option).replace(" ", ""))
#         for option in itemDict if current.lower() in str(option).lower()
#     ][:25]
# async def armor_color_type_autocomplete(interaction: discord.Interaction, current: str):
#     return [
#         app_commands.Choice(name=str(option.value[0]), value=str(option.value[0]).replace(" ", ""))
#         for option in list(Color) if current.lower() in str(option.value[0]).lower()
#     ][:25]

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
advancedMixCommandDescription = 'Mixes multiple hexes in steps and displays the result. (Same as adding multiple dyes at once)'
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

visualDistanceCommandDescription = 'Displays information about the visual distance between two colors.'

databaseCommandDescription = 'Scan the database for a specific hex code, item, or both.'
databaseCommandColorDescription = 'Hex code to scan for.'
databaseCommandItemNameDescription = 'ItemName or ItemId to scan for.'
databaseCommandListPlayersDescription = 'Whether the player uuids should be listed (Requires Permission).'
databaseCommandShowItemTypesDescription = 'Whether the item types should be shown.'

similarItemsCommandDescription = 'Scan the database for items close to a specific hex code.'
similarItemsCommandColorDescription = 'Hex code to scan for.'
similarItemsCommandItemNameDescription = 'ItemName or ItemId to scan for.'
similarItemsCommandToleranceDescription = 'The amount off a hex code can be.'
similarItemsCommandListPlayersDescription = 'Whether the player uuids should be listed (Requires Permission).'

colorInfoCommandDescription = 'Displays information about a specific hex code.'
colorInfoCommandColorDescription = 'Enter a hex code.'

dyeInfoCommandDescription = 'Displays all pure dye hexes.'

scanPlayerCommandDescription = 'Scan the database for a specific player. (Doesn\'t scan their current items)'
scanPlayerCommandPlayerDescription = 'Player UUID/Username to scan for.'

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
        try:
            hexColor = HexColor(baseHex=baseHex)
            colorList.append(hexColor)
        except Exception as e:
            await interaction.response.send_message(f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
            return

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
@app_commands.choices(shape=shapeChoices, version=armorVersionChoices)
# @app_commands.autocomplete(armor=armor_type_autocomplete, colors=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    colors=armorCommandColorsDescription,
    armor=armorCommandArmorDescription,
    shape=armorCommandShapeDescription,
    version=armorCommandVersionDescription
)
async def displayArmor(interaction, colors: str, armor: str = None, shape: str = None, version: str = None):
    if colors is None and armor is None:
        await interaction.response.send_message("Please provide at least one hex code or armor type.", ephemeral=True)
        return

    defaultColorNames = ["base", "none", "default", "original"]
    if colors is None or not colors or any(value in colors for value in defaultColorNames):
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
        await interaction.response.send_message(f"Invalid armor type '{armor}'", ephemeral=True)
        return
    if shape not in stringToShapeTypeDict:
        await interaction.response.send_message(f"Invalid shape type '{shape}'", ephemeral=True)
        return
    if version not in stringToVersionTypeDict:
        await interaction.response.send_message(f"Invalid version type '{version}'", ephemeral=True)
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
            try:
                hexColor = HexColor(baseHex=baseHex)
                colorList.append(hexColor)
            except Exception as e:
                await interaction.response.send_message(f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
                return

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
@app_commands.choices(shape=shapeChoices, version=armorVersionChoices)
# @app_commands.autocomplete(armor=armor_type_autocomplete, colors=armor_color_type_autocomplete)
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

@client.tree.command(name='advancedmix', description=advancedMixCommandDescription)
@app_commands.choices(outputshape=shapeChoices, outputversion=armorVersionChoices)
# @app_commands.autocomplete(craftingsequence1=armor_color_type_autocomplete, craftingsequence2=armor_color_type_autocomplete, craftingsequence3=armor_color_type_autocomplete, outputarmor=armor_type_autocomplete)
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
@app_commands.choices(outputshape=shapeChoices, outputversion=armorVersionChoices)
# @app_commands.autocomplete(colors=armor_color_type_autocomplete, outputarmor=armor_type_autocomplete)
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
        await interaction.response.send_message("Please provide at least two hex codes to mix.", ephemeral=True)
        return

    if craftingsequence1 is None and (craftingsequence2 is not None or craftingsequence3 is not None):
        await interaction.response.send_message("Please provide the first hex code to mix.", ephemeral=True)
        return
    if craftingsequence2 is None and craftingsequence3 is not None:
        await interaction.response.send_message("Please provide the second hex code to mix.", ephemeral=True)
        return
    if colors is not None and (craftingsequence1 is not None or craftingsequence2 is not None or craftingsequence3 is not None):
        await interaction.response.send_message("Error: Cannot combine colors and crafting sequences.", ephemeral=True)
        return

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
                try:
                    hexColor = HexColor(baseHex=baseHex)
                    hexColorList.append(hexColor)
                except Exception as e:
                    await interaction.response.send_message(f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
                    return

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
                try:
                    hexColor = HexColor(baseHex=baseHex)
                    hexList.append(hexColor)
                except Exception as e:
                    await interaction.response.send_message(f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
                    return

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
            await interaction.response.send_message(f"Invalid armor type '{outputarmor}'", ephemeral=True)
            return
        if outputshape not in stringToShapeTypeDict:
            await interaction.response.send_message(f"Invalid shape type '{outputshape}'", ephemeral=True)
            return
        if outputversion not in stringToVersionTypeDict:
            await interaction.response.send_message(f"Invalid version type '{outputversion}'", ephemeral=True)
            return

        armorEnum = stringToArmorTypeDict[outputarmor]
        shapeEnum = stringToShapeTypeDict[outputshape]
        versionEnum = stringToVersionTypeDict[outputversion]

        buffer, filePath, colors = GetCombinedArmorSetBuffer(
            armorType=armorEnum,
            hexList=[finalHex],
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

    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed)

@client.tree.command(name='exotic', description=exoticCommandDescription)
@app_commands.describe(color=exoticCommandColorDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColorStatusExotic(interaction, color: str):
    try:
        hexColor = HexColor(baseHex=color)
    except Exception as e:
        await interaction.response.send_message(f"Invalid hex code '{color}' - {e}", ephemeral=True)
        return

    statusString, explanationString = GetColorStatusText(hexColor)

    embed = discord.Embed(
        title = f"__**#{hexColor.GetHexCode()}**__ is {statusString}.",
        description = f"{explanationString}",
        color = discord.Color(int(f"0x{hexColor.GetHexCode()}", 16))
    )

    colorSquare = CreateColorSquare([hexColor], imageSize=128)
    buffer = io.BytesIO()
    colorSquare.save(buffer, "PNG")
    buffer.seek(0)
    discordFile = discord.File(buffer, filename="colorSquare.png")

    embed.set_image(url=f"attachment://colorSquare.png")
    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed, file=discordFile)
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
@app_commands.choices(shape=normalShapeChoices, version=armorVersionChoices)
# @app_commands.autocomplete(armor=armor_type_autocomplete, colors=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayCompareArmor(
        interaction,
        set1: str,
        set2: str = None,
        set3: str = None,
        set4: str = None,
        set5: str = None,
        shape: str = None,
        version: str = None
):
    inputItemListList = [set1, set2, set3, set4, set5]

    if shape is None:
        shape = "Vertical"
    if version is None:
        version = "1.8.9"

    if type(shape) == str:
        shape = shape.lower().replace(' ', '').strip()
    if type(version) == str:
        version = version.lower().replace(' ', '').strip()

    if shape not in stringToShapeTypeDict:
        await interaction.response.send_message(f"Invalid shape type '{shape}'", ephemeral=True)
        return
    if version not in stringToVersionTypeDict:
        await interaction.response.send_message(f"Invalid version type '{version}'", ephemeral=True)
        return

    shapeEnum = stringToShapeTypeDict[shape]
    versionEnum = stringToVersionTypeDict[version]

    finalImageList = []
    for itemList in inputItemListList:
        if itemList is None:
            continue

        currentWord = ""
        armorEnum = None

        reversedItemList = itemList[::-1]
        armorTypeSplit = re.split(r'(\s)', reversedItemList)
        armorTypeSplit = [x for i, x in enumerate(armorTypeSplit) if i % 2 == 0]
        for word in armorTypeSplit:
            word = word[::-1].strip()
            currentWord = (currentWord + word).strip()
            if currentWord in stringToArmorTypeDict:
                armorEnum = stringToArmorTypeDict[word]
                break

        if armorEnum is None:
            armorEnum = ArmorType.FullSet

        itemList = re.sub(fr' {currentWord}(?!.* {currentWord})', '', itemList, 1)

        hexList = []
        if itemList is not None:
            colorSplit = re.split(r'(\s)', itemList)
            colorSplit = [x for i, x in enumerate(colorSplit) if i % 2 == 0]

            for baseHex in colorSplit:
                try:
                    hexList.append(HexColor(baseHex=baseHex))
                except Exception as e:
                    await interaction.response.send_message(f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
                    return

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
        await interaction.response.send_message("Please provide at least one armor color or armor type.", ephemeral=True)
        return

    resultImage = Image.new(mode='RGBA', size=(0, 0), color=(0, 0, 0, 0))
    armorSpacing = 10
    for i, imageData in enumerate(finalImageList):
        buffer, filePath, colors = imageData

        if shapeEnum == ShapeType.Vertical:
            if i != 0:
                resultImage = MergeImagesHorizontal(resultImage, Image.new(mode='RGBA', size=(armorSpacing, 0), color=(0, 0, 0, 0)))
            resultImage = MergeImagesHorizontal(resultImage, Image.open(buffer))
        elif shapeEnum == ShapeType.Horizontal:
            if i != 0:
                resultImage = MergeImagesVertical(resultImage, Image.new(mode='RGBA', size=(0, armorSpacing), color=(0, 0, 0, 0)))
            resultImage = MergeImagesVertical(resultImage, Image.open(buffer))

    buffer = io.BytesIO()
    resultImage.save(buffer, "PNG")
    buffer.seek(0)

    discordFile = discord.File(buffer, filename=f"armorComparison.png")
    await interaction.response.send_message(file=discordFile)

@client.tree.command(name='hexdifference', description=hexDifferenceCommandDescription)
@app_commands.describe(color1=hexDifferenceCommandColor1Description, color2=hexDifferenceCommandColor2Description)
# @app_commands.autocomplete(color1=armor_color_type_autocomplete, color2=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayHexDifference(interaction, color1: str, color2: str):
    try:
        hexColor1 = HexColor(baseHex=color1)
    except Exception as e:
        await interaction.response.send_message(f"Invalid hex code '{color1}' - {e}", ephemeral=True)
        return
    try:
        hexColor2 = HexColor(baseHex=color2)
    except Exception as e:
        await interaction.response.send_message(f"Invalid hex code '{color2}' - {e}", ephemeral=True)
        return

    hex1 = hexColor1.GetHexCode()
    hex2 = hexColor2.GetHexCode()
    rgb1 = hexColor1.GetRGBList()
    rgb2 = hexColor2.GetRGBList()

    absoluteDifference, eulerDistance = GetHexDifference(hexColor1, hexColor2)
    absoluteDifferenceString = f"{absoluteDifference}"
    eulerDistanceString = f"{eulerDistance:.2f}"

    explanationString = f"**Absolute Difference: __{absoluteDifferenceString}__**\n**Visual Distance: __{eulerDistanceString}__**\n-# Use /visualdistance for more information."

    embed = discord.Embed(
        title = f"__**#{hex1} vs #{hex2}**__",
        color = discord.Color(int(f"0x{hex1}", 16))
    )
    embed.add_field(name = "", value = "", inline = False)
    embed.add_field(
        name=f"**#{hex1}:**",
        value=f"**RGB**\n{tuple(rgb1)}",
        inline=True)
    embed.add_field(
        name=f"**#{hex2}:**",
        value=f"**RGB**\n{tuple(rgb2)}",
        inline=True)

    embed.add_field(name="", value="", inline=False)
    embed.add_field(
        name="",
        value=f"{explanationString}",
        inline=False
    )

    colorSquare = CreateColorSquare([hexColor1, hexColor2], imageSize=128)
    buffer = io.BytesIO()
    colorSquare.save(buffer, "PNG")
    buffer.seek(0)
    discordFile = discord.File(buffer, filename="colorSquare.png")

    embed.set_image(url=f"attachment://colorSquare.png")
    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed, file=discordFile)
@client.tree.command(name='checkdifference', description=hexDifferenceCommandDescription)
@app_commands.describe(color1=hexDifferenceCommandColor1Description, color2=hexDifferenceCommandColor2Description)
# @app_commands.autocomplete(color1=armor_color_type_autocomplete, color2=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayCheckHexDifference(interaction, color1: str, color2: str):
    await displayHexDifference.callback(interaction, color1, color2)
@client.tree.command(name='colordifference', description=hexDifferenceCommandDescription)
@app_commands.describe(color1=hexDifferenceCommandColor1Description, color2=hexDifferenceCommandColor2Description)
# @app_commands.autocomplete(color1=armor_color_type_autocomplete, color2=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColorDifference(interaction, color1: str, color2: str):
    await displayHexDifference.callback(interaction, color1, color2)

@client.tree.command(name='visualdistance', description=visualDistanceCommandDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayVisualDistanceInfo(interaction):
    embed = discord.Embed(
        title=f"**Visual Distance Information**",
        color=discord.Color(int(f"0x7fcc19", 16))
    )
    embed.add_field(
        name=f"",
        value=f"__Visual Distance measures how different two colors appear to the human eye.__"
              f"\n\nA lower distance value indicates that the colors are more similar, while a higher value indicates that the colors are further apart.",
        inline=False
    )
    embed.add_field(
        name=f"",
        value=f"The difference is calculated using the Euclidean distance between the two colors in the CIELAB color space.",
        inline=False
    )

    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed)

@client.tree.command(name='scandatabase', description=databaseCommandDescription)
@app_commands.describe(color=databaseCommandColorDescription, itemname=databaseCommandItemNameDescription, listplayers=databaseCommandListPlayersDescription, showitemtypes=databaseCommandShowItemTypesDescription)
# @app_commands.autocomplete(color=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayDatabaseInfo(interaction, color: str = None, itemname: str = None, listplayers: bool = False, showitemtypes: bool = False):
    if color is None and itemname is None:
        await interaction.response.send_message("Please provide a color or item name.", ephemeral=True)
        return

    hexColor = None
    itemID = None
    if color is not None:
        try:
            hexColor = HexColor(baseHex=color)
        except Exception as e:
            await interaction.response.send_message(f"Invalid hex code '{color}' - {e}", ephemeral=True)
            return

    isArmorType = False
    if itemname is not None:
        isValid = False
        itemID = UpdateItemID(itemname)
        if itemID in itemIDToItemCount:
            isValid = True
        elif itemname.lower() == str(GetArmorType(itemname)).lower():
            isValid = True
            isArmorType = True

        if not isValid:
            await interaction.response.send_message(f"Invalid item id '{itemname}'", ephemeral=True)
            return

    hexCode = hexColor.GetHexCode() if hexColor is not None else None

    itemCount = GetItemCount(itemHex=hexCode, itemID=itemID, isArmorType=isArmorType)
    currentDescription = f"Found `{itemCount:,}` matching items."

    databasePlayers = GetDatabasePlayers(itemHex=hexCode, itemID=itemID, isArmorType=isArmorType)

    combinedItemDict = {}
    for playerUUID in databasePlayers:
        for item, baseHex in databasePlayers[playerUUID]:
            if item not in combinedItemDict:
                combinedItemDict[item] = []
            combinedItemDict[item].append(baseHex)

    discordFile = None
    if listplayers:
        if interaction.user.id in allowedDatabaseUsers:
            playerCount = len(databasePlayers.items())
            if playerCount > 0:
                itemCount = sum([len(value) for value in databasePlayers.values()])

                extraString = ""
                if itemCount <= 25:
                    extraString = "- "

                tempDescription = ""
                i = -1
                currentPlayerUUID = ""
                for playerUUID in dict(sorted(databasePlayers.items(), key=lambda sortedItem: len(sortedItem[1]), reverse=True)):
                    if currentPlayerUUID != playerUUID:
                        currentPlayerUUID = playerUUID
                        if i != -1:
                            tempDescription += f"\n\n"
                        tempDescription += f"**{playerUUID.lower()}**"
                    for item, baseHex in databasePlayers[playerUUID]:
                        i += 1
                        tempDescription += f"\n{extraString}#{baseHex} - {item}"

                if itemCount > 25:
                    buffer = io.BytesIO()
                    buffer.write(tempDescription.replace("**", "").encode())
                    buffer.seek(0)

                    fileName = ""
                    if hexCode and itemID:
                        fileName = f"{hexCode}_{itemID}.txt"
                    elif itemID is not None:
                        fileName = f"{itemID}.txt"
                    elif hexCode is not None:
                        fileName = f"{hexCode}.txt"
                    discordFile = discord.File(buffer, filename=fileName)
                else:
                    currentDescription += f"\n\n__**Items:**__\n{tempDescription}"
        else:
            currentDescription += "\n\nNo permission to list players."

    descriptionName = ""
    itemList = [f"#{hexCode}", itemID]
    for item in itemList:
        if item is not None and item != "#None":
            if descriptionName != "":
                descriptionName += " - "
            descriptionName += f"{item}"

    combinedItemCounts = ""
    if showitemtypes:
        if isArmorType or itemID is None:
            i = -1
            currentArmorType = ""

            for item in sorted(combinedItemDict.items(), key=lambda sortedItem: sortedItem, reverse=False):
                armorType = item[0].split("_")[0]
                if currentArmorType != armorType:
                    currentArmorType = armorType
                    if i != -1:
                        combinedItemCounts += f"\n"

                i += 1
                if i != 0:
                    combinedItemCounts += "\n"
                combinedItemCounts += f"{item[0]} - {len(item[1])}"

            combinedItemCounts += "\n\n"
    else:
        currentDescription += "\n-# Add showitemtypes to display item type counts."

    color = discord.Color(int(f"0xFFFFFF", 16))
    if hexCode is not None:
        color = discord.Color(int(f"0x{hexCode}", 16))
    embed = discord.Embed(
        title=f"**{descriptionName}**",
        description=f"{combinedItemCounts}{currentDescription}",
        color=color
    )

    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    if discordFile:
        await interaction.response.send_message(embed=embed, file=discordFile)
        return
    await interaction.response.send_message(embed=embed)
@client.tree.command(name='database', description=databaseCommandDescription)
@app_commands.describe(color=databaseCommandColorDescription, itemname=databaseCommandItemNameDescription, listplayers=databaseCommandListPlayersDescription)
# @app_commands.autocomplete(color=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayDatabase(interaction, color: str = None, itemname: str = None, listplayers: bool = False):
    await displayDatabaseInfo.callback(interaction, color, itemname, listplayers)

@client.tree.command(name='findsimilaritems', description=similarItemsCommandDescription)
@app_commands.describe(color=similarItemsCommandColorDescription, itemname=similarItemsCommandItemNameDescription, tolerance=similarItemsCommandToleranceDescription, listplayers=similarItemsCommandListPlayersDescription)
# @app_commands.autocomplete(color=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displaySimilarItems(interaction, color: str, itemname: str, tolerance: int = 25, listplayers: bool = False):
    if color is None and itemname is None:
        await interaction.response.send_message("Please provide a color or item name.", ephemeral=True)
        return

    if tolerance is None or tolerance < 0:
        await interaction.response.send_message("Please provide a valid tolerance.", ephemeral=True)
        return

    try:
        hexColor = HexColor(baseHex=color)
    except Exception as e:
        await interaction.response.send_message(f"Invalid hex code '{color}' - {e}", ephemeral=True)
        return

    itemID = UpdateItemID(itemname)
    if itemID not in itemIDToItemCount:
        await interaction.response.send_message(f"Invalid item id '{itemname}'", ephemeral=True)
        return

    hexCode = hexColor.GetHexCode()

    matchingItemsList, matchingItemCount = GetMatchingItems(itemHex=hexColor, itemID=itemID, tolerance=tolerance)
    currentDescription = f"Found `{matchingItemCount:,}` matching items within a tolerance of `{tolerance}`."

    discordFile = None
    if matchingItemCount > 0:
        extraString = ""
        if matchingItemCount <= 25:
            extraString = "- "

        shouldListPlayers = False
        if listplayers:
            if interaction.user.id in allowedDatabaseUsers:
                shouldListPlayers = True

        i = -1
        tempDescription = ""
        currentOffAmount = 0
        for playerList in sorted(matchingItemsList.items(), key=lambda x: x[1][1]):
            offAmount = playerList[1][1]
            if currentOffAmount != offAmount:
                currentOffAmount = offAmount
                if i != -1:
                    tempDescription += f"\n"
            for playerUUID in playerList[1][0]:
                i += 1
                if i != 0:
                    tempDescription += f"\n"

                playerString = f"{playerUUID}\n" if shouldListPlayers else ""
                tempDescription += f"{playerString}{extraString}#{playerList[0]} - {itemID} - {offAmount}"

        if matchingItemCount > 25:
            buffer = io.BytesIO()
            buffer.write(tempDescription.encode())
            buffer.seek(0)

            fileName = f"{hexCode}_{itemID}_{tolerance}.txt"
            discordFile = discord.File(buffer, filename=fileName)
        else:
            currentDescription += f"\n\n__**Items:**__\n{tempDescription}"

        if not shouldListPlayers and listplayers:
            currentDescription += "\n\nNo permission to list players."

    embed = discord.Embed(
        title=f"**#{hexCode} - {itemID}**",
        description=f"{currentDescription}",
        color=discord.Color(int(f"0x{hexCode}", 16))
    )

    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    if discordFile:
        await interaction.response.send_message(embed=embed, file=discordFile)
        return
    await interaction.response.send_message(embed=embed)
@client.tree.command(name='findnearbyitems', description=similarItemsCommandDescription)
@app_commands.describe(color=similarItemsCommandColorDescription, itemname=similarItemsCommandItemNameDescription, tolerance=similarItemsCommandToleranceDescription, listplayers=similarItemsCommandListPlayersDescription)
# @app_commands.autocomplete(color=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayNearbyItems(interaction, color: str, itemname: str, tolerance: int = 25, listplayers: bool = False):
    await displaySimilarItems.callback(interaction, color, itemname, tolerance, listplayers)
@client.tree.command(name='findcloseitems', description=similarItemsCommandDescription)
@app_commands.describe(color=similarItemsCommandColorDescription, itemname=similarItemsCommandItemNameDescription, tolerance=similarItemsCommandToleranceDescription, listplayers=similarItemsCommandListPlayersDescription)
# @app_commands.autocomplete(color=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayCloseItems(interaction, color: str, itemname: str, tolerance: int = 25, listplayers: bool = False):
    await displaySimilarItems.callback(interaction, color, itemname, tolerance, listplayers)

@client.tree.command(name='colorinfo', description=colorInfoCommandDescription)
@app_commands.describe(color=colorInfoCommandColorDescription)
# @app_commands.autocomplete(color=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColorInfo(interaction, color: str):
    if color is None:
        await interaction.response.send_message("Please provide a color.", ephemeral=True)
        return

    try:
        hexColor = HexColor(baseHex=color)
    except Exception as e:
        await interaction.response.send_message(f"Invalid hex code '{color}' - {e}", ephemeral=True)
        return

    hexCode = hexColor.GetHexCode()
    rgb = hexColor.GetRGBList()
    nearestColorName = GetNearestColorName(hexCode)

    aiResponseData = aiClient.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content":
                "You are a master color inspector." +
                "\nYour job is to analyze any given hex color with precision, providing a detailed description of its appearance." +
                "\nKeep responses short and to the point, focusing on the most important aspects of the color." +
                "\nResponses should be tailored to the specific color, avoiding generic or repetitive descriptions."
            },
            {"role": "user", "content": f"{hexCode}"},
        ],
        stream=False
    )

    embed = discord.Embed(
        title=f"**{nearestColorName}**",
        description="",
        color=discord.Color(int(f"0x{hexCode}", 16))
    )
    embed.add_field(name="", value="", inline=False)
    embed.add_field(
        name=f"**Hex**",
        value=f"#{hexCode}",
        inline=True
    )
    embed.add_field(name="", value="", inline=False)
    embed.add_field(
        name=f"**RGB**",
        value=f"{tuple(rgb)}",
        inline=True
    )
    embed.add_field(name="", value="", inline=False)

    closestPureColor = None
    closestPureColorDistance = float('inf')
    for color in pureColorToDiscordEmotes.keys():
        colorHex = color.value[1]
        colorDistance = GetAbsoluteDifference(hexColor, HexColor(baseHex=colorHex))
        if colorDistance < closestPureColorDistance:
            closestPureColorDistance = colorDistance
            closestPureColor = color

    if closestPureColor is not None and closestPureColorDistance < 20:
        embed.add_field(
            name=f"**Closest Pure Color**",
            value=f"{pureColorToDiscordEmotes[closestPureColor]} `{closestPureColor.value[0]}` - {closestPureColorDistance} off",
            inline=False
        )
        embed.add_field(name="", value="", inline=False)

    statusString, explanationString = GetColorStatusText(hexColor)
    if not explanationString:
        embed.add_field(
            name=f"**Color Status**",
            value=f"__**#{hexColor.GetHexCode()}**__ is {statusString}.",
            inline=False
        )
        embed.add_field(name="", value="", inline=False)
    else:
        embed.add_field(
            name=f"**Color Status**",
            value=f"__**#{hexColor.GetHexCode()}**__ is {statusString}.\n{explanationString}",
            inline=False
        )
    embed.add_field(name="", value="", inline=False)
    embed.add_field(
        name=f"**AI Evaluation**",
        value=f"{aiResponseData.choices[0].message.content}",
        inline=False
    )

    colorSquare = CreateColorSquare([hexColor], imageSize=128)
    buffer = io.BytesIO()
    colorSquare.save(buffer, "PNG")
    buffer.seek(0)
    discordFile = discord.File(buffer, filename="colorSquare.png")

    embed.set_thumbnail(url=f"attachment://colorSquare.png")
    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed, file=discordFile)
@client.tree.command(name='info', description=colorInfoCommandDescription)
@app_commands.describe(color=colorInfoCommandColorDescription)
# @app_commands.autocomplete(color=armor_color_type_autocomplete)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayInfo(interaction, color: str):
    await displayColorInfo.callback(interaction, color)

@client.tree.command(name='dyes', description=dyeInfoCommandDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayDyes(interaction):
    pureColorsDescription = ""
    trueColorsDescription = ""
    for color in pureColorToDiscordEmotes.keys():
        pureColorsDescription += f"{pureColorToDiscordEmotes[color]} `#{color.value[1]}` - {color.value[0]}\n"
    for color in trueColorToDiscordEmotes.keys():
        trueColorsDescription += f"{trueColorToDiscordEmotes[color]} `#{color.value[1]}` - {color.value[0]}\n"

    embed = discord.Embed(
        title=f"**Dye Info**",
        description=f" ",
        color=discord.Color(int(f"0xFFFFFF", 16))
    )
    embed.add_field(
        name=f"**Pure Colors**",
        value=f"{pureColorsDescription}",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)
    embed.add_field(
        name=f"**True Colors**",
        value=f"{trueColorsDescription}",
        inline=False
    )

    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed)
@client.tree.command(name='dyeinfo', description=dyeInfoCommandDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayDyeInfo(interaction):
    await displayDyes.callback(interaction)
@client.tree.command(name='scanplayer', description=scanPlayerCommandDescription)
@app_commands.describe(player=scanPlayerCommandPlayerDescription)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayScanPlayer(interaction, player: str):
    if player is None:
        await interaction.response.send_message("Please provide a player.", ephemeral=True)
        return

    playerData = player.replace("-", "").lower().strip()

    playerUsername = None
    playerUUID = None
    headers = {
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"https://crafthead.net/profile/{playerData}", headers=headers) as response:
                if response.status == 200:
                    playerInfo = await response.json()
                    if "name" in playerInfo:
                        playerUsername = str(playerInfo["name"])
                        playerUUID = str(playerInfo["id"]).upper()
                else:
                    print(f"Request failed with status code: {response.status}")
        except Exception as error:
            print("1 ERROR", json.dumps(str(error)), error)

    if playerUUID is None or playerUsername is None:
        await interaction.response.send_message(f"Error when looking up '{player}'.", ephemeral=True)
        return
    if playerUUID not in playerUUIDToItemList:
        await interaction.response.send_message(f"Player '{player}' not found in the database.", ephemeral=True)
        return

    playerItemList = playerUUIDToItemList[playerUUID]
    playerItemCount = len(playerItemList)

    discordFile = None
    currentDescription = ""
    if playerItemCount > 0:
        extraString = ""
        if playerItemCount <= 25:
            extraString = "- "

        tempDescription = ""
        i = -1
        for item in sorted(playerItemList, key=lambda x: x[0]):
            i += 1
            if i != 0:
                tempDescription += f"\n"
            tempDescription += f"{extraString}#{item[1]} {extraString}{item[0]}"

        if playerItemCount > 25:
            buffer = io.BytesIO()
            buffer.write(tempDescription.encode())
            buffer.seek(0)

            fileName = f"{playerUUID}.txt"
            discordFile = discord.File(buffer, filename=fileName)
        else:
            currentDescription += f"{tempDescription}"

    embed = discord.Embed(
        title=f"**{playerUsername}**",
        description=f" ",
        color=discord.Color(int(f"0xFFFFFF", 16))
    )
    embed.add_field(
        name=f"**UUID:**",
        value=f"{playerUUID}",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)
    if currentDescription != "":
        embed.add_field(
            name=f"**Items ({playerItemCount}):**",
            value=f"{currentDescription}\n-# *Only shows historical database items.",
            inline=False
        )
    else:
        embed.add_field(
            name=f"**Items:**",
            value=f"Player has* `{playerItemCount:,}` items.\n-# *Only shows historical database items.",
            inline=False
        )

    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    if discordFile:
        await interaction.response.send_message(embed=embed, file=discordFile)
        return
    await interaction.response.send_message(embed=embed)

with open('AIToken') as file:
    aiClient = OpenAI(api_key=file.read().strip(), base_url="https://api.groq.com/openai/v1")

with open('BotToken') as file:
    LoadColorNames()
    LoadDatabase("Database/Combined-S.html")
    client.run(file.read().strip())