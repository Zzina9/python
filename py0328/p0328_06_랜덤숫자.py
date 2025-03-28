# 숫자 맞추기 프로그램
import random


input_list=[] #입력한 숫자 저장 리스트타입
#randiant(1,45) 1~45번 사이의 숫자 1개를 가져옴.
lotto =random.randint(1,45)

#---------
for i in range(10):
    input_num=int(input("{}번째 숫자를 입력하세요.(1~45번 사이)>>".format(i+1)))
    input.list.append(input_num)
    #랜덤번호와 입력번호 비교
    if lotto==input:
        print("당첨")
        break # for문 종료
    elif lotto>input_num:
        print("틀렸습니다.{}보다, 더 큰 수를 입력하세요!".format(input_num))
    else:
        print("틀렸습니다.{}보다, 더 작은 수를 입력하새요!".format(input_num))
    
#-------------------
print("랜덤번호:{}".format(lotto))
print("입력번호:{}".format(input_num))