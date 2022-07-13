The algorithm is still under revision for improvements in terms of complexity.

The first and the second for loop have been improved with the help of itertool.repeat().

The third loop is the longest, and as one can see with the print(elapsed time), the algorithm takes a bit of time to be computed (around 11.7s with my machine).
The efficiency of the loop is mined by the inability of the for loop to stop if f != 0.
More precisely, the way the loop is coded is only able to prevent it to go through the first if statement, but it still loops for each i in (0, 99).

Moreover, applyig itertool.repeat() apparently caused unsolved problems with extracting the ff value, therefore it is still under revisioning.
