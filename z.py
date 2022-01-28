from typing import Counter
from cv2 import detail_AffineBestOf2NearestMatcher
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import random

from scipy import rand

df = pd.read_csv("z.csv")

data = df["claps"].tolist()

mean = statistics.mean(data)
sd = statistics.stdev(data)

def randy (counter):
    dataset= []
    for i in  range(0,counter):
        d = random.randint(0,len(data)-1)
        dv = data[d]
        dataset.append(dv)
    dsm = statistics.mean(dataset)
    return dsm

meanList=[]
for i in range(0,100):
    meanies=randy(30)
    meanList.append(meanies)
mean_real = statistics.mean(meanList)
sd_real = statistics.stdev(meanList)


df1 = pd.read_csv("z.csv")

data1 = df1["claps"].tolist()

mean1 = statistics.mean(data)
sd1 = statistics.stdev(data)

df2 = pd.read_csv("z.csv")

data2 = df2["claps"].tolist()

mean2 = statistics.mean(data)
sd2 = statistics.stdev(data)

fig = ff.create_distplot([meanList],["claps"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean_real,mean_real],y=[0,0.20],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.20],mode="lines",name="mean1"))
fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.20],mode="lines",name="mean2"))
fig.show()

sds,sde = mean_real-sd,mean+sd
sd1s,sd1e = mean1-(2*sd1),mean1+(2*sd1)
sd2s,sd2e = mean2-(3*sd1),mean2+(3*sd1)

fig = ff.create_distplot([meanList],["claps"],show_hist=False)
fig.add_trace(go.Scatter(x=[sds,sds],y=[0,0.17],mode="lines",name="sds"))
fig.add_trace(go.Scatter(x=[sd1s,sd1s],y=[0,0.17],mode="lines",name="sds1"))
fig.add_trace(go.Scatter(x=[sd2s,sd2s],y=[0,0.17],mode="lines",name="sds2"))
fig.add_trace(go.Scatter(x=[sde,sde],y=[0,0.17],mode="lines",name="sde"))
fig.add_trace(go.Scatter(x=[sd1e,sd1e],y=[0,0.17],mode="lines",name="sde1"))
fig.add_trace(go.Scatter(x=[sd2e,sd2e],y=[0,0.17],mode="lines",name="sde2"))
fig.show()

z_score = (mean_real-mean1)/sd_real
print("Z SCORE =",z_score)