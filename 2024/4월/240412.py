# 파라 240413
# oop : 객체 지향 언어
# oop의 첫 걸음, 캡슐화
# 파이썬에서는 다른 사용자가 바꾸면 안되는 것을 __을 붙여서 변수 선언.
# 두 번째, 상속class 안에는 변수도 있고 함수도 있음
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         return
#     def move(self):
#        return
   
# class Dog(Animal):
#     def __init__(self, name, age):         # 위 class는 Dog가 Animal을 상속         
#        super().__init__(name, age) # 부모 클래스
#     def eat(self):
#         return "개가 밥을 먹는다."
#     def __str__(self):
#         return f"{self.name}/{self.age}"
    
# myDog = Dog("뽀삐", 17)
# urDog = Dog("봉구", 6)
# print(myDog.name, urDog.name)# $ 뽀삐 봉구
# print(myDog)# $ 뽀삐 /17
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def eat(self):
#         return "고양이가 밥을 먹는다"
#     def __str__(self):
#         return f"{self.name}/{self.age}"
# myCat = Cat("레오", 119) # oop를 쓰면 유지보수가 편함.
# # # pip install pygame
# import pygame, sys, datetime, time
# colors = {"RED":(255, 0, 0), "BLUE":(0,0,255),"GREEN":(0, 255, 0), "BLACK":(0, 0, 0), "WHITE":(255, 255, 255)}
# HEIGHT= 600
# WIDTH = 600
# EMPTY = 0
# RED = 1
# BLUE = 2
# block = [[EMPTY]*3 for i in range(3)]
# def winCheck():
#     for i in range(3):
#         if block[i][0] == block[i][1] == block[i][2] != EMPTY:
#             return block[i][0]
#         if block[0][i] == block[1][i] == block[2][i] != EMPTY:
#             return block[0][i]
#     if block[0][0] == block[1][1] == block[2][2] != EMPTY:
#         return block[0][0]
#     if block[0][2] == block[1][1] == block[2][0] != EMPTY:
#         return block[0][2]
#     return EMPTY
# def main():    
#     pygame.init()
#     display = pygame.display.set_mode([WIDTH, HEIGHT], False)
#     run = True; turn = 0 # 나중에 사용될 유저 순서값   while run:

#     # pygame.display_set_caption("파라는 내꺼 틱택토")
#     return