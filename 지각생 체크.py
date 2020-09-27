import time
def Student(s):
    print("학생 목록")
    

def Alearner(s):
    for i in range(5):
        print(i+1,s[i])
    print()

def Students(s):
    number = int (input("넣으실 자리를 선택해주세요"))
    s[number - 1] = int (time.time())


Student = [0,0,0,0,0]
totalprice = 0
while True:
    print("1.지각생 체크 2.지각생 입력 3.종료")
    choice = int(input("원하는 직업은?"))
    print()
    if choice == 1:
        Alearner(Student)
    elif choice == 2:
        Students(Student)
    else : break
