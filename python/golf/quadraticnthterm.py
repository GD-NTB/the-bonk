from math import trunc as t;s=[0]*5
for i in range(5):s[i]=int(input('{0} term: '.format(str(i+1)+{1:'st',2:'nd',3:'rd'}.get(4 if 10<=i+1%100<20 else i+1%10,'th'))))
a=((s[2]-s[1])-(s[1]-s[0]))/2;b=(s[1]-s[0])-(3*a);c=s[0]-a-b;s=''
if a!=0:s+=str(t(a)if a%1<1 else a)+'n² + '
if b!=0:s+=str(t(b)if b%1<1 else b)+'n + '
if c!=0:s+=str(t(c)if c%1<1 else c);print(s)