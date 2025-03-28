# #파이썬 변수 타입
# #변수 선언
# 변수=10
# a = 20
# num = 30

# #print()
# print("안녕")
# print("입력된 숫자",a)
# print ("입력된 숫자 : %d" % (a))
# print("입력된 숫자 : {}".format (a))

# print(f "입력된 숫자": {a})

# #입력 - input => 타입 : str 타입
# # 입력된 값은 타입 : str 타입이기 때문에 형변환을 해줘야 함.
# num1= input ( "숫자를 입력하세요.>>")
# num2=float(input("숫자를 입력하세요.>>"))
# print("입력된 숫자 : {} , {}/ 합계 : {}".format (num1,num2,num1+num2))

# 학생성적 프로그램
#이름, 국어, 영어, 수학 입력받아, 합계와 평균을 출력하는 프로그램을 구현
print("-"*50)
print("           학생성적프로그램")
print("-"*50)
name=input("이름을 입력하세요.>>") #str 타입
kor=int(input("국어점수를 입력하세요.>>"))
eng=int(input("영어 점수를 입력하세요.>>"))
math=int(input("수학 점수를 입력하세요.>>"))
total= kor+eng+math
avg=(kor+eng+math)/3
print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print("_"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,kor+eng+math,(kor+eng+math)/3))
