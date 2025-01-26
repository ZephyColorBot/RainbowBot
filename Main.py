import re
import io
import discord

from discord.ext import commands
from discord import app_commands
from Armor import *

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

# @client.tree.command(name='hello', description='Say hello')
# async def sayHello(interaction):
#     await interaction.response.send_message('Hello!')

@client.tree.command(name='color', description='Generate hex code images.')
@app_commands.describe(colors="Enter a list of hex codes separated by spaces (e.g., #334CB2 #191919)")
async def displayColor(interaction, colors: str):
    originalHexList = re.split(r'(\s)', colors)
    originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]

    colorList = []
    colorString = ""
    for baseHex in originalHexList:
        fixedHex = GetFixedHex(baseHex)
        hexRGB = GetRBGFromHex(fixedHex)
        colorList.append(hexRGB)

        if colorString != "":
            colorString += ", "
        colorString += f"#{fixedHex}"

    buffer = io.BytesIO()
    image = CreateColorSquare(colorList)
    image.save(buffer, "PNG")

    buffer.seek(0)

    discordFile = discord.File(buffer, filename="colorSquare.png")
    await interaction.response.send_message(f"**{colorString}**", file=discordFile)

async def armor_type_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=str(option), value=str(option))
        for option in itemDict if current.lower() in str(option).lower()
    ][:25]
async def armor_color_type_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=str(option.value[0]), value=str(option.value[0]))
        for option in list(ColorType) if current.lower() in str(option.value[0]).lower()
    ][:25]

# TODO: fix to only be the dye colors
async def mix_color_type_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=str(option.value[0]), value=str(option.value[0]))
        for option in list(ColorType) if current.lower() in str(option.value[0]).lower()
    ][:25]

display_choices = [
    app_commands.Choice(name="Vertical", value="Vertical"),
    app_commands.Choice(name="Horizontal", value="Horizontal"),
    app_commands.Choice(name="Square", value="Square"),
]
armor_version_choices = [
    app_commands.Choice(name="1.8.9", value="1.8.9"),
    app_commands.Choice(name="1.14+", value="1.14+")
]

@client.tree.command(name='armor', description='Displays an armor set with the given hex color(s).')
@app_commands.autocomplete(armor=armor_type_autocomplete, colors=armor_color_type_autocomplete)
@app_commands.choices(shape=display_choices, version=armor_version_choices)
@app_commands.describe(
    colors="Enter a list of hex codes separated by spaces (e.g., #334CB2 #191919)",
    armor="Enter the armor type. (e.g., Superior, Young Baby)",
    shape="Enter the display type. (e.g., Vertical, Horizontal, Square)",
    version="Enter the version type. (e.g., 1.8.9, 1.14+)")
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
    if shape not in stringToDisplayTypeDict:
        await interaction.response.send_message(f"Invalid display type '{shape}'")
        return
    if version not in stringToVersionTypeDict:
        await interaction.response.send_message(f"Invalid version type '{version}'")
        return

    armorEnum = stringToArmorTypeDict[armor]
    shapeEnum = stringToDisplayTypeDict[shape]
    versionEnum = stringToVersionTypeDict[version]

    colorList = []
    colorString = ""
    if type(colors) == str:
        originalHexList = re.split(r'(\s)', colors)
        originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]

        for baseHex in originalHexList:
            fixedHex = GetFixedHex(baseHex)
            hexRGB = GetRBGFromHex(fixedHex)
            colorList.append(hexRGB)

    armorSet, colors = CreateArmorSetImage(
        armorType=armorEnum,
        hexList=colorList,
        versionType=versionEnum,
        displayType=shapeEnum,
        imageSpacing=20,
        imageSize=128
    )
    for baseHex in colors:
        if colorString != "":
            colorString += ", "
        colorString += f"#{GetFixedHex(baseHex)}"

    buffer = io.BytesIO()
    filePath = f"armorSet.png"
    if type(armorSet) == list:
        filePath = f"armorSet.webp"
        armorSet[0].save(
            buffer,
            save_all=True,
            append_images=armorSet[1:],
            duration=225,
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
    discordFile = discord.File(buffer, filename=filePath)
    await interaction.response.send_message(f"**{colorString}**", file=discordFile)

@client.tree.command(name='mix', description='Mixes the given hexes and displays the result.')
# @app_commands.autocomplete(colors=mix_color_type_autocomplete)
@app_commands.describe(
    colors="Enter a list of hex codes, they will be combined one by one. (Same as crafting after each dye)",
    craftingsequence1="Enter a list of hex codes, they will be combined in one step. (Same as putting 1-8 dyes then crafting)",
    craftingsequence2="Enter a list of hex codes, they will be combined in two steps. (Step 1 will be completed first, output will be used as start hex for step 2)",
    craftingsequence3="Enter a list of hex codes, they will be combined in three steps. (Step 2 will be completed first, output will be used as start hex for step 3)"
)
async def displayMix(interaction, colors: str = None, craftingsequence1: str = None, craftingsequence2: str = None, craftingsequence3: str = None):
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
    finalRGB = None
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

        for colorList in inputColorList:
            hexList = []
            for baseHex in colorList:
                fixedHex = GetFixedHex(baseHex)
                hexRGB = GetRBGFromHex(fixedHex)
                hexList.append(hexRGB)

            if finalRGB is None:
                finalRGB = MixRGBList(hexList[0], hexList[1:])
            else:
                finalRGB = MixRGBList(finalRGB, hexList)
    else:
        colorSplit = re.split(r'(\s)', colors)
        inputColorList += [[x for i, x in enumerate(colorSplit) if i % 2 == 0]]

        for colorList in inputColorList:
            hexList = []
            for baseHex in colorList:
                fixedHex = GetFixedHex(baseHex)
                hexRGB = GetRBGFromHex(fixedHex)
                hexList.append(hexRGB)

            for baseHex in hexList:
                if finalRGB is None:
                    finalRGB = baseHex
                else:
                    finalRGB = MixRGBList(finalRGB, [baseHex])

    print(2, finalRGB, GetHexFromRGB(finalRGB))

    # if colors is None and armor is None:
    #     await interaction.response.send_message("Please provide at least one hex code or armor type.")
    #     return
    #
    # if colors is None:
    #     colors = []
    # if armor is None:
    #     armor = "Full Set"
    # if shape is None:
    #     shape = "Vertical"
    # if version is None:
    #     version = "1.8.9"
    #
    # if type(armor) == str:
    #     armor = armor.lower().replace(' ', '').strip()
    # if type(shape) == str:
    #     shape = shape.lower().replace(' ', '').strip()
    # if type(version) == str:
    #     version = version.lower().replace(' ', '').strip()
    #
    # if armor not in stringToArmorTypeDict:
    #     await interaction.response.send_message(f"Invalid armor type '{armor}'")
    #     return
    # if shape not in stringToDisplayTypeDict:
    #     await interaction.response.send_message(f"Invalid display type '{shape}'")
    #     return
    # if version not in stringToVersionTypeDict:
    #     await interaction.response.send_message(f"Invalid version type '{version}'")
    #     return
    #
    # armorEnum = stringToArmorTypeDict[armor]
    # shapeEnum = stringToDisplayTypeDict[shape]
    # versionEnum = stringToVersionTypeDict[version]
    #
    # colorList = []
    # colorString = ""
    # if type(colors) == str:
    #     originalHexList = re.split(r'(\s)', colors)
    #     originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]
    #
    #     for baseHex in originalHexList:
    #         fixedHex = GetFixedHex(baseHex)
    #         hexRGB = GetRBGFromHex(fixedHex)
    #         colorList.append(hexRGB)
    #
    # armorSet, colors = CreateArmorSetImage(
    #     armorType=armorEnum,
    #     hexList=colorList,
    #     versionType=versionEnum,
    #     displayType=shapeEnum,
    #     imageSpacing=20,
    #     imageSize=128
    # )
    # for baseHex in colors:
    #     if colorString != "":
    #         colorString += ", "
    #     colorString += f"#{GetFixedHex(baseHex)}"
    #
    # buffer = io.BytesIO()
    # filePath = f"Output/armorSet.png"
    # if type(armorSet) == list:
    #     filePath = f"Output/armorSet.webp"
    #     armorSet[0].save(
    #         buffer,
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
    #     armorSet.save(
    #         buffer,
    #         format="PNG",
    #         quality=100,
    #         # method=3,
    #         lossless=True
    #     )
    #
    # buffer.seek(0)
    # discordFile = discord.File(buffer, filename=filePath)
    # await interaction.response.send_message(f"**{colorString}**", file=discordFile)

@client.tree.command(name='help', description='Displays information about the bot.')
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
        value = "Displays an armour set with the given hex color(s).\n-# Optional Armor Type and Display Type.\n-# Aliases: /armour",
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
        name = "/exotic <hexes>",
        value = "Checks the type of the given hexes.\n-# Aliases: /fairy, /crystal",
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

with open('BotToken') as file:
    client.run(file.read().strip())