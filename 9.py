import turtle as t
t.tracer(2)
t.screensize(2000,2000)

def levi(n,a):
    if n == 0:
        t.fd(a)
    else:
        t.lt(45)
        levi(n-1,a)
        t.rt(90)
        levi(n-1,a)
        t.lt(45)


levi(10,5)
t.update()
t.done()