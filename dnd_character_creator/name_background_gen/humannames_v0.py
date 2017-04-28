from random import *

nm1 = ["", "", "b", "bh", "f", "h", "j", "kh", "m", "n", "nh", "r", "rh", "s", "z"]
nm2 = ["a", "e", "u", "a", "e", "u", "a", "e", "u", "i", "ei"]
nm3 = ["b", "d", "hm", "hn", "hl", "kh", "l", "m", "rd", "r", "s", "sh", "z"]
nm4 = ["d", "m", "n", "r"]
nm5 = ["", "", "c", "f", "h", "j", "m", "n", "r", "s", "sh", "y", "z"]
nm6 = ["a", "e", "u", "a", "e", "u", "o", "o", "i", "i", "ei"]
nm7 = ["d", "f", "hn", "hl", "hm", "hr", "l", "m", "n", "p", "r", "s", "sh", "sm", "sn", "t", "v", "z"]
nm8 = ["h", "l"]
nm9 = ["b", "bh", "c", "d", "dh", "h", "j", "kh", "m", "n", "p", "r", "rh", "sh", "z"]
nm10 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "a", "a", "ei"]
nm11 = ["d", "h", "hr", "hl", "k", "kh", "l", "m", "mm", "n", "nn", "ss", "st", "sh"]
nm12 = ["", "", "", "", "", "d", "l", "m", "n", "r"]
nm13 = ["", "b", "br", "d", "g", "gr", "h", "m", "n", "r", "st", "t", "v"]
nm14 = ["a", "e", "i", "o", "u"]
nm15 = ["", "br", "cr", "gr", "kv", "kr", "l", "ll", "ld", "lv", "nd", "ng", "nk", "nv", "rd", "rg", "rk", "rst", "rv", "v"]
nm16 = ["", "", "", "d", "dd", "g", "l", "lm", "m", "n", "r", "rk", "rn"]
nm17 = ["", "c", "j", "jh", "k", "l", "m", "n", "r", "s", "sh", "t"]
nm18 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "ee", "ai", "ei", "ie"]
nm19 = ["ch", "dr", "l", "ll", "lr", "ldr", "ls", "lz", "n", "ndr", "rl", "r", "rr", "rv", "ss", "sr", "sv", "w", "z", "zz", "zn"]
nm20 = ["", "", "", "", "h", "l", "ll", "n"]
nm21 = ["Axe", "Glow", "Blade", "Blood", "Bone", "Cloud", "Crag", "Crest", "Doom", "Dream", "Coven", "Elf", "Fern", "Feather", "Fire", "Fist", "Flame", "Forest", "Hammer", "Heart", "Hell", "Leaf",
        "Light", "Moon", "Rage", "River", "Rock", "Shade", "Shadow", "Shield", "Snow", "Spirit", "Star", "Steel", "Stone", "Swift", "Tree", "Whisper", "Wind", "Wolf", "Wood", "Gloom", "Glory", "Orb",
        "Ash", "Blaze", "Amber", "Autumn", "Barley", "Battle", "Bear", "Black", "Blue", "Boulder", "Bright", "Bronze", "Burning", "Cask", "Chest", "Cinder", "Clan", "Claw", "Clear", "Cliff", "Cold",
        "Common", "Crystal", "Dark", "Dawn", "Day", "Dead", "Death", "Deep", "Dew", "Dirge", "Distant", "Down", "Dragon", "Dusk", "Dust", "Eagle", "Earth", "Ember", "Even", "Far", "Flat", "Flint",
        "Fog", "Fore", "Four", "Free", "Frost", "Frozen", "Full", "Fuse", "Gold", "Horse", "Gore", "Grand", "Gray", "Grass", "Great", "Green", "Grizzly", "Hallow", "Hallowed", "Hard", "Hawk", "Haze",
        "Heavy", "Haven", "High", "Hill", "Holy", "Honor", "Forest", "Humble", "Hydra", "Ice", "Iron", "Keen", "Laughing", "Lightning", "Lion", "Lone", "Long", "Low", "Luna", "Marble", "Meadow",
        "Mild", "Mirth", "Mist", "Molten", "Monster", "Morning", "Moss", "Mountain", "Moon", "Mourn", "Mourning", "Night", "Noble", "Nose", "Oat", "Ocean", "Pale", "Peace", "Phoenix", "Pine", "Plain",
        "Pride", "Proud", "Pyre", "Rain", "Rapid", "Raven", "Red", "Regal", "Rich", "Rose", "Rough", "Rumble", "Rune", "Sacred", "Sage", "Saur", "Sea", "Serpent", "Sharp", "Silent", "Silver",
        "Simple", "Single", "Skull", "Sky", "Slate", "Smart", "Snake", "Soft", "Solid", "Spider", "Spring", "Stag", "Star", "Stern", "Still", "Storm", "Stout", "Strong", "Summer", "Sun", "Tall",
        "Three", "Thunder", "Titan", "True", "Truth", "Marsh", "Tusk", "Twilight", "Two", "Void", "War", "Wheat", "Whit", "White", "Wild", "Winter", "Wise", "Wyvern", "Young", "Alpen", "Crest",
        "Crow", "Fallen", "Farrow", "Haven", "Master", "Nether", "Nickle", "Raven", "River", "Stone", "Tarren", "Terra", "Water", "Willow", "Wooden"]
nm22 = ["axe", "glow", "beam", "blade", "blood", "bone", "cloud", "dane", "crag", "crest", "doom", "dream", "feather", "fire", "fist", "flame", "forest", "hammer", "heart", "hell", "leaf", "light",
        "moon", "rage", "river", "rock", "shade", "claw", "shadow", "shield", "snow", "spirit", "star", "steel", "stone", "swift", "tree", "whisper", "wind", "wolf", "wood", "gloom", "glory", "orb",
        "ash", "blaze", "arm", "arrow", "bane", "bash", "basher", "beard", "belly", "bend", "bender", "binder", "bleeder", "blight", "bloom", "blossom", "blower", "glade", "bluff", "bough", "bow",
        "brace", "braid", "branch", "brand", "breaker", "breath", "breeze", "brew", "bringer", "brook", "brow", "caller", "chaser", "reaper", "chewer", "cleaver", "creek", "crusher", "cut", "cutter",
        "dancer", "dew", "down", "draft", "dreamer", "drifter", "dust", "eye", "eyes", "fall", "fang", "flare", "flaw", "flayer", "flow", "follower", "flower", "force", "forge", "fury", "gaze",
        "gazer", "gem", "gleam", "glide", "grain", "grip", "grove", "guard", "gust", "hair", "hand", "helm", "hide", "horn", "hunter", "jumper", "keep", "keeper", "killer", "lance", "lash", "less",
        "mane", "mantle", "mark", "maul", "maw", "might", "more", "mourn", "oak", "ore", "peak", "pelt", "pike", "punch", "reaver", "rider", "ridge", "ripper", "roar", "run", "runner", "scar",
        "scream", "scribe", "seeker", "shaper", "shard", "shot", "shout", "singer", "sky", "slayer", "snarl", "snout", "soar", "song", "sorrow", "spark", "spear", "spell", "spire", "splitter",
        "sprinter", "stalker", "steam", "stream", "strength", "stride", "strider", "strike", "striker", "sun", "surge", "sword", "sworn", "tail", "taker", "talon", "thorn", "tide", "toe", "track",
        "trap", "trapper", "vale", "valor", "vigor", "walker", "ward", "watcher", "water", "weaver", "whirl", "whisk", "winds", "wing", "woods", "wound", "brooke", "fall", "fallow", "horn", "root",
        "shine", "swallow", "thorne", "willow", "wood"]
nm23 = ["", "", "b", "br", "f", "g", "gl", "gr", "h", "k", "m", "n", "p", "r", "s", "v"]
nm24 = ["a", "e", "i", "o"]
nm25 = ["b", "br", "d", "dr", "dg", "g", "gr", "r", "rg", "rd", "rv", "s", "v", "z"]
nm26 = ["f", "l", "m", "n", "r"]
nm27 = ["c", "ch", "h", "k", "l", "m", "n", "r", "s", "t", "v", "z"]
nm28 = ["h", "hn", "hr", "l", "lm", "lr", "ln", "n", "nn", "r", "rn", "rl", "rm", "t", "th", "thr", "z"]
nm29 = ["", "", "", "", "", "", "h", "l", "n", "s"]
nm30 = ["b", "ch", "d", "gr", "gl", "k", "m", "n", "r", "s", "sh", "st", "v"]
nm31 = ["a", "e", "i", "o", "u"]
nm32 = ["d", "dr", "k", "kr", "kn", "l", "m", "n", "r", "rg", "rk", "rn", "rd", "v", "vr", "z"]
nm33 = ["dz", "g", "n", "rsk", "sk", "tsk", "v", "z"]
nm34 = ["", "", "", "bl", "br", "fr", "g", "gr", "l", "m", "r", "st", "str", "t", "tr", "v", "z"]
nm35 = ["a", "e", "o", "u"]
nm36 = ["ck", "dr", "dv", "gr", "gn", "lc", "ld", "lv", "lb", "m", "nn", "nd", "nv", "rd", "rc", "rk", "rb"]
nm37 = ["m", "n", "r", "rth", "th"]
nm38 = ["", "", "b", "c", "h", "k", "l", "m", "n", "r", "s", "v", "w", "z"]
nm39 = ["fn", "fl", "fr", "g", "l", "lg", "lr", "m", "n", "r", "rh", "sh", "str", "th", "thr", "v", "vr"]
nm40 = ["", "", "", "", "y"]
nm43 = ["b", "d", "g", "h", "j", "k", "l", "m", "n", "r", "s", "t", "th", "v", "z"]
nm44 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "io", "ao", "eo", "eu", "ue"]
nm45 = ["d-k", "d-v", "k-d", "k-v", "k-m", "k-r", "m-k", "m-z", "m-v", "n-v", "n-z", "n-d", "r-k", "r-v", "r-z", "t-k", "r-d", "h-k", "h-z", "-k", "-d", "-m", "-n", "-v", "-z", "-t", "-r", "ch", "d",
        "h", "hp", "hk", "hv", "j", "k", "m", "n", "r", "rh", "t", "th", "v", "z", "ch", "d", "h", "hp", "hk", "hv", "j", "k", "m", "n", "r", "rh", "t", "th", "v", "z", "ch", "d", "h", "hp", "hk",
        "hv", "j", "k", "m", "n", "r", "rh", "t", "th", "v", "z"]
nm46 = ["", "", "d", "f", "h", "k", "n", "r", "s", "th", "z"]
nm47 = ["c", "ch", "f", "h", "k", "l", "m", "n", "r", "s", "t", "th", "v", "z"]
nm48 = ["ch", "f", "fr", "h", "l", "m", "n", "ph", "s", "sh", "r", "th", "z", "zr", "zh"]
nm49 = ["", "", "", "", "", "", "", "h", "s", "th"]
nm50 = ["b", "d", "f", "h", "j", "l", "m", "n", "r", "s", "v", "z"]
nm51 = ["a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "o", "u", "ue", "uu"]
nm52 = ["cr", "ch", "hp", "hk", "hr", "j", "kr", "kd", "l", "lr", "ldr", "lt", "ltr", "nd", "nsk", "nkh", "nth", "ndr", "nkr", "nz", "pr", "pv", "th", "thr", "v", "vr", "z", "zr", "zd"]
nm53 = ["b", "d", "ft", "fk", "hd", "hr", "hk", "k", "kt", "ld", "m", "t"]
nm54 = ["b", "br", "d", "dr", "f", "g", "j", "k", "m", "r", "s", "sh", "t", "vl", "z"]
nm55 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "oo", "ou", "au"]
nm56 = ["d", "dj", "j", "lm", "ld", "lv", "m", "mz", "mv", "n", "nz", "nd", "nr", "nd", "r", "rg", "rd", "rl", "rv", "rz", "sl", "sv", "sd", "th", "tv", "v", "z"]
nm57 = ["c", "d", "k", "r", "s", "sk", "t"]
nm58 = ["", "", "d", "f", "h", "l", "m", "n", "r", "s", "sh", "t", "th", "v", "y", "z"]
nm59 = ["a", "e", "i", "u"]
nm60 = ["ch", "dr", "dh", "f", "fr", "gr", "h", "ldr", "lm", "ln", "lv", "lr", "mm", "mz", "mv", "ndr", "nr", "r", "rr", "rr", "rv", "rs", "rl", "v", "vr", "v", "vl"]
nm61 = ["", "", "", "", "", "", "", "", "", "", "", "", "l", "n", "s", "sh", "th"]
nm62 = ["", "", "ch", "d", "g", "gr", "h", "m", "n", "r", "st", "t", "tr", "v", "vr", "z"]
nm63 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "ye", "ya"]
nm64 = ["b", "d", "dz", "g", "k", "ld", "lb", "lm", "lz", "m", "mr", "mz", "n", "nz", "ng", "nt", "r", "rg", "rn", "rk", "th", "tr", "tv", "v", "vr", "vz", "b", "d", "g", "k", "m", "n", "r", "v"]
nm65 = ["", "", "ch", "f", "h", "j", "l", "m", "q", "sh", "t", "th", "w", "z"]
nm66 = ["a", "i", "e", "o", "u", "ia", "ui", "io", "ie", "iu"]
nm67 = ["", "", "", "h", "m", "n", "ng", "p", "w", "y"]
nm68 = ["b", "c", "ch", "d", "j", "l", "m", "n", "p", "q", "sh", "t", "ts", "x", "y", "z"]
nm69 = ["ai", "ia", "ao", "ei", "iao", "ui", "ua", "ue"]
nm70 = ["", "", "", "c", "ch", "d", "h", "j", "k", "l", "m", "n", "p", "q", "s", "sh", "t", "w", "x", "y", "z"]
nm71 = ["a", "i", "u", "ai", "ia", "iao", "ue", "ei", "ie", "ua", "ao"]
nm72 = ["", "", "", "m", "n", "ng", "y"]
nm73 = ["", "", "ch", "cr", "d", "gr", "f", "fr", "h", "m", "p", "r", "s", "t", "v", "z"]
nm74 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "ai", "ie", "ue", "ea"]
nm75 = ["b", "br", "c", "dr", "l", "ld", "lb", "m", "mb", "n", "nr", "nt", "nch", "r", "rf", "rv", "rn", "rc", "rd", "rt", "st", "sc", "t", "v", "z"]
nm76 = ["", "", "l", "n", "r", "s", "z"]
nm77 = ["", "", "", "b", "d", "f", "j", "l", "m", "q", "s", "v"]
nm78 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "ui", "ua", "ai", "ia", "ie", "ei"]
nm79 = ["d", "l", "lm", "m", "n", "nc", "nd", "ndr", "nt", "nn", "r", "rt", "s", "t", "tt", "v"]
nm80 = ["", "", "b", "c", "d", "f", "g", "h", "j", "m", "p", "r", "s", "v", "z"]
nm81 = ["br", "c", "dr", "g", "h", "l", "lb", "ld", "m", "n", "nd", "nz", "r", "rn", "rg", "s", "sc", "sq", "st", "v", "z"]


def nameGen():
    i = randint(0, 16)
    if (i < 2):
        rnd = randint(0, len(nm9))
        rnd2 = randint(0, len(nm10))
        rnd3 = randint(0, len(nm11))
        rnd4 = randint(0, len(nm10))
        rnd5 = randint(0, len(nm12))
        lname = nm9[rnd] + nm10[rnd2] + nm11[rnd3] + nm10[rnd4] + nm12[rnd5]
    elif (i < 4):
        rnd = randint(0, len(nm21))
        rnd2 = randint(0, len(nm22))
        while (rnd == rnd2):
            rnd2 = randint(0, len(nm22))

        lname = nm21[rnd] + nm22[rnd2]
    elif (i < 6):
        rnd = randint(0, len(nm30))
        rnd2 = randint(0, len(nm31))
        rnd5 = randint(0, len(nm33))
        if (i == 4):
            lname = nm30[rnd] + nm31[rnd2] + nm33[rnd5]
        else:
            rnd3 = randint(0, len(nm32))
            rnd4 = randint(0, len(nm31))
            lname = nm30[rnd] + nm31[rnd2] + nm32[rnd3] + nm31[rnd4] + nm33[rnd5]

    elif (i < 8):
        rnd = randint(0, len(nm21))
        rnd2 = randint(0, len(nm22))
        while (rnd == rnd2):
            rnd2 = randint(0, len(nm22))

        lname = nm21[rnd] + nm22[rnd2]
    elif (i < 10):
        rnd = randint(0, len(nm50))
        rnd2 = randint(0, len(nm51))
        rnd3 = randint(0, len(nm52))
        rnd4 = randint(0, len(nm51))
        rnd5 = randint(0, len(nm53))
        if (i == 8):
            rnd6 = randint(0, len(nm52))
            rnd7 = randint(0, len(nm51))
            lname = nm50[rnd] + nm51[rnd2] + nm52[rnd3] + nm51[rnd4] + nm52[rnd6] + nm51[rnd7] + nm53[rnd5]
        else:
            lname = nm50[rnd] + nm51[rnd2] + nm52[rnd3] + nm51[rnd4] + nm53[rnd5]

    elif (i < 12):
        rnd = randint(0, len(nm62))
        rnd2 = randint(0, len(nm63))
        rnd3 = randint(0, len(nm64))
        rnd4 = randint(0, len(nm63))
        rnd5 = randint(0, len(nm64))
        rnd6 = randint(0, len(nm63))
        if (i == 10):
            rnd7 = randint(0, len(nm64))
            rnd8 = randint(0, len(nm63))
            lname = nm62[rnd] + nm63[rnd2] + nm64[rnd3] + nm63[rnd4] + nm64[rnd5] + nm63[rnd6] + nm64[rnd7] + nm63[rnd8]
        else:
            lname = nm62[rnd] + nm63[rnd2] + nm64[rnd3] + nm63[rnd4] + nm64[rnd5] + nm63[rnd6]

    elif (i < 14):
        rnd = randint(0, len(nm70))
        rnd2 = randint(0, len(nm71))
        rnd3 = randint(0, len(nm72))
        if (rnd3 < 3):
            while (rnd < 3):
                rnd = randint(0, len(nm70))

        lname = nm70[rnd] + nm71[rnd2] + nm72[rnd3]
    else:
        rnd = randint(0, len(nm80))
        rnd2 = randint(0, len(nm14))
        rnd3 = randint(0, len(nm81))
        rnd4 = randint(0, len(nm14))
        rnd6 = randint(0, len(nm81))
        rnd7 = randint(0, len(nm14))
        rnd5 = randint(0, len(nm82))
        lname = nm80[rnd] + nm14[rnd2] + nm81[rnd3] + nm14[rnd4] + nm81[rnd6] + nm14[rnd7] + nm82[rnd5]

    if (tp == 3):
        rnd = randint(0, len(nm83))
        names = nm83[rnd]
    elif (tp == 4):
        rnd = randint(0, len(nm84))
        names = nm84[rnd]

    elif (tp == 1):
        if (i < 2):
            rnd = randint(0, len(nm5))
            rnd2 = randint(0, len(nm6))
            rnd3 = randint(0, len(nm7))
            rnd4 = randint(0, len(nm6))
            rnd5 = randint(0, len(nm8))
            if (i == 0):
                rnd6 = randint(0, len(nm7))
                rnd7 = randint(0, len(nm6))
                names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm7[rnd6] + nm6[rnd7] + nm8[rnd5] + " " + lname
            else:
                names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5] + " " + lname

        elif (i < 4):
            rnd = randint(0, len(nm17))
            rnd2 = randint(0, len(nm18))
            rnd3 = randint(0, len(nm19))
            rnd4 = randint(0, len(nm18))
            rnd5 = randint(0, len(nm20))
            if (i == 2):
                rnd6 = randint(0, len(nm19))
                rnd7 = randint(0, len(nm18))
                names = nm17[rnd] + nm18[rnd2] + nm19[rnd3] + nm18[rnd4] + nm19[rnd6] + nm18[rnd7] + nm20[rnd5] + " " + lname
            else:
                names = nm17[rnd] + nm18[rnd2] + nm19[rnd3] + nm18[rnd4] + nm20[rnd5] + " " + lname

        elif (i < 6):
            rnd = randint(0, len(nm27))
            rnd2 = randint(0, len(nm24))
            rnd5 = randint(0, len(nm29))
            if (i == 4):
                rnd3 = randint(0, len(nm28))
                rnd4 = randint(0, len(nm24))
                names = nm27[rnd] + nm24[rnd2] + nm28[rnd3] + nm24[rnd4] + nm29[rnd5] + " " + lname
            else:
                names = nm27[rnd] + nm24[rnd2] + nm29[rnd5] + " " + lname

        elif (i < 8):
            rnd = randint(0, len(nm38))
            rnd2 = randint(0, len(nm24))
            rnd3 = randint(0, len(nm39))
            rnd4 = randint(0, len(nm24))
            rnd5 = randint(0, len(nm40))
            if (i == 6):
                rnd6 = randint(0, len(nm39))
                rnd7 = randint(0, len(nm24))
                names = nm38[rnd] + nm24[rnd2] + nm39[rnd3] + nm24[rnd4] + nm39[rnd6] + nm24[rnd7] + nm40[rnd5] + " " + lname
            else:
                names = nm38[rnd] + nm24[rnd2] + nm39[rnd3] + nm24[rnd4] + nm40[rnd5] + " " + lname

        elif (i < 10):
            rnd = randint(0, len(nm47))
            rnd2 = randint(0, len(nm14))
            rnd3 = randint(0, len(nm48))
            rnd4 = randint(0, len(nm14))
            rnd5 = randint(0, len(nm49))
            if (i == 8):
                rnd6 = randint(0, len(nm48))
                rnd7 = randint(0, len(nm14))
                names = nm47[rnd] + nm14[rnd2] + nm48[rnd3] + nm14[rnd4] + nm48[rnd6] + nm14[rnd7] + nm49[rnd5] + " " + lname
            else:
                names = nm47[rnd] + nm14[rnd2] + nm48[rnd3] + nm14[rnd4] + nm49[rnd5] + " " + lname

        elif (i < 12):
            rnd = randint(0, len(nm58))
            rnd2 = randint(0, len(nm59))
            rnd3 = randint(0, len(nm60))
            rnd4 = randint(0, len(nm59))
            rnd5 = randint(0, len(nm61))
            if (i == 10):
                rnd6 = randint(0, len(nm60))
                rnd7 = randint(0, len(nm59))
                names = nm58[rnd] + nm59[rnd2] + nm60[rnd3] + nm59[rnd4] + nm60[rnd6] + nm59[rnd7] + nm61[rnd5] + " " + lname
            else:
                names = nm58[rnd] + nm59[rnd2] + nm60[rnd3] + nm59[rnd4] + nm61[rnd5] + " " + lname

        elif (i < 14):
            rnd = randint(0, len(nm68))
            rnd2 = randint(0, len(nm69))
            names = nm68[rnd] + nm69[rnd2] + " " + lname
        else:
            rnd = randint(0, len(nm77))
            rnd2 = randint(0, len(nm78))
            rnd3 = randint(0, len(nm79))
            rnd4 = randint(0, len(nm77))
            if (i == 10):
                rnd6 = randint(0, len(nm79))
                rnd7 = randint(0, len(nm77))
                names = nm77[rnd] + nm78[rnd2] + nm79[rnd3] + nm77[rnd4] + nm79[rnd6] + nm77[rnd7] + " " + lname
            else:
                names = nm77[rnd] + nm78[rnd2] + nm79[rnd3] + nm77[rnd4] + " " + lname


    else:
        if (i < 2):
            rnd = randint(0, len(nm1))
            rnd2 = randint(0, len(nm2))
            rnd3 = randint(0, len(nm3))
            rnd4 = randint(0, len(nm2))
            rnd5 = randint(0, len(nm4))
            names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5] + " " + lname
        elif (i < 4):
            rnd = randint(0, len(nm13))
            rnd2 = randint(0, len(nm14))
            rnd3 = randint(0, len(nm15))
            rnd4 = randint(0, len(nm14))
            rnd5 = randint(0, len(nm16))
            if (rnd5 < 3):
                rnd3 = 0
            else:
                while (rnd3 == 0):
                    rnd3 = randint(0, len(nm15))

            names = nm13[rnd] + nm14[rnd2] + nm15[rnd3] + nm14[rnd4] + nm16[rnd5] + " " + lname
        elif (i < 6):
            rnd = randint(0, len(nm23))
            rnd2 = randint(0, len(nm24))
            rnd5 = randint(0, len(nm26))
            if (i == 4):
                rnd3 = randint(0, len(nm25))
                rnd4 = randint(0, len(nm24))
                names = nm23[rnd] + nm24[rnd2] + nm25[rnd3] + nm24[rnd4] + nm26[rnd5] + " " + lname
            else:
                names = nm23[rnd] + nm24[rnd2] + nm26[rnd5] + " " + lname

        elif (i < 8):
            rnd = randint(0, len(nm34))
            rnd2 = randint(0, len(nm35))
            rnd5 = randint(0, len(nm37))
            if (i == 6):
                rnd3 = randint(0, len(nm36))
                rnd4 = randint(0, len(nm35))
                names = nm34[rnd] + nm35[rnd2] + nm36[rnd3] + nm35[rnd4] + nm37[rnd5] + " " + lname
            else:
                names = nm34[rnd] + nm35[rnd2] + nm37[rnd5] + " " + lname

        elif (i < 10):
            rnd = randint(0, len(nm43))
            rnd2 = randint(0, len(nm44))
            rnd3 = randint(0, len(nm45))
            rnd4 = randint(0, len(nm44))
            rnd5 = randint(0, len(nm46))
            if (i == 8):
                rnd6 = randint(0, len(nm45))
                rnd7 = randint(0, len(nm44))
                names = nm43[rnd] + nm44[rnd2] + nm45[rnd3] + nm44[rnd4] + nm45[rnd6] + nm44[rnd7] + nm46[rnd5] + " " + lname
            else:
                names = nm43[rnd] + nm44[rnd2] + nm45[rnd3] + nm44[rnd4] + nm46[rnd5] + " " + lname

        elif (i < 12):
            rnd = randint(0, len(nm54))
            rnd2 = randint(0, len(nm55))
            rnd3 = randint(0, len(nm56))
            rnd4 = randint(0, len(nm55))
            rnd5 = randint(0, len(nm57))
            if (i == 10):
                rnd6 = randint(0, len(nm56))
                rnd7 = randint(0, len(nm55))
                names = nm54[rnd] + nm55[rnd2] + nm56[rnd3] + nm55[rnd4] + nm56[rnd6] + nm55[rnd7] + nm56[rnd5] + " " + lname
            else:
                names = nm54[rnd] + nm55[rnd2] + nm56[rnd3] + nm55[rnd4] + nm57[rnd5] + " " + lname

        elif (i < 14):
            rnd = randint(0, len(nm65))
            rnd2 = randint(0, len(nm66))
            rnd3 = randint(0, len(nm67))
            if (rnd3 < 3):
                while (rnd < 2):
                    rnd = randint(0, len(nm65))

            names = nm65[rnd] + nm66[rnd2] + nm67[rnd3] + " " + lname
        else:
            rnd = randint(0, len(nm73))
            rnd2 = randint(0, len(nm74))
            rnd3 = randint(0, len(nm75))
            rnd4 = randint(0, len(nm74))
            rnd5 = randint(0, len(nm76))
            if (i == 14):
                rnd6 = randint(0, len(nm75))
                rnd7 = randint(0, len(nm74))
                names = nm73[rnd] + nm74[rnd2] + nm75[rnd3] + nm74[rnd4] + nm75[rnd6] + nm74[rnd7] + nm76[rnd5] + " " + lname
            else:
                names = nm73[rnd] + nm74[rnd2] + nm75[rnd3] + nm74[rnd4] + nm76[rnd5] + " " + lname


print(names)
