# CS 1302 PROJECT
# by: ERIC HOANG, RYAN PHAM, & TAOFFEK ADEYANJU

import pandas as pd
import matplotlib as mpl
import seaborn as sb
import os

data = pd.read_excel(os.path.join(os.path.dirname(__file__), 'Dry_Bean_Dataset.xlsx'))
dataClean = data.dropna() # clean data
dataByClass = data.groupby('Class')

# splitting data by class of bean. uncomment bean group var if u need to use it
#seker = dataByClass.get_group('SEKER')
barbunya = dataByClass.get_group('BARBUNYA')
bombay = dataByClass.get_group('BOMBAY')
#cali = dataByClass.get_group('CALI')
#dermason = dataByClass.get_group('DERMASON')
#horoz = dataByClass.get_group('HOROZ')
#sira = dataByClass.get_group('SIRA')

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

# BOMBAY STATS
gatherStats('Bombay', 'Area', bombay)
gatherStats('Bombay', 'Perimeter', bombay)
gatherStats('Bombay', 'roundness', bombay)

# smaller sample of data for scatter plots
dataCleanSamp = dataClean.sample(1000)

# charts
sb.set_palette("Set3")
sb.set(font_scale=0.6)

fig, axs = mpl.pyplot.subplots(ncols=4)
areaBar = sb.barplot(data=dataClean, x="Class", y="Area", ax=axs[0]).set_title("Avg Area for Each Bean Class")
roundnessBar = sb.barplot(data=dataClean, x="Class", y="roundness", ax=axs[1]).set_title("Avg Roundness for Each Bean Class")
roundVsAreaScatter = sb.scatterplot(data=dataCleanSamp, x="roundness", y="Area", hue="Class", ax=axs[2], size=0.00001).set_title("Roundness vs Area")
lwRatioScatter = sb.scatterplot(data=dataCleanSamp, x="MajorAxisLength", y="MinorAxisLength", hue="Class", ax=axs[3], size=0.00001).set_title("Length vs Width")
# display plots
mpl.pyplot.show()
