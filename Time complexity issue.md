The algorithm is still under revision for improvements in terms of complexity.

The first and the second for loop have been improved with the help of itertool.repeat().

The third loop is the longest, and as one can see with the print(elapsed time), the algorithm takes a bit of time to be computed (around 11.7s with my machine).
The efficiency of the loop is mined by the inability of the for loop to stop if f != 0.
More precisely, the way the loop is coded is only able to prevent it to go through the first if statement, but it still loops for each i in (0, 99).

Furthermore, it can't be improved as the other ones with itertools.repeat() because it doesn't loop the i variable through the vector (0:99), but it simply
repeats the cycle the number of times specified
