# 좌표 맞추기 프로그램을 구현하시오.
import random
#1차원 리스트 생성후 랜덤 섞기
first_list=[i+1 for i in range(25)]
random.shuffle(first_list)

#2차원 리스트 생성후 1차원 리스트 값을 넣기
a_list=[[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j]=first_list[5*i+j]
        
#2차원 형태로 출력
while True:
    print(" [좌표 맞추기 프로그램]")
    print("-"*45)
    print("*ㅣ",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print('-'*45)
    for i in range(5):
        print(f"{i}ㅣ",end="\t")
        for j in range(5):
            print(a_list[i][j],end="\t")
        print()
#입력부분
print("-"*50)



