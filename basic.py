print  ("khiem");
a = 10
def  sum (a, b) :
    print a
    print b
    return (a+b)
c = sum (2, 3);
print c
print "---------"
print "for"
i = [0, 10]
for j in xrange(0, 10):
    print j
print "---------"
# dictionary
print "dictionary"
point = {'x': 1,'y': 2}
print point ['x']
print "-".join(point)
point['z'] = 3
print point
print point.has_key('z')
print "---------"
import random
print random .__file__
print dir ()