import io
import re
import math
import discord
import imageio

from PIL import Image, ImageDraw
from discord.ext import commands
from discord import app_commands, Color
from typing import Optional
from enum import Enum

stringToColorTypeDict = {}
stringToArmorTypeDict = {}
stringToItemTypeDict = {}
stringToVersionTypeDict = {}
stringToDisplayTypeDict = {}

class ColorType(Enum):
    PureRed = ("Red", "993333")
    Red = PureRed
    PureOrange = ("Orange", "D87F33")
    Orange = PureOrange
    PureYellow = ("Yellow", "E5E533")
    Yellow = PureYellow
    PureLime = ("Lime", "7FCC19")
    Lime = PureLime
    PureDarkGreen = ("DarkGreen", "667F33")
    DarkGreen = PureDarkGreen
    PureGreen = PureDarkGreen
    Green = PureDarkGreen
    PureDG = PureDarkGreen
    DG = PureDarkGreen
    PureLightBlue = ("LightBlue", "6699D8")
    LightBlue = PureLightBlue
    PureLB = PureLightBlue
    LB = PureLightBlue
    PureCyan = ("Cyan", "4C7F99")
    Cyan = PureCyan
    PureDarkBlue = ("DarkBlue", "334CB2")
    DarkBlue = PureDarkBlue
    PureBlue = PureDarkBlue
    Blue = PureDarkBlue
    PureDB = PureDarkBlue
    DB = PureDarkBlue
    PurePink = ("Pink", "F27FA5")
    Pink = PurePink
    PureMagenta = ("Magenta", "B24CD8")
    Magenta = PureMagenta
    PurePurple = ("Purple", "7F3FB2")
    Purple = PurePurple
    PureBrown = ("Brown", "664C33")
    Brown = PureBrown
    PureLightGrey = ("LightGray", "999999")
    LightGrey = PureLightGrey
    PureLightGray = PureLightGrey
    LightGray = PureLightGrey
    PureGray = PureLightGrey
    Gray = PureLightGrey
    PureGrey = PureLightGrey
    Grey = PureLightGrey
    PureDarkGrey = ("DarkGray", "4C4C4C")
    DarkGrey = PureDarkGrey
    PureDarkGray = PureDarkGrey
    DarkGray = PureDarkGrey
    PureWhite = ("White", "FFFFFF")
    White = PureWhite
    PureBlack = ("Black", "191919")
    Black = PureBlack
    TrueBlack = ("TrueBlack", "000000")

    TrueLeather = ("Leather", "A06540")
    Leather = TrueLeather
    TrueMint = ("Mint", "86D28D")
    Mint = TrueMint
    TrueMaroon = ("Maroon", "592626")
    Maroon = TrueMaroon
    TrueNavy = ("Navy", "263265")
    Navy = TrueNavy
    TrueIce = ("Ice", "B2CCEB")
    Ice = TrueIce
    TrueGold = ("Gold", "DEB233")
    Gold = TrueGold

    Holy = ("Holy", "47D147")
    Old = ("Old", "F0E6AA")
    Protector = ("Protector", "99978B")
    StrongChestplate = ("StrongChestplate", "D91E41")
    StrongLeggings = ("StrongLeggings", "E09419")
    StrongBoots = ("StrongBoots", "F0D124")
    Superior = ("Superior", "F2DF11")
    SuperiorBoots = ("SuperiorBoots", "F25D18")
    Unstable = ("Unstable", "B212E3")
    Wise = ("Wise", "29F0E9")
    Young = ("Young", "DDE4F0")
    Angler = ("Angler", "0B004F")
    ArmorOfThePackHelmet = ("PackHelmet", "FFFFFF")
    ArmorOfThePackChestplate = ("PackChestplate", "FF0000")
    Bat = ("Bat", "000000")
    Biohazard = ("Biohazard", "FFAC00")
    Blaze = ("Blaze", "F7DA33")
    FrozenBlaze = ("FrozenBlaze", "A0DAEF")
    Goblin = ("Goblin", "37B042")
    Glacite = ("Glacite", "03FCF8")
    GoldorChestplate = ("GoldorChestplate", "45413C")
    GoldorLeggings = ("GoldorLeggings", "65605A")
    GoldorBoots = ("GoldorBoots", "88837E")
    Lapis = ("Lapis", "0000FF")
    Leaflet = ("Leaflet", "4DCC4D")
    MaxorChestplate = ("MaxorChestplate", "4A14B7")
    MaxorLeggings = ("MaxorLeggings", "5D2FB9")
    MaxorBoots = ("MaxorBoots", "8969C8")
    NecromancerLordChestplate = ("NecromancerLordChestplate", "000000")
    NecromancerLordLeggings = ("NecromancerLordLeggings", "370147")
    NecromancerLordBoots = ("NecromancerLordBoots", "400352")
    NecronChestplate = ("NecronChestplate", "E7413C")
    NecronLeggings = ("NecronLeggings", "E75C3C")
    NecronBoots = ("NecronBoots", "E76E3C")
    RisingSunLeggings = ("RisingSunLeggings", "DEBC15")
    RisingSunBoots = ("RisingSunBoots", "9F8609")
    ShadowAssassin = ("ShadowAssassin", "000000")
    Shark = ("Shark", "002CA6")
    SnowSuit = ("SnowSuit", "FFFFFF")
    Sponge = ("Sponge", "FFDC51")
    Spooky = ("Spooky", "606060")
    StormChestplate = ("StormChestplate", "1793C4")
    StormLeggings = ("StormLeggings", "17A8C4")
    StormBoots = ("StormBoots", "1CD4E4")
    Tarantula = ("Tarantula", "000000")
    CheapTuxedoChestplate = ("CheapTuxedoChestplate", "383838")
    CheapTuxedoLeggings = ("CheapTuxedoLeggings", "C7C7C7")
    CheapTuxedoBoots = ("CheapTuxedoBoots", "383838")
    FancyTuxedoChestplate = ("FancyTuxedoChestplate", "332A2A")
    FancyTuxedoLeggings = ("FancyTuxedoLeggings", "d4d4d4")
    FancyTuxedoBoots = ("FancyTuxedoBoots", "332A2A")
    ElegantTuxedoChestplate = ("ElegantTuxedoChestplate", "191919")
    ElegantTuxedoLeggings = ("ElegantTuxedoLeggings", "FEFDFC")
    ElegantTuxedoBoots = ("ElegantTuxedoBoots", "191919")
    Werewolf = ("Werewolf", "1D1105")

    FF3399 = ("FF3399", "FF3399")
    F39 = FF3399
    FF007F = ("FF007F", "FF007F")
    _660033 = ("660033", "660033")
    _603 = _660033
    _99004C = ("99004C", "99004C")
    CC0066 = ("CC0066", "CC0066")
    C06 = CC0066
    FF66B2 = ("FF66B2", "FF66B2")
    FF99CC = ("FF99CC", "FF99CC")
    F9C = FF99CC
    FFCCE5 = ("FFCCE5", "FFCCE5")
    _660066 = ("660066", "660066")
    _606 = _660066
    _990099 = ("990099", "990099")
    _909 = _990099
    CC00CC = ("CC00CC", "CC00CC")
    C0C = CC00CC
    FF00FF = ("FF00FF", "FF00FF")
    F0F = FF00FF
    FF33FF = ("FF33FF", "FF33FF")
    F3F = FF33FF
    FF66FF = ("FF66FF", "FF66FF")
    F6F = FF66FF
    FF99FF = ("FF99FF", "FF99FF")
    F9F = FF99FF
    FFCCFF = ("FFCCFF", "FFCCFF")
    E5CCFF = ("E5CCFF", "E5CCFF")
    ECF = E5CCFF
    CC99FF = ("CC99FF", "CC99FF")
    C9F = CC99FF
    B266FF = ("B266FF", "B266FF")
    B6F = B266FF
    _9933FF = ("9933FF", "9933FF")
    _93F = _9933FF
    _7F00FF = ("7F00FF", "7F00FF")
    _6600CC = ("6600CC", "6600CC")
    _60C = _6600CC
    _4C0099 = ("4C0099", "4C0099")
    _330066 = ("330066", "330066")
    _306 = _330066

    FCF3FF = ("FCF3FF", "FCF3FF")
    FCF = FCF3FF
    EFE1F5 = ("EFE1F5", "EFE1F5")
    EFE = EFE1F5
    E5D1ED = ("E5D1ED", "E5D1ED")
    E5D = E5D1ED
    D9C1E3 = ("D9C1E3", "D9C1E3")
    D9C = D9C1E3
    C6A3D4 = ("C6A3D4", "C6A3D4")
    C6A = C6A3D4
    B88BC9 = ("B88BC9", "B88BC9")
    B88B = B88BC9
    BOOB = B88BC9
    BOOBS = B88BC9
    A875BD = ("A875BD", "A875BD")
    A87 = A875BD
    _9C64B3 = ("9C64B3", "9C64B3")
    _9C6 = _9C64B3
    _8E51A6 = ("8E51A6", "8E51A6")
    _8E5 = _8E51A6
    _7E4196 = ("7E4196", "7E4196")
    _7E4 = _7E4196
    _6A2C82 = ("6A2C82", "6A2C82")
    _6A2 = _6A2C82
    _63237D = ("63237D", "63237D")
    _632 = _63237D
    _5D1C78 = ("5D1C78", "5D1C78")
    _5D1 = _5D1C78
    _46085E = ("46085E", "46085E")
    _460 = _46085E
    _1F0030 = ("1F0030", "1F0030")
    _1F0 = _1F0030

    Bleach = TrueLeather
    Bleached = TrueLeather

    @staticmethod
    def GetOtherNames():
        return [
            ("660033", ColorType._660033),
            ("603", ColorType._660033),
            ("99004C", ColorType._99004C),
            ("660066", ColorType._660066),
            ("606", ColorType._660066),
            ("990099", ColorType._990099),
            ("909", ColorType._990099),
            ("9933FF", ColorType._9933FF),
            ("93F", ColorType._9933FF),
            ("7F00FF", ColorType._7F00FF),
            ("6600CC", ColorType._6600CC),
            ("60C", ColorType._6600CC),
            ("4C0099", ColorType._4C0099),
            ("330066", ColorType._330066),
            ("306", ColorType._330066),

            ("9C64B3", ColorType._9C64B3),
            ("9C6", ColorType._9C64B3),
            ("8E51A6", ColorType._8E51A6),
            ("8E5", ColorType._8E51A6),
            ("7E4196", ColorType._7E4196),
            ("7E4", ColorType._7E4196),
            ("6A2C82", ColorType._6A2C82),
            ("6A2", ColorType._6A2C82),
            ("63237D", ColorType._63237D),
            ("632", ColorType._63237D),
            ("5D1C78", ColorType._5D1C78),
            ("5D1", ColorType._5D1C78),
            ("46085E", ColorType._46085E),
            ("460", ColorType._46085E),
            ("1F0030", ColorType._1F0030),
            ("1F0", ColorType._1F0030)
        ]

    def __str__(self):
        return self.value

class ItemType(Enum):
    Helmet = "Helmet"
    Chestplate = "Chestplate"
    Leggings = "Leggings"
    Boots = "Boots"

    def __str__(self):
        return self.value

class VersionType(Enum):
    _1_8_9 = "Old"
    _1_14 = "New"

    @staticmethod
    def GetOtherNames():
        return [
            ("Old", VersionType._1_8_9),
            ("New", VersionType._1_14),
            ("1.8.9", VersionType._1_8_9),
            ("1.14", VersionType._1_14),
            ("1.14+", VersionType._1_14),
            ("1.20", VersionType._1_14),
            ("1.20+", VersionType._1_14),
        ]

    def __str__(self):
        return self.value

class DisplayType(Enum):
    Vertical = "Vertical"
    Horizontal = "Horizontal"
    Square = "Square"

    def __str__(self):
        return self.value

class ArmorType(Enum):
    FullSet = "Full Set"
    Helmet = "Helmet"
    Chestplate = "Chestplate"
    Leggings = "Leggings"
    Boots = "Boots"
    Holy = "Holy"
    HolyBaby = "Holy Baby"
    HolyShimmer = "Holy Shimmer"
    Old = "Old"
    OldBaby = "Old Baby"
    OldShimmer = "Old Shimmer"
    Protector = "Protector"
    ProtectorBaby = "Protector Baby"
    ProtectorShimmer = "Protector Shimmer"
    Strong = "Strong"
    StrongBaby = "Strong Baby"
    StrongShimmer = "Strong Shimmer"
    Superior = "Superior"
    SuperiorBaby = "Superior Baby"
    SuperiorShimmer = "Superior Shimmer"
    Unstable = "Unstable"
    UnstableBaby = "Unstable Baby"
    UnstableShimmer = "Unstable Shimmer"
    Wise = "Wise"
    WiseBaby = "Wise Baby"
    WiseShimmer = "Wise Shimmer"
    Young = "Young"
    YoungBaby = "Young Baby"
    YoungShimmer = "Young Shimmer"
    Angler = "Angler"
    ArmorOfThePack = "Armor Of The Pack"
    Bat = "Bat"
    Biohazard = "Biohazard"
    Blaze = "Blaze"
    FrozenBlaze = "Frozen Blaze"
    FrozenBlazeIcicle = "Frozen Blaze Icicle"
    Glacite = "Glacite"
    Goblin = "Goblin"
    GoblinBaby = "Goblin Baby"
    Goldor = "Goldor"
    GoldorCelesital = "Goldor Celesital"
    Lapis = "Lapis"
    Leaflet = "Leaflet"
    Maxor = "Maxor"
    MaxorCelesital = "Maxor Celesital"
    Necron = "Necron"
    NecronCelesital = "Necron Celesital"
    NecromancerLord = "Necromancer Lord"
    RisingSun = "Rising Sun"
    ShadowAssassin = "Shadow Assassin"
    ShadowAssassinAdmiral = "Shadow Assassin Admiral"
    ShadowAssassinCrimson = "Shadow Assassin Crimson"
    ShadowAssassinMuave = "Shadow Assassin Muave"
    Shark = "Shark"
    SnowSuit = "Snow Suit"
    SnowSuitSnowglobe = "Snow Suit Snowglobe"
    SpaceHelmet = "Space Helmet"
    Sponge = "Sponge"
    Spooky = "Spooky"
    Storm = "Storm"
    StormCelesital = "Storm Celesital"
    Tarantula = "Tarantula"
    Tuxedo = "Tuxedo"
    Werewolf = "Werewolf"

    def __str__(self):
        return self.value

def PopulateStringDictionaries():
    for name, colorType in ColorType.__members__.items():
        colorName = name.replace(" ", "").lower().strip()
        stringToColorTypeDict[colorName] = colorType
    for colorType in ColorType.GetOtherNames():
        colorName = colorType[0].replace(" ", "").lower().strip()
        stringToColorTypeDict[colorName] = colorType[1]

    for name, armorType in ArmorType.__members__.items():
        armorName = armorType.name.replace(" ", "").lower().strip()
        stringToArmorTypeDict[armorName] = armorType

    for name, itemType in ItemType.__members__.items():
        itemName = itemType.name.replace(" ", "").lower().strip()
        stringToItemTypeDict[itemName] = itemType

    for name, versionType in VersionType.__members__.items():
        versionName = versionType.name.replace(" ", "").lower().strip()
        stringToVersionTypeDict[versionName] = versionType
    for versionType in VersionType.GetOtherNames():
        versionName = versionType[0].replace(" ", "").lower().strip()
        stringToVersionTypeDict[versionName] = versionType[1]

    for name, displayType in DisplayType.__members__.items():
        displayName = displayType.name.replace(" ", "").lower().strip()
        stringToDisplayTypeDict[displayName] = displayType
PopulateStringDictionaries()

itemDict = {
    ArmorType.FullSet: (["LeatherHelmet.png", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], [ColorType.Leather.value[1], ColorType.Leather.value[1], ColorType.Leather.value[1], ColorType.Leather.value[1]]),
    ArmorType.Helmet: (["LeatherHelmet.png"], [ColorType.Leather.value[1]]),
    ArmorType.Chestplate: (["LeatherChestplate.png"], [ColorType.Leather.value[1]]),
    ArmorType.Leggings: (["LeatherLeggings.png"], [ColorType.Leather.value[1]]),
    ArmorType.Boots: (["LeatherBoots.png"], [ColorType.Leather.value[1]]),
    ArmorType.Holy: (["HolyHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Holy.value[1], ColorType.Holy.value[1], ColorType.Holy.value[1]]),
    ArmorType.HolyBaby: (["HolyHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Holy.value[1], ColorType.Holy.value[1], ColorType.Holy.value[1]]),
    ArmorType.HolyShimmer: (["a_HolyHelmetShimmer.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Holy.value[1], ColorType.Holy.value[1], ColorType.Holy.value[1]]),
    ArmorType.Old: (["OldHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Old.value[1], ColorType.Old.value[1], ColorType.Old.value[1]]),
    ArmorType.OldBaby: (["OldHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Old.value[1], ColorType.Old.value[1], ColorType.Old.value[1]]),
    ArmorType.OldShimmer: (["a_OldHelmetShimmer.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Old.value[1], ColorType.Old.value[1], ColorType.Old.value[1]]),
    ArmorType.Protector: (["ProtectorHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Protector.value[1], ColorType.Protector.value[1], ColorType.Protector.value[1]]),
    ArmorType.ProtectorBaby: (["ProtectorHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Protector.value[1], ColorType.Protector.value[1], ColorType.Protector.value[1]]),
    ArmorType.ProtectorShimmer: (["a_ProtectorHelmetShimmer.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Protector.value[1], ColorType.Protector.value[1], ColorType.Protector.value[1]]),
    ArmorType.Strong: (["StrongHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.StrongChestplate.value[1], ColorType.StrongLeggings.value[1], ColorType.StrongBoots.value[1]]),
    ArmorType.StrongBaby: (["StrongHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.StrongChestplate.value[1], ColorType.StrongLeggings.value[1], ColorType.StrongBoots.value[1]]),
    ArmorType.StrongShimmer: (["a_StrongHelmetShimmer.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.StrongChestplate.value[1], ColorType.StrongLeggings.value[1], ColorType.StrongBoots.value[1]]),
    ArmorType.Superior: (["SuperiorHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Superior.value[1], ColorType.Superior.value[1], ColorType.SuperiorBoots.value[1]]),
    ArmorType.SuperiorBaby: (["SuperiorHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Superior.value[1], ColorType.Superior.value[1], ColorType.SuperiorBoots.value[1]]),
    ArmorType.SuperiorShimmer: (["a_SuperiorHelmetShimmer.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Superior.value[1], ColorType.Superior.value[1], ColorType.SuperiorBoots.value[1]]),
    ArmorType.Unstable: (["UnstableHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Unstable.value[1], ColorType.Unstable.value[1], ColorType.Unstable.value[1]]),
    ArmorType.UnstableBaby: (["UnstableHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Unstable.value[1], ColorType.Unstable.value[1], ColorType.Unstable.value[1]]),
    ArmorType.UnstableShimmer: (["a_UnstableHelmetShimmer.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Unstable.value[1], ColorType.Unstable.value[1], ColorType.Unstable.value[1]]),
    ArmorType.Wise: (["WiseHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Wise.value[1], ColorType.Wise.value[1], ColorType.Wise.value[1]]),
    ArmorType.WiseBaby: (["WiseHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Wise.value[1], ColorType.Wise.value[1], ColorType.Wise.value[1]]),
    ArmorType.WiseShimmer: (["a_WiseHelmetShimmer.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Wise.value[1], ColorType.Wise.value[1], ColorType.Wise.value[1]]),
    ArmorType.Young: (["YoungHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Young.value[1], ColorType.Young.value[1], ColorType.Young.value[1]]),
    ArmorType.YoungBaby: (["YoungHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Young.value[1], ColorType.Young.value[1], ColorType.Young.value[1]]),
    ArmorType.YoungShimmer: (["a_YoungHelmetShimmer.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Young.value[1], ColorType.Young.value[1], ColorType.Young.value[1]]),
    ArmorType.Angler: (["AnglerHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Angler.value[1], ColorType.Angler.value[1], ColorType.Angler.value[1]]),
    ArmorType.ArmorOfThePack: (["LeatherHelmet.png", "LeatherChestplate.png", "IronLeggings.webp", "IronBoots.webp"], [ColorType.ArmorOfThePackHelmet.value[1], ColorType.ArmorOfThePackChestplate.value[1], "", ""]),
    ArmorType.Bat: (["BatHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Bat.value[1], ColorType.Bat.value[1], ColorType.Bat.value[1]]),
    ArmorType.Biohazard: (["BiohazardHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Biohazard.value[1], ColorType.Biohazard.value[1], ColorType.Biohazard.value[1]]),
    ArmorType.Blaze: (["BlazeHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Blaze.value[1], ColorType.Blaze.value[1], ColorType.Blaze.value[1]]),
    ArmorType.FrozenBlaze: (["FrozenBlazeHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.FrozenBlaze.value[1], ColorType.FrozenBlaze.value[1], ColorType.FrozenBlaze.value[1]]),
    ArmorType.FrozenBlazeIcicle: (["FrozenBlazeHelmetIcicle.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.FrozenBlaze.value[1], ColorType.FrozenBlaze.value[1], ColorType.FrozenBlaze.value[1]]),
    ArmorType.Glacite: (["GlaciteHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Glacite.value[1], ColorType.Glacite.value[1], ColorType.Glacite.value[1]]),
    ArmorType.Goblin: (["GoblinHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Goblin.value[1], ColorType.Goblin.value[1], ColorType.Goblin.value[1]]),
    ArmorType.GoblinBaby: (["GoblinHelmetBaby.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Goblin.value[1], ColorType.Goblin.value[1], ColorType.Goblin.value[1]]),
    ArmorType.Goldor: (["GoldorHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.GoldorChestplate.value[1], ColorType.GoldorLeggings.value[1], ColorType.GoldorBoots.value[1]]),
    ArmorType.GoldorCelesital: (["a_GoldorHelmetCelestial.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.GoldorChestplate.value[1], ColorType.GoldorLeggings.value[1], ColorType.GoldorBoots.value[1]]),
    ArmorType.Lapis: (["LapisHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Lapis.value[1], ColorType.Lapis.value[1], ColorType.Lapis.value[1]]),
    ArmorType.Leaflet: (["OakLeaves.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Leaflet.value[1], ColorType.Leaflet.value[1], ColorType.Leaflet.value[1]]),
    ArmorType.Maxor: (["MaxorHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.MaxorChestplate.value[1], ColorType.MaxorLeggings.value[1], ColorType.MaxorBoots.value[1]]),
    ArmorType.MaxorCelesital: (["a_MaxorHelmetCelestial.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.MaxorChestplate.value[1], ColorType.MaxorLeggings.value[1], ColorType.MaxorBoots.value[1]]),
    ArmorType.NecromancerLord: (["NecromancerLordHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.NecromancerLordChestplate.value[1], ColorType.NecromancerLordLeggings.value[1], ColorType.NecromancerLordBoots.value[1]]),
    ArmorType.Necron: (["NecronHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.NecronChestplate.value[1], ColorType.NecronLeggings.value[1], ColorType.NecronBoots.value[1]]),
    ArmorType.NecronCelesital: (["a_NecronHelmetCelestial.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.NecronChestplate.value[1], ColorType.NecronLeggings.value[1], ColorType.NecronBoots.value[1]]),
    ArmorType.RisingSun: (["RisingSunHelmet.webp", "GoldenChestplate.webp", "LeatherLeggings.png", "LeatherBoots.png"], ["", "", ColorType.RisingSunLeggings.value[1], ColorType.RisingSunBoots.value[1]]),
    ArmorType.ShadowAssassin: (["ShadowAssassinHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.ShadowAssassin.value[1], ColorType.ShadowAssassin.value[1], ColorType.ShadowAssassin.value[1]]),
    ArmorType.ShadowAssassinAdmiral: (["ShadowAssassinHelmetAdmiral.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.ShadowAssassin.value[1], ColorType.ShadowAssassin.value[1], ColorType.ShadowAssassin.value[1]]),
    ArmorType.ShadowAssassinCrimson: (["ShadowAssassinHelmetCrimson.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.ShadowAssassin.value[1], ColorType.ShadowAssassin.value[1], ColorType.ShadowAssassin.value[1]]),
    ArmorType.ShadowAssassinMuave: (["ShadowAssassinHelmetMauve.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.ShadowAssassin.value[1], ColorType.ShadowAssassin.value[1], ColorType.ShadowAssassin.value[1]]),
    ArmorType.Shark: (["SharkHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Shark.value[1], ColorType.Shark.value[1], ColorType.Shark.value[1]]),
    ArmorType.SnowSuit: (["SnowSuitHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.SnowSuit.value[1], ColorType.SnowSuit.value[1], ColorType.SnowSuit.value[1]]),
    ArmorType.SnowSuitSnowglobe: (["a_SnowSuitHelmetSnowglobe.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.SnowSuit.value[1], ColorType.SnowSuit.value[1], ColorType.SnowSuit.value[1]]),
    ArmorType.SpaceHelmet: (["a_OldSpaceHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Leather.value[1], ColorType.Leather.value[1], ColorType.Leather.value[1]]),
    ArmorType.Sponge: (["SpongeHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Sponge.value[1], ColorType.Sponge.value[1], ColorType.Sponge.value[1]]),
    ArmorType.Spooky: (["SpookyHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Spooky.value[1], ColorType.Spooky.value[1], ColorType.Spooky.value[1]]),
    ArmorType.Storm: (["StormHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.StormChestplate.value[1], ColorType.StormLeggings.value[1], ColorType.StormBoots.value[1]]),
    ArmorType.StormCelesital: (["a_StormHelmetCelestial.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.StormChestplate.value[1], ColorType.StormLeggings.value[1], ColorType.StormBoots.value[1]]),
    ArmorType.Tarantula: (["LeatherHelmet.png", "ChainmailChestplate.webp", "LeatherLeggings.png", "ChainmailBoots.webp"], [ColorType.Tarantula.value[1], "", ColorType.Tarantula.value[1], ""]),
    ArmorType.Tuxedo: (["LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], [ColorType.CheapTuxedoChestplate.value[1], ColorType.CheapTuxedoLeggings.value[1], ColorType.CheapTuxedoBoots.value[1]]),
    ArmorType.Werewolf: (["WerewolfHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", ColorType.Werewolf.value[1], ColorType.Werewolf.value[1], ColorType.Werewolf.value[1]])
}

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

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

        # try:
        #     synced = await self.tree.sync()
        #     print(f'Synced {synced} commands')
        # except Exception as e:
        #     print(f'Failed to sync commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'hello':
            await message.channel.send('Hello!')

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix='/', intents=intents)

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

def GetFixedHex(hex):
    if hex is None:
        return "000000"
    if type(hex) is list:
        hex = GetHexFromRGB(hex)

    hex = hex.lower().strip()
    if hex in stringToColorTypeDict:
        hex = stringToColorTypeDict[hex].value[1]

    hex = hex.upper().replace(',', '')
    hex = hex.lstrip('#').strip()
    hex = hex.rjust(6, '0')
    return hex

def GetRBGFromHex(hex):
    color = list(int(hex[i:i+2], 16) for i in (0, 2, 4))
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

        total_rows = math.ceil(num_images / grid_size)
        grid_height = total_rows * (max_height + imageSpacing) - imageSpacing

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
    for hex in finalHexList:
        if hex == "" or hex is None:
            continue
        returnHexList.append(hex)

    return image, returnHexList

def GetArmorPiecePath(itemType: ItemType) -> str:
    return f"Images/{itemType}.png"

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
    if overlayPath is not None:
        if "Leather" in overlayPath:
            if str(versionType) not in overlayPath:
                splitPath = overlayPath.split("Leather")
                overlayPath = f"{splitPath[0]}{versionType}Leather{splitPath[1]}"

            if "128x" not in overlayPath and "256x" not in overlayPath:
                targetSize = "256x"
                if imageSize == 128:
                    targetSize = "128x"
                elif imageSize == 256:
                    targetSize = "256x"

                splitPath = overlayPath.split("/")
                overlayPath = f"{splitPath[0]}/{targetSize}{splitPath[1]}"

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

# @client.tree.command(name='helloo', description='Say hello')
# async def sayHello(interaction):
#     await interaction.response.send_message('Hello!')

@client.tree.command(name='color', description='Generate hex code images.')
@app_commands.describe(hexcodes="Enter a list of hex codes separated by spaces (e.g., #334CB2 #191919)")
async def displayColor(interaction, hexcodes: str):
    originalHexList = re.split(r'(\s)', hexcodes)
    originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]

    colorList = []
    colorString = ""
    for hex in originalHexList:
        fixedHex = GetFixedHex(hex)
        hexRGB = GetRBGFromHex(fixedHex)
        colorList.append(hexRGB)

        if colorString != "":
            colorString += ", "
        colorString += f"#{fixedHex}"

    image = CreateColorSquare(colorList)
    image.save("colorSquare.png", "PNG")

    file = discord.File("colorSquare.png", filename="colorSquare.png")
    await interaction.response.send_message(f"**{colorString}**", file=file)


async def armor_type_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=str(option), value=str(option))
        for option in itemDict if current.lower() in str(option).lower()
    ][:25]
async def color_type_autocomplete(interaction: discord.Interaction, current: str):
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

@client.tree.command(name='armor', description='Displays an armour set with the given hex color(s).')
@app_commands.autocomplete(armor=armor_type_autocomplete, colors=color_type_autocomplete)
@app_commands.choices(shape=display_choices, version=armor_version_choices)
@app_commands.describe(colors="Enter a list of hex codes separated by spaces (e.g., #334CB2 #191919)")
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

    hexList = []
    colorList = []
    colorString = ""
    if type(colors) == str:
        originalHexList = re.split(r'(\s)', colors)
        originalHexList = [x for i, x in enumerate(originalHexList) if i % 2 == 0]

        for hex in originalHexList:
            fixedHex = GetFixedHex(hex)
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
    for hex in colors:
        if colorString != "":
            colorString += ", "
        colorString += f"#{GetFixedHex(hex)}"

    filePath = "armorSet.png"
    if type(armorSet) == list:
        filePath = "armorSet.webp"
        armorSet[0].save(
            filePath,
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
            filePath,
            format="PNG",
            quality=100,
            method=3,
            lossless=True
        )

    file = discord.File(filePath, filename=filePath)
    await interaction.response.send_message(f"**{colorString}**", file=file)

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
        name = "/armor <hexes> [<armortype>] [<displaytype>]",
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

# # /armor
# # /color - DONE
# # /exotic
# # /help
# # /info
# # /mix

# armorSet = CreateArmorSetImage(
#     armorTypeString="Full Set",
#     hexList=["e753c3", "E75C3C", "1B08BF", "A8DEAD"],
#     leatherArmorType=LeatherType.Old,
#     displayType=DisplayType.Vertical,
#     imageSpacing=20,
#     imageSize=128
# )
# armorSet = CreateArmorSetImage(
#     armorTypeString="Young Baby",
#     hexList=["F18BAF", "F18BAF", "F18BAF"],
#     leatherArmorType=LeatherType.Old,
#     displayType=DisplayType.Vertical,
#     imageSpacing=20,
#     imageSize=128
# )
# armorSet = CreateArmorSetImage(
#     armorTypeString="Tarantula",
#     hexList=["E75C3C", "A8DEAD"],
#     leatherArmorType=LeatherType.Old,
#     displayType=DisplayType.Vertical,
#     imageSpacing=20,
#     imageSize=128
# )
# armorSet = CreateArmorSetImage(
#     armorTypeString="Space Helmet",
#     hexList=["E75C3C", "1B08BF", "A8DEAD"],
#     leatherArmorType=LeatherType.Old,
#     displayType=DisplayType.Square,
#     imageSpacing=20,
#     imageSize=128
# )
# armorSet = CreateArmorSetImage(
#     armorTypeString="Snow Suit Snowglobe",
#     hexList=["E75C3C", "1B08BF", "A8DEAD"],
#     leatherArmorType=LeatherType.Old,
#     displayType=DisplayType.Vertical,
#     imageSpacing=20,
#     imageSize=128
# )
# armorSet, colors = CreateArmorSetImage(
#     armorType=ArmorType.Holy,
#     hexList=[],
#     versionType=VersionType._1_8_9,
#     displayType=DisplayType.Vertical,
#     imageSpacing=20,
#     imageSize=128
# )

#
# if type(armorSet) == list:
#     output_path = "armorSet.webp"
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
#     armorSet.save("armorSet.png", format="PNG", quality=100, method=6, lossless=True)

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