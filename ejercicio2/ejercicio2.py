a=int(raw_input())
b=int(raw_input())
resul=[]
resul1=[]
for i in range (a,b+1):
	resul.append (i)
print resul
for i in range (a,b):
	if 	i%2 == 0:
		resul1.append (i)
print resul1
raw_input()