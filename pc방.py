"""PC방 매출 계산 프로그램 - 관리자 행동에 따라 다음을 반복하도록 한다. (총 15개 좌석)
1 현재 비어있는 좌석 보기
2 입장하기 (좌석번호만 입력 - 현재 시간 자동입력)
3 퇴장하기 (좌석번호만 입력 - 현재 시간 자동반영해서 요금계산)
요금계산법 : 15초 당 1천원, 60초 이상 10%, 120초 이상 20% 할인 적용
4 현재까지 매출금액 보기
5 현재까지 이용자 수 보기
6 끝내기"""
import time
def showseat(s):
  for i in range(5):
    print(i+1,s[i])

def enterseat(s):
  sno = int(input("입장 좌석번호? "))
  s[sno-1] = int(time.time()) 

def exitseat(s):
  sno = int(input("퇴장 좌석번호? "))
  now = int(time.time()) 
  seconds = now - s[sno-1]
  s[sno-1] = 0
  price = int((seconds+14)/15) * 1000
  print("요금(원) :", price, "시간(초) :",seconds)
  return price

seats = [0,0,0,0,0]
totalprice = 0
totaluser = 0
while True:
  print("1.좌석 2.입장 3.퇴장 4.매출 5.이용자 6.종료")
  choice = int(input("원하는 작업?"))
  if choice == 1 : showseat(seats)
  elif choice == 2 : 
    enterseat(seats)
    totaluser += 1
  elif choice == 3 : 
    totalprice += exitseat(seats)   
  elif choice == 4 : print("매출(원) :",totalprice)    
  elif choice == 5 : print("입장객(명) :",totaluser)
  else : break   
    
