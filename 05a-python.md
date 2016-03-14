# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?
```
tuples are immutable object arrays. You can have both integers and strings in tuples, but cannot 
do this with lists. Lists are the most simple arrays that you can do in python. Tuples would work as 
keys in dictionaries because they are immutable and have a 2d reference.
```
---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?
```
Python lists are the simplest version of an array of strings or integers - they are mutable and 
easy to iterate over. Sets are similar to lists and dictionaries, but they take up less memory 
when you are iterating over them than lists do, so performance is better in from a set for finding 
an element. You can also easily use sets to succinctly compute (ex, set(x) - set(y) where x and y 
are sets and you are finding the difference). 
```
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.
```
a lambda function is an 'anonymous' function because it is undefined (by def at the 
beginning of a code). You can use the lambda operator for single use functions within a 
larger framework of code, and do not have to define the function every time. For example, while 
creating a dictionary such as in the first question on this list, you could write a lambda 
function to sort the dictionary once it has been created - something you would only need to do once.
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.
```
(Section 19.2) List comprehensions are basically lists within lists. You can use the concept 
to more succinctly apply further code to a list you've already created. In addition to 
manipulating the items in a list with a list comprehension, you can use list comprehension to 
filter a list (ex: print only items from the list that are all upper case). A list comprehension 
can be written to do the things that the map and filter operators do. The benefit to a list 
comprehension is that its operations can be tweaked, whereas an operator will always produce 
the result it was originally written to produce. 
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
import datetime
def number_days():
	date_stop = datetime.datetime(2015, 7, 28)
	date_start = datetime.datetime(2013, 1, 2)
	print((date_stop-date_start).days)
number_days()
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





