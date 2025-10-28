import turtle as t
t.tracer(2)
t.screensize(2000,2000)

def kv(n,a):
    for i in range(4):
        t.fd(a)
        t.rt(90)
    t.rt(10)
    t.up()
    t.fd(a/11)
    t.down()
    kv(n-1, a*9/10)
kv(10,200)
t.update()
t.done()