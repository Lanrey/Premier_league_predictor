import pandas
import matplotlib.pyplot as plt

#load dataset
names = ['Team','Shots pg', 'Discipline', 'Possesion', 'PassSuccess', 'Aerials Won', 
        'Ratings', 'Team', 'OpenPlay','CounterAttack', 'SetPiece', 'Penalty', 'OwnGoal']

dataset = pandas.read_csv('/home/lanrey/htdocs/BPL_Pred/footyData.csv',names=names)
array = dataset.values
print(array)