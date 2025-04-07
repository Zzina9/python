#파일 입출력: 파일 열기-파일 읽기, 파일 쓰기-파일 닫기
#파일 열기-3가지 모드:r:읽기 모드,w:쓰기 모드,a:추가 모드,b:이진파일-파일 복사
# f=open("a.txt","r") #읽기 모드
# f=open("a.txt","w") #쓰기 모드
# f=open("a.txt","a") #추가 모드

#news.txt 파일 출력하시오.
f= open("py0404/news.txt","r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close()

# f=open("py0404/news.txt","r",....)

#파일 읽어오기-절대 경로
# f= open("c:/workspace/python/a.txt","r",encoding="utf-8")
# f= open("/py0404/b.txt","r",encoding="utf-8") #폴더안에 있는 파일 읽어오기
# for line in f:
#     print(line.strip())
# f.close()

# while True:#3줄
#     line= f.readline()
#     if not line:break
#     print(line.strip())
# f.close()



#파일 읽기-readlines():모두 읽어오기
# f=open("a.txt","r",encoding="utf-8")
# lines= f.realines() #모두 읽어오기
# for line in lines:
#     print(line.strip())
# f.close()

# f=open("a.txt","r",encoding="utf-8")
# print(type(f))
# for line in f:
#     print(line.strip())
# f.close()

# print("완료되었습니다.")