import random
numbers=[]
num = random.randrange(1,45)
for i in range(6):
        while num in numbers:
            num = random.randrange(1,45)
        numbers.append(num)
print("오늘의 로또 추첨번호는 !!!",numbers,"입니다!!!\n")
print("당신의 행운을 빕니다")


'''랜덤 모듈을 불러옴
numbers 라는 리스트를 만들어줌
num 에 1부터 45의 숫자중 하나를 랜덤으로 할당시켜줌

이후 for문은 numbers라는 리스트에 6개의 숫자가 들어가도록 6번 반복해줌

while 은 트루일때 실행됨
만일 num에서 골라진 임의의 숫자가 이미 리스트에 있는 숫자라면
다시 한번 뽑는 일을 수행한다

리스트에 없는 숫자가 num에 할당되면 while문을 탈출한다'''
     
