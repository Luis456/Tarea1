a=raw_input("palabra :")
b=len(a)
c=0
for i in range(b):
    if a[i]==a[-(i+1)]:
        c=c+1
if c==b:
    print "True"
else:
    print "False"