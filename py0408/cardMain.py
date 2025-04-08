#카드 프로그램-card 객체 사용
class Card:
    #self.shape
    #self.number
    #__str__
    pass
class CardFunc:
    #함수
    pass
#cardMain.py
#카드리스트 호출
#카드객체 호출 45장
#각각 5장을 나눠준 다음,비교해소 큰 수가 승리하는 형태로 구현

import random

class Card:
    def __init__(self, shape, number):
        self.shape = shape  # 모양: 하트, 스페이드 등
        self.number = number  # 숫자: 1~13

    def __str__(self):
        return f"{self.shape} {self.number}"