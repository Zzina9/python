#구구단을 출력하시오.
for i in range(1,10):
    
    for j in range(2,10):
        print("{} x {} = {}".format(j,i,i*j),end="   ")
    print()
        
# ## 은행가면 001 002 003 ...0103 011 012..999
# for i in range(1,1000):
#     print("{:03d}".format(i))
    