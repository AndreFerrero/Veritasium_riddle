import random
import time
# Used to evaluate elapsed time
from turtle import color
from matplotlib.animation import FFMpegWriter
import matplotlib.pyplot as plt
import statistics
import itertools
# useful to substitute for loops with itertools.repeat

# n = number of experiments
# b = boxes vector
# s = slips vector
# ff = final failure counter
# r = range for trials
st = time.time()
# success rate vector
sr_vector = []
for a in itertools.repeat(None, 100):
    ff = 0
    r = 100
    for n in itertools.repeat(None, r):
        b = list(range(1, 101))
        random.shuffle(b)
        s = list(range(1, 101))
        random.shuffle(s)
        
        # c = loop dimensions counter
        # f = failure counter for each trial
        f = 0
        for i in range(100):
            c = 0
            if b[i] != s[i] and f == 0:
                c += 1
                p = b.index(s[i])
                while True: 
                    c += 1
                    p = b.index(s[p])
                    # failure increases
                    if c >= 50:
                        f += 1
                        ff += 1

                    if s[p] == b[i] or c >= 50:
                        break
    sr_vector.append(1 - ff/r)

et = time.time()

elt = et - st
print("Elapsed time is:", elt, "seconds")

# Data analysis and visualisation
avg = statistics.mean(sr_vector)
v = statistics.variance(sr_vector)
m = statistics.median(sr_vector)

plt.style.use('ggplot')
plt.hist(sr_vector, bins = 20, edgecolor = "white", color= "c")
plt.xlabel("Success rates")
plt.ylabel("Frequencies")

# adding mean and median
plt.axvline(avg, color = "red", label = "Mean")
plt.axvline(m, color= "green", label= "Median")
plt.legend()

plt.show()
