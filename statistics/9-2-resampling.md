[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)
Exercise 2  
In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.
An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.

Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation.

Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?

````
means permute preglength
p-value = 0.1674
actual = 0.0780372667775
ts max = 0.226752436104

means permute birthweight
p-value = 0.0
actual = 0.124761184535
ts max = 0.112243501197
n    |   test1  | test2  | test2  | test4 
--------|--------|--------|--------|--------
9148 |	0.16 |	0.00 |	0.00 |	0.00
4574	0.03	0.02	0.00	0.00
2287	0.04	0.07	0.00	0.00
1143	0.70	0.04	0.80	0.07
571	0.53	0.00	0.00	0.35
285	0.96	0.84	0.35	0.53
142	0.87	0.49	0.20	0.06

````


```python
import first
import thinkstats2 as ts2
import numpy as np

class DiffMeansPermute(ts2.HypothesisTest):
    """Tests a difference in means by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return(test_stat)

    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return(data)



class DiffMeansResample(DiffMeansPermute):
	def RunModel(self):
		group1 = np.random.choice(self.pool, self.n, replace=True)
		group2 = np.random.choice(self.pool, self.m, replace=True)
		return(group1, group2)

def main():
	live, firsts, others = first.MakeFrames()
	data = firsts.prglngth.values, others.prglngth.values
	ht = DiffMeansResample(data)
	p_value = ht.PValue(iters=10000)
	print('\nmeans permute preglength')
	print('p-value =', p_value)
	print('actual =', ht.actual)
	print('ts max =', ht.MaxTestStat())
	print('')
	data = (firsts.totalwgt_lb.dropna().values,
			others.totalwgt_lb.dropna().values())
	ht = DiffMeansPermute(data)
	p_value = ht.PValue(iters=10000)
	print('\nmeans permute birthweight')
	print('p-value =', p_value)
	print('actual =', ht.actual)
	print('ts max =', ht.MaxTestStat())


if __name__ == "__main__":
	main()	

