import random

temp = False
STATS = ["str", "con", "dex", "int", "wis", "cha"]

print("Overhaul - a dnd overhauled by Sorgham Snowball and Blazeraiders")
print("Character Creator:")
print("""Choose a difficulty:
      Easy[e] | Normal[n] | Hard[h]""")

# difficulty
temp = True
while temp == True:
    difficulty = input("\nChoose difficulty: ")
    difficulty = difficulty.lower()
    difficulties = ["e", "n", "h"]
    for i in range(len(difficulties)):
        if difficulty == difficulties[i]:
            temp = False

# Name
temp = True
while temp == True:
    character_name = input("\nCreate a character name: ")
    if len(character_name) < 50:
        temp = False

# Race
temp = True
while temp == True:
    character_race = input("\nCreate a character race: ")
    if len(character_race) < 25:
        temp = False

# Race buff
temp = True
while temp == True:
    character_race_buff = input("""\nChoose a stat buff relevant to that race from the following options:
                                - Str(ength)
                                - con(stitution)
                                - dex(terity)
                                - int(eligence)
                                - wis(dom)
                                - cha(risma)
                                """)
    character_race_buff = character_race_buff.lower()
    for i in range(len(STATS)):
        if character_race_buff == STATS[i]:
            temp = False

# Race
temp = True
while temp == True:
    character_class = input("\nCreate a character class: ")
    if len(character_class) < 25:
        temp = False

# Race buff
temp = True
while temp == True:
    character_class_stat = input("""\nChoose a main stat relevant to that class from the following options:
                                 - Str(ength)
                                 - con(stitution)
                                 - dex(terity)
                                 - int(eligence)
                                 - wis(dom)
                                 - cha(risma)
                                 """)
    character_class_stat = character_class_stat.lower()
    for i in range(len(STATS)):
        if character_class_stat == STATS[i]:
            temp = False

# Stat generation
if difficulty == "e":
    character_stats = {"str" : random.randint(-1, 4),
                   "con" : random.randint(-1, 4),
                   "dex" : random.randint(-1, 4),
                   "int" : random.randint(-1, 4),
                   "wis" : random.randint(-1, 4),
                   "cha" : random.randint(-1, 4),}
    for i in range(len(STATS)):
        if character_race_buff == STATS[i]:
            character_stats[f"{character_race_buff.lower()}"] += 5
elif difficulty == "n":
    character_stats = {"str" : random.randint(-2, 3),
                   "con" : random.randint(-2, 3),
                   "dex" : random.randint(-2, 3),
                   "int" : random.randint(-2, 3),
                   "wis" : random.randint(-2, 3),
                   "cha" : random.randint(-2, 3),}
    for i in range(len(STATS)):
        if character_race_buff == STATS[i]:
            character_stats[f"{character_race_buff.lower()}"] += 3
elif difficulty == "h":
    character_stats = {"str" : random.randint(-3, 2),
                   "con" : random.randint(-3, 2),
                   "dex" : random.randint(-3, 2),
                   "int" : random.randint(-3, 2),
                   "wis" : random.randint(-3, 2),
                   "cha" : random.randint(-3, 2),}
    for i in range(len(STATS)):
        if character_race_buff == STATS[i]:
            character_stats[f"{character_race_buff.lower()}"] += 1

#Extras
lvl = 1
exp_needed = lvl * 10
exp = 0
total_hp = 100 + (character_stats["con"] * 10)
hp = total_hp
total_stm = 100 + (character_stats["con"] * 10) + (character_stats["dex"] * 10)
stm = total_stm
total_mana = 100 + (character_stats["int"] * 10) + (character_stats["wis"] * 10)
mana = total_mana

print(f"""Name: {character_name}
Race: {character_race}(+{character_race_buff})
class: {character_class}({character_class_stat})
    
Lvl: {lvl}
Exp: {exp}/{exp_needed}
    
HP: {hp}/{total_hp}
Stm: {stm}/{total_stm}
Mana: {mana}/{total_mana}

Stats:
    str: {character_stats["str"]}   int: {character_stats["int"]}
    con: {character_stats["con"]}   wis: {character_stats["wis"]}
    dex: {character_stats["dex"]}   cha: {character_stats["cha"]}
    """)

with open(f"{character_name}.ocs", "w") as ocs:
    ocs.writelines(f"""Name: {character_name}
Race: {character_race}(+{character_race_buff})
class: {character_class}({character_class_stat})
    
Lvl: {lvl}
Exp: {exp}/{exp_needed}
    
HP: {hp}/{total_hp}
Stm: {stm}/{total_stm}
Mana: {mana}/{total_mana}

Stats:
    str: {character_stats["str"]}   int: {character_stats["int"]}
    con: {character_stats["con"]}   wis: {character_stats["wis"]}
    dex: {character_stats["dex"]}   cha: {character_stats["cha"]}
    """)