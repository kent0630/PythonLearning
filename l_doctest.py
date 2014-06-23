# encoding=utf-8

# 以下三种需求可能会用到doctest
# 1. 验证模块（例如，方法）中的文档或说明书是否得及时更新。
# 2. 执行回归测试（regression test）。
# 3. 写培训文档，或说明文档，有点程序可读性测试的味道。

#可以显式调用doctest，2.6后也可这样调用:
# python -m doctest -v thefile.py 
''''' 
@author: Arthur 
@license: *** 
@contact: ****@***** 
@see: http://wenku.baidu.com/view/1d2ac17fa26925c52cc5bf92.html 
@version: 0.0.1 
@todo[0.0.2]: a new story 
 
@note: a comment 
@attention: please attention 
@bug: a exist bug 
@warning: warnings 
'''  
def factorial (n):
    '''Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.
    >>> [factorial(n) for n in range(6)] #看看python的语法就是这么简洁
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000L
    >>> factorial(30L)
    265252859812191058636308480000000L
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: n must be >= 0
    
    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
    ...
    ValueError: n must be exact integer
    >>> factorial(1e100)
    Traceback (most recent call last):
    ...
    OverflowError: n too large
    ''' #三引号引起来的字都是说明
    
    import math
    if not n>=0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n: # cache a value like le300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
