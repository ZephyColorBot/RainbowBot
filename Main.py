import aiohttp
import discord

from discord.ext import commands
from discord import app_commands, Forbidden
from openai import OpenAI
from ColorNames import *
from Armor import *
from Database import *

defaultColor = discord.Color(0xD2EBEB)
avatarLink = "https://cdn.discordapp.com/avatars/1000919610251558993/7c7d0e2f2d831a5241b9053fd0ca6fd1.webp"
footerText = "Made by zeph.y"
allowedDatabaseUsers = [
    263058850234499072, # me
    687154466243477535 # elays
]

def AppCommandWithAliases(tree, name, aliases=None, **kwargs):
    aliases = aliases or []

    def decorator(func):
        tree.command(name=name, **kwargs)(func)

        for alias in aliases:
            async def wrapper(interaction, *args, **kw):
                return await func(interaction, *args, **kw)

            import functools
            functools.update_wrapper(wrapper, func)

            tree.command(name=alias, **kwargs)(wrapper)

        return func
    return decorator

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
allColorTypeChoices = [
    app_commands.Choice(name="Fairy", value="Fairy"),
    app_commands.Choice(name="OG Fairy", value="OG Fairy"),
    app_commands.Choice(name="All Fairy", value="All Fairy"),
    app_commands.Choice(name="Crystal", value="Crystal"),
    app_commands.Choice(name="Pure Colors", value="Pure Colors"),
    app_commands.Choice(name="True Colors", value="True Colors"),
    app_commands.Choice(name="Pure+True Colors", value="Pure+True Colors"),
    app_commands.Choice(name="Hypixel Dyes", value="Hypixel Dyes"),
    app_commands.Choice(name="Mix Pure Colors", value="Mix Pure Colors"),
]
visualOrAbsoluteDistanceChoices = [
    app_commands.Choice(name="Visual Distance", value="Visual"),
    app_commands.Choice(name="Absolute Difference", value="Absolute")
]

'''
Auto complete for some reason makes discord not allow up arrow command resending.
'''
# async def armor_type_autocomplete(interaction: discord.Interaction, current: str):
#     return [
#         app_commands.Choice(name = str(option), value =str(option).replace(" ", ""))
#         for option in itemDict if current.lower() in str(option).lower()
#     ][:25]
# async def armor_color_type_autocomplete(interaction: discord.Interaction, current: str):
#     return [
#         app_commands.Choice(name = str(option.value[0]), value =str(option.value[0]).replace(" ", ""))
#         for option in list(Color) if current.lower() in str(option.value[0]).lower()
#     ][:25]

colorCommandDescription = 'Generate a color square with the given hex code(s).'

colorDescription = 'Enter a hex code.'
colorListDescription = 'Enter a list of hex codes separated by spaces (e.g., #334CB2 #191919)'
outputArmorDescription = 'Enter the armor type. (e.g., Superior, Young Baby)'
outputShapeDescription = 'Enter the armor shape. (e.g., Vertical, Horizontal, Square)'
outputVersionDescription = 'Enter the armor version. (e.g., 1.8.9, 1.14+)'

colorCommandMaxColumnsDescription = "The maximum number of columns to display."
colorCommandMaxRowsDescription = "The maximum number of rows to display."

armorCommandDescription = 'Displays an armor set with the given hex color(s).'

compareArmorCommandSetListStringDescription = "Enter a list of armor sets separated by '|'. (e.g., #334CB2 #191919 babyyoung|#000000 #FFFFFF babysuperior)"

exoticCommandDescription = 'Checks the type of a given hex.'

simpleMixCommandDescription = 'Mixes the given hexes and displays the result.'
simpleMixCommandColorsDescription = 'Enter a list of hex codes, they will be combined one by one. (Same as crafting after each dye)'

advancedMixCommandDescription = 'Mixes multiple hexes in steps and displays the result. (Same as adding multiple dyes at once)'
advancedMixCommandCraftingSequence1Description = 'Enter a list of hex codes, they will be combined in one crafting step.'
advancedMixCommandCraftingSequence2Description = 'Enter a list of hex codes, they will be combined in two crafting steps.'
advancedMixCommandCraftingSequence3Description = 'Enter a list of hex codes, they will be combined in three crafting steps.'

helpCommandDescription = 'Displays information about the bot.'

hexDifferenceCommandDescription = 'Displays the absolute and visual distance between two hexes.'

visualDistanceCommandDescription = 'Displays information about the visual distance between two colors.'

inputItemNameDescription = 'ItemName or ItemID to scan for.'
listPlayerUUIDsDescription = 'Whether the player UUIDs should be listed (Requires Permission).'

databaseCommandDescription = 'Scan the database for a specific hex code, item, or both.'
databaseCommandListHexesDescription = 'Whether item hexes should be listed.'
databaseCommandShowItemTypesDescription = 'Whether item types should be shown.'

similarItemsCommandDescription = 'Scan the database for items close to a specific hex code.'
similarItemsCommandToleranceDescription = 'The amount off a hex code can be.'
similarItemsCommandVisualOrAbsoluteDistanceDescription = 'Whether the visual or absolute distance should be used.'

compareArmorCommandDescription = 'Compares multiple armor sets and displays the result.'

colorInfoCommandDescription = 'Displays information about a specific hex code.'

dyeInfoCommandDescription = 'Displays all pure and true dye hexes.'

scanPlayerCommandDescription = 'Scan the database for a specific player.'
scanPlayerCommandPlayerDescription = 'Player UUID/Username to scan for.'

allColorsCommandDescription = 'Displays all hexes of a given type on a given armor type.'
allColorsCommandColorTypeDescription = "Enter the dye type. (e.g., Fairy, Crystal, Pure Colors, True Colors, Pure+True Colors, Hypixel Dyes)"

@AppCommandWithAliases(
    client.tree,
    name='color',
    aliases=["colour", "colors", "colours"],
    description=colorCommandDescription
)
@app_commands.describe(
    colors=colorListDescription,
    maxcolumns=colorCommandMaxColumnsDescription,
    maxrows=colorCommandMaxRowsDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColor(
    interaction: discord.Interaction,
    colors: str,
    maxcolumns: int = None,
    maxrows: int = None
):
    originalHexList = re.split(r'(\s)', colors)
    originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]

    colorList = []
    colorString = ""
    for baseHex in originalHexList:
        try:
            hexColor = HexColor(baseHex = baseHex)
            colorList.append(hexColor)
        except Exception as e:
            await interaction.response.send_message(f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
            return

        if colorString != "":
            colorString += ", "
        colorString += f"#{hexColor.GetHexCode()}"

    if maxcolumns is None:
        maxcolumns = -1
    if maxrows is None:
        maxrows = -1

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
        buffer = io.BytesIO()
        image = CreateColorSquare(hexColorList=colorList, maxColumns=maxcolumns, maxRows=maxrows)
        image.save(buffer, "PNG")
        buffer.seek(0)

        if len(colorString) > 2000:
            colorString = " "

        discordFile = discord.File(buffer, filename="colorSquare.png")
        try:
            if colorString != "":
                colorString = f"**{colorString}**"
            await interaction.followup.send(content=colorString, file=discordFile)
        except Forbidden as e:
            await interaction.followup.send(content=f"Error: Bot has no permissions to send images.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='armor',
    aliases=["armour", "displayarmor", "displayarmour"],
    description=armorCommandDescription
)
@app_commands.choices(
    outputshape=shapeChoices,
    outputversion=armorVersionChoices
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    colors=colorListDescription,
    outputarmor=outputArmorDescription,
    outputshape=outputShapeDescription,
    outputversion=outputVersionDescription
)
async def displayArmor(
    interaction: discord.Interaction,
    colors: str = None,
    outputarmor: str = None,
    outputshape: str = None,
    outputversion: str = None
):
    if colors is None and outputarmor is None:
        await interaction.response.send_message("Please provide at least one hex code or armor type.", ephemeral=True)
        return

    defaultColorNames = ["base", "none", "default", "original"]
    if colors is None or not colors or any(value in colors for value in defaultColorNames):
        colors = []
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

    colorList = []
    colorString = ""
    if type(colors) == str:
        originalHexList = re.split(r'(\s)', colors)
        originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]

        for baseHex in originalHexList:
            try:
                hexColor = HexColor(baseHex = baseHex)
                colorList.append(hexColor)
            except Exception as e:
                await interaction.response.send_message(f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
                return

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
        buffer, filePath, colors = GetCombinedArmorSetBuffer(
            armorType=armorEnum,
            hexList=colorList,
            versionType=versionEnum,
            shapeType=shapeEnum,
            imageXSpacing=0,
            imageYSpacing=20,
            imageSize=128
        )
        for baseHex in colors:
            if colorString != "":
                colorString += ", "
            colorString += f"#{baseHex.GetHexCode()}"

        discordFile = discord.File(buffer, filename=filePath)
        try:
            if colorString != "":
                colorString = f"**{colorString}**"
            await interaction.followup.send(content=colorString, file=discordFile)
        except Forbidden as e:
            await interaction.followup.send(content=f"Error: Bot has no permissions to send images.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='advancedmix',
    aliases=["advancedmixcolors", "mixadvancedcolors", "mixadvanced", "craftingmix", "mixcrafting", "mixsteps"],
    description=advancedMixCommandDescription
)
@app_commands.choices(
    outputshape=shapeChoices,
    outputversion=armorVersionChoices
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    craftingsequence1=advancedMixCommandCraftingSequence1Description,
    craftingsequence2=advancedMixCommandCraftingSequence2Description,
    craftingsequence3=advancedMixCommandCraftingSequence3Description,
    outputarmor=outputArmorDescription,
    outputshape=outputShapeDescription,
    outputversion=outputVersionDescription
)
async def displayAdvancedMix(
    interaction: discord.Interaction,
    craftingsequence1: str,
    craftingsequence2: str = None,
    craftingsequence3: str = None,
    outputarmor: str = None,
    outputshape: str = None,
    outputversion: str = None
):
    await displayMix(interaction, None, craftingsequence1, craftingsequence2, craftingsequence3, outputarmor, outputshape, outputversion)

@AppCommandWithAliases(
    client.tree,
    name='mix',
    aliases=["mixcolors", "mixcolor", "mixcolours", "mixdyes", "mixdye", "mixhex", "mixhexes"],
    description=simpleMixCommandDescription
)
@app_commands.choices(
    outputshape=shapeChoices,
    outputversion=armorVersionChoices
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    colors=simpleMixCommandColorsDescription,
    outputarmor=outputArmorDescription,
    outputshape=outputShapeDescription,
    outputversion=outputVersionDescription
)
async def displaySimpleMix(
    interaction: discord.Interaction,
    colors: str,
    outputarmor: str = None,
    outputshape: str = None,
    outputversion: str = None
):
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

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
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
                        hexColor = HexColor(baseHex = baseHex)
                        hexColorList.append(hexColor)
                    except Exception as e:
                        await interaction.followup.send(content=f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
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
                        hexColor = HexColor(baseHex = baseHex)
                        hexList.append(hexColor)
                    except Exception as e:
                        await interaction.followup.send(content=f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
                        return

                for baseHex in hexList:
                    if colorString != "":
                        colorString += " + "
                    colorString += f"#{baseHex.GetHexCode()}"

                    if finalHex is None:
                        finalHex = baseHex
                    else:
                        finalHex = MixHexColorList(finalHex, [baseHex])
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected mixing hex: {e}", ephemeral=True)
        return

    try:
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
                await interaction.followup.send(content=f"Invalid armor type '{outputarmor}'", ephemeral=True)
                return
            if outputshape not in stringToShapeTypeDict:
                await interaction.followup.send(content=f"Invalid shape type '{outputshape}'", ephemeral=True)
                return
            if outputversion not in stringToVersionTypeDict:
                await interaction.followup.send(content=f"Invalid version type '{outputversion}'", ephemeral=True)
                return

            armorEnum = stringToArmorTypeDict[outputarmor]
            shapeEnum = stringToShapeTypeDict[outputshape]
            versionEnum = stringToVersionTypeDict[outputversion]

            buffer, filePath, colors = GetCombinedArmorSetBuffer(
                armorType=armorEnum,
                hexList=[finalHex],
                versionType=versionEnum,
                shapeType=shapeEnum,
                imageXSpacing=0,
                imageYSpacing=20,
                imageSize=128
            )
        else:
            filePath = "colorSquare.png"
            buffer = io.BytesIO()
            image = CreateColorSquare([finalHex])
            image.save(buffer, "PNG")
            buffer.seek(0)

        discordFile = discord.File(buffer, filename=filePath)
        try:
            if colorString != "":
                colorString = f"**{colorString}**"
            await interaction.followup.send(content=colorString, file=discordFile)
        except Forbidden as e:
            await interaction.followup.send(content=f"Error: Bot has no permissions to send images.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='help',
    aliases=["commands", "commandlist"],
    description=helpCommandDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def helpCommand(
    interaction: discord.Interaction
):
    embed = discord.Embed(
        title="Rainbow",
        description="A useful bot for your exotics needs.",
        color=defaultColor
    )

    embed.add_field(
        name="/help",
        value=helpCommandDescription,
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/armor <hexes> [<armor>] [<shape>] [<version>]",
        value=armorCommandDescription + "\n-# Optional Armor Type, Shape, and Version.\n-# Aliases: /armour",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/color <hexes>",
        value=colorCommandDescription + "\n-# Aliases: /colour",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/exotic <hex>",
        value=exoticCommandDescription + "\n-# Aliases: /fairy, /crystal",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/mix <hexes> [<outputarmor>] [<outputshape>] [<outputversion>]",
        value=simpleMixCommandDescription + "\n-# Optional Output Armor Type, Shape, and Version.",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/advancedmix <step1hexes> [<step2hexes>] [<step3hexes>] [<outputarmor>] [<outputshape>] [<outputversion>]",
        value=advancedMixCommandDescription + "\n-# Optional Output Armor Type, Shape, and Version.",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/checkdifference <hex1> <hex2>",
        value=hexDifferenceCommandDescription,
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/visualdistance <hex1> <hex2>",
        value=visualDistanceCommandDescription,
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/scandatabase <[<hex>, <itemname>]> [<listplayers>] [<listhexes>] [<showitemtypes>]",
        value=databaseCommandDescription + "\n-# Optional List Players, Hexes, and Item Types.",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/similaritems <hex> <itemname> [<tolerance>] [<listplayers>]",
        value=similarItemsCommandDescription + "\n-# Optional Tolerance and List Players.",
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/colorinfo <hex>",
        value=colorInfoCommandDescription,
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/dyes",
        value=dyeInfoCommandDescription,
        inline=False
    )
    embed.add_field(name="", value="", inline=False)

    embed.add_field(
        name="/scanplayer <player>",
        value=scanPlayerCommandDescription,
        inline=False
    )

    embed.set_footer(text=footerText, icon_url=avatarLink)
    embed.timestamp = interaction.created_at

    await interaction.response.send_message(embed=embed)

@AppCommandWithAliases(
    client.tree,
    name='exotic',
    aliases=["crystal", "fairy", "isexotic", "iscrystal", "isfairy", "colorstatus"],
    description=exoticCommandDescription
)
@app_commands.describe(
    color=colorDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColorStatusExotic(
    interaction: discord.Interaction,
    color: str
):
    try:
        hexColor = HexColor(baseHex=color)
    except Exception as e:
        await interaction.response.send_message(f"Invalid hex code '{color}' - {e}", ephemeral=True)
        return

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
        statusString, explanationString = GetColorStatusText(hexColor)

        embed = discord.Embed(
            title=f"__**#{hexColor.GetHexCode()}**__ is {statusString}.",
            description=f"{explanationString}",
            color=discord.Color(MinMaxHexInt(int(f"0x{hexColor.GetHexCode()}", 16)))
        )

        colorSquare = CreateColorSquare([hexColor], imageSize=128)
        buffer = io.BytesIO()
        colorSquare.save(buffer, "PNG")
        buffer.seek(0)
        discordFile = discord.File(buffer, filename="colorSquare.png")

        embed.set_image(url=f"attachment://colorSquare.png")
        embed.set_footer(text=footerText, icon_url=avatarLink)
        embed.timestamp = interaction.created_at

        try:
            await interaction.followup.send(embed=embed, file=discordFile)
        except Forbidden as e:
            await interaction.followup.send(content=f"Error: Bot has no permissions to send images.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='comparearmor',
    aliases=["comparearmors", "comparearmorcolors", "comparearmour", "comparearmours", "comparearmourcolors", "compareset", "comparesets", "comparearmorsets", "comparearmoursets"],
    description=compareArmorCommandDescription
)
@app_commands.choices(
    outputshape=normalShapeChoices,
    outputversion=armorVersionChoices
)
@app_commands.describe(
    set1=outputArmorDescription,
    set2=outputArmorDescription,
    set3=outputArmorDescription,
    set4=outputArmorDescription,
    set5=outputArmorDescription,
    setliststring=compareArmorCommandSetListStringDescription,
    outputshape=outputShapeDescription,
    outputversion=outputVersionDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayCompareArmor(
    interaction: discord.Interaction,
    set1: str = None,
    set2: str = None,
    set3: str = None,
    set4: str = None,
    set5: str = None,
    setliststring: str = None,
    outputshape: str = None,
    outputversion: str = None
):
    if not set1 and not set2 and not set3 and not set4 and not set5 and not setliststring:
        await interaction.response.send_message("Please provide at least one armor set.", ephemeral=True)
        return

    inputItemListList = [set1, set2, set3, set4, set5]

    if setliststring is not None:
        setList = []
        # if ", " in setliststring:
        #     setList = setliststring.split(', ')
        if "|" in setliststring:
            setList = setliststring.split('|')
        else:
            setList = [setliststring]

        for setItem in setList:
            setItem = setItem.strip()
            if setItem:
                inputItemListList.append(setItem)

    if outputshape is None:
        outputshape = "Vertical"
    if outputversion is None:
        outputversion = "1.8.9"

    if type(outputshape) == str:
        outputshape = outputshape.lower().replace(' ', '').strip()
    if type(outputversion) == str:
        outputversion = outputversion.lower().replace(' ', '').strip()

    if outputshape not in stringToShapeTypeDict:
        await interaction.response.send_message(f"Invalid shape type '{outputshape}'", ephemeral=True)
        return
    if outputversion not in stringToVersionTypeDict:
        await interaction.response.send_message(f"Invalid version type '{outputversion}'", ephemeral=True)
        return

    shapeEnum = stringToShapeTypeDict[outputshape]
    versionEnum = stringToVersionTypeDict[outputversion]

    await interaction.response.defer(thinking=True, ephemeral=False)

    finalText = ""
    finalImageList = []
    try:
        lastArmor = None
        for itemList in inputItemListList:
            if itemList is None:
                continue

            currentWord = ""
            armorEnum = lastArmor

            reversedItemList = itemList[::-1]
            armorTypeSplit = re.split(r'(\s)', reversedItemList)
            armorTypeSplit = [x for i, x in enumerate(armorTypeSplit) if i % 2 == 0]
            for word in armorTypeSplit:
                word = word[::-1].strip()
                currentWord = (currentWord + word).strip()
                if currentWord in stringToArmorTypeDict:
                    armorEnum = stringToArmorTypeDict[word]
                    lastArmor = armorEnum
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
                        hexColor = HexColor(baseHex=baseHex)
                        hexList.append(hexColor)

                        if finalText != "":
                            finalText += ", "
                        finalText += f"#{hexColor.GetHexCode()}"

                    except Exception as e:
                        await interaction.followup.send(content=f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
                        return

            buffer, filePath, colors = GetCombinedArmorSetBuffer(
                armorType=armorEnum,
                hexList=hexList,
                versionType=versionEnum,
                shapeType=shapeEnum,
                imageXSpacing=0,
                imageYSpacing=20,
                imageSize=128
            )
            finalImageList.append((buffer, filePath, colors))
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error creating armors: {e}", ephemeral=True)
        return

    try:
        if len(finalImageList) == 0:
            await interaction.followup.send(content="Please provide at least one armor color or armor type.", ephemeral=True)
            return

        resultImage = Image.new(mode = 'RGBA', size = (0, 0), color = (0, 0, 0, 0))
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
        try:
            if finalText != "":
                finalText = f"**{finalText}**"
            await interaction.followup.send(content=finalText, file=discordFile)
        except Forbidden as e:
            await interaction.followup.send(content=f"Error: Bot has no permissions to send images.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error combining armors: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='hexdifference',
    aliases=["colordifference", "colourdifference", "checkdifference", "comparecolors", "comparehexes", "comparecolours"],
    description=hexDifferenceCommandDescription
)
@app_commands.describe(
    color1=colorDescription,
    color2=colorDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayHexDifference(
    interaction: discord.Interaction,
    color1: str,
    color2: str
):
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

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
        absoluteDifference, eulerDistance = GetHexDifference(hexColor1, hexColor2)
        absoluteDifferenceString = f"{absoluteDifference}"
        eulerDistanceString = f"{eulerDistance:.2f}"

        explanationString = f"**Absolute Difference: __{absoluteDifferenceString}__**\n**Visual Distance: __{eulerDistanceString}__**\n-# Use /visualdistance for more information."

        embed = discord.Embed(
            title=f"__**#{hex1} vs #{hex2}**__",
            color=discord.Color(MinMaxHexInt(int(f"0x{hex1}", 16)))
        )
        embed.add_field(name="", value="", inline=False)
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
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error getting hex difference: {e}", ephemeral=True)

    try:
        colorSquare = CreateColorSquare([hexColor1, hexColor2], imageSize=128)
        buffer = io.BytesIO()
        colorSquare.save(buffer, "PNG")
        buffer.seek(0)
        discordFile = discord.File(buffer, filename="colorSquare.png")

        embed.set_image(url=f"attachment://colorSquare.png")
        embed.set_footer(text=footerText, icon_url=avatarLink)
        embed.timestamp = interaction.created_at

        try:
            await interaction.followup.send(embed=embed, file=discordFile)
        except Forbidden as e:
            await interaction.followup.send(content=f"Error: Bot has no permissions to send images.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error creating color square: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='visualdistance',
    aliases=[],
    description=visualDistanceCommandDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayVisualDistanceInfo(
    interaction: discord.Interaction
):
    embed = discord.Embed(
        title=f"**Visual Distance Information**",
        color=defaultColor
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

@AppCommandWithAliases(
    client.tree,
    name='scandatabase',
    aliases=["scandb", "scan", "dbscan", "databasescan", "scanitems", "database"],
    description=databaseCommandDescription
)
@app_commands.describe(
    color=colorDescription,
    itemname=inputItemNameDescription,
    listplayers=listPlayerUUIDsDescription,
    listhexes=databaseCommandListHexesDescription,
    showitemtypes=databaseCommandShowItemTypesDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayDatabaseInfo(
    interaction: discord.Interaction,
    color: str = None,
    itemname: str = None,
    listplayers: bool = False,
    listhexes: bool = False,
    showitemtypes: bool = False
):
    if color is None and itemname is None:
        await interaction.response.send_message("Please provide a color or item name.", ephemeral=True)
        return

    hexColor = None
    if color is not None:
        try:
            hexColor = HexColor(baseHex=color)
        except Exception as e:
            await interaction.response.send_message(f"Invalid hex code '{color}' - {e}", ephemeral=True)
            return

    isValid, itemID, isArmorType = GetValidItemIDFromItemName(itemname)
    if not isValid and itemname is not None:
        await interaction.response.send_message(f"Invalid item id '{itemname}'", ephemeral=True)
        return

    hexCode = hexColor.GetHexCode() if hexColor is not None else None

    for crystalColor in allCrystalHexes.keys():
        if hexCode is not None and hexCode == crystalColor.value[1]:
            await interaction.response.send_message(f"Crystal hexes can\'t be scanned.", ephemeral=True)
            return
    for fairyColor in allFairyHexes.keys():
        if hexCode is not None and hexCode == fairyColor.value[1]:
            await interaction.response.send_message(f"Fairy hexes can\'t be scanned.", ephemeral=True)
            return

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
        itemCount = GetItemCount(itemHex=hexCode, itemID=itemID, isArmorType=isArmorType)
        # if itemCount == -1:
        #     await interaction.followup.send(f"Invalid item id '{itemname}'", ephemeral = True)
        #     return

        currentDescription = f"Found `{itemCount:,}` matching items."
        databasePlayers = GetDatabasePlayers(itemHex=hexCode, itemID=itemID, isArmorType=isArmorType)

        combinedItemDict = {}
        for playerUUID in databasePlayers:
            for item, baseHex in databasePlayers[playerUUID]:
                if item not in combinedItemDict:
                    combinedItemDict[item] = []
                combinedItemDict[item].append(baseHex)

        discordFile = None
        if listplayers or listhexes:
            canListPlayers = interaction.user.id in allowedDatabaseUsers and listplayers

            playerCount = len(databasePlayers.items())
            if playerCount > 0:
                itemCount = sum([len(value) for value in databasePlayers.values()])

                extraString = ""
                if itemCount <= 25:
                    extraString = "- "

                tempDescription = ""
                i = -1
                currentPlayerUUID = ""

                uuidList = dict(sorted(databasePlayers.items(), key = lambda sortedItem: len(sortedItem[1]), reverse = True))
                shouldShowNames = True if len(uuidList) <= 25 else False

                for playerUUID in uuidList:
                    if currentPlayerUUID != playerUUID:
                        playerUsername = ""
                        if shouldShowNames:
                            async with aiohttp.ClientSession() as session:
                                try:
                                    async with session.get(f"https://crafthead.net/profile/{playerUUID}", headers={"Content-Type": "application/json"}) as response:
                                        if response.status == 200:
                                            playerInfo = await response.json()
                                            if "name" in playerInfo:
                                                playerUsername = f"**" + str(playerInfo["name"]) + f" - {playerUUID.lower()}**"
                                        else:
                                            print(f"Request failed with status code: {response.status}")
                                except Exception as error:
                                    print("1 ERROR", json.dumps(str(error)), error)

                        if playerUsername == "":
                            playerUsername = f"**{playerUUID.lower()}**"

                        currentPlayerUUID = playerUUID
                        if i != -1:
                            tempDescription += f"\n"
                        if canListPlayers:
                            tempDescription += f"\n{playerUsername}"
                    for item, baseHex in databasePlayers[playerUUID]:
                        i += 1
                        tempDescription += f"\n{extraString}#{baseHex} - {item}"

                tempDescription = tempDescription.strip()

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

            if not canListPlayers and listplayers:
                currentDescription += "\n\nNo permission to list players."

        descriptionName = ""
        itemList = [f"#{hexCode}", itemID]
        for item in itemList:
            if item is not None and item != "#None":
                if descriptionName != "":
                    descriptionName += " - "
                descriptionName += f"{item}"

        combinedItemCounts = ""
        if showitemtypes or len(combinedItemDict) <= 15:
            if isArmorType or itemID is None:
                i = -1
                currentArmorType = ""

                for item in sorted(combinedItemDict.items(), key = lambda sortedItem: sortedItem, reverse = False):
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
            currentDescription += "\n-# Add showitemtypes to display all item counts."

        color = defaultColor
        if hexCode is not None:
            color = discord.Color(MinMaxHexInt(int(f"0x{hexCode}", 16)))
        embed = discord.Embed(
            title=f"**{descriptionName}**",
            description=f"{combinedItemCounts}{currentDescription}",
            color=color
        )

        embed.set_footer(text=footerText, icon_url=avatarLink)
        embed.timestamp = interaction.created_at

        if discordFile:
            try:
                await interaction.followup.send(embed=embed, file=discordFile)
            except Forbidden as e:
                await interaction.followup.send(content=f"Error: Bot has no permissions to send files.", ephemeral=True)
            return
        await interaction.followup.send(embed=embed)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='findsimilaritems',
    aliases=["findnearbyitems", "findnearbyitem", "findsimilar", "findnearby", "findsimilararmor", "findnearbyarmor", "findsimilaritem", "findcloseitems"],
    description=similarItemsCommandDescription
)
@app_commands.describe(
    color=colorDescription,
    itemname=inputItemNameDescription,
    tolerance=similarItemsCommandToleranceDescription,
    listplayers=listPlayerUUIDsDescription,
    visual_or_absolute_distance=similarItemsCommandVisualOrAbsoluteDistanceDescription
)
@app_commands.choices(
    visual_or_absolute_distance=visualOrAbsoluteDistanceChoices
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displaySimilarItems(
    interaction: discord.Interaction,
    color: str,
    itemname: str,
    tolerance: int = -1,
    listplayers: bool = False,
    visual_or_absolute_distance: str = None
):
    if color is None and itemname is None:
        await interaction.response.send_message("Please provide a color or item name.", ephemeral=True)
        return

    try:
        hexColor = HexColor(baseHex=color)
    except Exception as e:
        await interaction.response.send_message(f"Invalid hex code '{color}' - {e}", ephemeral=True)
        return

    if color is None and itemname is None:
        await interaction.response.send_message("Please provide a color or item name.", ephemeral=True)
        return

    if visual_or_absolute_distance is not None:
        if visual_or_absolute_distance.lower() == "visual":
            visualDistance = True
        elif visual_or_absolute_distance.lower() == "absolute":
            visualDistance = False
        else:
            await interaction.response.send_message("Please provide a valid distance type.", ephemeral=True)
            return
    else:
        visualDistance = False

    if tolerance == -1 and visualDistance:
        tolerance = 10
    elif tolerance == -1:
        tolerance = 25

    if tolerance is None or tolerance < 0:
        await interaction.response.send_message("Please provide a valid tolerance.", ephemeral=True)
        return

    isValid, itemID, isArmorType = GetValidItemIDFromItemName(itemname)
    if itemname != "any":
        if not isValid and itemname is not None:
            await interaction.response.send_message(f"Invalid item id '{itemname}'", ephemeral=True)
            return
    else:
        itemID = itemname

    hexCode = hexColor.GetHexCode()

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
        matchingItemsList, matchingItemCount = GetMatchingItems(itemHex=hexColor, itemID=itemID, tolerance=tolerance, isArmorType=isArmorType, visualDistance=visualDistance)
        # if matchingItemCount == -1:
        #     await interaction.followup.send(f"Invalid item id '{itemname}'", ephemeral = True)
        #     return

        distanceDescription = "visual distance" if visualDistance else "absolute difference"
        toleranceString = f"{tolerance:.2f}" if visualDistance else f"{tolerance}"
        currentDescription = f"Found `{matchingItemCount:,}` matching items within a {distanceDescription} of `{toleranceString}`."

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
            for playerList in sorted(matchingItemsList.items(), key = lambda x: x[1][1]):
                offAmount = playerList[1][1]
                if currentOffAmount != offAmount and playerList[1][0]:
                    currentOffAmount = offAmount
                    if i != -1:
                        tempDescription += f"\n"

                shouldShowNames = True if len(playerList[1][0]) <= 25 else False
                for playerData in playerList[1][0]:
                    i += 1
                    if i != 0:
                        tempDescription += f"\n"

                    playerUsername = ""
                    if shouldShowNames:
                        async with aiohttp.ClientSession() as session:
                            try:
                                async with session.get(f"https://crafthead.net/profile/{playerData[1]}", headers={
                                    "Content-Type": "application/json"}) as response:
                                    if response.status == 200:
                                        playerInfo = await response.json()
                                        if "name" in playerInfo:
                                            playerUsername = str(playerInfo["name"]) + f" - {playerData[1]}"
                                    else:
                                        print(f"Request failed with status code: {response.status}")
                            except Exception as error:
                                print("1 ERROR", json.dumps(str(error)), error)

                    if playerUsername == "":
                        playerUsername = f"{playerData[1]}"

                    playerString = f"{playerUsername}\n" if shouldListPlayers else ""

                    toleranceString = f"{offAmount:.2f}" if visualDistance else f"{offAmount}"
                    tempDescription += f"{playerString}{extraString}#{playerList[0]} - {playerData[0]} - {toleranceString}"

            if matchingItemCount > 25:
                buffer = io.BytesIO()
                buffer.write(tempDescription.encode())
                buffer.seek(0)

                fileName = f"{hexCode}_{itemID.upper()}_{tolerance}.txt"
                discordFile = discord.File(buffer, filename=fileName)
            else:
                currentDescription += f"\n\n__**Items:**__\n{tempDescription}"

            if not shouldListPlayers and listplayers:
                currentDescription += "\n\nNo permission to list players."

        embed = discord.Embed(
            title=f"**#{hexCode} - {itemID.upper()}**",
            description=f"{currentDescription}",
            color=discord.Color(MinMaxHexInt(int(f"0x{hexCode}", 16)))
        )

        embed.set_footer(text=footerText, icon_url=avatarLink)
        embed.timestamp = interaction.created_at

        if discordFile:
            try:
                await interaction.followup.send(embed=embed, file=discordFile)
            except Forbidden as e:
                await interaction.followup.send(content=f"Error: Bot has no permissions to send files.", ephemeral=True)
            return
        await interaction.followup.send(embed=embed)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error combining armors: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='colorinfo',
    aliases=["colorinformation", "hexinfo", "hexinformation", "info", "information"],
    description=colorInfoCommandDescription
)
@app_commands.describe(
    color=colorDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayColorInfo(
    interaction: discord.Interaction,
    color: str
):
    if color is None:
        await interaction.response.send_message("Please provide a color.", ephemeral=True)
        return

    try:
        hexColor = HexColor(baseHex=color)
    except Exception as e:
        await interaction.response.send_message(f"Invalid hex code '{color}' - {e}", ephemeral=True)
        return

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
        hexCode = hexColor.GetHexCode()
        rgb = hexColor.GetRGBList()
        nearestColorName = GetNearestColorName(hexCode)

        aiResponseData = aiClient.chat.completions.create(
            # model = "llama-3.1-8b-instant",
            model="meta-llama/llama-4-maverick-17b-128e-instruct",
            messages=[
                # {"role": "system", "content":
                #     "You are a master color inspector." +
                #     "\nYour job is to analyze any given hex color with precision, providing a detailed description of its appearance." +
                #     "\nKeep responses short and to the point, focusing on the most important aspects of the color." +
                #     "\nResponses should be tailored to the specific color, avoiding generic or repetitive descriptions."
                # },
                {"role": "system", "content":
                    "You are a precision color analyzer that evaluates 1.8.9 Minecraft leather armor hex color codes with technical accuracy." +
                    "\nFor any hex code provided, return the following information:" +
                    "\n1. Provide a descriptive name that accurately represents the shade (e.g., 'midnight blue', 'coral red', 'forest green', etc.)" +
                    "\n2. Describe the color's characteristics but dont describe the RGB or HSL values. Descriptions should be about 200 words and 2-3 sentences." +

                    "\n\nEnsure descriptions are technically accurate, precise, and consistent with the mathematical properties of the color, not on subjective interpretation."
                    "\nDon't include headers for the color name or description."
                },
                {"role": "user", "content": f"{hexCode}"},
            ],
            stream=False
        )
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error getting AI response: {e}", ephemeral=True)
        return

    try:

        embed = discord.Embed(
            title=f"**{nearestColorName}**",
            description="",
            color=discord.Color(MinMaxHexInt(int(f"0x{hexCode}", 16)))
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
        pureAndTrueColorDictionary = {**pureColorToDiscordEmotes, **trueColorToDiscordEmotes}
        for color in pureAndTrueColorDictionary.keys():
            colorHex = color.value[1]
            colorDistance = GetAbsoluteDifference(hexColor, HexColor(baseHex=colorHex))
            if colorDistance < closestPureColorDistance:
                closestPureColorDistance = colorDistance
                closestPureColor = color

        if closestPureColor is not None:
            embed.add_field(
                name=f"**Closest Pure Color**",
                value=f"{pureAndTrueColorDictionary[closestPureColor]} `{closestPureColor.value[0]}` - {closestPureColorDistance} off",
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
            value=f"{aiResponseData.choices[0].message.content.strip()}",
            inline=False
        )
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error getting closest color: {e}", ephemeral=True)
        return

    try:
        colorSquare = CreateColorSquare([hexColor], imageSize=128)
        buffer = io.BytesIO()
        colorSquare.save(buffer, "PNG")
        buffer.seek(0)
        discordFile = discord.File(buffer, filename="colorSquare.png")

        embed.set_thumbnail(url=f"attachment://colorSquare.png")
        embed.set_footer(text=footerText, icon_url=avatarLink)
        embed.timestamp = interaction.created_at

        try:
            await interaction.followup.send(embed=embed, file=discordFile)
        except Forbidden as e:
            await interaction.followup.send(content=f"Error: Bot has no permissions to send images.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error creating color square: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='dyes',
    aliases=["dyelist", "alldyes", "alldye", "alldyeinfo", "dyeinfo", "dyeinformation", "alldyesinfo"],
    description=dyeInfoCommandDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayDyes(
    interaction: discord.Interaction
):
    pureColorsDescription = ""
    trueColorsDescription = ""

    pureAndTrueColorDictionary = {**pureColorToDiscordEmotes, **trueColorToDiscordEmotes}
    for color in pureAndTrueColorDictionary.keys():
        if color in pureColorToDiscordEmotes:
            pureColorsDescription += f"{pureAndTrueColorDictionary[color]} `#{color.value[1]}` - {color.value[0]}\n"
        else:
            trueColorsDescription += f"{pureAndTrueColorDictionary[color]} `#{color.value[1]}` - {color.value[0]}\n"

    embed = discord.Embed(
        title=f"**Dye Info**",
        description=f" ",
        color=defaultColor
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

@AppCommandWithAliases(
    client.tree,
    name='scanplayer',
    aliases=["playerscan", "playerinfo", "playerinformation", "scanplayerinfo", "scanplayerinformation"],
    description=scanPlayerCommandDescription
)
@app_commands.describe(
    player=scanPlayerCommandPlayerDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayScanPlayer(
    interaction: discord.Interaction,
    player: str
):
    if player is None:
        await interaction.response.send_message("Please provide a player.", ephemeral=True)
        return

    playerData = player.replace("-", "").lower().strip()

    playerUsername = None
    playerUUID = None
    headers = {
        "Content-Type": "application/json"
    }

    await interaction.response.defer(thinking=True, ephemeral=False)

    try:
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
            await interaction.followup.send(content=f"Error when looking up '{player}'.", ephemeral=True)
            return
        if playerUUID not in playerUUIDToItemList:
            await interaction.followup.send(content=f"Player '{player}' not found in the database.", ephemeral=True)
            return
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error getting player username: {e}", ephemeral=True)
        return

    try:
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
            for item in sorted(playerItemList, key = lambda x: x[0]):
                i += 1
                if i != 0:
                    tempDescription += f"\n"
                tempDescription += f"{extraString}#{item[1]} {extraString}{item[0]}"

            if playerItemCount > 25:
                buffer = io.BytesIO()
                buffer.write(tempDescription.encode())
                buffer.seek(0)

                fileName = f"{playerUUID.lower()}.txt"
                discordFile = discord.File(buffer, filename=fileName)
            else:
                currentDescription += f"{tempDescription}"

        embed = discord.Embed(
            title=f"**{playerUsername}**",
            description=f" ",
            color=defaultColor
        )
        embed.add_field(
            name=f"**UUID:**",
            value=f"{playerUUID.lower()}",
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
            try:
                await interaction.followup.send(embed=embed, file=discordFile)
            except Forbidden as e:
                await interaction.followup.send(content=f"Error: Bot has no permissions to send files.", ephemeral=True)
            return
        await interaction.followup.send(embed=embed)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error combining armors: {e}", ephemeral=True)

@AppCommandWithAliases(
    client.tree,
    name='allcolors',
    aliases=["allarmorcolors", "allarmorcolor"],
    description=allColorsCommandDescription
)
@app_commands.choices(
    outputshape=normalShapeChoices,
    outputversion=armorVersionChoices,
    colortype=allColorTypeChoices
)
@app_commands.describe(
    colortype=allColorsCommandColorTypeDescription,
    outputarmor=outputArmorDescription,
    outputshape=outputShapeDescription,
    outputversion=outputVersionDescription
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def displayAllColors(
    interaction: discord.Interaction,
    colortype: str,
    outputarmor: str = None,
    outputshape: str = None,
    outputversion: str = None,
    mixcount: int = None
):
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

    mixColors = False

    inputItemListList = []
    colorList = []
    fairyColorList = []
    if colortype == "Fairy":
        fairyColorList = list(allFairyHexes.items())[::-1]
    elif colortype == "OG Fairy":
        fairyColorList = list(allFairyHexes.items())
    elif colortype == "All Fairy":
        fairyColorList = list(allFairyHexes.items())
    elif colortype == "Crystal":
        colorList = list(allCrystalHexes.items())
    elif colortype == "Pure Colors":
        colorList = list(allPureExoticHexes.items())
    elif colortype == "True Colors":
        for color in trueColorToDiscordEmotes.keys():
            colorList.append(color)
    elif colortype == "Pure+True Colors":
        colorList = list(allPureExoticHexes.items())
        for color in trueColorToDiscordEmotes.keys():
            colorList.append(color)
    elif colortype == "Hypixel Dyes":
        colorList = allHypixelDyeHexes.items()
    elif colortype == "Mix Pure Colors":
        if mixcount is None:
            mixcount = 1
        if mixcount < 1 or mixcount > 8:
            await interaction.response.send_message("Please provide a valid mix count (1-8).", ephemeral=True)
            return

        if outputarmor == "fullset":
            await interaction.response.send_message("Invalid armor type 'fullset' for mix pure colors.", ephemeral=True)
            return

        mixColors = True
    else:
        await interaction.response.send_message(f"Invalid color type '{colortype}'", ephemeral=True)
        return

    if len(colorList) == 0 and len(fairyColorList) == 0 and not mixColors:
        await interaction.response.send_message(f"No colors found for '{colortype}'", ephemeral=True)
        return

    await interaction.response.defer(thinking=True, ephemeral=False)

    armorSpacing = 10
    try:
        armorEnumString = str(armorEnum).replace(" ", "").strip().lower()
        finalText = ""
        if len(colorList) > 0:
            for color in colorList:
                try:
                    hexColor = HexColor(baseHex=color[1])
                except Exception as e:
                    hexColor = HexColor(baseHex=color.value[1])
                hexCode = hexColor.GetHexCode()
                finalString = f"{hexCode} {armorEnumString}".strip()
                inputItemListList.append(finalString)
                if finalText != "":
                    finalText += ", "
                finalText += f"#{hexCode}"
        elif len(fairyColorList) > 0:
            for color, fairyType in fairyColorList:
                itemList = []
                if colortype == "Fairy":
                    itemList = fairyType[0]
                elif colortype == "OG Fairy":
                    itemList = fairyType[1]
                elif colortype == "All Fairy":
                    itemList = fairyType[0] + fairyType[1]
                    if len(itemList) == 4:
                        itemList = ["All"]

                if len(itemList) == 0:
                    continue

                hexColor = HexColor(baseHex=color.value[1])
                hexCode = hexColor.GetHexCode()
                itemHex = ""
                itemName = armorEnumString if armorEnumString != "fullset" else ""
                allItems = ["Helmet", "Chestplate", "Leggings", "Boots"]
                if itemList == ["All"]:
                    itemList = allItems

                if finalText != "":
                    finalText += ", "
                finalText += f"#{hexCode}"
                if armorEnum == ArmorType.FullSet:
                    itemHex = hexCode
                    if len(itemList) != 4:
                        for itemType in itemList:
                            itemName += f"{itemType.lower()}"
                else:
                    i = -1
                    armorData = itemDict[armorEnum]
                    for armorColorData in armorData[1]:
                        i += 1
                        if armorColorData:
                            if allItems[i] in itemList:
                                itemHex += f"{hexCode} "
                            else:
                                itemHex += "empty "

                    if len(armorData) == 3:
                        armorSpacing = armorData[2]

                if itemHex.replace("empty", "").strip() == "":
                    continue
                finalString = f"{itemHex.strip()} {itemName.strip()}".strip()
                inputItemListList.append(finalString)
        else:
            hexDictionary = {}
            for color, exoticColorHex in allPureExoticHexes.items():
                armorData = itemDict[armorEnum]
                if len(armorData) == 3:
                    armorSpacing = armorData[2]
                for armorColorHex in armorData[1]:
                    if armorColorHex == "":
                        continue
                    try:
                        armorColor = HexColor(baseHex=armorColorHex)
                    except Exception as e:
                        await interaction.followup.send(content=f"Invalid hex code '{armorColorHex}' - {e}", ephemeral=True)
                        return

                    finalHex = armorColor
                    for i in range(mixcount):
                        try:
                            exoticColor = HexColor(baseHex=exoticColorHex)
                        except Exception as e:
                            await interaction.followup.send(content=f"Invalid hex code '{exoticColorHex}' - {e}", ephemeral=True)
                            return
                        finalHex = MixHexColorList(finalHex, [exoticColor])

                    if color not in hexDictionary:
                        hexDictionary[color] = []
                    hexDictionary[color].append(finalHex)

            for color in hexDictionary:
                finalString = ""
                for mixHex in hexDictionary[color]:
                    finalString += f"#{mixHex.GetHexCode().strip()} "

                inputItemListList.append(f"{finalString.strip()} {outputarmor.strip()}".strip())
                if finalText != "":
                    finalText += " | "
                finalText += f"+{mixcount} {pureColorToDiscordEmotes[color]}: {finalString.strip()}"

    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error parsing input: {e}", ephemeral=True)
        return

    try:
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
                        await interaction.followup.send(content=f"Invalid hex code '{baseHex}' - {e}", ephemeral=True)
                        return

            buffer, filePath, colors = GetCombinedArmorSetBuffer(
                armorType=armorEnum,
                hexList=hexList,
                versionType=versionEnum,
                shapeType=shapeEnum,
                imageXSpacing=0,
                imageYSpacing=20,
                imageSize=128
            )
            finalImageList.append((buffer, filePath, colors))
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error creating armors: {e}", ephemeral=True)
        return

    try:
        if len(finalImageList) == 0:
            await interaction.followup.send(content="Please provide at least one armor color or armor type.", ephemeral=True)
            return

        resultImage = Image.new(mode = 'RGBA', size = (0, 0), color = (0, 0, 0, 0))
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

        try:
            if finalText != "":
                finalText = f"**{finalText}**"
            await interaction.followup.send(content=finalText, file=discordFile)
        except Forbidden as e:
            await interaction.followup.send(content=f"Error: Bot has no permissions to send images.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(content=f"Unexpected Error combining armors: {e}", ephemeral=True)

if __name__ == "__main__":
    with open('AIToken') as file:
        aiClient = OpenAI(api_key=file.read().strip(), base_url="https://api.groq.com/openai/v1")

    with open('BotToken') as file:
        LoadColorNames()
        LoadDatabase("Database/Combined-S.html")
        client.run(file.read().strip())