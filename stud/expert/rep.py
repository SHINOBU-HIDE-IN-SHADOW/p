import functools
def repeat(n):
    def dr(func):
        @functools.wraps(func)
        def wra(*args,**kwargs):
            for x in range(n):
                a = func(*args,**kwargs)
            return a
        return wra
    return dr
def de(func):
    @functools.wraps(func)
    def wra(*args,**kwargs):
        ag = [repr(a) for a in args]
        ag1 = [f"{k}={v!r}"for k,v in kwargs.items()]
        sig = "".join(ag+ag1)
        print(f"{func.__name__} {sig}")
        result = func(*args,**kwargs)
        print(f"{func.__name__!r} {result!r}")
        return result
    return wra
@de
@repeat(4)
def say():
    print("Hello")
    return "Hello"
say()
# print(say.__name__)