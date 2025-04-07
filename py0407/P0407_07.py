class car:
    speed=0
    tire=4
    door=5
    def speedUp(self,s):
        self.speed +=s
        print("현재 속도:",self.speed)
    color="red"
        
class Sedan(car):
    
    color="red"
c=car()    
# print(c.gireType) #없는 변수를 출력시 에러

s=Sedan()
print(s.tire) 