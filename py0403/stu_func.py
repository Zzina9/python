def stu_output(title,students):
    print('[학생 성적 츨력]')
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60) 
    for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()

#화면 출력 함수 선언
def stu_print():
    
    print('[학생 성적 프로그램]')
    print("-"*40)
    print("1.학생 성적 입력")
    print("2.학생 성적 출력")
    print("3.학생 성적 수정")
    print("4.등수처리")
    print("0.프로그램 종료")
    print("-"*40)
    choice=int(input("원하는 번호를 입력하세요.>>"))
    return choice

def stu_input(count,students):
    no=count
    name=input(f"{no}번 학생 이름을 입력하세요.")
    kor=int(input("국어 점수를 입력하세요.>>"))
    eng=int(input("영어 점수를 입력하세요."))
    math=int(input("수학 점수를 입력하세요."))
    total=kor+eng+math
    avg=total/3
    rank=0
    students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
    
    count+=1
    return count

def stu_rank(students):
    print("[등수처리]")
    for s in students:
            num=1
            for ss in students:
                if s['total']<ss['total']:#등수비교
                    num+=1                #등수1증가
            s['rank']=num                 #등수입력
    print("등수 처리가 완료되었습니다.")
    print()