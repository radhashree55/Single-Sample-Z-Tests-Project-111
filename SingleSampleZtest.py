import random
import pandas as pd
import statistics as st
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

# Base Graph Code.
fig = ff.create_distplot([data], ["Reading Time"], show_hist=False)
# fig.show()


def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean


def showFig(meanList):
    df = meanList
    mean = st.mean(df)
    fig = ff.create_distplot([df], ["Reading Time"], show_hist=False)
    fig.show()


meanList = []
for i in range(0, 100):
    setOfMean = randomSetOfMean(30)
    meanList.append(setOfMean)
showFig(meanList)
samplingMean = st.mean(meanList)
samplingStdev = st.stdev(meanList)

print("Mean of Sampling Distribution is", samplingMean)
print("Standard Deviation of Sampling Distribution is", samplingStdev)

mean = st.mean(data)
zScore = (mean - samplingMean) / samplingStdev
print("Mean of Sample is", mean)
print("Z Score is", zScore)
