#파이썬 타입
#bool 타입, 숫자- int 타입, float 타입 , str 타입

#bool 타입-true, false
#int타입- 정수형 타입 소수점 없음
#float 타입- 실수형 타입: 소수점 있음
#str타입-문자열 타입:"",''안에 입력을 해야 함

# if True:
#     print("참입니다.")
    
# if False:
#     print("거짓입니다.")
# if 10>3:
#     print("정상")
# else:
#     print("비정상")
# if True:
#     print("정상")
# print(10>3)

#타입 변경 문자열 -> 숫자형태 일 경우
# #print(int("안녕1")) #숫자 형태 문자열만 숫자 타입으로 변경 가능

# print(int("1")+1) #"" str 타입
# #숫자를 타입 변경-int 타입,float 타입으로 변경 가능
# print(int(1.5)) #실수형-> 정수형으로 타입 변경: 소수점이 사라짐.
# #문자열 float타입을 int타입으로 변경 안 됨.
# print(int("1.5")) #error
# print(float("1.5"))# 가능
# print(str(1.5)) #문자열 타입 변경

# # print(1+2)
# # print(1+1.2)

# # # print("안녕"+1) #타입이 다른 경우 error
# # print("안녕",1)
# # print("숫자: {:.2f}".format(10/3))

# #-----------
# #변수
# a=10 # = 할당의 의미
# a=5 #int 타입
# b=1.5 #float타입  
# c="안녕" #str타입

# print(c+a) #str 타입 +int 타입 더하기 연산은 불가능
# print(a+b) #int 타입 + float 타입 더하기 가능 (숫자)

# #list 타입- 값을 여러개 저장 
# list_a=[1,2,3,4]
# print(list_a)
# print(list_a[0] +list_a[1]+list_[2] +list_a[3])

# #input():데이터를 입력 받는 명령어-str타입 1개
# score= input("데이터를 입력하세요.>>") 
# print("입력 데이터:",score)   

## 두 수를 입력 받아 합계, 평균을 출력하시오.
# num1=input("숫자를 입력하세요.>>")
# num2=input("숫자를 입력하세요.>>")
# print(num1+num2) #100 200

# #문자열 타입->int타입으로 변경
# num1= int(input("숫자를 입력하세요.>>"))
# num2=int(input("숫자를 입력하세요.>>"))
# print(num1+num2) #300

# #조건문
# # score=int(input("점수를 입력하세요."))
# # if score>60:
# #     print("합격")
# # else:
# #     print("불합격")

# if score>=70:
#     print("합격")
# elif score>=60:
#     print("재시험")
# else:
#     print("불합격")

score=int(input("점수를 입력하세요.>>"))
#90점 이상 A,B,C,D,F 출력하시오.
if score>=90:print("A")
elif score>=80:print("B")
elif score>=70:print('c')
elif score>=60:print('D')
else: print('F')
