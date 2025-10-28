import turtle as t
t.tracer(5)
t.screensize(2000,2000)

def koh(n,a):
    if n == 0:
        t.fd(a)
    else:
        koh(n-1,a/3)
        t.lt(60)
        koh(n-1,a/3)
        t.rt(120)
        koh(n-1,a/3)
        t.lt(60)
        koh(n-1, a/3)
for i in range(3):
    koh(5,400)
    t.rt(120)
t.update()
t.done()