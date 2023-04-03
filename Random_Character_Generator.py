import random
def random_stats():
	stats = []
	while len(stats) < 6:
		one_d6=list(range(1,7))
		r1=random.choice(one_d6)
		r2=random.choice(one_d6)
		r3=random.choice(one_d6)
		r4=random.choice(one_d6)
		#get results put into the totals list
		totals=[r1,r2,r3,r4]
		#drop the lowest number from the list and add the remainder
		totals.remove(min(totals))
		result=sum(totals)
		stats.append(result)
		stats.sort()
	return stats

          
stats = random_stats()





classes=['barbarian','bard','cleric','druid','monk','paladin','sorcerer','ranger','wizard','warlock','rogue','fighter']
the_class=random.choice(classes)

races=['human','dwarf','elf','gnome','goblin','minotaur','vedalkin','teifling','halfling']

if the_class=='barbarian':
	print(random.choice(races).title(),'\nBarbarian\nSTR:',stats[5],
	'\nDEX:',stats[3],
	'\nCON:',stats[4],
	'\nINT:',stats[0],
	'\nWIS:',stats[1],
	'\nCHA:',stats[2])	
if the_class=='bard':
	print(random.choice(races).title(),'\nBard\nSTR:',stats[2],
	'\nDEX:',stats[4],
	'\nCON:',stats[1],
	'\nINT:',stats[0],
	'\nWIS:',stats[3],
	'\nCHA:',stats[5])	
if the_class=='cleric':
	print(random.choice(races).title(),'\nCleric\nSTR:',stats[3],
	'\nDEX:',stats[0],
	'\nCON:',stats[4],
	'\nINT:',stats[1],
	'\nWIS:',stats[5],
	'\nCHA:',stats[2])	
if the_class=='druid':
	print(random.choice(races).title(),'\nDruid\nSTR:',stats[4],
	'\nDEX:',stats[1],
	'\nCON:',stats[3],
	'\nINT:',stats[2],
	'\nWIS:',stats[5],
	'\nCHA:',stats[0])	
if the_class=='monk':
	print(random.choice(races).title(),'\nMonk\nSTR:',stats[2],
	'\nDEX:',stats[5],
	'\nCON:',stats[4],
	'\nINT:',stats[1],
	'\nWIS:',stats[3],
	'\nCHA:',stats[0])	
if the_class=='paladin':
	print(random.choice(races).title(),'\nPaladin\nSTR:',stats[4],
	'\nDEX:',stats[0],
	'\nCON:',stats[5],
	'\nINT:',stats[1],
	'\nWIS:',stats[2],
	'\nCHA:',stats[3])	
if the_class=='sorcerer':
	print(random.choice(races).title(),'\nSorcerer\nSTR:',stats[0],
	'\nDEX:',stats[4],
	'\nCON:',stats[2],
	'\nINT:',stats[3],
	'\nWIS:',stats[1],
	'\nCHA:',stats[5])
if the_class=='ranger':
	print(random.choice(races).title(),'\nRanger\nSTR:',stats[3],
	'\nDEX:',stats[5],
	'\nCON:',stats[2],
	'\nINT:',stats[1],
	'\nWIS:',stats[4],
	'\nCHA:',stats[0])
if the_class=='wizard':
	print(random.choice(races).title(),'\nWizard\nSTR:',stats[0],
	'\nDEX:',stats[3],
	'\nCON:',stats[4],
	'\nINT:',stats[5],
	'\nWIS:',stats[2],
	'\nCHA:',stats[1])	
if the_class=='warlock':
	print(random.choice(races).title(),'\nWarlock\nSTR:',stats[0],
	'\nDEX:',stats[4],
	'\nCON:',stats[3],
	'\nINT:',stats[1],
	'\nWIS:',stats[2],
	'\nCHA:',stats[5])	
if the_class=='rogue':
	print(random.choice(races).title(),'\nRogue\nSTR:',stats[0],
	'\nDEX:',stats[5],
	'\nCON:',stats[2],
	'\nINT:',stats[1],
	'\nWIS:',stats[4],
	'\nCHA:',stats[3])	
if the_class=='fighter':
	print(random.choice(races).title(),'\nFighter\nSTR:',stats[5],
	'\nDEX:',stats[3],
	'\nCON:',stats[4],
	'\nINT:',stats[0],
	'\nWIS:',stats[1],
	'\nCHA:',stats[2])	
