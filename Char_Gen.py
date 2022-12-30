import NPC_SPAWN
import NPC_TYPES




# Charicter Description Generation

need a format for npc descritions so that i can mad lib them. some can be mad libbed and some need to be procedural generated, like a 5 part description with each section that has descriptions that can fit in and out. think description roulet.

describe the mans/womans armour and or clothes,

describe his/her weapon and any outward hung gear from his inventory, some inventory should trigger a description prompt. like a roll of rope.

describe his/her hair and hair cut,

describe his/her over aura,

describe how he/she carries him self, confident, with purpous, shifty, on edge...etc.

describe his/her shoes if you are roll a win for perception. "no one looks at a mans shoes."




----------------------------------------------------------------------------------------------------------------------------------------------------

# Name generation


# courtesy of chatgpt

def NPC_random_name_gen(gender):
	if gender == 'male':
		first = random.choice(male_names_list)
    elif gender == 'female':
		first = random.choice(female_names_list)
    else:
		first = random.choice(male_names + female_names)
	# catch all
    last = random.choice(family_names_list)
    return f'{first} {last}'


-------------------------------------------------------------------------------------------------------------------------------------------------------

# Stat generation

# courtesy of chatgpt

def generate_stats():
  stats = {}
  stats['Strength'] = random.randint(1, 20)
  stats['Dexterity'] = random.randint(1, 20)
  stats['Constitution'] = random.randint(1, 20)
  stats['Intelligence'] = random.randint(1, 20)
  stats['Wisdom'] = random.randint(1, 20)
  stats['Charisma'] = random.randint(1, 20)
  return stats
  
  
