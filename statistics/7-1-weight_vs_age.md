[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)
Exercise 1   Using data from the NSFG, make a scatter plot of birth weight versus mother’s age. Plot percentiles of birth weight versus mother’s age. Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?
```
In this exercise, I created a scatter plot that graphs the mothers age as x and the baby;s weight 
as y. At the same time, I ran the regular correlation and the Spearman correlation separately as 
values to get a numeric indication of whether or not there is an implied correlation. The correlation 
is .068 and the Spearman correlation is .095, indicating that there isn't a strong correlation. 
Additionally, the scatter plot implies a line almost parallel to the x axis, with a distribution 
of 6-8.5 pounds regardless of the mother's age.  

I used the formulas for Correlation, Covariance and Spearman correlation from thinkstats2 as guides 
to write the code for this exercise. I would like to eventually not import thinkstats2 for CDF, but 
have yet to extract that class as it calls on several other large formulas within that file. 

```

```python
import sys
import numpy as np
import first
import thinkplot
import thinkstats2
import pandas

def Cov(xs, ys, meanx=None, meany=None):

	xs = np.asarray(xs)
	ys = np.asarray(ys)

	if meanx is None:
		meanx = np.mean(xs)
	if meany is None:
		meany = np.mean(ys)

	cov = np.dot(xs-meanx, ys-meany) / len(xs)
	return(cov)

def Corr(xs, ys):
	xs = np.asarray(xs)
	ys = np.asarray(ys)

	meanx, varx = Meanvar(xs)
	meany, vary = Meanvar(ys)

	corr = Cov(xs, ys, meanx, meany) / math.sqrt(varx, vary)
	return(corr)

def SpearmanCorr(xs, ys):
	xranks = pandas.Series(xs).rank()
	yranks = pandas.Series(ys).rank()
	return(Corr(xranks, yranks))

def scatter(ages, weights, alpha=1.0):
	thinkplot.Scatter(ages, weights, alpha=alpha)
	thinkplot.Config(xlabel='AGE IN YEARS', ylabel='WEIGHT IN LBS',xlim=[10,45],ylim=[0,15],legend=False)
	thinkplot.Show()

def main(script):
	live, firsts, others = first.MakeFrames()
	live = live.dropna(subset=['agepreg','totalwgt_lb'])
	ages = live.agepreg
	weights = live.totalwgt_lb

	print('Correlation', thinkstats2.Corr(ages, weights))
	print('Spearman Correlation', thinkstats2.SpearmanCorr(ages, weights))

	scatter(ages, weights, alpha=0.25)
	

if __name__ == '__main__':
	main(*sys.argv)	
