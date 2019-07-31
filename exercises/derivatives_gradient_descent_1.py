f = lambda x: 3*x**2-12*x+20

# 2
def method1(f, x, e):
    return (f(x + e) - f(x)) / e

# 3
def method2(f, x, e):
    return (f(x + e) - f(x - e)) / (2 * e)

# 4
print("method1 - " , "e = 0.1: " , method1(f, 4, 0.1) ,
" e = 0.01: " , method1(f, 4, 0.01) ,
" e = 0.001: " , method1(f, 4, 0.001))

# 5
print("method2 - " , "e = 0.1: " , method2(f, 4, 0.1) ,
" e = 0.01: " , method2(f, 4, 0.01) ,
" e = 0.001: " , method2(f, 4, 0.001))
