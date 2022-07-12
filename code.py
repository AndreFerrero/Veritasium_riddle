import random
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
# it creates a better plot at the end
#sns.set()

# n = number of experiments
# b = boxes vector
# s = slips vector
# ff = final failure counter
f_vector = []
for a in range(100):
    ff = 0
    for n in range(100):
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
    f_vector.append(ff/100)

#print(ff/100)                          
#print(f_vector[0:5])

#######################################################
plt.hist(f_vector, bins = 20)
plt.xlabel("Failure rates")
plt.ylabel("Frequencies")
plt.show()
