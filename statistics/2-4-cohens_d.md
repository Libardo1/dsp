[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

import thinkstats2
import nsfg
import first


def WeightDifference(live, firsts, others):
    """Explore the difference in weight between first babies and others.

    live: DataFrame of all live births
    firsts: DataFrame of first babies
    others: DataFrame of others
    """
    mean0 = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print("Cohen's d is", d)

    if d > .49:
    	print("The effect size is large")
    if d > .29:
    	print("The effect size is medium")
    else: 
    	print("the effect size is small")	


def main():
	live, firsts, others = first.MakeFrames()
	WeightDifference(live, firsts, others)	

if __name__ == '__main__':
    main()
