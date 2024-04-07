import random

def f(x):
    return (x)**2 

def hill_climbing(f, x_min, x_max, step_size=0.1, max_iter=1000):
    x = random.uniform(x_min, x_max) 
    for _ in range(max_iter):
        x_new = x + random.uniform(-step_size, step_size)  
        if x_new < x_min or x_new > x_max:
            continue 
        if f(x_new) > f(x): 
            x = x_new
    return x, f(x)

x_min = 0
x_max = 6
step_size = 0.1
max_iter = 1000

max_x, max_val = hill_climbing(f, x_min, x_max, step_size, max_iter)

print "Maximum value found at x={}, f(x)={}".format(max_x, max_val)
