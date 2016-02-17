[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)
Exercise 2  
Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.
Repeat the experiment with a few different values of n and make a plot of standard error versus n.
```
I chose the sample sizes 10, 100, 1000 to study the standard error and bounds of a 90% confidence interval. 
As the sample size gets larger, the standard error shrinks. The confidence interval also becomes tighter, 
hovering around 2 as the sample size gets larger. This makes sense as we become more confident that the sample 
describes the population as the sample size becomes larger. 
```
n | St. Error | Conf Interval
------------ | ------------- | -------------
10 | 0.90 | (1.3, 3.9)
100 | 0.21 | (1.7, 2.4)
1000 | 0.06 | (1.9, 2.1)

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
