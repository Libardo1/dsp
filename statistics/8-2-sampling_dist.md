[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)
Exercise 2  
Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.
Repeat the experiment with a few different values of n and make a plot of standard error versus n.

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

```python
import thinkstats2
import thinkplot
import math
import random
import numpy as np
from estimation import RMSE, MeanError




def SimulateSample(lam=2, n=10, m=1000):
	def VertLine(x, y=1):
		thinkplot.Plot([x, x], [0, y], color='.8', linewidth=3)
	estimates = []
	for j in range(m):
		xs = np.random.exponential(1.0/lam, n)
		lamhat = 1.0 / np.mean(xs)
		estimates.append(lamhat)

	stderr = RMSE(estimates, lam)
	print('standard error is ', stderr)

	cdf = thinkstats2.Cdf(estimates)
	ci = cdf.Percentile(5), cdf.Percentile(95)
	print('confidence interval is ', ci)
	VertLine(ci[0])
	VertLine(ci[1])

	#plots cdf
	thinkplot.Cdf(cdf)
	thinkplot.Show(root='estimation', xlabel='estimate', ylabel='CDF', title='Sampling distribution')

	return(stderr)

def main():
	thinkstats2.RandomSeed(17)

	for n in [10, 100, 1000]:
		stderr = SimulateSample(n=n)
		print(n, stderr)

if __name__ == '__main__':
	main()	
