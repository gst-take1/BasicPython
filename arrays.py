arr = [1,2,4,5,6,7,8]
for i in arr:
    print i;

for idx,val in enumerate(arr):
    print 'In enumerate idx :' + `idx` + ' Value: ' + `val`

if len(arr) > 6:
    print("Array %s is a big array of %d" % ('arr', len(arr)));

if len(arr) > 6 and len(arr) <= 10:
    print('Array %(array)s is a medium sized ..array of length %(len)d' % {"array": 'arr', "len":len(arr)});

print "arr[1:5]", arr[1:5]