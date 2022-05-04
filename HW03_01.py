def triangle(n):
     count=0
     i=65
     j=1
     
     while i >= 65 and i<91:
         l=chr(i)
         print(l,end='')
         count+=1
         
         if count==n:
             break
         
         if count==j:
             print('\n',end='')
             count=0
             j+=1
        
         if l=='Z':
             i=64
             
         i+=1
         
         
n=eval(input())
triangle(n)
