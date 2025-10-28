import turtle as t
t.tracer(1)
t.screensize(2000,2000)

def ice(n,a):
    if n == 0:
        t.fd(a)
    else:
        ice(n-1,a)
        t.lt(90)
        ice(n-1,a/2)
        t.rt(180)
        ice(n-1,a/2)
        t.lt(90)
        ice(n-1,a)  


ice(3,100)
t.update()
t.done()