import pandas as pd
import numpy as np
import random
import math

WEAPON_NOUNS = ["Sword","Longsword","Battleaxe", "Warhammer"]
TOOL_NOUNS = ["Plough","Axe","Hammer","Saw"]
TRINKET_NOUNS = ["Ring","Amulet","Pendant"]

WEAPON_ABSTRACTIONS = ["Power", "Wrath", "Flame", "Justice", "Rage", "Wounding", "Glory"]
TOOL_ABSTRACTIONS = ["Prosperity", "Plenty", "Industry", "Capability"]
TRINKET_ABSTRACTIONS = ["Hope", "Protection", "Melancholy", "Winter", "Joy", "Beauty", "Truth", "Abstraction"]

def get_random_nonweapon_color():
 return random.choice(["red"]*2+["blue"]*4+["green"]*3+["yellow"]*3)

def get_random_weapon_color():
 return random.choice(["red"]*4+["blue"]*3+["green"]*3+["yellow"]*3)


def get_blue_mana_amt():
 return random.choice([1,2,3,4,5,6,7,8,9,10])*random.choice([1,2,3,4,5,6])

def get_red_mana_amt():
 return random.choice([1,2,3,4,5,6])*random.choice([1,2,3,4])*random.choice([1,2,3,4])

def get_yellow_mana_amt():
 return 17+random.choice([1,2,3,4])

def get_green_mana_amt():
 return 2*random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def get_weapon_modifier(mana):
 return int(math.floor(mana/10))

def gen_random_weapon(color="random"):
 weapon={}
 
 if color=="random":
  color=get_random_nonweapon_color()
 weapon["color"]=color
 
 if color=="blue":
  weapon["mana"]=get_blue_mana_amt()
 if color=="red":
  weapon["mana"]=get_red_mana_amt()
 if color=="green":
  weapon["mana"]=get_green_mana_amt()
 if color=="yellow":
  weapon["mana"]=get_yellow_mana_amt()
 
 weapon["name"] = random.choice(WEAPON_NOUNS) + " of " + random.choice(WEAPON_ABSTRACTIONS)
 modifier=get_weapon_modifier(weapon["mana"])
 if modifier>0:
  weapon["name"]=weapon["name"]+" +"+ str(modifier)
 
 if color =="blue":
  weapon["reading"]=weapon["mana"]+random.choice([-1,1])
 else:
  weapon["reading"]=get_blue_mana_amt()
 
 weapon["price"]=20+20*modifier+random.choice([1,2,3,4,5,6])
 
 return weapon

def gen_random_tool(color="random"):
 tool={}
 
 if color=="random":
  color=get_random_nonweapon_color()
 tool["color"]=color
 
 if color=="blue":
  tool["mana"]=get_blue_mana_amt()
 if color=="red":
  tool["mana"]=get_red_mana_amt()
 if color=="green":
  tool["mana"]=get_green_mana_amt()
 if color=="yellow":
  tool["mana"]=get_yellow_mana_amt()
 
 tool["name"] = random.choice(TOOL_NOUNS) + " of " + random.choice(TOOL_ABSTRACTIONS)
 
 if random.choice([True,False]):
  tool["name"]=tool["name"]+" +"+ str(random.choice([1,2,3,4]))
 
 if color =="blue":
  tool["reading"]=tool["mana"]+random.choice([-1,1])
 else:
  tool["reading"]=get_blue_mana_amt()
 
 tool["price"]=30+random.choice([1,2,3,4])+random.choice([1,2,3,4])
 
 return tool

def gen_random_trinket(color="random"):
 trinket={}
 
 if color=="random":
  color=get_random_nonweapon_color()
 trinket["color"]=color
 
 if color=="blue":
  trinket["mana"]=get_blue_mana_amt()
 if color=="red":
  trinket["mana"]=get_red_mana_amt()
 if color=="green":
  trinket["mana"]=get_green_mana_amt()
 if color=="yellow":
  trinket["mana"]=get_yellow_mana_amt()
 
 trinket["name"] = random.choice(TRINKET_NOUNS) + " of " + random.choice(WEAPON_ABSTRACTIONS+TOOL_ABSTRACTIONS+TRINKET_ABSTRACTIONS)
 
 if random.choice([True,False]):
  trinket["name"]=trinket["name"]+" +"+ str(random.choice([1,2,3,4,5,6]))
 
 if color =="blue":
  trinket["reading"]=trinket["mana"]+random.choice([-1,1])+22
 else:
  trinket["reading"]=get_blue_mana_amt()+22
 
 trinket["price"]=30+random.choice([1,2,3,4,5,6,7,8,9,10])
 
 return trinket

def get_spread():
 spread=[]
 
 weapons=random.choice([4,5])
 tools=random.choice([2,3])
 trinkets=random.choice([5,6])
 for item in range(weapons):
  spread.append(gen_random_weapon())
 for item in range(tools):
  spread.append(gen_random_tool())
 for item in range(trinkets):
  spread.append(gen_random_trinket())
 
 return spread

def gen_the_dset(N=418):
 dictForDf = {}
 
 dictForDf["name"]=[]
 dictForDf["color"]=[]
 dictForDf["mana"]=[]
 dictForDf["reading"]=[]
 
 df=pd.DataFrame(dictForDf)
 
 for i in range(N):
  spread = get_spread()
  shoppingTripOver=False
  while not shoppingTripOver:
   choiceOne = random.choice(spread)
   choiceTwo = random.choice(spread)
   nonSharey = True
   for word in choiceOne["name"].split():
    if word in choiceTwo["name"].split() and word!="of":
     nonSharey=False
   if nonSharey:
    shoppingTripOver=True
  df = df.append(choiceOne, ignore_index=True)
  df = df.append(choiceTwo, ignore_index=True)
 
 return df
 

if __name__ == '__main__':
 spread = get_spread()
 for thingy in spread:
  print(thingy)
 theDf=gen_the_dset()
 print(theDf)
 theDf.to_csv("d_and_d_II.csv")
