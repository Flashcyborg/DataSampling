import pandas as pd
import statistics
import csv
import random

df = pd.read_csv("data.csv") 
data = df["average"].tolist()

samples = []
for test in range(1,100):
    x = random.randint(1,len(data)-1)
    samples.append(data[x])
print (samples)
mean = statistics.mean(samples)