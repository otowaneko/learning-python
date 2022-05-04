#函式:計算有幾個解及答案
def answer(a,b,c):

    #answer有幾個解.d判別式
    global answer
    d=b**2-(4*a*c)

    #無限多解1無解無實數解0恰一實數解1兩個實數解2
    if (a==0 and b==0 and c==0):
        answer=-1
    elif (d<0 or (a==0 and b==0 and c!=0)):
        answer=0
    elif (d==0 or (a==0 and b!=0 and c!=0)):
        answer=1
    else:
        answer=2
    
    print(answer)

    #印出解;x1.x2為解
    if(answer==1):
        if(a==0 and b!=0 and c!=0):#一元一次方程式
            x1=-c/b
        else:
            x1=round((-b+(b**2-4*a*c)**0.5)/2*a,3)
        print(x1)
        
    elif(answer==2):
        x1=round((-b+(b**2-4*a*c)**0.5)/2*a,3)
        x2=round((-b-(b**2-4*a*c)**0.5)/2*a,3)
        
        #從小到大
        if(x1>x2):
            print(x2)
            print(x1)
        else:
            print(x1)
            print(x2)


#主要執行:輸入資料執行函式;abc係數
a=eval(input())
b=eval(input())
c=eval(input())
answer(a,b,c)
