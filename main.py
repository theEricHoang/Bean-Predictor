import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sb
import os

data = pd.read_excel(os.path.join(os.path.dirname(__file__), 'Dry_Bean_Dataset.xlsx'))
dataClean = data.dropna() # clean data
dataByClass = data.groupby('Class')

# splitting data by class of bean
seker = dataByClass.get_group('SEKER')
barbunya = dataByClass.get_group('BARBUNYA')
bombay = dataByClass.get_group('BOMBAY')
cali = dataByClass.get_group('CALI')
dermason = dataByClass.get_group('DERMASON')
horoz = dataByClass.get_group('HOROZ')
sira = dataByClass.get_group('SIRA')

# TODO: gather stats for 2 or 3 classes of beans. only need to do mean, median, variance, std, etc. for AREA, PERIMETER, and ROUNDNESS
def gatherStats(type, stat, group):
    print(type, stat, 'mean:', group[stat].mean())
    print(type, stat, 'median:', group[stat].median())
    print(type, stat, 'variance:', group[stat].var())
    print(type, stat, 'standard deviation:', group[stat].std())
    print()
# BARBUNYA STATS
gatherStats('Barbunya', 'Area', barbunya)
gatherStats('Barbunya', 'Perimeter', barbunya)
gatherStats('Barbunya', 'roundness', barbunya)

# TODO: Charts

# TODO: Regression/Classification model