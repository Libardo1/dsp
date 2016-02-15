[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
Exercise 4   Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?


The basic question: is there is a difference in weight, on average, between first babies and other babies?

The Cohen's D of this problem came out to -.089, meaning that other babies are ever so slightly heavier on average than first babies. I created print statements at the end of the program to denote whether or not the effect is large, based on further research on how to interpret Cohen's d http://rpsychologist.com/d3/cohend/. As with P-values, it's bad practice to rely on 'canned effect sizes'; in this case, it seems that the effect size is small enough to be practically inconsequential if we weren't looking at birth weights of babies. This information about the difference could be important enough to be of concern for first-time mothers. 


```python
import math
import nsfg
import first

def WeightDifference(live, firsts, others):
    mean0 = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return(d)
def main():
    live, firsts, others = first.MakeFrames()
    WeightDifference(live, firsts, others)
    group1 = firsts.total_lb()
    group2 = others.totalwgt_lb()
    d = CohenEffectSize(group1, group2)
    print("Cohen D", d)
    if d > .49:
        print("The effect size is large")
    if d > .29:
        print("The effect size is medium")
    else: 
        print("the effect size is small")   
if __name__ == '__main__':
    main()

