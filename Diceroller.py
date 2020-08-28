import sys
import argparse
import random
from collections import Counter
print(len(sys.argv))

def valid_dice(dice_string):
	'''Check for valid dice request'''
	try:
		[num_dice,dice_size]=dice_string.split("d")
	except:
		print(f'{dice_string} is an invalid request')

class dice_engine:
	def __init__(self):
		self.dice_ls=[]
		self.roll_history=[]
		self.roll_summary={}

	def add_die(self,dice_string):
		try:
			[num_dice,dice_size]=dice_string.split("d")
		except:
			print(f'{dice_string} is an invalid request')
		self.dice_ls.append((int(num_dice),int(dice_size)))

	def roll(self):
		_roll_summary={}
		for (j,k) in self.dice_ls:
			dice_rolls=[]
			for l in range(j):
				dice_rolls.append(random.randrange(1,k))
			_dice_summary={}
			_dice_summary[f'{j}d{k}']={}
			_dice_summary[f'{j}d{k}']['total']=sum(dice_rolls)
			print(f'sum {_dice_summary[f'{j}d{k}']['total']}')
			_dice_summary[f'{j}d{k}']['counter']=Counter(dice_rolls)
			_dice_summary[f'{j}d{k}']['dice_summ']=dice_rolls
			_roll_summary[f'{j}d{k}']=_dice_summary
		_roll_summary['total']=0
		_roll_summary['counter']=Counter()
		for key in _roll_summary.keys():
			_roll_summary['total']+=_roll_summary[key][key]['total']
			_roll_summary['counter'].update(_roll_summary[key][key]['counter'])
		self.roll_history.append(_roll_summary)
		print(self.roll_history[-1])




dengine = dice_engine()
dengine.add_die("20d6")
dengine.roll()



'''
return dice 
roll_summary - a summary of all the different dices that roll
roll_history, list of roll_summaries
'''