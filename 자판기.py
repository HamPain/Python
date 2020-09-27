def showmenu() :
  print("음료 : 1.콜라(1000) 2.주스(1500) 3.녹차(2000)")

coin = 0
drinkname = ["콜라", "주스", "녹차"]
drinkprice = [1000, 1500, 2000]

while True:
  print("1.메뉴보기 2.동전넣기 3.음료선택 4.잔돈반환 5.끝내기 (현재금액 ",coin,"원)")
  choice = int(input("무엇을 하십니까?")) 
  if choice == 1 : 
    showmenu()
  elif choice == 2 :
    newcoin = int(input("얼마를 넣으시겠습니까?"))
    if ( newcoin >=0 ):
      coin = coin + newcoin
    elif ( newcoin <0):
      print("다시 입력해주세요")
      continue;
  elif choice == 3 :
    drink = int(input("음료번호를 골라주세요"))
    if drink in (1,2,3) :
      if coin >= drinkprice[drink-1] :
        print(drinkname[drink-1],"음료를 받아주세요")
        coin = coin - drinkprice[drink-1]
      else :
        print("금액이 부족합니다")
    else :
      print("이 자판기에 없는 음료입니다.")
      
  elif choice == 4 :
    print(coin,"원을 가져가세요")
    coin = 0
  elif choice == 5 :
    break
  elif choice == 'String' :
    continue;
  else :
    print("잘못입력하셨네요... 다시 입력해주세요")
    continue;






  
