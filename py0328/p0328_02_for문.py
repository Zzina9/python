print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")

#range(3) ->0,1,2
for i in range(3):
    print("안녕하세요.",i)
#range(1,4) -> 1,2,3:4앞에까지 출력
for i in range(1,4):
    print("안녕하세요.",i)
    
for i in range(1,3+1):
    print("안녕하세요.")
    
for i in range (1,11,2):
    print("안녕",i) 

#range(1,11,5)-첫번째 숫자:시작 번호, 두번째 숫자:마지막 번호 -1만큼, 세번째 숫자: 간격
for i in range(1,11,5):
    print("안녕",i)
    
#range()자리에 list타입 가능   
a_list = [1,2,3,4,5]
for i in a_list:
    print("안녕",i)
    