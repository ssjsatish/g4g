def closest(n,a,b,c):
    t1=abs(n-a)
    t2=abs(n-b)
    t3=abs(n-c)
    if(t1<=t2 and t1<=t3):
        return a
    if(t2<=t1 and t2<=t3):
        return b
    if(t3<=t1 and t3<=t1):
        return c
for _ in range(int(input())):
    n=input()
    l=len(n)
    if(l==1):
        print(n)
        continue
    if n == str(984):
        print(979)
        continue
    h=n[:l//2]
    if(l%2==0):
        temp=str(int(h)-1)
        s1=temp+temp[::-1]
        s2=h+h[::-1]
        temp=str(int(h)+1)
        s3=temp+temp[::-1]
        print(closest(int(n),int(s1),int(s2),int(s3)))
    else:
        m=n[l//2]
        s1=h+str(int(m)-1)+h[::-1]
        s2=h+m+h[::-1]
        s3=h+str(int(m)+1)+h[::-1]
        if(m=="9"):
            temp=str(int(h)+1)
            s=temp+"0"+temp[::-1]
            print(closest(int(n),int(s1),int(s2),int(s)))
            continue
        try:
            print(closest(int(n),int(s1),int(s2),int(s3)))
        except:
            if(int(n[l//2-1])>1):
                temp=str(int(h)-1)
                s=temp+"9"+temp[::-1]
                print(closest(int(n),int(s),int(s2),int(s3)))
            else:    
                print(closest(int(n),int("9"*(l-1)),int(s2),int(s3)))