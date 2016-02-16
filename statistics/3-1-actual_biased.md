[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Exercise 1   Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.

Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb


Class Size Paradox - a computation that can be done with a PMF. For example - faculty ratios are 10/1 at american colleges, but students are surprised to find that their class sizes are generally much larger. Two reasons for this descrepency are that students typically take 4-5 classes per semester, but professors only teach 1-2 and that the number of students who will take a small class is small, but the number of students who take a large class is large, but nature of the metric. We are more concerned with the second reason for class size paradox.

work in progress

``` python
from __future__ import print_function
import numpy as np
import nsfg
import first
import sys
import thinkplot
import thinkstats2

def PmfVar(pmf, mu=None):
	if mu is None:
		mu = pmf.Mean()
	var = 0.0
	for x, p in pmf.d.items():
		var += p * (x - mu) ** 2
	return(var)

def Diffs(t):
	first = t[0]
	rest = t[1:]
	diffs = [first - x for x in rest]
	return(diffs)


def PmfMean(pmf):
	mean = 0.0
	for x, p in pmf.d.items():
		mean += p * x
	return(mean)

def PairWiseDifference(live):
	live = live[live.prglngth >= 37]
	preg_map = nsfg.MakePregMap(live)

	diffs = []
	for caseid, indices in preg_map.items():
		lengths = live.loc[indices].prglngth.values
		if len(lengths) >= 2:
			diffs.extend(Diffs(lengths))
	pmf = thinkstats2.Pmf(diffs)
	thinkplot.Hist(pmf, align='center')
	thinkplot.Show(xlabel='Difference in weeks',ylabel='PMF')


def main(script):
	live, firsts, others = first.MakeFrames()
	PairWiseDifference(live)

	prglngth = live.prglngth
	pmf = thinkstats2.Pmf(prglngth)
	mean = PmfMean(pmf)
	var = PmfVar(pmf)

	assert(mean == pmf.Mean())
	assert(var == pmf.Var())

if __name__ == '__main__':
	main(*sys.argv)				

