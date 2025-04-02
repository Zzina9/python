a_list=[["x","x","x","x","x","x"],[6,"x",8,9,10]]

#현재 리스트의 x개수 확인
no=0
for i in range(5):
    if a_list[0][i]=="x":
        no+=1
if no==5:
    print("빙고 완성!!")       
print(f"현재[0]방의 x개수:{no}")        
        
    

