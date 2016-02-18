[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)
Exercise 3  
In games like hockey and soccer, the time between goals is roughly exponential. So you could estimate a team’s goal-scoring rate by observing the number of goals they score in a game. This estimation process is a little different from sampling the time between goals, so let’s see how it works.
Write a function that takes a goal-scoring rate, lam, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.

Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE.

Is this way of making an estimate biased? Plot the sampling distribution of the estimates and the 90% confidence interval. What is the standard error? What happens to sampling error for increasing values of lam?

```
The RMSE for estimating lambda is 1.4. The mean error is small and decreases with m, so this estimation appears
to be unbiased. 

If the time between goals is exponential, the distribution of goals scored in a game is Poisson.

```



``` python
import thinkstats2 as ts2
import thinkplot
import math
import random
import numpy as np
import scipy
from estimation import RMSE, MeanError

def SimulateGame(lam):
	goals = 0
	t = 0
	while True:
		time_between_goals = random.expovariate(lam)
		t += time_between_goals
		if t > 1:
			break
		goals += 1

	L = goals
	return(L)

def Estimate(lam=2, m=1000000):
	estimates = []
	for i in range(m):
		L = SimulateGame(lam)
		estimates.append(L)

	print('hockey game')
	print('RMSE L', RMSE(estimates, lam))
	print('mean error L', MeanError(estimates, lam))

	pmf = ts2.Pmf(estimates)
	thinkplot.Hist(pmf)
	thinkplot.Show()	


def main():
	Estimate()

if __name__ == '__main__':
	main()	



