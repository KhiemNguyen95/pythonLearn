result = []
for y in xrange(2000,3200):
    if (y % 7 ==0 ) and ( y % 5 !=0):
    	result.append(str(y))
print (','.join(result))

# ---------------------
print "in range"
for y in reversed(range(10)):
    print y
print "------------------"
for y in range(10):
    print y