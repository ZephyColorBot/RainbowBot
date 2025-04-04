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
    PureCyan = ("Cyan", "4C7F99", ColorType.PureDye)
    Cyan = PureCyan
    PureLightBlue = ("Light Blue", "6699D8", ColorType.PureDye)
    LightBlue = PureLightBlue
    PureLB = PureLightBlue
    LB = PureLightBlue
    PureDarkBlue = ("Dark Blue", "334CB2", ColorType.PureDye)
    DarkBlue = PureDarkBlue
    PureBlue = PureDarkBlue
    Blue = PureDarkBlue
    PureDB = PureDarkBlue
    DB = PureDarkBlue
    PurePurple = ("Purple", "7F3FB2", ColorType.PureDye)
    Purple = PurePurple
    PureMagenta = ("Magenta", "B24CD8", ColorType.PureDye)
    Magenta = PureMagenta
    PurePink = ("Pink", "F27FA5", ColorType.PureDye)
    Pink = PurePink
    PureBrown = ("Brown", "664C33", ColorType.PureDye)
    Brown = PureBrown
    PureWhite = ("White", "FFFFFF", ColorType.PureDye)
    White = PureWhite
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

    FermentoChestplate = ("Fermento Chestplate", "58890C", ColorType.Armor)
    FermentoCP = FermentoChestplate
    FermentoChest = FermentoChestplate
    FermentoLeggings = ("Fermento Leggings", "6A9C1B", ColorType.Armor)
    FermentoLegs = FermentoLeggings
    FermentoBoots = ("Fermento Boots", "83B03B", ColorType.Armor)
    SquashChestplate = ("Squash Chestplate", "03430E", ColorType.Armor)
    SquashCP = SquashChestplate
    SquashChest = SquashChestplate
    SquashLeggings = ("Squash Leggings", "0C4A16", ColorType.Armor)
    SquashLegs = SquashLeggings
    SquashBoots = ("Squash Boots", "13561E", ColorType.Armor)
    CropieChestplate = ("Cropie Chestplate", "7A2900", ColorType.Armor)
    CropieCP = CropieChestplate
    CropieChest = CropieChestplate
    CropieLeggings = ("Cropie Leggings", "94451F", ColorType.Armor)
    CropieLegs = CropieLeggings
    CropieBoots = ("Cropie Boots", "BB6535", ColorType.Armor)
    MelonArmor = ("Melon Armor", "899E20", ColorType.Armor)
    Melon = MelonArmor

    MagmaLord = ("Magma Lord", "6F0F08", ColorType.Armor)

    CrimsonChestplate = ("Crimson Chestplate", "FF6F0C", ColorType.Armor)
    CrimsonCP = CrimsonChestplate
    CrimsonChest = CrimsonChestplate
    CrimsonLeggings = ("Crimson Leggings", "E66105", ColorType.Armor)
    CrimsonLegs = CrimsonLeggings
    CrimsonBoots = ("Crimson Boots", "E65300", ColorType.Armor)
    TerrorChestplate = ("Terror Chestplate", "3E05AF", ColorType.Armor)
    TerrorCP = TerrorChestplate
    TerrorChest = TerrorChestplate
    TerrorLeggings = ("Terror Leggings", "5D23D1", ColorType.Armor)
    TerrorLegs = TerrorLeggings
    TerrorBoots = ("Terror Boots", "7C44EC", ColorType.Armor)
    AuroraChestplate = ("Aurora Chestplate", "2841F1", ColorType.Armor)
    AuroraCP = AuroraChestplate
    AuroraChest = AuroraChestplate
    AuroraLeggings = ("Aurora Leggings", "3F56FB", ColorType.Armor)
    AuroraLegs = AuroraLeggings
    AuroraBoots = ("Aurora Boots", "6184FC", ColorType.Armor)
    HollowChestplate = ("Hollow Chestplate", "FFCB0D", ColorType.Armor)
    HollowCP = HollowChestplate
    HollowChest = HollowChestplate
    HollowLeggings = ("Hollow Leggings", "FFF6A3", ColorType.Armor)
    HollowLegs = HollowLeggings
    HollowBoots = ("Hollow Boots", "E3FFFA", ColorType.Armor)
    FervorChestplate = ("Fervor Chestplate", "F04729", ColorType.Armor)
    FervorCP = FervorChestplate
    FervorChest = FervorChestplate
    FervorLeggings = ("Fervor Leggings", "17BF89", ColorType.Armor)
    FervorLegs = FervorLeggings
    FervorBoots = ("Fervor Boots", "07A674", ColorType.Armor)

    Thunder = ("Thunder", "24DDE5", ColorType.Armor)
    ThunderArmor = Thunder
    FinalDestinationChestplate = ("Final Destination Chestplate", "0A0011", ColorType.Armor)
    FinalDestinationCP = FinalDestinationChestplate
    FinalDestinationChest = FinalDestinationChestplate
    FinalDestinationLeggings = ("Final Destination Leggings", "FF75FF", ColorType.Armor)
    FinalDestinationLegs = FinalDestinationLeggings
    FinalDestinationBoots = ("Final Destination Boots", "0A0011", ColorType.Armor)

    _330066 = ("330066", "330066", ColorType.Fairy)
    _306 = _330066
    _4C0099 = ("4C0099", "4C0099", ColorType.Fairy)
    _6600CC = ("6600CC", "6600CC", ColorType.Fairy)
    _60C = _6600CC
    _7F00FF = ("7F00FF", "7F00FF", ColorType.Fairy)
    _9933FF = ("9933FF", "9933FF", ColorType.Fairy)
    _93F = _9933FF
    B266FF = ("B266FF", "B266FF", ColorType.Fairy)
    B6F = B266FF
    CC99FF = ("CC99FF", "CC99FF", ColorType.Fairy)
    C9F = CC99FF
    E5CCFF = ("E5CCFF", "E5CCFF", ColorType.Fairy)
    FFCCFF = ("FFCCFF", "FFCCFF", ColorType.Fairy)
    FF99FF = ("FF99FF", "FF99FF", ColorType.Fairy)
    F9F = FF99FF
    FF66FF = ("FF66FF", "FF66FF", ColorType.Fairy)
    F6F = FF66FF
    FF33FF = ("FF33FF", "FF33FF", ColorType.Fairy)
    F3F = FF33FF
    FF00FF = ("FF00FF", "FF00FF", ColorType.Fairy)
    F0F = FF00FF
    CC00CC = ("CC00CC", "CC00CC", ColorType.Fairy)
    C0C = CC00CC
    _990099 = ("990099", "990099", ColorType.Fairy)
    _909 = _990099
    _660066 = ("660066", "660066", ColorType.Fairy)
    _606 = _660066
    _660033 = ("660033", "660033", ColorType.Fairy)
    _603 = _660033
    _99004C = ("99004C", "99004C", ColorType.Fairy)
    CC0066 = ("CC0066", "CC0066", ColorType.Fairy)
    C06 = CC0066
    FF007F = ("FF007F", "FF007F", ColorType.Fairy)
    FF3399 = ("FF3399", "FF3399", ColorType.Fairy)
    F39 = FF3399
    FF66B2 = ("FF66B2", "FF66B2", ColorType.Fairy)
    FF99CC = ("FF99CC", "FF99CC", ColorType.Fairy)
    F9C = FF99CC
    FFCCE5 = ("FFCCE5", "FFCCE5", ColorType.Fairy)

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
    _54146E = ("54146E", "54146E", ColorType.Crystal)
    _541 = _54146E
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
    Treasure = ("Treasure", "FCD12A", ColorType.HypixelDye)
    TreasureDye = Treasure

    def __str__(self):
        return self.value

allFairyHexes = {
    Color._330066: ([], ["All"]),
    Color._4C0099: ([], ["All"]),
    Color._6600CC: ([], ["All"]),
    Color._7F00FF: ([], ["All"]),
    Color._9933FF: ([], ["All"]),
    Color.B266FF: ([], ["All"]),
    Color.CC99FF: ([], ["All"]),
    Color.E5CCFF: ([], ["All"]),
    Color.FFCCFF: ([], ["All"]),
    Color.FF99FF: ([], ["All"]),
    Color.FF66FF: ([], ["All"]),
    Color.FF33FF: ([], ["All"]),
    Color.FF00FF: ([], ["All"]),
    Color.CC00CC: ([], ["All"]),
    Color._990099: ([], ["All"]),
    Color._660066: ([], ["All"]),
    Color._660033: (["Helmet"], ["Chestplate", "Leggings", "Boots"]),
    Color._99004C: (["Helmet", "Chestplate"], ["Leggings", "Boots"]),
    Color.CC0066: (["Helmet", "Chestplate", "Leggings"], ["Boots"]),
    Color.FF007F: (["All"], []),
    Color.FF3399: (["All"], []),
    Color.FF66B2: (["Chestplate", "Leggings", "Boots"], ["Helmet"]),
    Color.FF99CC: (["Leggings", "Boots"], ["Helmet", "Chestplate"]),
    Color.FFCCE5: (["Boots"], ["Helmet", "Chestplate", "Leggings"]),
}
allCrystalHexes = {}
allHypixelDyeHexes = {Color.TrueBlack.value[1]: Color.TrueBlack.value[1], Color.PureWhite.value[1]: Color.PureWhite.value[1]}
allPureExoticHexes = {}
pureColorToDiscordEmotes = {
    Color.PureRed:       "<:RedDye:1334768678612238357>",
    Color.PureOrange:    "<:OrangeDye:1334768730101780571>",
    Color.PureYellow:    "<:YellowDye:1334768821923352586>",
    Color.PureLime:      "<:LimeDye:1334768853988675636>",
    Color.PureDarkGreen: "<:DarkGreenDye:1334768739895218187>",
    Color.PureCyan:      "<:CyanDye:1334768832471896124>",
    Color.PureLightBlue: "<:LightBlueDye:1334768799215259667>",
    Color.PureDarkBlue:  "<:DarkBlueDye:1334768754734665748>",
    Color.PurePurple:    "<:PurpleDye:1334768766613192734>",
    Color.PureMagenta:   "<:MagentaDye:1334768786229956729>",
    Color.PurePink:      "<:PinkDye:1334768777581170739>",
    Color.PureBrown:     "<:BrownDye:1334768649809956955>",
    Color.PureWhite:     "<:WhiteDye:1334768808656769024>",
    Color.PureLightGrey: "<:LightGrayDye:1334768841963733044>",
    Color.PureDarkGrey:  "<:DarkGrayDye:1334768865334399078>",
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
    HolyDrake = "Holy Drake"
    DrakeHoly = HolyDrake
    Old = "Old"
    OldBaby = "Old Baby"
    BabyOld = OldBaby
    OldShimmer = "Old Shimmer"
    ShimmerOld = OldShimmer
    OldDrake = "Old Drake"
    DrakeOld = OldDrake
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
    ProtectorDrake = "Protector Drake"
    DrakeProtector = ProtectorDrake
    ProtDrake = ProtectorDrake
    DrakeProt = ProtectorDrake
    Strong = "Strong"
    StrongBaby = "Strong Baby"
    BabyStrong = StrongBaby
    StrongShimmer = "Strong Shimmer"
    ShimmerStrong = StrongShimmer
    StrongDrake = "Strong Drake"
    DrakeStrong = StrongDrake
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
    SuperiorDrake = "Superior Drake"
    DrakeSuperior = SuperiorDrake
    SupDrake = SuperiorDrake
    DrakeSup = SuperiorDrake
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
    UnstableDrake = "Unstable Drake"
    DrakeUnstable = UnstableDrake
    UnstDrake = UnstableDrake
    DrakeUnst = UnstableDrake
    Wise = "Wise"
    WiseBaby = "Wise Baby"
    BabyWise = WiseBaby
    WiseShimmer = "Wise Shimmer"
    ShimmerWise = WiseShimmer
    WiseDrake = "Wise Drake"
    DrakeWise = WiseDrake
    Young = "Young"
    YoungBaby = "Young Baby"
    BabyYoung = YoungBaby
    YoungShimmer = "Young Shimmer"
    ShimmerYoung = YoungShimmer
    YoungDrake = "Young Drake"
    DrakeYoung = YoungDrake
    Angler = "Angler"
    Pack = "Pack"
    Bat = "Bat"
    Biohazard = "Biohazard"
    Blaze = "Blaze"
    FrozenBlaze = "Frozen Blaze"
    FB = FrozenBlaze
    FrozenBlazeIcicle = "Frozen Blaze Icicle"
    Icicle = FrozenBlazeIcicle
    FrozenBlazeIceberg = "Frozen Blaze Iceberg"
    FrozenBlazeIceburg = FrozenBlazeIceberg
    Iceberg = FrozenBlazeIceberg
    Iceburg = FrozenBlazeIceburg

    EmberHelmet = "Ember Helmet"
    Ember = EmberHelmet
    RekindledEmber = "Rekindled Ember"
    SmolderingEmber = "Smoldering Ember"
    DeepSeaAngler = "Deep Sea Angler"
    DeepSea = DeepSeaAngler
    Sorrow = "Sorrow"
    PaladinSorrow = "Paladin Sorrow"
    SorrowPaladin = PaladinSorrow

    CloverHelmet = "Clover Helmet"
    Clover = CloverHelmet
    Glacite = "Glacite"
    Goblin = "Goblin"
    GoblinBaby = "Goblin Baby"
    Goldor = "Goldor"
    GoldorCelestial = "Goldor Celestial"
    CelestialGoldor = GoldorCelestial
    Lapis = "Lapis"
    Leaflet = "Leaflet"
    Leaf = Leaflet
    Maxor = "Maxor"
    MaxorCelestial = "Maxor Celestial"
    CelestialMaxor = MaxorCelestial
    Necron = "Necron"
    NecronCelestial = "Necron Celestial"
    CelestialNecron = NecronCelestial
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
    ShadowAssassinSlyFox = "Shadow Assassin Sly Fox"
    ShadowAssassinSly = ShadowAssassinSlyFox
    SlyFox = ShadowAssassinSlyFox
    SASlyFox = ShadowAssassinSlyFox
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
    StormCelestial = "Storm Celestial"
    CelestialStorm = StormCelestial
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

    Crimson = "Crimson"
    CrimsonArmor = Crimson
    Terror = "Terror"
    TerrorArmor = Terror
    Aurora = "Aurora"
    AuroraArmor = Aurora
    Fervor = "Fervor"
    FervorArmor = Fervor
    Hollow = "Hollow"
    HollowArmor = Hollow
    Hallow = Hollow
    HallowArmor = Hollow

    Melon = "Melon"
    MelonArmor = Melon
    Cropie = "Cropie"
    CropieArmor = Cropie
    Squash = "Squash"
    SquashArmor = Squash
    Fermento = "Fermento"
    FermentoArmor = Fermento
    FinalDestination = "Final Destination"
    FinalDestinationArmor = FinalDestination
    Thunder = "Thunder"
    ThunderArmor = Thunder

    ReaperMask = "Reaper Mask"
    ReaperMaskSpirit = "Reaper Mask Spirit"
    Reaper = ReaperMask
    ReaperSpirit = ReaperMaskSpirit
    SpiritReaper = ReaperMaskSpirit
    OniReaperMask = "Oni Reaper Mask"
    OniReaper = OniReaperMask
    Oni = OniReaperMask
    RedOniReaperMask = "Red Oni Reaper Mask"
    RedOniReaper = RedOniReaperMask
    RedOni = RedOniReaperMask
    BlueOniReaperMask = "Blue Oni Reaper Mask"
    BlueOniReaper = BlueOniReaperMask
    BlueOni = BlueOniReaperMask

    MagmaLord = "Magma Lord"
    MagmaLordMeteor = "Magma Lord Meteor"
    MagmaLordShark = "Magma Lord Shark"
    MagmaLordSharkBrown = MagmaLordShark
    MagmaLordSharkWhite = "Magma Lord Shark White"
    MagmaLordSharkGold = "Magma Lord Shark Gold"
    MagmaLordSharkLime = "Magma Lord Shark Lime"
    MagmaLordSharkDiamond = "Magma Lord Shark Diamond"
    MagmaLordSharkRose = "Magma Lord Shark Rose"
    MagmaLordSharkRed = "Magma Lord Shark Red"
    MagmaLordSharkPurple = "Magma Lord Shark Purple"
    MagmaLordSharkPortal = "Magma Lord Shark Portal"
    MagmaLordSharkLava = "Magma Lord Shark Lava"
    MagmaLordSharkBlack = "Magma Lord Shark Black"
    MagmaLordSharkPastel = "Magma Lord Shark Pastel"
    MagmaLordSharkWarding = "Magma Lord Shark Warding"
    MagmaLordSharkToxic = "Magma Lord Shark Toxic"

    WitherGoggles = "Wither Goggles"
    WitherGogglesCorrupt = "Corrupt Wither Goggles"
    WitherGogglesCelestial = "Celestial Wither Goggles"
    WitherGogglesCyberpunk = "Cyberpunk Wither Goggles"
    TarantulaBlackWidow = "Tarantula Black Widow"
    TaraBlackWidow = TarantulaBlackWidow
    WardenHelmetTrueWarden = "True Warden"
    TrueWarden = WardenHelmetTrueWarden
    WardenTrueWarden = WardenHelmetTrueWarden
    WardenHelmetSentinelWarden = "Sentinel Warden"
    SentinelWarden = WardenHelmetSentinelWarden
    WardenHelmetSentinelWardenTeal = "Sentinel Warden Teal"
    SentinelWardenTeal = WardenHelmetSentinelWardenTeal
    WardenHelmetSentinelWardenPurple = "Sentinel Warden Purple"
    SentinelWardenPurple = WardenHelmetSentinelWardenPurple
    WardenHelmetSentinelWardenPink = "Sentinel Warden Pink"
    SentinelWardenPink = WardenHelmetSentinelWardenPink
    WardenHelmetSentinelWardenOrange = "Sentinel Warden Orange"
    SentinelWardenOrange = WardenHelmetSentinelWardenOrange
    WardenHelmetSentinelWardenMaroon = "Sentinel Warden Maroon"
    SentinelWardenMaroon = WardenHelmetSentinelWardenMaroon
    WardenHelmetSentinelWardenGreen = "Sentinel Warden Green"
    SentinelWardenGreen = WardenHelmetSentinelWardenGreen
    WardenHelmetSentinelWardenBlack = "Sentinel Warden Black"
    SentinelWardenBlack = WardenHelmetSentinelWardenBlack

    MendingCrown = "Mending Crown"
    MendersCrown = MendingCrown
    MenderCrown = MendingCrown
    Mending = MendingCrown
    Menders = MendingCrown
    Mender = MendingCrown
    MendingCrownCaduceus = "Caduceus Mending Crown"
    CaduceusMendingCrown = MendingCrownCaduceus
    MendersCrownCaduceus = MendingCrownCaduceus
    CaduceusMendersCrown = MendingCrownCaduceus
    MenderCrownCaduceus = MendingCrownCaduceus
    CaduceusMenderCrown = MendingCrownCaduceus
    CaduceusMending = MendingCrownCaduceus
    MendingCaduceus = MendingCrownCaduceus
    MendersCaduceus = MendingCrownCaduceus
    MenderCaduceus = MendingCrownCaduceus
    CaduceusMenders = MendingCrownCaduceus
    CaduceusMender = MendingCrownCaduceus
    MendingCrownCaduceusBlue = "Blue Caduceus Mending Crown"
    CaduceusMendingCrownBlue = MendingCrownCaduceusBlue
    MendersCrownCaduceusBlue = MendingCrownCaduceusBlue
    CaduceusMendersCrownBlue = MendingCrownCaduceusBlue
    MenderCrownCaduceusBlue = MendingCrownCaduceusBlue
    CaduceusMenderCrownBlue = MendingCrownCaduceusBlue
    MendingCaduceusBlue = MendingCrownCaduceusBlue
    CaduceusMendingBlue = MendingCrownCaduceusBlue
    MendersCaduceusBlue = MendingCrownCaduceusBlue
    CaduceusMendersBlue = MendingCrownCaduceusBlue
    MenderCaduceusBlue = MendingCrownCaduceusBlue
    CaduceusMenderBlue = MendingCrownCaduceusBlue
    MendingCrownCaduceusGreen = "Green Caduceus Mending Crown"
    CaduceusMendingCrownGreen = MendingCrownCaduceusGreen
    MendersCrownCaduceusGreen = MendingCrownCaduceusGreen
    CaduceusMendersCrownGreen = MendingCrownCaduceusGreen
    MenderCrownCaduceusGreen = MendingCrownCaduceusGreen
    CaduceusMenderCrownGreen = MendingCrownCaduceusGreen
    MendingCaduceusGreen = MendingCrownCaduceusGreen
    CaduceusMendingGreen = MendingCrownCaduceusGreen
    MendersCaduceusGreen = MendingCrownCaduceusGreen
    CaduceusMendersGreen = MendingCrownCaduceusGreen
    MenderCaduceusGreen = MendingCrownCaduceusGreen
    CaduceusMenderGreen = MendingCrownCaduceusGreen
    MendingCrownCaduceusPurple = "Purple Caduceus Mending Crown"
    CaduceusMendingCrownPurple = MendingCrownCaduceusPurple
    MendersCrownCaduceusPurple = MendingCrownCaduceusPurple
    CaduceusMendersCrownPurple = MendingCrownCaduceusPurple
    MenderCrownCaduceusPurple = MendingCrownCaduceusPurple
    CaduceusMenderCrownPurple = MendingCrownCaduceusPurple
    MendingCaduceusPurple = MendingCrownCaduceusPurple
    CaduceusMendingPurple = MendingCrownCaduceusPurple
    MendersCaduceusPurple = MendingCrownCaduceusPurple
    CaduceusMendersPurple = MendingCrownCaduceusPurple
    MenderCaduceusPurple = MendingCrownCaduceusPurple
    CaduceusMenderPurple = MendingCrownCaduceusPurple
    MendingCrownCaduceusRed = "Red Caduceus Mending Crown"
    CaduceusMendingCrownRed = MendingCrownCaduceusRed
    MendersCrownCaduceusRed = MendingCrownCaduceusRed
    CaduceusMendersCrownRed = MendingCrownCaduceusRed
    MenderCrownCaduceusRed = MendingCrownCaduceusRed
    CaduceusMenderCrownRed = MendingCrownCaduceusRed
    MendingCaduceusRed = MendingCrownCaduceusRed
    CaduceusMendingRed = MendingCrownCaduceusRed
    MendersCaduceusRed = MendingCrownCaduceusRed
    CaduceusMendersRed = MendingCrownCaduceusRed
    MenderCaduceusRed = MendingCrownCaduceusRed
    CaduceusMenderRed = MendingCrownCaduceusRed

    Divan = "Divan"
    ArmorOfDivan = Divan
    DivanGemstone = "Divan Gemstone"
    GemstoneDivan = DivanGemstone
    DivanGemstoneSapphire = "Gemstone Divan Sapphire"
    GemstoneDivanSapphire = DivanGemstoneSapphire
    SapphireDivanGemstone = DivanGemstoneSapphire
    DivanGemstoneBlue = DivanGemstoneSapphire
    BlueDivanGemstone = DivanGemstoneSapphire
    BlueGemstoneDivan = DivanGemstoneSapphire
    DivanGemstoneAmethyst = "Gemstone Divan Amethyst"
    GemstoneDivanAmethyst = DivanGemstoneAmethyst
    AmethystDivanGemstone = DivanGemstoneAmethyst
    DivanGemstonePurple = DivanGemstoneAmethyst
    PurpleDivanGemstone = DivanGemstoneAmethyst
    PurpleGemstoneDivan = DivanGemstoneAmethyst
    DivanGemstoneJasper = "Gemstone Divan Jasper"
    GemstoneDivanJasper = DivanGemstoneJasper
    JasperDivanGemstone = DivanGemstoneJasper
    DivanGemstonePink = DivanGemstoneJasper
    PinkDivanGemstone = DivanGemstoneJasper
    PinkGemstoneDivan = DivanGemstoneJasper
    DivanGemstoneRuby = "Gemstone Divan Ruby"
    GemstoneDivanRuby = DivanGemstoneRuby
    RubyDivanGemstone = DivanGemstoneRuby
    DivanGemstoneRed = DivanGemstoneRuby
    RedDivanGemstone = DivanGemstoneRuby
    RedGemstoneDivan = DivanGemstoneRuby
    DivanGemstoneTopaz = "Gemstone Divan Topaz"
    GemstoneDivanTopaz = DivanGemstoneTopaz
    TopazDivanGemstone = DivanGemstoneTopaz
    DivanGemstoneYellow = DivanGemstoneTopaz
    YellowDivanGemstone = DivanGemstoneTopaz
    YellowGemstoneDivan = DivanGemstoneTopaz
    DivanGemstoneJade = "Gemstone Divan Jade"
    GemstoneDivanJade = DivanGemstoneJade
    JadeDivanGemstone = DivanGemstoneJade
    DivanGemstoneGreen = DivanGemstoneJade
    GreenDivanGemstone = DivanGemstoneJade
    GreenGemstoneDivan = DivanGemstoneJade
    DivanGemstoneOpal = "Gemstone Divan Opal"
    GemstoneDivanOpal = DivanGemstoneOpal
    OpalDivanGemstone = DivanGemstoneOpal
    DivanGemstoneWhite = DivanGemstoneOpal
    WhiteDivanGemstone = DivanGemstoneOpal
    WhiteGemstoneDivan = DivanGemstoneOpal
    DivanGemstoneCitrine = "Gemstone Divan Citrine"
    GemstoneDivanCitrine = DivanGemstoneCitrine
    CitrineDivanGemstone = DivanGemstoneCitrine
    DivanGemstoneOrange = DivanGemstoneCitrine
    OrangeDivanGemstone = DivanGemstoneCitrine
    OrangeGemstoneDivan = DivanGemstoneCitrine
    GemstoneDivanAmber = GemstoneDivan
    DivanGemstoneAmber = GemstoneDivan
    AmberDivanGemstone = GemstoneDivan
    DivanGemstoneGold = GemstoneDivan
    GoldDivanGemstone = GemstoneDivan
    GoldGemstoneDivan = GemstoneDivan
    DivanGemstonePeridot = "Gemstone Divan Peridot"
    GemstoneDivanPeridot = DivanGemstonePeridot
    PeridotDivanGemstone = DivanGemstonePeridot
    DivanGemstoneLime = DivanGemstonePeridot
    LimeDivanGemstone = DivanGemstonePeridot
    LimeGemstoneDivan = DivanGemstonePeridot
    DivanGemstoneAquamarine = "Gemstone Divan Aquamarine"
    GemstoneDivanAquamarine = DivanGemstoneAquamarine
    AquamarineDivanGemstone = DivanGemstoneAquamarine
    DivanGemstoneAqua = DivanGemstoneAquamarine
    AquaDivanGemstone = DivanGemstoneAquamarine
    AquaGemstoneDivan = DivanGemstoneAquamarine
    DivanGemstoneOnyx = "Gemstone Divan Onyx"
    GemstoneDivanOnyx = DivanGemstoneOnyx
    OnyxDivanGemstone = DivanGemstoneOnyx
    DivanGemstoneBlack = DivanGemstoneOnyx
    BlackDivanGemstone = DivanGemstoneOnyx
    BlackGemstoneDivan = DivanGemstoneOnyx

    Diver = "Diver"
    DiverHelmetFrozen = "Frozen Diver Helmet"
    FrozenDiver = DiverHelmetFrozen
    DiverFrozen = DiverHelmetFrozen
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

    FermentoBloom = "Fermento Bloom"
    BloomFermento = FermentoBloom
    FermentoLeaf = "Fermento Leaf"
    LeafFermento = FermentoLeaf

    FermentoCactus = "Fermento Cactus"
    FermentoCactusBlack = "Fermento Cactus Black"
    FermentoCactusBlue = "Fermento Cactus Blue"
    FermentoCactusGreen = "Fermento Cactus Green"
    FermentoCactusOrange = "Fermento Cactus Orange"
    FermentoCactusPurple = "Fermento Cactus Purple"
    FermentoCactusRed = "Fermento Cactus Red"
    FermentoCactusWhite = "Fermento Cactus White"
    FermentoCactusYellow = "Fermento Cactus Yellow"
    FermentoCarrot = "Fermento Carrot"
    FermentoCarrotBlack = "Fermento Carrot Black"
    FermentoCarrotBlue = "Fermento Carrot Blue"
    FermentoCarrotGreen = "Fermento Carrot Green"
    FermentoCarrotOrange = "Fermento Carrot Orange"
    FermentoCarrotPurple = "Fermento Carrot Purple"
    FermentoCarrotRed = "Fermento Carrot Red"
    FermentoCarrotWhite = "Fermento Carrot White"
    FermentoCarrotYellow = "Fermento Carrot Yellow"
    FermentoCocoa = "Fermento Cocoa"
    FermentoCocoaBlack = "Fermento Cocoa Black"
    FermentoCocoaBlue = "Fermento Cocoa Blue"
    FermentoCocoaGreen = "Fermento Cocoa Green"
    FermentoCocoaOrange = "Fermento Cocoa Orange"
    FermentoCocoaPurple = "Fermento Cocoa Purple"
    FermentoCocoaRed = "Fermento Cocoa Red"
    FermentoCocoaWhite = "Fermento Cocoa White"
    FermentoCocoaYellow = "Fermento Cocoa Yellow"
    FermentoMushroom = "Fermento Mushroom"
    FermentoMushroomBlack = "Fermento Mushroom Black"
    FermentoMushroomBlue = "Fermento Mushroom Blue"
    FermentoMushroomGreen = "Fermento Mushroom Green"
    FermentoMushroomOrange = "Fermento Mushroom Orange"
    FermentoMushroomPurple = "Fermento Mushroom Purple"
    FermentoMushroomRed = "Fermento Mushroom Red"
    FermentoMushroomWhite = "Fermento Mushroom White"
    FermentoMushroomYellow = "Fermento Mushroom Yellow"
    FermentoMelon = "Fermento Melon"
    FermentoMelonBlack = "Fermento Melon Black"
    FermentoMelonBlue = "Fermento Melon Blue"
    FermentoMelonGreen = "Fermento Melon Green"
    FermentoMelonOrange = "Fermento Melon Orange"
    FermentoMelonPurple = "Fermento Melon Purple"
    FermentoMelonRed = "Fermento Melon Red"
    FermentoMelonWhite = "Fermento Melon White"
    FermentoMelonYellow = "Fermento Melon Yellow"
    FermentoPotato = "Fermento Potato"
    FermentoPotatoBlack = "Fermento Potato Black"
    FermentoPotatoBlue = "Fermento Potato Blue"
    FermentoPotatoGreen = "Fermento Potato Green"
    FermentoPotatoOrange = "Fermento Potato Orange"
    FermentoPotatoPurple = "Fermento Potato Purple"
    FermentoPotatoRed = "Fermento Potato Red"
    FermentoPotatoWhite = "Fermento Potato White"
    FermentoPotatoYellow = "Fermento Potato Yellow"
    FermentoPumpkin = "Fermento Pumpkin"
    FermentoPumpkinBlack = "Fermento Pumpkin Black"
    FermentoPumpkinBlue = "Fermento Pumpkin Blue"
    FermentoPumpkinGreen = "Fermento Pumpkin Green"
    FermentoPumpkinOrange = "Fermento Pumpkin Orange"
    FermentoPumpkinPurple = "Fermento Pumpkin Purple"
    FermentoPumpkinRed = "Fermento Pumpkin Red"
    FermentoPumpkinWhite = "Fermento Pumpkin White"
    FermentoPumpkinYellow = "Fermento Pumpkin Yellow"
    FermentoSugarCane = "Fermento Sugar Cane"
    FermentoSugarCaneBlack = "Fermento Sugar Cane Black"
    FermentoSugarCaneBlue = "Fermento Sugar Cane Blue"
    FermentoSugarCaneGreen = "Fermento Sugar Cane Green"
    FermentoSugarCaneOrange = "Fermento Sugar Cane Orange"
    FermentoSugarCanePurple = "Fermento Sugar Cane Purple"
    FermentoSugarCaneRed = "Fermento Sugar Cane Red"
    FermentoSugarCaneWhite = "Fermento Sugar Cane White"
    FermentoSugarCaneYellow = "Fermento Sugar Cane Yellow"
    FermentoCane = FermentoSugarCane
    FermentoCaneBlack = FermentoSugarCaneBlack
    FermentoCaneBlue = FermentoSugarCaneBlue
    FermentoCaneGreen = FermentoSugarCaneGreen
    FermentoCaneOrange = FermentoSugarCaneOrange
    FermentoCanePurple = FermentoSugarCanePurple
    FermentoCaneRed = FermentoSugarCaneRed
    FermentoCaneWhite = FermentoSugarCaneWhite
    FermentoCaneYellow = FermentoSugarCaneYellow
    FermentoNetherwart = "Fermento Netherwart"
    FermentoNetherwartBlack = "Fermento Netherwart Black"
    FermentoNetherwartBlue = "Fermento Netherwart Blue"
    FermentoNetherwartGreen = "Fermento Netherwart Green"
    FermentoNetherwartOrange = "Fermento Netherwart Orange"
    FermentoNetherwartPurple = "Fermento Netherwart Purple"
    FermentoNetherwartRed = "Fermento Netherwart Red"
    FermentoNetherwartWhite = "Fermento Netherwart White"
    FermentoNetherwartYellow = "Fermento Netherwart Yellow"
    FermentoWart = FermentoNetherwart
    FermentoWartBlack = FermentoNetherwartBlack
    FermentoWartBlue = FermentoNetherwartBlue
    FermentoWartGreen = FermentoNetherwartGreen
    FermentoWartOrange = FermentoNetherwartOrange
    FermentoWartPurple = FermentoNetherwartPurple
    FermentoWartRed = FermentoNetherwartRed
    FermentoWartWhite = FermentoNetherwartWhite
    FermentoWartYellow = FermentoNetherwartYellow
    FermentoWheat = "Fermento Wheat"
    FermentoWheatBlack = "Fermento Wheat Black"
    FermentoWheatBlue = "Fermento Wheat Blue"
    FermentoWheatGreen = "Fermento Wheat Green"
    FermentoWheatOrange = "Fermento Wheat Orange"
    FermentoWheatPurple = "Fermento Wheat Purple"
    FermentoWheatRed = "Fermento Wheat Red"
    FermentoWheatWhite = "Fermento Wheat White"
    FermentoWheatYellow = "Fermento Wheat Yellow"

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
    MusicPants = "Stereo Pants"
    Stereo = MusicPants
    StereoLeggings = MusicPants
    StereoLegs = MusicPants
    Stereos = MusicPants
    StereoPants = MusicPants
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
    DiamondNecronKnight = "Diamond Necron Knight"
    DiaNecronKnight = DiamondNecronKnight
    KnightDiamondNecron = DiamondNecronKnight
    KnightDiaNecron = DiamondNecronKnight
    DiamondKnightNecron = DiamondNecronKnight
    DiaKnightNecron = DiamondNecronKnight
    DiamondKnight = DiamondNecronKnight
    DiaKnight = DiamondNecronKnight
    KnightDiamond = DiamondNecronKnight
    KnightDia = DiamondNecronKnight

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

        if color.value[2] == ColorType.Crystal:
            allCrystalHexes[color] = colorValue
        elif color.value[2] == ColorType.HypixelDye:
            allHypixelDyeHexes[color] = colorValue
        elif color.value[2] == ColorType.PureDye:
            allPureExoticHexes[color] = colorValue

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
fermentoArmorColor = ["", Color.FermentoChestplate.value[1], Color.FermentoLeggings.value[1], Color.FermentoBoots.value[1]]
itemDict = {
    ArmorType.FullSet: (fullArmorSet, [*([Color.Leather.value[1]] * 4)]),
    ArmorType.Helmet:     (["LeatherHelmet.png"   , "EmptyImageChestplate.png", "EmptyImageLeggings.png", "EmptyImageBoots.png"], [Color.Leather.value[1], "", "", ""]),
    ArmorType.Chestplate: (["EmptyImageHelmet.png", "LeatherChestplate.png"   , "EmptyImageLeggings.png", "EmptyImageBoots.png"], ["", Color.Leather.value[1], "", ""]),
    ArmorType.Leggings:   (["EmptyImageHelmet.png", "EmptyImageChestplate.png", "LeatherLeggings.png"   , "EmptyImageBoots.png"], ["", "", Color.Leather.value[1], ""]),
    ArmorType.Boots:      (["EmptyImageHelmet.png", "EmptyImageChestplate.png", "EmptyImageLeggings.png", "LeatherBoots.png"   ], ["", "", "", Color.Leather.value[1]]),

    ArmorType.HelmetChestplate: (["LeatherHelmet.png", "LeatherChestplate.png", "EmptyImageLeggings.png", "EmptyImageBoots.png"], [Color.Leather.value[1], Color.Leather.value[1], "", ""]),
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
    ArmorType.HolyDrake: (["HolyHelmetDrake.webp", *baseArmorSet], ["", *([Color.Holy.value[1]] * 3)]),
    ArmorType.Old: (["OldHelmet.webp", *baseArmorSet], ["", *([Color.Old.value[1]] * 3)]),
    ArmorType.OldBaby: (["OldHelmetBaby.webp", *baseArmorSet], ["", *([Color.Old.value[1]] * 3)]),
    ArmorType.OldShimmer: (["OldHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Old.value[1]] * 3)]),
    ArmorType.OldDrake: (["OldHelmetDrake.webp", *baseArmorSet], ["", *([Color.Old.value[1]] * 3)]),
    ArmorType.Protector: (["ProtectorHelmet.webp", *baseArmorSet], ["", *([Color.Protector.value[1]] * 3)]),
    ArmorType.ProtectorBaby: (["ProtectorHelmetBaby.webp", *baseArmorSet], ["", *([Color.Protector.value[1]] * 3)]),
    ArmorType.ProtectorShimmer: (["ProtectorHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Protector.value[1]] * 3)]),
    ArmorType.ProtectorDrake: (["ProtectorHelmetDrake.webp", *baseArmorSet], ["", *([Color.Protector.value[1]] * 3)]),
    ArmorType.Strong: (["StrongHelmet.webp", *baseArmorSet], ["", Color.StrongChestplate.value[1], Color.StrongLeggings.value[1], Color.StrongBoots.value[1]]),
    ArmorType.StrongBaby: (["StrongHelmetBaby.webp", *baseArmorSet], ["", Color.StrongChestplate.value[1], Color.StrongLeggings.value[1], Color.StrongBoots.value[1]]),
    ArmorType.StrongShimmer: (["StrongHelmetShimmer.webp", *baseArmorSet], ["", Color.StrongChestplate.value[1], Color.StrongLeggings.value[1], Color.StrongBoots.value[1]]),
    ArmorType.StrongDrake: (["StrongHelmetDrake.webp", *baseArmorSet], ["", Color.StrongChestplate.value[1], Color.StrongLeggings.value[1], Color.StrongBoots.value[1]]),
    ArmorType.Superior: (["SuperiorHelmet.webp", *baseArmorSet], ["", Color.Superior.value[1], Color.Superior.value[1], Color.SuperiorBoots.value[1]]),
    ArmorType.SuperiorBaby: (["SuperiorHelmetBaby.webp", *baseArmorSet], ["", Color.Superior.value[1], Color.Superior.value[1], Color.SuperiorBoots.value[1]]),
    ArmorType.SuperiorShimmer: (["SuperiorHelmetShimmer.webp", *baseArmorSet], ["", Color.Superior.value[1], Color.Superior.value[1], Color.SuperiorBoots.value[1]]),
    ArmorType.SuperiorDrake: (["SuperiorHelmetDrake.webp", *baseArmorSet], ["", Color.Superior.value[1], Color.Superior.value[1], Color.SuperiorBoots.value[1]]),
    ArmorType.Unstable: (["UnstableHelmet.webp", *baseArmorSet], ["", *([Color.Unstable.value[1]] * 3)]),
    ArmorType.UnstableBaby: (["UnstableHelmetBaby.webp", *baseArmorSet], ["", *([Color.Unstable.value[1]] * 3)]),
    ArmorType.UnstableShimmer: (["UnstableHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Unstable.value[1]] * 3)]),
    ArmorType.UnstableDrake: (["UnstableHelmetDrake.webp", *baseArmorSet], ["", *([Color.Unstable.value[1]] * 3)]),
    ArmorType.Wise: (["WiseHelmet.webp", *baseArmorSet], ["", *([Color.Wise.value[1]] * 3)]),
    ArmorType.WiseBaby: (["WiseHelmetBaby.webp", *baseArmorSet], ["", *([Color.Wise.value[1]] * 3)]),
    ArmorType.WiseShimmer: (["WiseHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Wise.value[1]] * 3)]),
    ArmorType.WiseDrake: (["WiseHelmetDrake.webp", *baseArmorSet], ["", *([Color.Wise.value[1]] * 3)]),
    ArmorType.Young: (["YoungHelmet.webp", *baseArmorSet], ["", *([Color.Young.value[1]] * 3)]),
    ArmorType.YoungBaby: (["YoungHelmetBaby.webp", *baseArmorSet], ["", *([Color.Young.value[1]] * 3)]),
    ArmorType.YoungShimmer: (["YoungHelmetShimmer.webp", *baseArmorSet], ["", *([Color.Young.value[1]] * 3)]),
    ArmorType.YoungDrake: (["YoungHelmetDrake.webp", *baseArmorSet], ["", *([Color.Young.value[1]] * 3)]),
    ArmorType.Angler: (["AnglerHelmet.webp", *baseArmorSet], ["", *([Color.Angler.value[1]] * 3)]),
    ArmorType.DeepSeaAngler: (["DeepSeaAnglerHelmet.webp", *baseArmorSet], ["", *([Color.Angler.value[1]] * 3)]),
    ArmorType.Pack: (["LeatherHelmet.png", "LeatherChestplate.png", "IronLeggings.webp", "IronBoots.webp"], [Color.PackHelmet.value[1], Color.PackChestplate.value[1], "", ""]),
    ArmorType.Bat: (["BatHelmet.webp", *baseArmorSet], ["", *([Color.Bat.value[1]] * 3)]),
    ArmorType.Biohazard: (["BiohazardHelmet.webp", *baseArmorSet], ["", *([Color.Biohazard.value[1]] * 3)]),
    ArmorType.Blaze: (["BlazeHelmet.webp", *baseArmorSet], ["", *([Color.Blaze.value[1]] * 3)]),
    ArmorType.FrozenBlaze: (["FrozenBlazeHelmet.webp", *baseArmorSet], ["", *([Color.FrozenBlaze.value[1]] * 3)]),
    ArmorType.FrozenBlazeIcicle: (["FrozenBlazeHelmetIcicle.webp", *baseArmorSet], ["", *([Color.FrozenBlaze.value[1]] * 3)]),
    ArmorType.FrozenBlazeIceberg: (["FrozenBlazeHelmetIceberg.webp", *baseArmorSet], ["", *([Color.FrozenBlaze.value[1]] * 3)]),
    ArmorType.Ember: (["EmberHelmet.webp", "ChainmailChestplate.webp", "ChainmailLeggings.webp", "ChainmailBoots.webp"], ["", "", "", ""]),
    ArmorType.RekindledEmber: (["RekindledEmberHelmet.webp", "ChainmailChestplate.webp", "ChainmailLeggings.webp", "ChainmailBoots.webp"], ["", "", "", ""]),
    ArmorType.SmolderingEmber: (["SmolderingEmberHelmet.webp", "ChainmailChestplate.webp", "ChainmailLeggings.webp", "ChainmailBoots.webp"], ["", "", "", ""]),
    ArmorType.Sorrow : (["ChainmailHelmet.webp", "ChainmailChestplate.webp", "ChainmailLeggings.webp", "ChainmailBoots.webp"], ["", "", "", ""]),
    ArmorType.SorrowPaladin: (["SorrowPaladinHelmet.webp", "ChainmailChestplate.webp", "ChainmailLeggings.webp", "ChainmailBoots.webp"], ["", "", "", ""]),
    ArmorType.CloverHelmet: (["CloverHelmet.webp", *baseArmorSet], ["", *([Color.HollyDye.value[1]] * 3)]),
    ArmorType.Glacite: (["GlaciteHelmet.webp", *baseArmorSet], ["", *([Color.Glacite.value[1]] * 3)]),
    ArmorType.Goblin: (["GoblinHelmet.webp", *baseArmorSet], ["", *([Color.Goblin.value[1]] * 3)]),
    ArmorType.GoblinBaby: (["GoblinHelmetBaby.webp", *baseArmorSet], ["", *([Color.Goblin.value[1]] * 3)]),
    ArmorType.Goldor: (["GoldorHelmet.webp", *baseArmorSet], ["", Color.GoldorChestplate.value[1], Color.GoldorLeggings.value[1], Color.GoldorBoots.value[1]]),
    ArmorType.GoldorCelestial: (["GoldorHelmetCelestial.webp", *baseArmorSet], ["", Color.GoldorChestplate.value[1], Color.GoldorLeggings.value[1], Color.GoldorBoots.value[1]]),
    ArmorType.Lapis: (["LapisHelmet.webp", *baseArmorSet], ["", *([Color.Lapis.value[1]] * 3)]),
    ArmorType.Leaflet: (["LeafletHelmet.webp", *baseArmorSet], ["", *([Color.Leaflet.value[1]] * 3)]),
    ArmorType.Maxor: (["MaxorHelmet.webp", *baseArmorSet], ["", Color.MaxorChestplate.value[1], Color.MaxorLeggings.value[1], Color.MaxorBoots.value[1]]),
    ArmorType.MaxorCelestial: (["MaxorHelmetCelestial.webp", *baseArmorSet], ["", Color.MaxorChestplate.value[1], Color.MaxorLeggings.value[1], Color.MaxorBoots.value[1]]),
    ArmorType.NecromancerLord: (["NecromancerLordHelmet.webp", *baseArmorSet], ["", Color.NecromancerLordChestplate.value[1], Color.NecromancerLordLeggings.value[1], Color.NecromancerLordBoots.value[1]]),
    ArmorType.Necron: (["NecronHelmet.webp", *baseArmorSet], ["", Color.NecronChestplate.value[1], Color.NecronLeggings.value[1], Color.NecronBoots.value[1]]),
    ArmorType.NecronCelestial: (["NecronHelmetCelestial.webp", *baseArmorSet], ["", Color.NecronChestplate.value[1], Color.NecronLeggings.value[1], Color.NecronBoots.value[1]]),
    ArmorType.RacingHelmet: (["RacingHelmet.webp", *baseArmorSet], ["", *([Color.Carmine.value[1]] * 3)]),
    ArmorType.RisingSun: (["RisingSunHelmet.webp", "GoldChestplate.webp", "LeatherLeggings.png", "LeatherBoots.png"], ["", "", Color.RisingSunLeggings.value[1], Color.RisingSunBoots.value[1]]),
    ArmorType.ShadowAssassin: (["ShadowAssassinHelmet.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinAdmiral: (["ShadowAssassinHelmetAdmiral.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinCrimson: (["ShadowAssassinHelmetCrimson.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinMuave: (["ShadowAssassinHelmetMauve.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.ShadowAssassinSlyFox: (["ShadowAssassinHelmetSlyFox.webp", *baseArmorSet], ["", *([Color.ShadowAssassin.value[1]] * 3)]),
    ArmorType.Shark: (["SharkHelmet.webp", *baseArmorSet], ["", *([Color.Shark.value[1]] * 3)]),
    ArmorType.SnowSuit: (["SnowSuitHelmet.webp", *baseArmorSet], ["", *([Color.SnowSuit.value[1]] * 3)]),
    ArmorType.SnowSuitSnowglobe: (["SnowSuitHelmetSnowglobe.webp", *baseArmorSet], ["", *([Color.SnowSuit.value[1]] * 3)]),
    ArmorType.SpaceHelmet: (["a_OldSpaceHelmet.webp", *baseArmorSet], ["", *([Color.BrickRed.value[1]] * 3)]),
    ArmorType.Sponge: (["SpongeHelmet.webp", *baseArmorSet], ["", *([Color.Sponge.value[1]] * 3)]),
    ArmorType.Spooky: (["SpookyHelmet.webp", *baseArmorSet], ["", *([Color.Spooky.value[1]] * 3)]),
    ArmorType.Storm: (["StormHelmet.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.StormCelestial: (["StormHelmetCelestial.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.Tarantula: (["LeatherHelmet.png", "ChainmailChestplate.webp", "LeatherLeggings.png", "IronBoots.webp"], [Color.Tarantula.value[1], "", Color.Tarantula.value[1], ""]),
    ArmorType.Tuxedo: ([*baseArmorSet], [Color.CheapTuxedoChestplate.value[1], Color.CheapTuxedoLeggings.value[1], Color.CheapTuxedoBoots.value[1]]),
    ArmorType.WardenHelmet: (["WardenHelmet.webp", *baseArmorSet], ["", *([Color.White.value[1]] * 3)]),
    ArmorType.Werewolf: (["WerewolfHelmet.webp", *baseArmorSet], ["", *([Color.Werewolf.value[1]] * 3)]),

    ArmorType.ReaperMask: (["ReaperMaskHelmet.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.ReaperMaskSpirit: (["ReaperMaskHelmetSpirit.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.OniReaperMask: (["OniReaperMaskHelmet.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.RedOniReaperMask: (["RedOniReaperMaskHelmet.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.BlueOniReaperMask: (["BlueOniReaperMaskHelmet.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.MagmaLord: (["MagmaLordHelmet.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordMeteor: (["MagmaLordHelmetMeteor.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkBrown: (["MagmaLordHelmetSharkBrown.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkWhite: (["MagmaLordHelmetSharkWhite.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkGold: (["MagmaLordHelmetSharkGold.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkLime: (["MagmaLordHelmetSharkLime.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkDiamond: (["MagmaLordHelmetSharkDiamond.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkRose: (["MagmaLordHelmetSharkRose.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkRed: (["MagmaLordHelmetSharkRed.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkPurple: (["MagmaLordHelmetSharkPurple.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkPortal: (["MagmaLordHelmetSharkPortal.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkLava: (["MagmaLordHelmetSharkLava.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkBlack: (["MagmaLordHelmetSharkBlack.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkPastel: (["MagmaLordHelmetSharkPastel.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkWarding: (["MagmaLordHelmetSharkWarding.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.MagmaLordSharkToxic: (["MagmaLordHelmetSharkToxic.webp", *baseArmorSet], ["", *([Color.MagmaLord.value[1]] * 3)]),
    ArmorType.TarantulaBlackWidow: (["TarantulaHelmetBlackWidow.webp", "ChainmailChestplate.webp", "LeatherLeggings.png", "IronBoots.webp"], ["", "", Color.Tarantula.value[1], ""]),
    ArmorType.WardenHelmetTrueWarden: (["WardenHelmetTrueWarden.webp", *baseArmorSet], ["", *([Color.TentacleDye.value[1]] * 3)]),
    ArmorType.SentinelWarden: (["WardenHelmetSentinel.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.SentinelWardenTeal: (["WardenHelmetSentinelTeal.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.SentinelWardenPurple: (["WardenHelmetSentinelPurple.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.SentinelWardenPink: (["WardenHelmetSentinelPink.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.SentinelWardenOrange: (["WardenHelmetSentinelOrange.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.SentinelWardenMaroon: (["WardenHelmetSentinelMaroon.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.SentinelWardenGreen: (["WardenHelmetSentinelGreen.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.SentinelWardenBlack: (["WardenHelmetSentinelBlack.webp", *baseArmorSet], ["", *([Color.Reaper.value[1]] * 3)]),
    ArmorType.Divan: (["DivanHelmet.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivan: (["GemstoneDivanHelmet.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanSapphire: (["GemstoneDivanHelmetSapphire.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanAmethyst: (["GemstoneDivanHelmetAmethyst.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanJasper: (["GemstoneDivanHelmetJasper.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanRuby: (["GemstoneDivanHelmetRuby.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanTopaz: (["GemstoneDivanHelmetTopaz.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanJade: (["GemstoneDivanHelmetJade.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanOpal: (["GemstoneDivanHelmetOpal.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanCitrine: (["GemstoneDivanHelmetCitrine.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanPeridot: (["GemstoneDivanHelmetPeridot.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanAquamarine: (["GemstoneDivanHelmetAquamarine.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.GemstoneDivanOnyx: (["GemstoneDivanHelmetOnyx.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.WitherGoggles: (["WitherGogglesHelmet.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.WitherGogglesCorrupt: (["WitherGogglesHelmetCorrupt.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.WitherGogglesCelestial: (["WitherGogglesHelmetCelestial.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.WitherGogglesCyberpunk: (["a_WitherGogglesHelmetCyberpunk.webp", *baseArmorSet], ["", Color.StormChestplate.value[1], Color.StormLeggings.value[1], Color.StormBoots.value[1]]),
    ArmorType.Diver: (["DiverHelmet.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.DiverHelmetPuffer: (["DiverHelmetPuffer.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
    ArmorType.DiverHelmetFrozen: (["DiverHelmetFrozen.webp", "GoldChestplate.webp", "GoldLeggings.webp", "GoldBoots.webp"], ["", "", "", ""]),
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
    ArmorType.GodAngler: (["AnglerHelmet.webp", *baseArmorSet], ["", "4F3B49", "595536", "461E3A"]),
    ArmorType.BuildersClay: (["BuildersClayHelmet.webp", *baseArmorSet], ["", *([Color.NecronDye.value[1]] * 3)]),

    ArmorType.Mineral: (["MineralHelmet.webp", *baseArmorSet], ["", *([Color.Mineral.value[1]] * 3)]),
    ArmorType.DiamondNecron: (["DiamondNecronHelmet.webp", *baseArmorSet], ["", *([Color.AquamarineDye.value[1]] * 3)]),
    ArmorType.DiamondNecronKnight: (["KnightDiamondNecronHelmet.webp", *baseArmorSet], ["", *([Color.TrueBlack.value[1]] * 3)]),

    ArmorType.MendingCrown: (["MendingCrownHelmet.webp", *baseArmorSet], ["", *([Color.MangoDye.value[1]] * 3)]),
    ArmorType.CaduceusMendingCrown: (["CaduceusMendingCrownHelmet.webp", *baseArmorSet], ["", *([Color.MangoDye.value[1]] * 3)]),
    ArmorType.CaduceusMendingCrownBlue: (["CaduceusMendingCrownHelmetBlue.webp", *baseArmorSet], ["", *([Color.MangoDye.value[1]] * 3)]),
    ArmorType.CaduceusMendingCrownGreen: (["CaduceusMendingCrownHelmetGreen.webp", *baseArmorSet], ["", *([Color.MangoDye.value[1]] * 3)]),
    ArmorType.CaduceusMendingCrownPurple: (["CaduceusMendingCrownHelmetPurple.webp", *baseArmorSet], ["", *([Color.MangoDye.value[1]] * 3)]),
    ArmorType.CaduceusMendingCrownRed: (["CaduceusMendingCrownHelmetRed.webp", *baseArmorSet], ["", *([Color.MangoDye.value[1]] * 3)]),

    ArmorType.Fermento: (["FermentoHelmet.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoLeaf: (["FermentoHelmetLeaf.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoBloom: (["FermentoHelmetBloom.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactus: (["FermentoHelmetCactus.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactusBlack: (["FermentoHelmetCactusBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactusBlue: (["FermentoHelmetCactusBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactusGreen: (["FermentoHelmetCactusGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactusOrange: (["FermentoHelmetCactusOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactusPurple: (["FermentoHelmetCactusPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactusRed: (["FermentoHelmetCactusRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactusWhite: (["FermentoHelmetCactusWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCactusYellow: (["FermentoHelmetCactusYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrot: (["FermentoHelmetCarrot.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrotBlack: (["FermentoHelmetCarrotBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrotBlue: (["FermentoHelmetCarrotBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrotGreen: (["FermentoHelmetCarrotGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrotOrange: (["FermentoHelmetCarrotOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrotPurple: (["FermentoHelmetCarrotPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrotRed: (["FermentoHelmetCarrotRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrotWhite: (["FermentoHelmetCarrotWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCarrotYellow: (["FermentoHelmetCarrotYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoa: (["FermentoHelmetCocoa.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoaBlack: (["FermentoHelmetCocoaBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoaBlue: (["FermentoHelmetCocoaBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoaGreen: (["FermentoHelmetCocoaGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoaOrange: (["FermentoHelmetCocoaOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoaPurple: (["FermentoHelmetCocoaPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoaRed: (["FermentoHelmetCocoaRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoaWhite: (["FermentoHelmetCocoaWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoCocoaYellow: (["FermentoHelmetCocoaYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroom: (["FermentoHelmetMushroom.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroomBlack: (["FermentoHelmetMushroomBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroomBlue: (["FermentoHelmetMushroomBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroomGreen: (["FermentoHelmetMushroomGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroomOrange: (["FermentoHelmetMushroomOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroomPurple: (["FermentoHelmetMushroomPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroomRed: (["FermentoHelmetMushroomRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroomWhite: (["FermentoHelmetMushroomWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMushroomYellow: (["FermentoHelmetMushroomYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwart: (["FermentoHelmetNetherwart.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwartBlack: (["FermentoHelmetNetherwartBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwartBlue: (["FermentoHelmetNetherwartBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwartGreen: (["FermentoHelmetNetherwartGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwartOrange: (["FermentoHelmetNetherwartOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwartPurple: (["FermentoHelmetNetherwartPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwartRed: (["FermentoHelmetNetherwartRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwartWhite: (["FermentoHelmetNetherwartWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoNetherwartYellow: (["FermentoHelmetNetherwartYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotato: (["FermentoHelmetPotato.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotatoBlack: (["FermentoHelmetPotatoBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotatoBlue: (["FermentoHelmetPotatoBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotatoGreen: (["FermentoHelmetPotatoGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotatoOrange: (["FermentoHelmetPotatoOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotatoPurple: (["FermentoHelmetPotatoPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotatoRed: (["FermentoHelmetPotatoRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotatoWhite: (["FermentoHelmetPotatoWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPotatoYellow: (["FermentoHelmetPotatoYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkin: (["FermentoHelmetPumpkin.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkinBlack: (["FermentoHelmetPumpkinBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkinBlue: (["FermentoHelmetPumpkinBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkinGreen: (["FermentoHelmetPumpkinGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkinOrange: (["FermentoHelmetPumpkinOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkinPurple: (["FermentoHelmetPumpkinPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkinRed: (["FermentoHelmetPumpkinRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkinWhite: (["FermentoHelmetPumpkinWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoPumpkinYellow: (["FermentoHelmetPumpkinYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCane: (["FermentoHelmetSugarCane.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCaneBlack: (["FermentoHelmetSugarCaneBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCaneBlue: (["FermentoHelmetSugarCaneBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCaneGreen: (["FermentoHelmetSugarCaneGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCaneOrange: (["FermentoHelmetSugarCaneOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCanePurple: (["FermentoHelmetSugarCanePurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCaneRed: (["FermentoHelmetSugarCaneRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCaneWhite: (["FermentoHelmetSugarCaneWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoSugarCaneYellow: (["FermentoHelmetSugarCaneYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelon: (["FermentoHelmetMelon.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelonBlack: (["FermentoHelmetMelonBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelonBlue: (["FermentoHelmetMelonBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelonGreen: (["FermentoHelmetMelonGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelonOrange: (["FermentoHelmetMelonOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelonPurple: (["FermentoHelmetMelonPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelonRed: (["FermentoHelmetMelonRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelonWhite: (["FermentoHelmetMelonWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoMelonYellow: (["FermentoHelmetMelonYellow.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheat: (["FermentoHelmetWheat.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheatBlack: (["FermentoHelmetWheatBlack.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheatBlue: (["FermentoHelmetWheatBlue.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheatGreen: (["FermentoHelmetWheatGreen.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheatOrange: (["FermentoHelmetWheatOrange.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheatPurple: (["FermentoHelmetWheatPurple.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheatRed: (["FermentoHelmetWheatRed.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheatWhite: (["FermentoHelmetWheatWhite.webp", *baseArmorSet], fermentoArmorColor),
    ArmorType.FermentoWheatYellow: (["FermentoHelmetWheatYellow.webp", *baseArmorSet], fermentoArmorColor),

    ArmorType.Crimson: (["CrimsonHelmet.webp", *baseArmorSet], ["", Color.CrimsonChestplate.value[1], Color.CrimsonLeggings.value[1], Color.CrimsonBoots.value[1]]),
    ArmorType.Terror: (["TerrorHelmet.webp", *baseArmorSet], ["", Color.TerrorChestplate.value[1], Color.TerrorLeggings.value[1], Color.TerrorBoots.value[1]]),
    ArmorType.Aurora: (["AuroraHelmet.webp", *baseArmorSet], ["", Color.AuroraChestplate.value[1], Color.AuroraLeggings.value[1], Color.AuroraBoots.value[1]]),
    ArmorType.Fervor: (["FervorHelmet.webp", *baseArmorSet], ["", Color.FervorChestplate.value[1], Color.FervorLeggings.value[1], Color.FervorBoots.value[1]]),
    ArmorType.Hollow: (["HollowHelmet.webp", *baseArmorSet], ["", Color.HollowChestplate.value[1], Color.HollowLeggings.value[1], Color.HollowBoots.value[1]]),
    ArmorType.FinalDestination: (["FinalDestinationHelmet.webp", *baseArmorSet], ["", Color.FinalDestinationChestplate.value[1], Color.FinalDestinationLeggings.value[1], Color.FinalDestinationBoots.value[1]]),
    ArmorType.Thunder: (["ThunderHelmet.webp", *baseArmorSet], ["", *([Color.Thunder.value[1]] * 3)]),
    ArmorType.Melon: (["MelonHelmet.webp", *baseArmorSet], ["", *([Color.Melon.value[1]] * 3)]),
    ArmorType.Cropie: (["CropieHelmet.webp", *baseArmorSet], ["", Color.CropieChestplate.value[1], Color.CropieLeggings.value[1], Color.CropieBoots.value[1]]),
    ArmorType.Squash: (["SquashHelmet.webp", *baseArmorSet], ["", Color.SquashChestplate.value[1], Color.SquashLeggings.value[1], Color.SquashBoots.value[1]]),
}