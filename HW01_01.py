##函式:停車費計算
def park(t1,t2,x):
    
    #將12的時與分隔開,強制將Y/N轉為大寫;t1進場時間.t2離場時間.x是否有證件
    t1=t1.split(sep=":")
    t2=t2.split(sep=":")
    x=x.upper()

    if (t2[0]==24 or t2[0]<t1[0] or (t2[0]==t1[0] and t1[1]>t2[1])):
        t2[0]=23
        t2[1]=59
        
    ##計算時間;time準確停車時間
    time=(int(t2[0])-int(t1[0]))*60+(int(t2[1])-int(t1[1]))
    global timep
    
    ##不滿30分鐘以30分鐘計算,同一分鐘進出則免費;timep計算停車費用的時間
    if time>1:
        if time%30!=0:
            timep=time+(30-(time%30))
        else:
            timep=time
    else:
        timep=0


    ##計算價格
    if x=="N":
        cost=int(timep/30*20)

    elif x=="Y":
        if time<30:
            cost=0
        else:
            cost=int(timep/30*10)
            
    print(cost)

##主要執行:輸入資料,執行函式            
t1=input()
t2=input()
x=input()
park(t1,t2,x)
