# #조건문 <if,if~else,if
# #3가지 조건
# #음수,0,양수

# num=int(Input("숫자를 입력하세요.>>"))

# if num>0:
#     print("양수입니다.")

# # elif num==0:
# #     print("0입니다")
# # else:
# #     print("음수입니다.")

# #60점 이상이면 합격, 60점 미만 불합격 출력하시오.
# num=int(input("점수를 입력하세요."))
# if num>60:
#     print("합격입니다.")
# else:
#     print("불합격입니다.")
    
# num=int(input("점수를 입력하세요."))
# if num>70:
#      print("합격입니다.")
# elif 69>=num>=60:
#     print("재시험 입니다")
# else:
#     print("불합격입니다.")

#시험-> 90점이상 A, 80점 이상 B, 70점 이상 c, 60점이상 D,F
#100~97점 A+,96~93 A, 92~90 A-, 89~87점 B+, 86~83 B, 82~80 B-
score = int(input("점수를 입력하세요.>>"))

if score>=90:
     print("A", end="")
     if score>=97:print("+")
     elif score>=93:pass
     else:print("-")
elif score>=80:
    print("B", end="")
    if score>=87:print("+")
    elif score>=83:pass
    else:print("-")
     
elif score>=70:
     print("C", end="")
     if score>=77:print("+")
     elif score>=73:pass
     else:print("-")
elif score>=60:
     print("D",end="-")
     if score>=67:print("+")
     elif score>=63:pass
else:print("-")
    

# print("안녕",end="") #줄단락 #end 옵션 사용하면 줄바꿈을 하지 않음.
# print("하세요")


    