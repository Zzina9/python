#     학생성적 프로그램
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
