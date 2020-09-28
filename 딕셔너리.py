abstract = { "이름": "기찬" , "파이썬" : "딕셔너리" }

print(abstract)

dic = { 1 : 'a' , 2: 'aa' , 3 : 'aaa' }

print(dic)
print()

abstract['연락처'] ='010-0000-0000'

print(abstract)
print (abstract['이름'])
print (abstract['파이썬'])
print (abstract['연락처'])
print()

print(abstract.get('연락처'))
print()



sing = {}

sing['이름'] = '유성'
sing['특징'] = '반짝반짝'
sing['목소리'] = '멋있다.'

for k in sing.keys():
    print('%s -> %s' %( k ,sing[k]))

foods =  {'사과' : '바나나','체리':'파인애플','떡볶이':'파스타','유성':'은하수'};

while(True):
    myfood = input(str(list(foods.keys()))+"중 좋아하는 것은")
    if myfood in foods :
        print("<%s> 좋은건 <%s> 다같이."%(myfood , foods.get(myfood)))
    elif myfood == "끝":
        break;
    else :
        print("다 너무좋아")


# & 교집합 | 합집합 - 차집합 ^ 대칭 차집합 #
numList =[ k for k in range (1,6) ]
print(numList)

print()

foods =['떡볶이' , '짜장면','라면','피자','맥주','치킨']
sides =['오뎅' , '단무지' , '김밥']

for food ,side in zip(foods,sides):
    print(food,'-->',side)

