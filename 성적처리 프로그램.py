while(1):
    score = int(input("점수를 입력해주세여"))
    
    if score >= 90:
        print("등급은 A 입니다")
    elif score >= 80:
        print("등급은 B 입니다")
    elif score >= 70:
        print("등급은 C 입니다")
    elif score >=60:
        print("등급은 D 입니다")
    else :
        print("등급은 F 입니다")
        print("재수강 요청")
