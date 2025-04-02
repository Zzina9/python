#1차원 리스트
import random
s_list=[i for i in range(1,26)] #1차원리스트 생성
random.shuffle(s_list)
#random.random(),random.randint(),random.sample,random.shuffle()

#2차원 리스트
my_list=[[0]*5 for _ in range(5)] #2차원리스트 생성
#my_list[0][1]=1#값 변경
#1차원리스트 값-> 2차원리스트 입력
for i in range(5):
    for j in range(5):
        my_list[i][j]=s_list[5*i+j] #5x+y
        
#화면 출력
while True: 
    print(""*5,end="")
    print('[좌표 맞추기 프로그램]')
    print("-"*50)
    print(" ㅣ",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*50)
    for i in range(5) :
        print(f"{i}ㅣ",end="\t")
        for j in range(5):
            print(my_list[i][j],end="\t")
        print()  
    
    print("-"*45)   
    #번호 입력 x표시
    num=int(input("1-25까지 번호를 입력하세요.>>"))
    #25개 모두 비교
    stop=0
    for i in range(5):
        for j in range(5):
            if my_list[i][j]==num:
                my_list[i][j]="x"
                stop=1
                break
        if stop==1:break
            
    #좌표 입력 X표시
    # x=int(input("x좌표를 입력하세요.>>"))
    # y=int(input("y좌표를 입력하세요.>>"))

    # my_list[y][x] ="x"