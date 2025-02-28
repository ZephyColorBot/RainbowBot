from enum import Enum

class ColorType(Enum):
    Exotic = "Exotic"
    PureDye = "Pure"
    TrueDye = "True"
    Fairy = "Fairy"
    OGFairy = "OG Fairy"
    Crystal = "Crystal"
    Armor = "Armor"
    HypixelDye = "Dye"
    Bleached = "Bleached"
    _None = "None"

    def __str__(self):
        return self.value

class Color(Enum):
    PureRed = ("Red", "993333", ColorType.PureDye)
    Red = PureRed
    PureOrange = ("Orange", "D87F33", ColorType.PureDye)
    Orange = PureOrange
    PureYellow = ("Yellow", "E5E533", ColorType.PureDye)
    Yellow = PureYellow
    PureLime = ("Lime", "7FCC19", ColorType.PureDye)
    Lime = PureLime
    PureDarkGreen = ("Dark Green", "667F33", ColorType.PureDye)
    DarkGreen = PureDarkGreen
    PureGreen = PureDarkGreen
    Green = PureDarkGreen
    PureDG = PureDarkGreen
    DG = PureDarkGreen
    PureLightBlue = ("Light Blue", "6699D8", ColorType.PureDye)
    LightBlue = PureLightBlue
    PureLB = PureLightBlue
    LB = PureLightBlue
    PureCyan = ("Cyan", "4C7F99", ColorType.PureDye)
    Cyan = PureCyan
    PureDarkBlue = ("Dark Blue", "334CB2", ColorType.PureDye)
    DarkBlue = PureDarkBlue
    PureBlue = PureDarkBlue
    Blue = PureDarkBlue
    PureDB = PureDarkBlue
    DB = PureDarkBlue
    PurePink = ("Pink", "F27FA5", ColorType.PureDye)
    Pink = PurePink
    PureMagenta = ("Magenta", "B24CD8", ColorType.PureDye)
    Magenta = PureMagenta
    PurePurple = ("Purple", "7F3FB2", ColorType.PureDye)
    Purple = PurePurple
    PureBrown = ("Brown", "664C33", ColorType.PureDye)
    Brown = PureBrown
    PureLightGrey = ("Light Gray", "999999", ColorType.PureDye)
    LightGrey = PureLightGrey
    PureLightGray = PureLightGrey
    LightGray = PureLightGrey
    PureGray = PureLightGrey
    Gray = PureLightGrey
    PureGrey = PureLightGrey
    Grey = PureLightGrey
    LG = PureLightGrey
    PureDarkGrey = ("Dark Gray", "4C4C4C", ColorType.PureDye)
    DarkGrey = PureDarkGrey
    PureDarkGray = PureDarkGrey
    DarkGray = PureDarkGrey
    PureWhite = ("White", "FFFFFF", ColorType.PureDye)
    White = PureWhite
    PureBlack = ("Black", "191919", ColorType.PureDye)
    Black = PureBlack

    TrueBlack = ("TrueBlack", "000000", ColorType.TrueDye)
    TrueRed = ("TrueRed", "FF0000", ColorType.TrueDye)
    TrueOrange = ("TrueOrange", "FF7F00", ColorType.TrueDye)
    TrueYellow = ("TrueYellow", "FFFF00", ColorType.TrueDye)
    TrueGreen = ("TrueGreen", "00FF00", ColorType.TrueDye)
    TrueBlue = ("TrueBlue", "0000FF", ColorType.TrueDye)
    TruePurple = ("TruePurple", "7F00FF", ColorType.TrueDye)
    TruePink = ("TruePink", "FF00FF", ColorType.TrueDye)

    TrueLeather = ("Leather", "A06540", ColorType.Bleached)
    Leather = TrueLeather
    TrueMint = ("Mint", "86D28D", ColorType.TrueDye)
    Mint = TrueMint
    TrueMaroon = ("Maroon", "592626", ColorType.TrueDye)
    Maroon = TrueMaroon
    TrueNavy = ("Navy", "263265", ColorType.TrueDye)
    Navy = TrueNavy
    TrueIce = ("Ice", "B2CCEB", ColorType.TrueDye)
    Ice = TrueIce
    TrueGold = ("Gold", "DEB233", ColorType.TrueDye)
    Gold = TrueGold

    Holy = ("Holy", "47D147", ColorType.Armor)
    Old = ("Old", "F0E6AA", ColorType.Armor)
    Protector = ("Protector", "99978B", ColorType.Armor)
    Prot = Protector
    StrongChestplate = ("Strong Chestplate", "D91E41", ColorType.Armor)
    StrongCP = StrongChestplate
    StrongChest = StrongChestplate
    StrongLeggings = ("Strong Leggings", "E09419", ColorType.Armor)
    StrongLegs = StrongLeggings
    StrongBoots = ("Strong Boots", "F0D124", ColorType.Armor)
    Superior = ("Superior", "F2DF11", ColorType.Armor)
    Sup = Superior
    SuperiorBoots = ("Superior Boots", "F25D18", ColorType.Armor)
    SupBoots = SuperiorBoots
    Unstable = ("Unstable", "B212E3", ColorType.Armor)
    Unst = Unstable
    Wise = ("Wise", "29F0E9", ColorType.Armor)
    Young = ("Young", "DDE4F0", ColorType.Armor)
    Angler = ("Angler", "0B004F", ColorType.Armor)
    PackHelmet = ("Pack Helmet", "FFFFFF", ColorType.Armor)
    PackHelm = PackHelmet
    PackChestplate = ("Pack Chestplate", "FF0000", ColorType.Armor)
    PackCP = PackChestplate
    PackChest = PackChestplate
    Bat = ("Bat", "000000", ColorType.Armor)
    Biohazard = ("Biohazard", "FFAC00", ColorType.Armor)
    Blaze = ("Blaze", "F7DA33", ColorType.Armor)
    FrozenBlaze = ("Frozen Blaze", "A0DAEF", ColorType.Armor)
    FB = FrozenBlaze
    Goblin = ("Goblin", "37B042", ColorType.Armor)
    Glacite = ("Glacite", "03FCF8", ColorType.Armor)
    GoldorChestplate = ("Goldor Chestplate", "45413C", ColorType.Armor)
    GoldorCP = GoldorChestplate
    GoldorChest = GoldorChestplate
    GoldorLeggings = ("Goldor Leggings", "65605A", ColorType.Armor)
    GoldorLegs = GoldorLeggings
    GoldorBoots = ("Goldor Boots", "88837E", ColorType.Armor)
    Lapis = ("Lapis", "0000FF", ColorType.Armor)
    Leaflet = ("Leaflet", "4DCC4D", ColorType.Armor)
    MaxorChestplate = ("Maxor Chestplate", "4A14B7", ColorType.Armor)
    MaxorCP = MaxorChestplate
    MaxorChest = MaxorChestplate
    MaxorLeggings = ("Maxor Leggings", "5D2FB9", ColorType.Armor)
    MaxorLegs = MaxorLeggings
    MaxorBoots = ("Maxor Boots", "8969C8", ColorType.Armor)
    NecromancerLordChestplate = ("Necromancer Lord Chestplate", "000000", ColorType.Armor)
    NecromancerLordCP = NecromancerLordChestplate
    NecromancerLordChest = NecromancerLordChestplate
    NecroLordChestplate = NecromancerLordChestplate
    NecroLordCP = NecromancerLordChestplate
    NecroLordChest = NecromancerLordChestplate
    NecromancerChestplate = NecromancerLordChestplate
    NecromancerCP = NecromancerLordChestplate
    NecromancerChest = NecromancerLordChestplate
    NecroChestplate = NecromancerLordChestplate
    NecroCP = NecromancerLordChestplate
    NecroChest = NecromancerLordChestplate
    NecromancerLordLeggings = ("Necromancer Lord Leggings", "370147", ColorType.Armor)
    NecromancerLordLegs = NecromancerLordLeggings
    NecroLordLeggings = NecromancerLordLeggings
    NecromancerLeggings = NecromancerLordLeggings
    NecroLeggings = NecromancerLordLeggings
    NecroLegs = NecromancerLordLeggings
    NecromancerLordBoots = ("Necromancer Lord Boots", "400352", ColorType.Armor)
    NecromancerBoots = NecromancerLordBoots
    NecroLordBoots = NecromancerLordBoots
    NecroBoots = NecromancerLordBoots
    NecronChestplate = ("Necron Chestplate", "E7413C", ColorType.Armor)
    NecronCP = NecronChestplate
    NecronChest = NecronChestplate
    NecronLeggings = ("Necron Leggings", "E75C3C", ColorType.Armor)
    NecronLegs = NecronLeggings
    NecronBoots = ("Necron Boots", "E76E3C", ColorType.Armor)
    RisingSunLeggings = ("Rising Sun Leggings", "DEBC15", ColorType.Armor)
    RisingSunLegs = RisingSunLeggings
    RisingSunBoots = ("Rising Sun Boots", "9F8609", ColorType.Armor)
    ShadowAssassin = ("Shadow Assassin", "000000", ColorType.Armor)
    SA = ShadowAssassin
    Shark = ("Shark", "002CA6", ColorType.Armor)
    SnowSuit = ("Snow Suit", "FFFFFF", ColorType.Armor)
    Snow = SnowSuit
    Sponge = ("Sponge", "FFDC51", ColorType.Armor)
    Spooky = ("Spooky", "606060", ColorType.Armor)
    StormChestplate = ("Storm Chestplate", "1793C4", ColorType.Armor)
    StormCP = StormChestplate
    StormChest = StormChestplate
    StormLeggings = ("Storm Leggings", "17A8C4", ColorType.Armor)
    StormLegs = StormLeggings
    StormBoots = ("Storm Boots", "1CD4E4", ColorType.Armor)
    Tarantula = ("Tarantula", "000000", ColorType.Armor)
    Tara = Tarantula
    CheapTuxedoChestplate = ("Cheap Tuxedo Chestplate", "383838", ColorType.Armor)
    CheapTuxChestplate = CheapTuxedoChestplate
    CheapTuxCP = CheapTuxedoChestplate
    CheapTuxChest = CheapTuxedoChestplate
    CheapTuxedoCP = CheapTuxedoChestplate
    CheapTuxedoChest = CheapTuxedoChestplate
    CheapTuxedoLeggings = ("Cheap Tuxedo Leggings", "C7C7C7", ColorType.Armor)
    CheapTuxLeggings = CheapTuxedoLeggings
    CheapTuxedoLegs = CheapTuxedoLeggings
    CheapTuxLegs = CheapTuxedoLeggings
    CheapTuxedoBoots = ("Cheap Tuxedo Boots", "383838", ColorType.Armor)
    CheapTuxBoots = CheapTuxedoBoots
    FancyTuxedoChestplate = ("Fancy Tuxedo Chestplate", "332A2A", ColorType.Armor)
    FancyTuxChestplate = FancyTuxedoChestplate
    FancyTuxCP = FancyTuxedoChestplate
    FancyTuxChest = FancyTuxedoChestplate
    FancyTuxedoCP = FancyTuxedoChestplate
    FancyTuxedoChest = FancyTuxedoChestplate
    FancyTuxedoLeggings = ("Fancy Tuxedo Leggings", "d4d4d4", ColorType.Armor)
    FancyTuxLeggings = FancyTuxedoLeggings
    FancyTuxedoLegs = FancyTuxedoLeggings
    FancyTuxLegs = FancyTuxedoLeggings
    FancyTuxedoBoots = ("Fancy Tuxedo Boots", "332A2A", ColorType.Armor)
    FancyTuxBoots = FancyTuxedoBoots
    ElegantTuxedoChestplate = ("Elegant Tuxedo Chestplate", "191919", ColorType.Armor)
    ElegantTuxChestplate = ElegantTuxedoChestplate
    ElegantTuxCP = ElegantTuxedoChestplate
    ElegantTuxChest = ElegantTuxedoChestplate
    ElegantTuxedoCP = ElegantTuxedoChestplate
    ElegantTuxedoChest = ElegantTuxedoChestplate
    ElegantTuxedoLeggings = ("Elegant Tuxedo Leggings", "FEFDFC", ColorType.Armor)
    ElegantTuxLeggings = ElegantTuxedoLeggings
    ElegantTuxedoLegs = ElegantTuxedoLeggings
    ElegantTuxLegs = ElegantTuxedoLeggings
    ElegantTuxedoBoots = ("Elegant Tuxedo Boots", "191919", ColorType.Armor)
    ElegantTuxBoots = ElegantTuxedoBoots
    Werewolf = ("Werewolf", "1D1105", ColorType.Armor)
    Reaper = ("Reaper", "1B1B1B", ColorType.Armor)

    Mushroom = ("Mushroom", "FF0000", ColorType.Armor)
    Mush = Mushroom
    Pumpkin = ("Pumpkin", "EDAA36", ColorType.Armor)
    FarmSuit = ("Farm Suit", "FFFF00", ColorType.Armor)
    FarmArmor = ("Farm Armor", "FFD700", ColorType.Armor)
    Speedster = ("Speedster", "E0FCF7", ColorType.Armor)
    Cactus = ("Cactus", "00FF00", ColorType.Armor)
    Miner = ("Miner", "7A7964", ColorType.Armor)
    Prospecting = Miner
    Growth = ("Growth", "00BE00", ColorType.Armor)
    GuardianChestplate = ("Guardian Chestplate", "117391", ColorType.Armor)
    Guardian = GuardianChestplate
    CreeperPants = ("Creeper Pants", "7AE82C", ColorType.Armor)
    Creeper = CreeperPants
    ArmorOfMagma = ("Armor of Magma", "FF9300", ColorType.Armor)
    Magma = ArmorOfMagma
    Emerald = ("Emerald", "00FF00", ColorType.Armor)
    Mineral = ("Mineral", " CCE5FF", ColorType.Armor)

    FF3399 = ("FF3399", "FF3399", ColorType.Fairy)
    F39 = FF3399
    FF007F = ("FF007F", "FF007F", ColorType.Fairy)
    _660033 = ("660033", "660033", ColorType.Fairy)
    _603 = _660033
    _99004C = ("99004C", "99004C", ColorType.Fairy)
    CC0066 = ("CC0066", "CC0066", ColorType.Fairy)
    C06 = CC0066
    FF66B2 = ("FF66B2", "FF66B2", ColorType.Fairy)
    FF99CC = ("FF99CC", "FF99CC", ColorType.Fairy)
    F9C = FF99CC
    FFCCE5 = ("FFCCE5", "FFCCE5", ColorType.Fairy)
    _660066 = ("660066", "660066", ColorType.Fairy)
    _606 = _660066
    _990099 = ("990099", "990099", ColorType.Fairy)
    _909 = _990099
    CC00CC = ("CC00CC", "CC00CC", ColorType.Fairy)
    C0C = CC00CC
    FF00FF = ("FF00FF", "FF00FF", ColorType.Fairy)
    F0F = FF00FF
    FF33FF = ("FF33FF", "FF33FF", ColorType.Fairy)
    F3F = FF33FF
    FF66FF = ("FF66FF", "FF66FF", ColorType.Fairy)
    F6F = FF66FF
    FF99FF = ("FF99FF", "FF99FF", ColorType.Fairy)
    F9F = FF99FF
    FFCCFF = ("FFCCFF", "FFCCFF", ColorType.Fairy)
    E5CCFF = ("E5CCFF", "E5CCFF", ColorType.Fairy)
    ECF = E5CCFF
    CC99FF = ("CC99FF", "CC99FF", ColorType.Fairy)
    C9F = CC99FF
    B266FF = ("B266FF", "B266FF", ColorType.Fairy)
    B6F = B266FF
    _9933FF = ("9933FF", "9933FF", ColorType.Fairy)
    _93F = _9933FF
    _7F00FF = ("7F00FF", "7F00FF", ColorType.Fairy)
    _6600CC = ("6600CC", "6600CC", ColorType.Fairy)
    _60C = _6600CC
    _4C0099 = ("4C0099", "4C0099", ColorType.Fairy)
    _330066 = ("330066", "330066", ColorType.Fairy)
    _306 = _330066

    FCF3FF = ("FCF3FF", "FCF3FF", ColorType.Crystal)
    FCF = FCF3FF
    EFE1F5 = ("EFE1F5", "EFE1F5", ColorType.Crystal)
    EFE = EFE1F5
    E5D1ED = ("E5D1ED", "E5D1ED", ColorType.Crystal)
    E5D = E5D1ED
    D9C1E3 = ("D9C1E3", "D9C1E3", ColorType.Crystal)
    D9C = D9C1E3
    C6A3D4 = ("C6A3D4", "C6A3D4", ColorType.Crystal)
    C6A = C6A3D4
    B88BC9 = ("B88BC9", "B88BC9", ColorType.Crystal)
    B88B = B88BC9
    BOOB = B88BC9
    BOOBS = B88BC9
    A875BD = ("A875BD", "A875BD", ColorType.Crystal)
    A87 = A875BD
    _9C64B3 = ("9C64B3", "9C64B3", ColorType.Crystal)
    _9C6 = _9C64B3
    _8E51A6 = ("8E51A6", "8E51A6", ColorType.Crystal)
    _8E5 = _8E51A6
    _7E4196 = ("7E4196", "7E4196", ColorType.Crystal)
    _7E4 = _7E4196
    _6A2C82 = ("6A2C82", "6A2C82", ColorType.Crystal)
    _6A2 = _6A2C82
    _63237D = ("63237D", "63237D", ColorType.Crystal)
    _632 = _63237D
    _5D1C78 = ("5D1C78", "5D1C78", ColorType.Crystal)
    _5D1 = _5D1C78
    _46085E = ("46085E", "46085E", ColorType.Crystal)
    _460 = _46085E
    _1F0030 = ("1F0030", "1F0030", ColorType.Crystal)
    _1F0 = _1F0030

    Bleach = TrueLeather
    Bleached = TrueLeather

    AquamarineDye = ("Aquamarine", "7FFFD4", ColorType.HypixelDye)
    Aquamarine = AquamarineDye
    ArchfiendDye = ("Archfiend", "B80036", ColorType.HypixelDye)
    Archfiend = ArchfiendDye
    BingoBlueDye = ("BingoBlue", "002FA7", ColorType.HypixelDye)
    BingoBlue = BingoBlueDye
    BoneDye = ("Bone", "E3DAC9", ColorType.HypixelDye)
    Bone = BoneDye
    BrickRedDye = ("BrickRed", "CB4154", ColorType.HypixelDye)
    BrickRed = BrickRedDye
    ByzantiumDye = ("Byzantium", "702963", ColorType.HypixelDye)
    Byzantium = ByzantiumDye
    CarmineDye = ("Carmine", "960018", ColorType.HypixelDye)
    Carmine = CarmineDye
    CeladonDye = ("Celadon", "ACE1AF", ColorType.HypixelDye)
    Celadon = CeladonDye
    CelesteDye = ("Celeste", "B2FFFF", ColorType.HypixelDye)
    Celeste = CelesteDye
    ChocolateDye = ("Chocolate", "7B3F00", ColorType.HypixelDye)
    Chocolate = ChocolateDye
    CopperDye = ("Copper", "B87333", ColorType.HypixelDye)
    Copper = CopperDye
    CyclamenDye = ("Cyclamen", "F56FA1", ColorType.HypixelDye)
    Cyclamen = CyclamenDye
    DarkPurpleDye = ("DarkPurple", "301934", ColorType.HypixelDye)
    DarkPurple = DarkPurpleDye
    DungDye = ("Dung", "4F2A2A", ColorType.HypixelDye)
    Dung = DungDye
    EmeraldDye = ("Emerald", "50C878", ColorType.HypixelDye)
    # Emerald = EmeraldDye
    FlameDye = ("Flame", "E25822", ColorType.HypixelDye)
    Flame = FlameDye
    FossilDye = ("Fossil", "866F12", ColorType.HypixelDye)
    Fossil = FossilDye
    FrostbittenDye = ("Frostbitten", "09D8EB", ColorType.HypixelDye)
    Frostbitten = FrostbittenDye
    HollyDye = ("Holly", "3C6746", ColorType.HypixelDye)
    Holly = HollyDye
    IcebergDye = ("Iceberg", "71A6D2", ColorType.HypixelDye)
    Iceberg = IcebergDye
    IceburgDye = IcebergDye
    Iceburg = IcebergDye
    JadeDye = ("Jade", "00A86B", ColorType.HypixelDye)
    Jade = JadeDye
    LividDye = ("Livid", "CEB7AA", ColorType.HypixelDye)
    Livid = LividDye
    MangoDye = ("Mango", "FDBE02", ColorType.HypixelDye)
    Mango = MangoDye
    MatchaDye = ("Matcha", "74A12E", ColorType.HypixelDye)
    Matcha = MatchaDye
    MidnightDye = ("Midnight", "50216C", ColorType.HypixelDye)
    Midnight = MidnightDye
    MochaDye = ("Mocha", "967969", ColorType.HypixelDye)
    Mocha = MochaDye
    NadeshikoDye = ("Nadeshiko", "F6ADC6", ColorType.HypixelDye)
    Nadeshiko = NadeshikoDye
    NecronDye = ("Necron", "E7413C", ColorType.HypixelDye)
    Necron = NecronDye
    NyanzaDye = ("Nyanza", "E9FFDB", ColorType.HypixelDye)
    Nyanza = NyanzaDye
    PearlescentDye = ("Pearlescent", "115555", ColorType.HypixelDye)
    Pearlescent = PearlescentDye
    PeltDye = ("Pelt", "50414C", ColorType.HypixelDye)
    Pelt = PeltDye
    PeriwinkleDye = ("Periwinkle", "CCCCFF", ColorType.HypixelDye)
    Periwinkle = PeriwinkleDye
    SangriaDye = ("Sangria", "D40808", ColorType.HypixelDye)
    Sangria = SangriaDye
    SecretDye = ("Secret", "7D7D7D", ColorType.HypixelDye)
    Secret = SecretDye
    WildStrawberryDye = ("WildStrawberry", "FF43A4", ColorType.HypixelDye)
    WildStrawberry = WildStrawberryDye
    TentacleDye = ("Tentacle", "324D6C", ColorType.HypixelDye)
    Tentacle = TentacleDye

    def __str__(self):
        return self.value

allFairyHexes = {
    Color.FFCCE5: (["Boots"], ["Helmet", "Chestplate", "Leggings"]),
    Color.FF99CC: (["Leggings", "Boots"], ["Helmet", "Chestplate"]),
    Color.FF66B2: (["Chestplate", "Leggings", "Boots"], ["Helmet"]),
    Color.FF3399: (["All"], []),
    Color.FF007F: (["All"], []),
    Color.CC0066: (["Helmet", "Chestplate", "Leggings"], ["Boots"]),
    Color._99004C: (["Helmet", "Chestplate"], ["Leggings", "Boots"]),
    Color._660033: (["Helmet"], ["Chestplate", "Leggings", "Boots"]),

    Color.FF99FF: ([], ["All"]),
    Color.FFCCFF: ([], ["All"]),
    Color.E5CCFF: ([], ["All"]),
    Color.CC99FF: ([], ["All"]),
    Color.CC00CC: ([], ["All"]),
    Color.FF00FF: ([], ["All"]),
    Color.FF33FF: ([], ["All"]),
    Color.FF66FF: ([], ["All"]),
    Color.B266FF: ([], ["All"]),
    Color._9933FF: ([], ["All"]),
    Color._7F00FF: ([], ["All"]),
    Color._660066: ([], ["All"]),
    Color._6600CC: ([], ["All"]),
    Color._4C0099: ([], ["All"]),
    Color._330066: ([], ["All"]),
    Color._990099: ([], ["All"])
}
allCrystalHexes = [
    Color.FCF3FF,
    Color.EFE1F5,
    Color.E5D1ED,
    Color.D9C1E3,
    Color.C6A3D4,
    Color.B88BC9,
    Color.A875BD,
    Color._9C64B3,
    Color._8E51A6,
    Color._7E4196,
    Color._6A2C82,
    Color._63237D,
    Color._5D1C78,
    Color._46085E,
    Color._1F0030
]
pureColorToDiscordEmotes = {
    Color.PureRed:       "<:RedDye:1334768678612238357>",
    Color.PureOrange:    "<:OrangeDye:1334768730101780571>",
    Color.PureYellow:    "<:YellowDye:1334768821923352586>",
    Color.PureLime:      "<:LimeDye:1334768853988675636>",
    Color.PureDarkGreen: "<:DarkGreenDye:1334768739895218187>",
    Color.PureLightBlue: "<:LightBlueDye:1334768799215259667>",
    Color.PureCyan:      "<:CyanDye:1334768832471896124>",
    Color.PureDarkBlue:  "<:DarkBlueDye:1334768754734665748>",
    Color.PurePink:      "<:PinkDye:1334768777581170739>",
    Color.PureMagenta:   "<:MagentaDye:1334768786229956729>",
    Color.PurePurple:    "<:PurpleDye:1334768766613192734>",
    Color.PureBrown:     "<:BrownDye:1334768649809956955>",
    Color.PureLightGrey: "<:LightGrayDye:1334768841963733044>",
    Color.PureDarkGrey:  "<:DarkGrayDye:1334768865334399078>",
    Color.PureWhite:     "<:WhiteDye:1334768808656769024>",
    Color.PureBlack:     "<:BlackDye:1334768718890139679>"
}
trueColorToDiscordEmotes = {
    Color.TrueMint: "<:TrueMint:1334727660722585691>",
    Color.TrueMaroon: "<:TrueMaroon:1334728556705611829>",
    Color.TrueNavy: "<:TrueNavy:1334727628292100146>",
    Color.TrueIce: "<:TrueIce:1334727641953206303>",
    Color.TrueGold: "<:TrueGold:1334727618733543484>"
}

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

class ShapeType(Enum):
    Vertical = "Vertical"
    Horizontal = "Horizontal"
    Square = "Square"

    def __str__(self):
        return self.value

class ArmorType(Enum):
    FullSet = "Full Set"
    Full = FullSet
    Helmet = "Helmet"
    Chestplate = "Chestplate"
    Leggings = "Leggings"
    Boots = "Boots"
    Holy = "Holy"
    HolyBaby = "Holy Baby"
    BabyHoly = HolyBaby
    HolyShimmer = "Holy Shimmer"
    ShimmerHoly = HolyShimmer
    Old = "Old"
    OldBaby = "Old Baby"
    BabyOld = OldBaby
    OldShimmer = "Old Shimmer"
    ShimmerOld = OldShimmer
    Protector = "Protector"
    Prot = Protector
    ProtectorBaby = "Protector Baby"
    BabyProtector = ProtectorBaby
    ProtBaby = ProtectorBaby
    BabyProt = ProtectorBaby
    ProtectorShimmer = "Protector Shimmer"
    ShimmerProtector = ProtectorShimmer
    ProtShimmer = ProtectorShimmer
    ShimmerProt = ProtectorShimmer
    Strong = "Strong"
    StrongBaby = "Strong Baby"
    BabyStrong = StrongBaby
    StrongShimmer = "Strong Shimmer"
    ShimmerStrong = StrongShimmer
    Superior = "Superior"
    Sup = Superior
    SuperiorBaby = "Superior Baby"
    BabySup = SuperiorBaby
    SupBaby = SuperiorBaby
    BabySuperior = SuperiorBaby
    SuperiorShimmer = "Superior Shimmer"
    ShimmerSuperior = SuperiorShimmer
    SupShimmer = SuperiorShimmer
    ShimmerSup = SuperiorShimmer
    Unstable = "Unstable"
    Unst = Unstable
    UnstableBaby = "Unstable Baby"
    BabyUnstable = UnstableBaby
    BabyUnst = UnstableBaby
    UnstBaby = UnstableBaby
    UnstableShimmer = "Unstable Shimmer"
    ShimmerUnstable = UnstableShimmer
    UnstShimmer = UnstableShimmer
    ShimmerUnst = UnstableShimmer
    Wise = "Wise"
    WiseBaby = "Wise Baby"
    BabyWise = WiseBaby
    WiseShimmer = "Wise Shimmer"
    ShimmerWise = WiseShimmer
    Young = "Young"
    YoungBaby = "Young Baby"
    BabyYoung = YoungBaby
    YoungShimmer = "Young Shimmer"
    ShimmerYoung = YoungShimmer
    Angler = "Angler"
    Pack = "Pack"
    Bat = "Bat"
    Biohazard = "Biohazard"
    Blaze = "Blaze"
    FrozenBlaze = "Frozen Blaze"
    FrozenBlazeIcicle = "Frozen Blaze Icicle"
    FB = FrozenBlaze
    CloverHelmet = "Clover Helmet"
    Clover = CloverHelmet
    Glacite = "Glacite"
    Goblin = "Goblin"
    GoblinBaby = "Goblin Baby"
    Goldor = "Goldor"
    GoldorCelesital = "Goldor Celesital"
    Lapis = "Lapis"
    Leaflet = "Leaflet"
    Leaf = Leaflet
    Maxor = "Maxor"
    MaxorCelesital = "Maxor Celesital"
    Necron = "Necron"
    NecronCelesital = "Necron Celesital"
    NecromancerLord = "Necromancer Lord"
    NecroLord = NecromancerLord
    Necromancer = NecromancerLord
    RacingHelmet = "Racing Helmet"
    Racing = RacingHelmet
    RisingSun = "Rising Sun"
    ShadowAssassin = "Shadow Assassin"
    ShadowAssassinAdmiral = "Shadow Assassin Admiral"
    ShadowAssassinCrimson = "Shadow Assassin Crimson"
    ShadowAssassinMuave = "Shadow Assassin Muave"
    SA = ShadowAssassin
    SAAdmiral = ShadowAssassinAdmiral
    SACrimson = ShadowAssassinCrimson
    SAMuave = ShadowAssassinMuave
    Shark = "Shark"
    SnowSuit = "Snow Suit"
    SnowSuitSnowglobe = "Snow Suit Snowglobe"
    Snow = SnowSuit
    Snowglobe = SnowSuitSnowglobe
    SpaceHelmet = "Space Helmet"
    Space = SpaceHelmet
    Sponge = "Sponge"
    Spooky = "Spooky"
    Storm = "Storm"
    StormCelesital = "Storm Celesital"
    Tarantula = "Tarantula"
    Tara = Tarantula
    Tuxedo = "Tuxedo"
    Tux = Tuxedo
    _3Piece = Tuxedo
    ThreePiece = Tuxedo
    ThreeP = Tuxedo
    _3P = Tuxedo
    Werewolf = "Werewolf"
    WardenHelmet = "Warden Helmet"
    Warden = WardenHelmet

    ReaperMask = "Reaper Mask"
    ReaperMaskSpirit = "Reaper Mask Spirit"
    Reaper = ReaperMask
    ReaperSpirit = ReaperMaskSpirit
    SpiritReaper = ReaperMaskSpirit
    WitherGoggles = "Wither Goggles"
    WitherGogglesCorrupt = "Corrupt Wither Goggles"
    WitherGogglesCelestial = "Celestial Wither Goggles"
    WitherGogglesCyberpunk = "Cyberpunk Wither Goggles"
    TarantulaBlackWidow = "Tarantula Black Widow"
    TaraBlackWidow = TarantulaBlackWidow
    WardenHelmetTrueWarden = "True Warden"
    TrueWarden = WardenHelmetTrueWarden
    WardenTrueWarden = WardenHelmetTrueWarden
    DiverHelmetPuffer = "Puffer Fish Diver Helmet"
    Puffer = DiverHelmetPuffer
    DiverPuffer = DiverHelmetPuffer
    MastiffHelmetPuppy = "Puppy Mastiff Helmet"
    Puppy = MastiffHelmetPuppy
    MastiffPuppy = MastiffHelmetPuppy
    PerfectHelmetReinforced = "Reinforced Perfect Helmet"
    Reinforced = PerfectHelmetReinforced
    PerfectReinforced = PerfectHelmetReinforced
    Chainmail = "Chainmail"
    Chain = Chainmail
    Iron = "Iron"
    Golden = "Gold"
    Diamond = "Diamond"

    Mushroom = "Mushroom"
    Mush = Mushroom
    Pumpkin = "Pumpkin"
    FarmSuit = "Farm Suit"
    FarmArmor = "Farm Armor"
    Speedster = "Speedster"
    Cactus = "Cactus"
    Miner = "Miner"
    Prospecting = Miner
    Growth = "Growth"
    GuardianChestplate = "Guardian Chestplate"
    GuardianChest = GuardianChestplate
    GuardianCP = GuardianChestplate
    Guardian = GuardianChestplate
    CreeperPants = "Creeper Pants"
    CreeperLegs = CreeperPants
    CreeperLeggings = CreeperPants
    Creeper = CreeperPants
    MonsterHunter = "Monster Hunter"
    MH = MonsterHunter
    MonsterRaider = "Monster Raider"
    ArmorOfMagma = "Magma"
    Magma = ArmorOfMagma
    Emerald = "Emerald"
    GodAngler = "God Angler"
    BuildersClay = "Builder's Clay"
    BuilderClay = BuildersClay
    ObsidianChestplate = "Obsidian Chestplate"
    Obsidian = ObsidianChestplate
    FarmerBoots = "Farmer Boots"
    Farmer = FarmerBoots
    FarmerBoot = FarmerBoots
    FarmersBoots = FarmerBoots
    Farmers = FarmerBoots
    RancherBoots = "Ranchers Boots"
    Rancher = RancherBoots
    RancherBoot = RancherBoots
    RanchersBoots = RancherBoots
    Ranchers = RancherBoots
    StereoPants = "Stereo Pants"
    Stereo = StereoPants
    StereoLeggings = StereoPants
    StereoLegs = StereoPants
    Stereos = StereoPants
    SquidBoots = "Squid Boots"
    Squid = SquidBoots
    SquidBoot = SquidBoots
    SquidsBoots = SquidBoots
    Squids = SquidBoots
    Crystal = "Crystal"
    Fairy = "Fairy"
    ZombieSoldier = "Zombie Soldier"
    Salmon = "Salmon"
    SpiritBoots = "Spirit Boots"
    ThornBoots = SpiritBoots
    ThornsBoots = SpiritBoots
    Mineral = "Mineral"
    CheapTuxedoChestplate = "Cheap Tuxedo Chestplate"
    CheapTuxChestplate = CheapTuxedoChestplate
    CheapTuxCP = CheapTuxedoChestplate
    CheapTuxChest = CheapTuxedoChestplate
    CheapTuxedoCP = CheapTuxedoChestplate
    CheapTuxedoChest = CheapTuxedoChestplate
    CheapTuxedoLeggings = "Cheap Tuxedo Leggings"
    CheapTuxLeggings = CheapTuxedoLeggings
    CheapTuxedoLegs = CheapTuxedoLeggings
    CheapTuxLegs = CheapTuxedoLeggings
    CheapTuxedoBoots = "Cheap Tuxedo Boots"
    CheapTuxBoots = CheapTuxedoBoots
    FancyTuxedoChestplate = "Fancy Tuxedo Chestplate"
    FancyTuxChestplate = FancyTuxedoChestplate
    FancyTuxCP = FancyTuxedoChestplate
    FancyTuxChest = FancyTuxedoChestplate
    FancyTuxedoCP = FancyTuxedoChestplate
    FancyTuxedoChest = FancyTuxedoChestplate
    FancyTuxedoLeggings = "Fancy Tuxedo Leggings"
    FancyTuxLeggings = FancyTuxedoLeggings
    FancyTuxedoLegs = FancyTuxedoLeggings
    FancyTuxLegs = FancyTuxedoLeggings
    FancyTuxedoBoots = "Fancy Tuxedo Boots"
    FancyTuxBoots = FancyTuxedoBoots
    ElegantTuxedoChestplate = "Elegant Tuxedo Chestplate"
    ElegantTuxChestplate = ElegantTuxedoChestplate
    ElegantTuxCP = ElegantTuxedoChestplate
    ElegantTuxChest = ElegantTuxedoChestplate
    ElegantTuxedoCP = ElegantTuxedoChestplate
    ElegantTuxedoChest = ElegantTuxedoChestplate
    ElegantTuxedoLeggings = "Elegant Tuxedo Leggings"
    ElegantTuxLeggings = ElegantTuxedoLeggings
    ElegantTuxedoLegs = ElegantTuxedoLeggings
    ElegantTuxLegs = ElegantTuxedoLeggings
    ElegantTuxedoBoots = "Elegant Tuxedo Boots"
    ElegantTuxBoots = ElegantTuxedoBoots

    Helm = Helmet
    Chest = Chestplate
    Legs = Leggings
    Leg = Leggings
    Boot = Boots

    HelmetChestplate = "Helmet Chestplate"
    HelmetChest = HelmetChestplate
    HelmetCP = HelmetChestplate
    HelmChestplate = HelmetChestplate
    HelmChest = HelmetChestplate
    HelmCP = HelmetChestplate
    HelmetLeggings = "Helmet Leggings"
    HelmetLegs = HelmetLeggings
    HelmetLeg = HelmetLeggings
    HelmLeggings = HelmetLeggings
    HelmLegs = HelmetLeggings
    HelmLeg = HelmetLeggings
    HelmetBoots = "Helmet Boots"
    HelmetBoot = HelmetBoots
    HelmBoots = HelmetBoots
    HelmBoot = HelmetBoots
    ChestplateLeggings = "Chestplate Leggings"
    ChestplateLegs = ChestplateLeggings
    ChestplateLeg = ChestplateLeggings
    ChestLeggings = ChestplateLeggings
    ChestLegs = ChestplateLeggings
    ChestLeg = ChestplateLeggings
    ChestplateBoots = "Chestplate Boots"
    ChestplateBoot = ChestplateBoots
    ChestBoots = ChestplateBoots
    ChestBoot = ChestplateBoots
    HelmetChestplateLeggings = "Helmet Chestplate Leggings"
    HelmetChestplateLegs = HelmetChestplateLeggings
    HelmetChestplateLeg = HelmetChestplateLeggings
    HelmetChestLeggings = HelmetChestplateLeggings
    HelmetChestLegs = HelmetChestplateLeggings
    HelmetChestLeg = HelmetChestplateLeggings
    HelmChestplateLeggings = "Helmet Chestplate Leggings"
    HelmChestplateLegs = HelmChestplateLeggings
    HelmChestplateLeg = HelmChestplateLeggings
    HelmChestLeggings = HelmChestplateLeggings
    HelmChestLegs = HelmChestplateLeggings
    HelmChestLeg = HelmChestplateLeggings
    HelmetChestplateBoots = "Helmet Chestplate Boots"
    HelmetChestplateBoot = HelmetChestplateBoots
    HelmetChestBoots = HelmetChestplateBoots
    HelmetChestBoot = HelmetChestplateBoots
    HelmChestplateBoots = "Helmet Chestplate Boots"
    HelmChestplateBoot = HelmChestplateBoots
    HelmChestBoots = HelmChestplateBoots
    HelmChestBoot = HelmChestplateBoots
    HelmetLeggingsBoots = "Helmet Leggings Boots"
    HelmetLeggingsBoot = HelmetLeggingsBoots
    HelmetLegsBoots = HelmetLeggingsBoots
    HelmetLegsBoot = HelmetLeggingsBoots
    HelmetLegBoots = HelmetLeggingsBoots
    HelmetLegBoot = HelmetLeggingsBoots
    HelmLeggingsBoots = "Helmet Leggings Boots"
    HelmLeggingsBoot = HelmLeggingsBoots
    HelmLegsBoots = HelmLeggingsBoots
    HelmLegsBoot = HelmLeggingsBoots
    HelmLegBoots = HelmLeggingsBoots
    HelmLegBoot = HelmLeggingsBoots
    ChestplateLeggingsBoots = "Chestplate Leggings Boots"
    ChestplateLeggingsBoot = ChestplateLeggingsBoots
    ChestplateLegsBoots = ChestplateLeggingsBoots
    ChestplateLegsBoot = ChestplateLeggingsBoots
    ChestplateLegBoots = ChestplateLeggingsBoots
    ChestplateLegBoot = ChestplateLeggingsBoots
    ChestLeggingsBoots = "Chestplate Leggings Boots"
    ChestLeggingsBoot = ChestLeggingsBoots
    ChestLegsBoots = ChestLeggingsBoots
    ChestLegsBoot = ChestLeggingsBoots
    ChestLegBoots = ChestLeggingsBoots
    ChestLegBoot = ChestLeggingsBoots
    LeggingsBoots = "Leggings Boots"
    LeggingsBoot = LeggingsBoots
    LegsBoots = LeggingsBoots
    LegsBoot = LeggingsBoots
    LegBoots = LeggingsBoots
    LegBoot = LeggingsBoots

    DiamondNecron = "Diamond Necron"
    DiaNecron = DiamondNecron

    def __str__(self):
        return self.value

stringToColorDict = {}
stringToArmorTypeDict = {}
stringToItemTypeDict = {}
stringToVersionTypeDict = {}
stringToShapeTypeDict = {}

def PopulateStringDictionaries():
    for name, color in Color.__members__.items():
        colorName = name.replace(" ", "").replace("_", "").lower().strip()
        colorValue = color.value[1].replace(" ", "").upper().strip()
        stringToColorDict[colorName] = color
        stringToColorDict[colorValue] = color
    # for color in Color.GetOtherNames():
    #     colorName = color[0].replace(" ", "").lower().strip()
    #     stringToColorDict[colorName] = color[1]

    for name, armorType in ArmorType.__members__.items():
        armorName = name.replace(" ", "").replace("_", "").lower().strip()
        armorValue = armorType.value.replace(" ", "").lower().strip()
        stringToArmorTypeDict[armorName] = armorType
        stringToArmorTypeDict[armorValue] = armorType

    for name, itemType in ItemType.__members__.items():
        itemName = itemType.name.replace(" ", "").lower().strip()
        stringToItemTypeDict[itemName] = itemType

    for name, versionType in VersionType.__members__.items():
        versionName = versionType.name.replace(" ", "").lower().strip()
        stringToVersionTypeDict[versionName] = versionType
    for versionType in VersionType.GetOtherNames():
        versionName = versionType[0].replace(" ", "").lower().strip()
        stringToVersionTypeDict[versionName] = versionType[1]

    for name, shapeType in ShapeType.__members__.items():
        shapeName = shapeType.name.replace(" ", "").lower().strip()
        stringToShapeTypeDict[shapeName] = shapeType
PopulateStringDictionaries()

baseArmorSet = ["LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"]
fullArmorSet = ["LeatherHelmet.png", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"]
itemDict = {
    ArmorType.FullSet: (fullArmorSet, [*([Color.Leather.value[1]] * 4)]),
    ArmorType.Helmet:     (["LeatherHelmet.png"   , "EmptyImageChestplate.png", "EmptyImageLeggings.png", "EmptyImageBoots.png"], [Color.Leather.value[1], "", "", ""]),
    ArmorType.Chestplate: (["EmptyImageHelmet.png", "LeatherChestplate.png"   , "EmptyImageLeggings.png", "EmptyImageBoots.png"], ["", Color.Leather.value[1], "", ""]),
    ArmorType.Leggings:   (["EmptyImageHelmet.png", "EmptyImageChestplate.png", "LeatherLeggings.png"   , "EmptyImageBoots.png"], ["", "", Color.Leather.value[1], ""]),
    ArmorType.Boots:      (["EmptyImageHelmet.png", "EmptyImageChestplate.png", "EmptyImageLeggings.png", "LeatherBoots.png"   ], ["", "", "", Color.Leather.value[1]]),

    ArmorType.HelmetChestplate: (["LeatherHelmet.png", "EmptyImageChestplate.png", "LeatherChestplate.png", "EmptyImageBoots.png"], [Color.Leather.value[1], Color.Leather.value[1], "", ""]),
    ArmorType.HelmetLeggings: (["LeatherHelmet.png", "EmptyImageChestplate.png", "LeatherLeggings.png", "EmptyImageBoots.png"], [Color.Leather.value[1], "", Color.Leather.value[1], ""]),
    ArmorType.HelmetBoots: (["LeatherHelmet.png", "EmptyImageChestplate.png", "EmptyImageLeggings.png", "LeatherBoots.png"], [Color.Leather.value[1], "", "", Color.Leather.value[1]]),
    ArmorType.ChestplateLeggings: (["EmptyImageHelmet.png", "LeatherChestplate.png", "LeatherLeggings.png", "EmptyImageBoots.png"], ["", Color.Leather.value[1], Color.Leather.value[1], ""]),
    ArmorType.ChestplateBoots: (["EmptyImageHelmet.png", "LeatherChestplate.png", "EmptyImageLeggings.png", "LeatherBoots.png"], ["", Color.Leather.value[1], "", Color.Leather.value[1]]),
    ArmorType.LeggingsBoots: (["EmptyImageHelmet.png", "EmptyImageChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", "", Color.Leather.value[1], Color.Leather.value[1]]),

    ArmorType.HelmetChestplateLeggings: (["LeatherHelmet.png", "LeatherChestplate.png", "LeatherLeggings.png", "EmptyImageBoots.png"], [Color.Leather.value[1], Color.Leather.value[1], Color.Leather.value[1], ""]),
    ArmorType.HelmetChestplateBoots: (["LeatherHelmet.png", "LeatherChestplate.png",  "EmptyImageLeggings.png", "LeatherBoots.png"], [Color.Leather.value[1], Color.Leather.value[1], "", Color.Leather.value[1]]),
    ArmorType.HelmetLeggingsBoots: (["LeatherHelmet.png", "EmptyImageChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], [Color.Leather.value[1], "", Color.Leather.value[1], Color.Leather.value[1]]),
    ArmorType.ChestplateLeggingsBoots: (["EmptyImageHelmet.png", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", Color.Leather.value[1], Color.Leather.value[1], Color.Leather.value[1]]),

    ArmorType.Holy: (["HolyHelmet.webp", *baseArmorSet], ["", *([Color.Holy.value[1]] * 3)]),
    ArmorType.HolyBaby: (["HolyHelmetBaby.webp", *baseArmorSet], ["", *([Color.Holy.value[1]] * 3)]),
    ArmorType.HolyShimmer: (["HolyHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Holy.value[1]] * 3)]),
    ArmorType.Old: (["OldHelmet.webp", *baseArmorSet], ["", *([Color.Old.value[1]] * 3)]),
    ArmorType.OldBaby: (["OldHelmetBaby.webp", *baseArmorSet], ["", *([Color.Old.value[1]] * 3)]),
    ArmorType.OldShimmer: (["OldHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Old.value[1]] * 3)]),
    ArmorType.Protector: (["ProtectorHelmet.webp", *baseArmorSet], ["", *([Color.Protector.value[1]] * 3)]),
    ArmorType.ProtectorBaby: (["ProtectorHelmetBaby.webp", *baseArmorSet], ["", *([Color.Protector.value[1]] * 3)]),
    ArmorType.ProtectorShimmer: (["ProtectorHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Protector.value[1]] * 3)]),
    ArmorType.Strong: (["StrongHelmet.webp", *baseArmorSet], ["", Color.StrongChestplate.value[1], Color.StrongLeggings.value[1], Color.StrongBoots.value[1]]),
    ArmorType.StrongBaby: (["StrongHelmetBaby.webp", *baseArmorSet], ["", Color.StrongChestplate.value[1], Color.StrongLeggings.value[1], Color.StrongBoots.value[1]]),
    ArmorType.StrongShimmer: (["StrongHelmetShimmer.webp", *baseArmorSet], ["", Color.StrongChestplate.value[1], Color.StrongLeggings.value[1], Color.StrongBoots.value[1]]),
    ArmorType.Superior: (["SuperiorHelmet.webp", *baseArmorSet], ["", Color.Superior.value[1], Color.Superior.value[1], Color.SuperiorBoots.value[1]]),
    ArmorType.SuperiorBaby: (["SuperiorHelmetBaby.webp", *baseArmorSet], ["", Color.Superior.value[1], Color.Superior.value[1], Color.SuperiorBoots.value[1]]),
    ArmorType.SuperiorShimmer: (["SuperiorHelmetShimmer.webp", *baseArmorSet], ["", Color.Superior.value[1], Color.Superior.value[1], Color.SuperiorBoots.value[1]]),
    ArmorType.Unstable: (["UnstableHelmet.webp", *baseArmorSet], ["", *([Color.Unstable.value[1]] * 3)]),
    ArmorType.UnstableBaby: (["UnstableHelmetBaby.webp", *baseArmorSet], ["", *([Color.Unstable.value[1]] * 3)]),
    ArmorType.UnstableShimmer: (["UnstableHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Unstable.value[1]] * 3)]),
    ArmorType.Wise: (["WiseHelmet.webp", *baseArmorSet], ["", *([Color.Wise.value[1]] * 3)]),
    ArmorType.WiseBaby: (["WiseHelmetBaby.webp", *baseArmorSet], ["", *([Color.Wise.value[1]] * 3)]),
    ArmorType.WiseShimmer: (["WiseHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Wise.value[1]] * 3)]),
    ArmorType.Young: (["YoungHelmet.webp", *baseArmorSet], ["", *([Color.Young.value[1]] * 3)]),
    ArmorType.YoungBaby: (["YoungHelmetBaby.webp", *baseArmorSet], ["", *([Color.Young.value[1]] * 3)]),
    ArmorType.YoungShimmer: (["YoungHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Young.value[1]] * 3)]),
    ArmorType.Angler: (["AnglerHelmet.webp", *baseArmorSet], ["", *([Color.Angler.value[1]] * 3)]),
    ArmorType.Pack: (["LeatherHelmet.png", "LeatherChestplate.png", "IronLeggings.webp", "IronBoots.webp"], [Color.PackHelmet.value[1], Color.PackChestplate.value[1], "", ""]),
    ArmorType.Bat: (["BatHelmet.webp", *baseArmorSet], ["", *([Color.Bat.value[1]] * 3)]),
    ArmorType.Biohazard: (["BiohazardHelmet.webp", *baseArmorSet], ["", *([Color.Biohazard.value[1]] * 3)]),
    ArmorType.Blaze: (["BlazeHelmet.webp", *baseArmorSet], ["", *([Color.Blaze.value[1]] * 3)]),
    ArmorType.FrozenBlaze: (["FrozenBlazeHelmet.webp", *baseArmorSet], ["", *([Color.FrozenBlaze.value[1]] * 3)]),
    ArmorType.FrozenBlazeIcicle: (["FrozenBlazeHelmetIcicle.webp", *baseArmorSet], ["", *([Color.FrozenBlaze.value[1]] * 3)]),
    ArmorType.CloverHelmet: (["CloverHelmet.webp", *baseArmorSet], ["", *([Color.HollyDye.value[1]] * 3)]),
    ArmorType.Glacite: (["GlaciteHelmet.webp", *baseArmorSet], ["", *([Color.Glacite.value[1]] * 3)]),
    ArmorType.Goblin: (["GoblinHelmet.webp", *baseArmorSet], ["", *([Color.Goblin.value[1]] * 3)]),
    ArmorType.GoblinBaby: (["GoblinHelmetBaby.webp", *baseArmorSet], ["", *([Color.Goblin.value[1]] * 3)]),
    ArmorType.Goldor: (["GoldorHelmet.webp", *baseArmorSet], ["", Color.GoldorChestplate.value[1], Color.GoldorLeggings.value[1], Color.GoldorBoots.value[1]]),
    ArmorType.GoldorCelesital: (["GoldorHelmetCelestial.webp", *baseArmorSet], ["", Color.GoldorChestplate.value[1], Color.GoldorLeggings.value[1], Color.GoldorBoots.value[1]]),
    ArmorType.Lapis: (["LapisHelmet.webp", *baseArmorSet], ["", *([Color.Lapis.value[1]] * 3)]),
    ArmorType.Leaflet: (["LeafletHelmet.webp", *baseArmorSet], ["", *([Color.Leaflet.value[1]] * 3)]),
    ArmorType.Maxor: (["MaxorHelmet.webp", *baseArmorSet], ["", Color.MaxorChestplate.value[1], Color.MaxorLeggings.value[1], Color.MaxorBoots.value[1]]),
    ArmorType.MaxorCelesital: (["MaxorHelmetCelestial.webp", *baseArmorSet], ["", Color.MaxorChestplate.value[1], Color.MaxorLeggings.value[1], Color.MaxorBoots.value[1]]),
    ArmorType.NecromancerLord: (["NecromancerLordHelmet.webp", *baseArmorSet], ["", Color.NecromancerLordChestplate.value[1], Color.NecromancerLordLeggings.value[1], Color.NecromancerLordBoots.value[1]]),
    ArmorType.Necron: (["NecronHelmet.webp", *baseArmorSet], ["", Color.NecronChestplate.value[1], Color.NecronLeggings.value[1], Color.NecronBoots.value[1]]),
    ArmorType.NecronCelesital: (["NecronHelmetCelestial.webp", *baseArmorSet], ["", Color.NecronChestplate.value[1], Color.NecronLeggings.value[1], Color.NecronBoots.value[1]]),
    ArmorType.RacingHelmet: (["RacingHelmet.webp", *baseArmorSet], ["", *([Color.Carmine.value[1]] * 3)]),
    ArmorType.RisingSun: (["RisingSunHelmet.webp", "GoldChestplate.webp", "LeatherLeggings.png", "LeatherBoots.png"], ["", "", Color.RisingSunLeggings.value[1], Color.RisingSunBoots.value[1]]),
    ArmorType.ShadowAssassin: (["ShadowAssassinHelmet.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinAdmiral: (["ShadowAssassinHelmetAdmiral.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinCrimson: (["ShadowAssassinHelmetCrimson.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinMuave: (["ShadowAssassinHelmetMauve.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.Shark: (["SharkHelmet.webp", *baseArmorSet], ["", *([Color.Shark.value[1]] * 3)]),
    ArmorType.SnowSuit: (["SnowSuitHelmet.webp", *baseArmorSet], ["", *([Color.SnowSuit.value[1]] * 3)]),
    ArmorType.SnowSuitSnowglobe: (["SnowSuitHelmetSnowglobe.webp", *baseArmorSet], ["", *([Color.SnowSuit.value[1]] * 3)]),
    ArmorType.SpaceHelmet: (["a_OldSpaceHelmet.webp", *baseArmorSet], ["", *([Color.BrickRed.value[1]] * 3)]),
    ArmorType.Sponge: (["SpongeHelmet.webp", *baseArmorSet], ["", *([Color.Sponge.value[1]] * 3)]),
    ArmorType.Spooky: (["SpookyHelmet.webp", *baseArmorSet], ["", *([Color.Spooky.value[1]] * 3)]),
    ArmorType.Storm: (["StormHelmet.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.StormCelesital: (["StormHelmetCelestial.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.Tarantula: (["LeatherHelmet.png", "ChainmailChestplate.webp", "LeatherLeggings.png", "IronBoots.webp"], [Color.Tarantula.value[1], "", Color.Tarantula.value[1], ""]),
    ArmorType.Tuxedo: ([*baseArmorSet], [Color.CheapTuxedoChestplate.value[1], Color.CheapTuxedoLeggings.value[1], Color.CheapTuxedoBoots.value[1]]),
    ArmorType.WardenHelmet: (["WardenHelmet.webp", *baseArmorSet], ["", *([Color.White.value[1]] * 3)]),
    ArmorType.Werewolf: (["WerewolfHelmet.webp", *baseArmorSet], ["", *([Color.Werewolf.value[1]] * 3)]),

    ArmorType.ReaperMask: (["ReaperMaskHelmet.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.ReaperMaskSpirit: (["ReaperMaskHelmetSpirit.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.TarantulaBlackWidow: (["TarantulaHelmetBlackWidow.webp", "ChainmailChestplate.webp", "LeatherLeggings.png", "IronBoots.webp"], ["", "", Color.Tarantula.value[1], ""]),
    ArmorType.WardenHelmetTrueWarden: (["WardenHelmetTrueWarden.webp", *baseArmorSet], ["", *([Color.TentacleDye.value[1]] * 3)]),
    ArmorType.WitherGoggles: (["WitherGogglesHelmet.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.WitherGogglesCorrupt: (["WitherGogglesHelmetCorrupt.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.WitherGogglesCelestial: (["WitherGogglesHelmetCelestial.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.WitherGogglesCyberpunk: (["a_WitherGogglesHelmetCyberpunk.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.DiverHelmetPuffer: (["DiverHelmetPuffer.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.MastiffHelmetPuppy: (["MastiffHelmetPuppy.webp", "GoldChestplate.webp", "DiamondLeggings.webp", "DiamondBoots.webp"], ["", "", "", ""]),
    ArmorType.PerfectHelmetReinforced: (["PerfectHelmetReinforced.webp", "DiamondChestplate.webp", "DiamondLeggings.webp", "DiamondBoots.webp"], ["", "", "", ""]),
    ArmorType.Chainmail: (["ChainmailHelmet.webp", "ChainmailChestplate.webp", "ChainmailLeggings.webp", "ChainmailBoots.webp"], ["", "", "", ""]),
    ArmorType.Iron: (["IronHelmet.webp", "IronChestplate.webp", "IronLeggings.webp", "IronBoots.webp"], ["", "", "", ""]),
    ArmorType.Golden: (["GoldHelmet.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.Diamond: (["DiamondHelmet.webp", "DiamondChestplate.webp", "DiamondLeggings.webp", "DiamondBoots.webp"], ["", "", "", ""]),

    ArmorType.Mushroom: (fullArmorSet, [*([Color.Mushroom.value[1]] * 4)]),
    ArmorType.Pumpkin: (fullArmorSet, [*([Color.Pumpkin.value[1]] * 4)]),
    ArmorType.FarmSuit: (fullArmorSet, [*([Color.FarmSuit.value[1]] * 4)]),
    ArmorType.FarmArmor: (fullArmorSet, [*([Color.FarmArmor.value[1]] * 4)]),
    ArmorType.Speedster: (fullArmorSet, [*([Color.Speedster.value[1]] * 4)]),
    ArmorType.Cactus: (fullArmorSet, [*([Color.Cactus.value[1]] * 4)]),
    ArmorType.Prospecting: (fullArmorSet, [*([Color.Prospecting.value[1]] * 4)]),
    ArmorType.Growth: (fullArmorSet, [*([Color.Growth.value[1]] * 4)]),
    ArmorType.GuardianChestplate: (["LeatherChestplate.png"], [Color.GuardianChestplate.value[1]]),
    ArmorType.CreeperPants: (["LeatherLeggings.png"], [Color.CreeperPants.value[1]]),
    ArmorType.MonsterHunter: (["IronHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "IronBoots.webp"], ["", Color.GuardianChestplate.value[1], Color.CreeperPants.value[1], ""]),
    ArmorType.MonsterRaider: (["IronHelmet.webp", "LeatherChestplate.png", "LeatherLeggings.png", "LeatherBoots.png"], ["", Color.GuardianChestplate.value[1], Color.CreeperPants.value[1], Color.Tarantula.value[1]]),
    ArmorType.ArmorOfMagma: (fullArmorSet, [*([Color.ArmorOfMagma.value[1]] * 4)]),
    ArmorType.Emerald: (fullArmorSet, [*([Color.Emerald.value[1]] * 4)]),
    ArmorType.GodAngler: (["DiamondHelmet.webp", *baseArmorSet], ["", "4F3B49", "595536", "461E3A"]),
    ArmorType.BuildersClay: (["BuildersClayHelmet.webp", *baseArmorSet], ["", *([Color.NecronDye.value[1]] * 3)]),

    ArmorType.Mineral: (["MineralHelmet.webp", *baseArmorSet], ["", *([Color.Mineral.value[1]] * 3)]),
    ArmorType.DiamondNecron: (["DiamondNecronHelmet.webp", *baseArmorSet], ["", *([Color.AquamarineDye.value[1]] * 3)]),
}