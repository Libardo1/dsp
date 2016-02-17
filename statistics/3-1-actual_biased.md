[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Exercise 1   Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.

Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb


Class Size Paradox - a computation that can be done with a PMF. For example - faculty ratios are 10/1 at american colleges, but students are surprised to find that their class sizes are generally much larger. Two reasons for this descrepency are that students typically take 4-5 classes per semester, but professors only teach 1-2 and that the number of students who will take a small class is small, but the number of students who take a large class is large, but nature of the metric. We are more concerned with the second reason for class size paradox.

```
The true mean of the distribution is 1.02, and the biased mean is 2.4. 
Children are more likely to have contact with families that have at least one child, 
so it makes sense that they would be biased to think that most people have children. 
From the step graph printed by the script below, we see that almost 50% of households have 0 children 
and almost 70% of households have 0 or 1 child. The biased mean shows a much higher assumption of children.  
```


```python
import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh)
thinkplot.Pmf(pmf, label='Num Kids Household in Rel to total')

def BiasPmf(pmf, label=''):
	new_pmf = pmf.Copy(label=label)
	for x, p in pmf.Items():
		new_pmf.Mult(x, x)

	new_pmf.Normalize()
	return(new_pmf)

biased = BiasPmf(pmf, label='biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()

print("True mean:", pmf.Mean(), "Biased Mean:", biased.Mean())
