#1-100까지 랜덤 숫자를 생성해서 정답을 맞추는 프로그램을 구현하시오.
#1.랜덤숫자 생성
#2.num list 생성
#3.n변수 생성
import random
num=[]
num =[]
# 1-100 랜덤 숫자 1개 생성
ran_num=random.randint(1,100)
n =0 #몇 번 시도
for n in range(1,11):
    in_num= int(input("숫자를 입력하세요.>>"))
    num.append(in_num)
    if ran_num==in_num:
        print("정답입니다.랜덤숫자:{}".format(ran_num)) 
        break  
    elif ran_num>in_num:
        print("더 큰 수를 입력하셔야 합니다.입력숫자:{}".format(in_num))
    else:
        print("더 작은 수를 입력하세요.입력숫자:{}".format(in_num))

print("도전 횟수:{}".format(n))
print("입력숫자:{}".format(num))
print("랜덤 숫자:{}".format(ran_num))