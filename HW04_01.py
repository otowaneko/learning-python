#T1.T2:空tuple
T1=()
T2=tuple()

#印出T1.T2的資料型態
print(type(T1))
print(type(T2))
print()

T3=('a','b','c')
print(type(T3))

#印出位置0~1的資料
print(T3[0:2])

#計算T3裡有幾個a
print(T3.count("a"))
print()

#S1:空set S2:set
S1=set()
S2={1,2}
print(type(S1))
print(type(S2))
print(S2)
print()

#D1:Dictionary D2:set D3.D4:Dictionary(空)
D1={'a':1,'b':2,'c':3}
D2={1,2,3}
D3={}
D4=dict()
print(type(D1))
print(type(D2))
print(type(D3))
print(type(D4))
print()

#印出D1裡的key和value
print(D1.items())

#印出D1裡的key
print(D1.keys())

#印出D1裡的value
print(D1.values())
