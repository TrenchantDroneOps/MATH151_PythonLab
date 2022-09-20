# -*- coding: utf-8 -*-
"""Copy of Lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y1k_SkDdJYsyYRvqBdf1phzUIRxs_RRE

## MATH 151 Lab  3

Jaden Ninan, Zane Akers, Keegan Barrier, Robert Santos, Samuel Martinez Course #548
"""

from sympy import *
from sympy.plotting import (plot,plot_parametric)

"""### Question 1"""

print('The intermediate value theorem says for any function f that's continuous over the interval [a,b], it will take on any value between f(a) and f(b) on that point.')
print('f has a root between 0 and 1 because f(0) is -1 and f(1) is 10 so there must an f for some point c such that f(c) = 0.')

"""#### 1a"""

x=symbols('x')

f = (x**5)+(4*x**3)-(2*x**2)+(8*x-1)

f_0 = f.subs(x,0)
print('f(0) =', f_0)

f_1 = f.subs(x,1)
print('f(1) =', f_1)

"""#### 1b"""

print('the root of the function inside [0,1] is', nsolve(f,x,0))

"""### Question 2

#### 2a
"""

f1 = 2*x - 3
f2 = 4*x - x**2
f3 = (x**2 - 6*x + 8)/(x-4)
f4 = exp((x-4) * log(3))
fo3_lhl = limit(f1,x,3)
fo3_rhl = limit(f2,x,3)
fo4_lhl = limit(f2,x,4)
fo4_rhl = limit(f3,x,4)
fo5_lhl = limit(f3,x,5)
fo5_rhl = limit(f4,x,5)

print('As x approaches 3 from the left, the limit of f(x) approaches', fo3_lhl)
print('As x approaches 3 from the right, the limit of f(x) approaches', fo3_rhl)
print('Since both lhl and rhl are 3, f is continuous at x=3')

#e^(stuff) is written exp(stuff)
#ln(stuff) is written log(stuff)
#infinity is written oo (double letter o)
#only graph question 3 up to 100, not infinity

print()
print('As x approaches 4 from the left, the limit of f(x) approaches', fo4_lhl)
print('As x approaches 4 from the right, the limit of f(x) approaches', fo4_rhl)
print('Since the lhl and rhl are not equal, the limit of f(x) at x=4 does not exist')
print('f is continuous from the left at x=4')

print()
print('As x approaches 5 from the left, the limit of f(x) approaches', fo5_lhl)
print('As x approaches 5 from the right, the limit of f(x) approaches', fo5_rhl)
print('Since both lhl and rhl are 3, f is continuous at x=5')


"""#### 2b"""
plot((f1,(x,0,3)),(f2, (x,3,4)), (f3, (x,4,5)), (f4, (x,5,6)))

"""### Question 3

#### 3a
"""

p_0, k, r, t = symbols('p_0 k r t')

p = (k*p_0)/(p_0 + (k - p_0)*exp(-r*t))
p1 = p.subs({p_0:10, k:1000, r:0.1})

plot(p1, (t, 0, 100))


p1_lim = limit(p1,t,oo)
print('The limit of p1 when k is 1000 as t goes to oo is', p1_lim)

"""#### 3b"""

p2 = p.subs({p_0:10, k:1, r:0.1})

plot(p2, (t, 0, 100), ylim=(-1,10))


p2_lim = limit(p2,t,oo)
print('The limit of p2 when k is 1 as t goes to oo is', p2_lim)

"""#### 3c"""

p3 = p.subs({p_0:10, k:15, r:0.1})

plot(p3, (t, 0, 100))

p3_lim = limit(p3,t,oo)
print('The limit of p3 when k is 15 as t goes to oo is', p3_lim)

"""#### 3d"""
As t goes to infinity, the population size approaches its maximim or minimum of K. K is the carrying capacity of the population. The population can not exceed the K values.



