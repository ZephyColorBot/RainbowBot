from enum import Enum

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

    AquamarineDye = ("Aquamarine", "7FFFD4")
    Aquamarine = AquamarineDye
    ArchfiendDye = ("Archfiend", "B80036")
    Archfiend = ArchfiendDye
    BingoBlueDye = ("BingoBlue", "002FA7")
    BingoBlue = BingoBlueDye
    BoneDye = ("Bone", "E3DAC9")
    Bone = BoneDye
    BrickRedDye = ("BrickRed", "CB4154")
    BrickRed = BrickRedDye
    ByzantiumDye = ("Byzantium", "702963")
    Byzantium = ByzantiumDye
    CarmineDye = ("Carmine", "960018")
    Carmine = CarmineDye
    CeladonDye = ("Celadon", "ACE1AF")
    Celadon = CeladonDye
    CelesteDye = ("Celeste", "B2FFFF")
    Celeste = CelesteDye
    ChocolateDye = ("Chocolate", "7B3F00")
    Chocolate = ChocolateDye
    CopperDye = ("Copper", "B87333")
    Copper = CopperDye
    CyclamenDye = ("Cyclamen", "F56FA1")
    Cyclamen = CyclamenDye
    DarkPurpleDye = ("DarkPurple", "301934")
    DarkPurple = DarkPurpleDye
    DungDye = ("Dung", "4F2A2A")
    Dung = DungDye
    EmeraldDye = ("Emerald", "50C878")
    Emerald = EmeraldDye
    FlameDye = ("Flame", "E25822")
    Flame = FlameDye
    FossilDye = ("Fossil", "866F12")
    Fossil = FossilDye
    FrostbittenDye = ("Frostbitten", "09D8EB")
    Frostbitten = FrostbittenDye
    HollyDye = ("Holly", "3C6746")
    Holly = HollyDye
    IcebergDye = ("Iceberg", "71A6D2")
    Iceberg = IcebergDye
    JadeDye = ("Jade", "00A86B")
    Jade = JadeDye
    LividDye = ("Livid", "CEB7AA")
    Livid = LividDye
    MangoDye = ("Mango", "FDBE02")
    Mango = MangoDye
    MatchaDye = ("Matcha", "74A12E")
    Matcha = MatchaDye
    MidnightDye = ("Midnight", "50216C")
    Midnight = MidnightDye
    MochaDye = ("Mocha", "967969")
    Mocha = MochaDye
    NadeshikoDye = ("Nadeshiko", "F6ADC6")
    Nadeshiko = NadeshikoDye
    NecronDye = ("Necron", "E7413C")
    Necron = NecronDye
    NyanzaDye = ("Nyanza", "E9FFDB")
    Nyanza = NyanzaDye
    PearlescentDye = ("Pearlescent", "115555")
    Pearlescent = PearlescentDye
    PeltDye = ("Pelt", "50414C")
    Pelt = PeltDye
    PeriwinkleDye = ("Periwinkle", "CCCCFF")
    Periwinkle = PeriwinkleDye
    SangriaDye = ("Sangria", "D40808")
    Sangria = SangriaDye
    SecretDye = ("Secret", "7D7D7D")
    Secret = SecretDye
    WildStrawberryDye = ("WildStrawberry", "FF43A4")
    WildStrawberry = WildStrawberryDye
    TentacleDye = ("Tentacle", "324D6C")
    Tentacle = TentacleDye

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
    CloverHelmet = "Clover Helmet"
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
    RacingHelmet = "Racing Helmet"
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
    WardenHelmet = "Warden Helmet"

    def __str__(self):
        return self.value

stringToColorTypeDict = {}
stringToArmorTypeDict = {}
stringToItemTypeDict = {}
stringToVersionTypeDict = {}
stringToDisplayTypeDict = {}

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

baseArmorSet = ["LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"]
itemDict = {
    ArmorType.FullSet: (["LeatherHelmet.png", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], [ColorType.Leather.value[1], ColorType.Leather.value[1], ColorType.Leather.value[1], ColorType.Leather.value[1]]),
    ArmorType.Helmet: (["LeatherHelmet.png"], [ColorType.Leather.value[1]]),
    ArmorType.Chestplate: (["LeatherChestplate.png"], [ColorType.Leather.value[1]]),
    ArmorType.Leggings: (["LeatherLeggings.png"], [ColorType.Leather.value[1]]),
    ArmorType.Boots: (["LeatherBoots.png"], [ColorType.Leather.value[1]]),
    ArmorType.Holy: (["HolyHelmet.webp", *baseArmorSet], ["", *([ColorType.Holy.value[1]] * 3)]),
    ArmorType.HolyBaby: (["HolyHelmetBaby.webp", *baseArmorSet], ["", *([ColorType.Holy.value[1]] * 3)]),
    ArmorType.HolyShimmer: (["a_HolyHelmetShimmer.webp", *baseArmorSet], ["", *([ColorType.Holy.value[1]] * 3)]),
    ArmorType.Old: (["OldHelmet.webp", *baseArmorSet], ["", *([ColorType.Old.value[1]] * 3)]),
    ArmorType.OldBaby: (["OldHelmetBaby.webp", *baseArmorSet], ["", *([ColorType.Old.value[1]] * 3)]),
    ArmorType.OldShimmer: (["a_OldHelmetShimmer.webp", *baseArmorSet], ["", *([ColorType.Old.value[1]] * 3)]),
    ArmorType.Protector: (["ProtectorHelmet.webp", *baseArmorSet], ["", *([ColorType.Protector.value[1]] * 3)]),
    ArmorType.ProtectorBaby: (["ProtectorHelmetBaby.webp", *baseArmorSet], ["", *([ColorType.Protector.value[1]] * 3)]),
    ArmorType.ProtectorShimmer: (["a_ProtectorHelmetShimmer.webp", *baseArmorSet], ["", *([ColorType.Protector.value[1]] * 3)]),
    ArmorType.Strong: (["StrongHelmet.webp", *baseArmorSet], ["", ColorType.StrongChestplate.value[1], ColorType.StrongLeggings.value[1], ColorType.StrongBoots.value[1]]),
    ArmorType.StrongBaby: (["StrongHelmetBaby.webp", *baseArmorSet], ["", ColorType.StrongChestplate.value[1], ColorType.StrongLeggings.value[1], ColorType.StrongBoots.value[1]]),
    ArmorType.StrongShimmer: (["a_StrongHelmetShimmer.webp", *baseArmorSet], ["", ColorType.StrongChestplate.value[1], ColorType.StrongLeggings.value[1], ColorType.StrongBoots.value[1]]),
    ArmorType.Superior: (["SuperiorHelmet.webp", *baseArmorSet], ["", ColorType.Superior.value[1], ColorType.Superior.value[1], ColorType.SuperiorBoots.value[1]]),
    ArmorType.SuperiorBaby: (["SuperiorHelmetBaby.webp", *baseArmorSet], ["", ColorType.Superior.value[1], ColorType.Superior.value[1], ColorType.SuperiorBoots.value[1]]),
    ArmorType.SuperiorShimmer: (["a_SuperiorHelmetShimmer.webp", *baseArmorSet], ["", ColorType.Superior.value[1], ColorType.Superior.value[1], ColorType.SuperiorBoots.value[1]]),
    ArmorType.Unstable: (["UnstableHelmet.webp", *baseArmorSet], ["", *([ColorType.Unstable.value[1]] * 3)]),
    ArmorType.UnstableBaby: (["UnstableHelmetBaby.webp", *baseArmorSet], ["", *([ColorType.Unstable.value[1]] * 3)]),
    ArmorType.UnstableShimmer: (["a_UnstableHelmetShimmer.webp", *baseArmorSet], ["", *([ColorType.Unstable.value[1]] * 3)]),
    ArmorType.Wise: (["WiseHelmet.webp", *baseArmorSet], ["", *([ColorType.Wise.value[1]] * 3)]),
    ArmorType.WiseBaby: (["WiseHelmetBaby.webp", *baseArmorSet], ["", *([ColorType.Wise.value[1]] * 3)]),
    ArmorType.WiseShimmer: (["a_WiseHelmetShimmer.webp", *baseArmorSet], ["", *([ColorType.Wise.value[1]] * 3)]),
    ArmorType.Young: (["YoungHelmet.webp", *baseArmorSet], ["", *([ColorType.Young.value[1]] * 3)]),
    ArmorType.YoungBaby: (["YoungHelmetBaby.webp", *baseArmorSet], ["", *([ColorType.Young.value[1]] * 3)]),
    ArmorType.YoungShimmer: (["a_YoungHelmetShimmer.webp", *baseArmorSet], ["", *([ColorType.Young.value[1]] * 3)]),
    ArmorType.Angler: (["AnglerHelmet.webp", *baseArmorSet], ["", *([ColorType.Angler.value[1]] * 3)]),
    ArmorType.ArmorOfThePack: (["LeatherHelmet.png", "LeatherChestplate.png", "IronLeggings.webp", "IronBoots.webp"], [ColorType.ArmorOfThePackHelmet.value[1], ColorType.ArmorOfThePackChestplate.value[1], "", ""]),
    ArmorType.Bat: (["BatHelmet.webp", *baseArmorSet], ["", *([ColorType.Bat.value[1]] * 3)]),
    ArmorType.Biohazard: (["BiohazardHelmet.webp", *baseArmorSet], ["", *([ColorType.Biohazard.value[1]] * 3)]),
    ArmorType.Blaze: (["BlazeHelmet.webp", *baseArmorSet], ["", *([ColorType.Blaze.value[1]] * 3)]),
    ArmorType.FrozenBlaze: (["FrozenBlazeHelmet.webp", *baseArmorSet], ["", *([ColorType.FrozenBlaze.value[1]] * 3)]),
    ArmorType.FrozenBlazeIcicle: (["FrozenBlazeHelmetIcicle.webp", *baseArmorSet], ["", *([ColorType.FrozenBlaze.value[1]] * 3)]),
    ArmorType.CloverHelmet: (["CloverHelmet.webp", *baseArmorSet], ["", *([ColorType.HollyDye.value[1]] * 3)]),
    ArmorType.Glacite: (["GlaciteHelmet.webp", *baseArmorSet], ["", *([ColorType.Glacite.value[1]] * 3)]),
    ArmorType.Goblin: (["GoblinHelmet.webp", *baseArmorSet], ["", *([ColorType.Goblin.value[1]] * 3)]),
    ArmorType.GoblinBaby: (["GoblinHelmetBaby.webp", *baseArmorSet], ["", *([ColorType.Goblin.value[1]] * 3)]),
    ArmorType.Goldor: (["GoldorHelmet.webp", *baseArmorSet], ["", ColorType.GoldorChestplate.value[1], ColorType.GoldorLeggings.value[1], ColorType.GoldorBoots.value[1]]),
    ArmorType.GoldorCelesital: (["a_GoldorHelmetCelestial.webp", *baseArmorSet], ["", ColorType.GoldorChestplate.value[1], ColorType.GoldorLeggings.value[1], ColorType.GoldorBoots.value[1]]),
    ArmorType.Lapis: (["LapisHelmet.webp", *baseArmorSet], ["", *([ColorType.Lapis.value[1]] * 3)]),
    ArmorType.Leaflet: (["OakLeaves.webp", *baseArmorSet], ["", *([ColorType.Leaflet.value[1]] * 3)]),
    ArmorType.Maxor: (["MaxorHelmet.webp", *baseArmorSet], ["", ColorType.MaxorChestplate.value[1], ColorType.MaxorLeggings.value[1], ColorType.MaxorBoots.value[1]]),
    ArmorType.MaxorCelesital: (["a_MaxorHelmetCelestial.webp", *baseArmorSet], ["", ColorType.MaxorChestplate.value[1], ColorType.MaxorLeggings.value[1], ColorType.MaxorBoots.value[1]]),
    ArmorType.NecromancerLord: (["NecromancerLordHelmet.webp", *baseArmorSet], ["", ColorType.NecromancerLordChestplate.value[1], ColorType.NecromancerLordLeggings.value[1], ColorType.NecromancerLordBoots.value[1]]),
    ArmorType.Necron: (["NecronHelmet.webp", *baseArmorSet], ["", ColorType.NecronChestplate.value[1], ColorType.NecronLeggings.value[1], ColorType.NecronBoots.value[1]]),
    ArmorType.NecronCelesital: (["a_NecronHelmetCelestial.webp", *baseArmorSet], ["", ColorType.NecronChestplate.value[1], ColorType.NecronLeggings.value[1], ColorType.NecronBoots.value[1]]),
    ArmorType.RacingHelmet: (["RacingHelmet.webp", *baseArmorSet], ["", *([ColorType.Carmine.value[1]] * 3)]),
    ArmorType.RisingSun: (["RisingSunHelmet.webp", "GoldenChestplate.webp", "LeatherLeggings.png", "LeatherBoots.png"], ["", "", ColorType.RisingSunLeggings.value[1], ColorType.RisingSunBoots.value[1]]),
    ArmorType.ShadowAssassin: (["ShadowAssassinHelmet.webp", *baseArmorSet], ["", *([ColorType.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinAdmiral: (["ShadowAssassinHelmetAdmiral.webp", *baseArmorSet], ["", *([ColorType.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinCrimson: (["ShadowAssassinHelmetCrimson.webp", *baseArmorSet], ["", *([ColorType.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinMuave: (["ShadowAssassinHelmetMauve.webp", *baseArmorSet], ["", *([ColorType.ShadowAssassin.value[1]] * 3)]),
    ArmorType.Shark: (["SharkHelmet.webp", *baseArmorSet], ["", *([ColorType.Shark.value[1]] * 3)]),
    ArmorType.SnowSuit: (["SnowSuitHelmet.webp", *baseArmorSet], ["", *([ColorType.SnowSuit.value[1]] * 3)]),
    ArmorType.SnowSuitSnowglobe: (["a_SnowSuitHelmetSnowglobe.webp", *baseArmorSet], ["", *([ColorType.SnowSuit.value[1]] * 3)]),
    ArmorType.SpaceHelmet: (["a_OldSpaceHelmet.webp", *baseArmorSet], ["", *([ColorType.BrickRed.value[1]] * 3)]),
    ArmorType.Sponge: (["SpongeHelmet.webp", *baseArmorSet], ["", *([ColorType.Sponge.value[1]] * 3)]),
    ArmorType.Spooky: (["SpookyHelmet.webp", *baseArmorSet], ["", *([ColorType.Spooky.value[1]] * 3)]),
    ArmorType.Storm: (["StormHelmet.webp", *baseArmorSet], ["", ColorType.StormChestplate.value[1], ColorType.StormLeggings.value[1], ColorType.StormBoots.value[1]]),
    ArmorType.StormCelesital: (["a_StormHelmetCelestial.webp", *baseArmorSet], ["", ColorType.StormChestplate.value[1], ColorType.StormLeggings.value[1], ColorType.StormBoots.value[1]]),
    ArmorType.Tarantula: (["LeatherHelmet.png", "ChainmailChestplate.webp", "LeatherLeggings.png", "ChainmailBoots.webp"], [ColorType.Tarantula.value[1], "", ColorType.Tarantula.value[1], ""]),
    ArmorType.Tuxedo: ([*baseArmorSet], [ColorType.CheapTuxedoChestplate.value[1], ColorType.CheapTuxedoLeggings.value[1], ColorType.CheapTuxedoBoots.value[1]]),
    ArmorType.WardenHelmet: (["WardenHelmet.webp", *baseArmorSet], ["", *([ColorType.White.value[1]] * 3)]),
    ArmorType.Werewolf: (["WerewolfHelmet.webp", *baseArmorSet], ["", *([ColorType.Werewolf.value[1]] * 3)]),
}