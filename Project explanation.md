# Veritasium_riddle
I coded the solution proposed by Veritasium to the riddle of the 100 prisoners.

The context is the following:
Inside a room there are 100 boxes, and inside each box there's a slip of paper. Both a numbered from 1 to 100.
100 prisoners have the chance to escape if all of them manage to find the slip of paper with their number on it.
Each prisoner can open up to 50 boxes. If one of them doesn't find his number, all of them lose.

If all of them open the boxes randomly, they have a probability of success of (0.5)^100, definitely a low chance of winning.

Nevertheless, they can first open the box with their number on it and then follow the loop, initialised by the number they find in the slip of paper,
untill they find their number.
It can be mathematically proven to result in a (about) 30% chance of winning the game, compared to the initial basically 0 probability of success.

I wanted to replicate the process and extract the probability of success. To do that, I extracted the failure rate over 100 trials, and used it to
construct a vector of 100 elements containing the complement of the failure rate, therefore the success rate.

To visualise the result, I plotted the histogram of the success rate, showing also the mean and the median

Obviously, as with each trial the boxes and the slips are shuffled in a different way, that creates a certain degree of variability with the length of
each loop for each box. 
Nevertheless the expected value and the median confirm our expectations about the success rate
