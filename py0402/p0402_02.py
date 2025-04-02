#문자열

print('1234'.isdigit()) #숫자인지 확인
print('abc'.isalpha()) # 알파벳인지 확인
print('abc123'.isalnum) # 글자및 숫자인지 확인
print('ABC'.islower()) #모두 소문자인지 확인
print('ABC'.isupper()) #모두 대문자인지 확인

# a="1234"
# if a.isdigit(): #숫자로 변환가능
#   print("숫자로 가능합니다.")
#my=int(input("숫자를 입력하세요.>>")) 

# while True:
#     my_input= input("숫자를 입력하세요.>>") 
#     if my_input.isdigit():
#         my_input=int(my_input)
# else:
#     print("숫자가 아닙니다. 숫자를 입력하셔야 합니다.")    
  
#map(함수,데이터값)
# score=['100','99','90']
# #함수
# def cal(x):
#     return int(x)*100
# s_list=list(map(cal,score))
# print(s_list)

# sum=0
# for s in score:
#     sum=sum+int(s) #형변환 str->int
# print("합계:",sum)  
 
# txt=","
# txt2=txt.join("안녕")
# print(txt2)


#데이터베이스(db)는 리스트를 저장할 수 없음
#문자열
# txt="1/홍길동/100/100/100/300/100/0/1"
# txt_list=txt.split("/")
# print(txt_list)
# txt_list[1]='유관순'
# print(txt_list)

# txt="a,b,c,d,안녕,반가워"
# txt_list=txt.split(",")
# print(txt_list)


# txt="안녕하  세요"

# print(txt.replace("","")) #문자를 다른 문자로 치환

# txt2="파이썬 공부가 너무 시러요~너무 시러요.파이썬은 재미있어요."
# print(txt2.replace("파이썬","자바"))
# txt3="----파이썬----"
# print(txt3.strip("-")) #특장글자제거
# print(txt3.replace("-",""))

# print(txt)
# print(txt.strip()) #공백제거-rsstrip():오른쪽 공백 제거,lstrip(): 왼쪽

# txt="파이썬 공부가 너무 시러요~너무 시러요.파이썬은 재미있어요."
# print(txt.count("파이썬")) #문자열의 검색하려고 하는 글자 갯수
# print(txt.count("요"))
# print(txt.find("공부"))#있을때 index 번호
# print(txt.find("자바")) #없을때-1

t="aaa.py"
print(t.endswith("py")) #있으면 True, 없으면 False

# txt="abBBcDd hello apple" #대소문자
# print(txt.upper())#대문자 출력
# print(txt.lower())#소문자
# print(txt.swapcase())#대문자는 소문자로, 소문자는 대문자로
# print(txt.title()) #단어 첫글자 대문자

# a_list=[1,2,3,4,5]

# print(a_list[1:3]) #1,2
# print(txt[1:3]) #녕하
# print(txt[2:])
# print(txt[:3])

# print(txt*3)
# print("-"*50)
# print(len(txt)) #글자길이

# print(txt[::-1]) #글자역순출력

# 문자열 index 번호 가짐.
# print(txt[1])
# print(a_list[1])