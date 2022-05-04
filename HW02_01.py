import sys

def StringSplit():
    num=input()
    num=num.split(sep=",")
    
    total1=0
    total2=0
    total3=0
    total4=0
    count=0
    count2=0
    
    for i in num:
        total1+=float(i)
        num.reverse() 
        if count==len(num):
            break
        else:
            total2=0
            count2=0
            for j in num:
                count2+=1
                if count2 < (len(num)-count):
                    total2+=float(j)
                    continue
                else:
                    break
            if total1==total2:
                print (True)
                sys.exit(0)
        num.reverse()
        count+=1
    
    count=0
    count2=0
    num.reverse()
    
    for k in num:
         total4+=float(k)
         num.reverse()
         if count==len(num):
             break
         else:
             total3=0
             count2=0
             for l in num:
                 count2+=1
                 if count2 < (len(num)-count):
                     total3+=float(l)
                     continue
                 else:
                     break
             if total3==total4:
                 print (True)
                 sys.exit(0)
         num.reverse()
         count+=1    
         
    print(False)
    
StringSplit()
