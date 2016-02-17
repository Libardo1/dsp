[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)
Exercise 1  
The distribution of income is famously skewed to the right. In this exercise, we’ll measure how strong that skew is.
The Current Population Survey (CPS) is a joint effort of the Bureau of Labor Statistics and the Census Bureau to study income and related variables. Data collected in 2013 is available from http://www.census.gov/hhes/www/cpstables/032013/hhinc/toc.htm. I downloaded hinc06.xls, which is an Excel spreadsheet with information about household income, and converted it to hinc06.csv, a CSV file you will find in the repository for this book. You will also find hinc2.py, which reads this file and transforms the data.

The dataset is in the form of a series of income ranges and the number of respondents who fell in each range. The lowest range includes respondents who reported annual household income “Under $5000.” The highest range includes respondents who made “$250,000 or more.”

To estimate mean and other statistics from these data, we have to make some assumptions about the lower and upper bounds, and how the values are distributed in each range. hinc2.py provides InterpolateSample, which shows one way to model this data. It takes a DataFrame with a column, income, that contains the upper bound of each range, and freq, which contains the number of respondents in each frame.

It also takes log_upper, which is an assumed upper bound on the highest range, expressed in log10 dollars. The default value, log_upper=6.0 represents the assumption that the largest income among the respondents is 106, or one million dollars.

InterpolateSample generates a pseudo-sample; that is, a sample of household incomes that yields the same number of respondents in each range as the actual data. It assumes that incomes in each range are equally spaced on a log10 scale.

Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?

```
with log_upper = 6
mean 74278.7075312
std 93946.9299635
median 51226.4544789
skewness 4.94992024443
pearson skewness 0.736125801914
cdf[mean] 0.660005879567
```
```
With log_upper=7
mean 124267.397222
std 559608.501374
median 51226.4544789
skewness 11.6036902675
pearson skewness 0.391564509277
cdf[mean] 0.856563066521
```
```python
import numpy as np
import density
import hinc
import thinkplot
import thinkstats2 as ts2

def InterpolateSample(df, log_upper=6.0):
	df['log_upper'] = np.log10(df.income)
	df['log_lower'] = df.log_upper.shift(1)
	df.log_lower[0] = 3.0
	df.log_upper[41] = log_upper

	arrays = []
	for _, row in df.iterrows():
		vals = np.linspace(row.log_lower, row.log_upper, row.freq)
		arrays.append(vals)

	log_sample = np.concatenate(arrays)
	return(log_sample)

def main():
	df = hinc.ReadData()
	log_sample = InterpolateSample(df, log_upper=6.0)

	log_cdf = ts2.Cdf(log_sample)
	thinkplot.Cdf(log_cdf)
	thinkplot.Show(xlabel='household income', ylabel='CDF')

	sample = np.power(10, log_sample)
	mean, median = density.Summarize(sample)

	cdf = ts2.Cdf(sample)
	thinkplot.Pdf(pdf)
	thinkplot.Show(xlabel='household income', ylabel='PDF')


if __name__ == '__main__':
	main()	
