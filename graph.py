import numpy as np
import matplotlib.pyplot as plt


#change data here
data = np.array([[90,80,65,87,67,98],
                [92,83,90,74,85,66],
                [77,63,86,51,76,78],
                [81,72,94,75,88,97],
                [60,75,65,87,67,70],
                [81,95,70,78,59,76]])
y_label='Scores'
title='Scores of each student'
x_label=('Amy','Bob','John','Mary','Henny','Tom')
colors=['#EE30A7','#EEA2AD','#EEE0E5','#7B68EE','#473C8B','#1E90FF']
legend=['Chineses','Math','English','Physics','Chemistry','Biology']
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

N = np.shape(data)[0]   # the number of the bars
ind = np.arange(N)    # the x locations for the bar',s
bot = np.zeros(N,dtype = np.int)

for i in range(N):
	p = plt.bar(ind,data[i],width,color = colors[i],bottom = bot)
	bot = bot+data[i]
 
plt.ylabel(y_label)
plt.title(title)
plt.xticks(ind,x_label)
plt.yticks(np.arange(0, 650, 50))
plt.legend(legend,loc='upper right',bbox_to_anchor=(1.3,1))

fig.subplots_adjust(right=0.8)
 
plt.show()
