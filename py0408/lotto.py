#lotto 프로그램

import random
my_list=[]
lotto_count=0
lotto_list=[]
ran_list=random.sample(range(1,45+1),6)

i=0
while i<6:
    print("랜덤 번호:{}".format(ran_list))
    my_input=int(input("{}번째 숫자를 입력하세요.".format(i+1)))
    if my_input not in my_list:
        my_list.append(my_input)
        i+=1
        
for j in range(6):
    if ran_list[j] in my_list:
     lotto_count =lotto_count +1
     lotto_list.append(my_list[j])
        
print("랜덥 번호:{}".format(ran_list))
print("입력 번호:{}".format(my_list))
print("당첨 갯수:{}".format(lotto_count))
print("당첨 번호:{}".format(lotto_list))


