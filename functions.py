tot = 30


def func1():
    a = 5
    b = 6
    tot = a + b
    print ("Inside func1 tot: %15d" %(tot))
    print ("%25s: %15d" % ("Inside func1 tot", tot))
    print ("{0:25s}: {1:5d}".format("Inside func1 tot", tot))


def func2():
    global tot
    tot = 40


print('Initial value of tot: %15d'  %(tot))
func1()
func2()
print('Updated value of tot: %15d'  %(tot))

print


#print('Initial value of tot: %15d'  %(tot))
print ("{0:25s}: {1:5d}".format("Initial value of tot", tot))

#print('Now Updated value of tot: %15d'  %(tot))
print ("{0:25s}: {1:5d}".format("Now Updated value of tot", tot))