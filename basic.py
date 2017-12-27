import math
# 출력
# print(10 + 5)
# print(10 * 5)

# ceil(올림), floor(내림), pow(자승), pi(파이)
# print(math.ceil(2.2))   # 올림
# print(math.floor(2.7))  # 내림
# print(math.pow(2,10))   # 승수
# print(math.pi)          # 파이

# 출력 2
# print('Hello ' + 'world')
# print('Hello ' * 3)
# print('Hello'[0])
# print('Hello'[1])

# 출력 3
# print('hello world'.capitalize())
# print('hello world'.upper())    # 대문자
# print('HELLO WORLD'.lower())    # 소문자
# print('hello world'.__len__())  # 길이
# print(len('hello world'))       # 길이
# print('Hellow world'.replace('world','programming')) # 문자 대체

# 특수문자
# print("#egoing's \"tutorial\"")
# print("\\")
# print("Hello\nworld")
# print("Hello\t\tworld")
# print("\a")

# str, int
# print(10+5)
# print("10"+"5")

# 변수 선언
# x=3
# y=7
# print(x*y)
# title = "python"
# print("Title is " + title)

# 수계산과 변수사용
# donation = 20
# student = 2
# sponsor = 10
# print((donation * student) / sponsor)

# 비교
# a = 1
# b = 1
# print("a==b : ", a==b)
# print("a==2 : ", a==2)
# print("1 > 2: ", 1 > 2)
# print("1 < 2: ", 1 < 2)

# 기초 조건문
# if True :
#     print("code1")
#     print("code2")

# input = 100
# real = 50
# if real == input:
#     print("일치")
# else :
#     print("불일치")

# input = 2
# real  = 1
# real2 = 2
# if real == input :
#     print("일치")
# elif real2 == input :
#     print("일치2")
# else :
#     print("불일치")

# type 자료형 출력
# var1 = 'Hello python'
# print(type(var1))
# var2 = 10
# print(type(var2))
# var3 = 123.456
# print(type(var3))

# 참조변수
# a = 10
# b = 12.34
# c = b
# d = 20
# id : memory address
# print(a); print(id(a))
# print(b); print(id(b))
# print(c); print(id(c))
# print(d); print(id(d))
# print(a == 20)
# print(a == d)
# print(a is b)
# print(b is c)
# print(a is d)

# 변수에 값 할당
# v1 = v2 = v3 = 10
# print(v1, v2, v3)

# end 같은 줄에 중복 출력
# print('출력1', end = ' // ')
# print('출력1')
# print("출력2")

# 변수 초기화
# v1, v2 = 100, 200
# print(v1, v2)
# v2, v1 = v1, v2
# print(v1, v2)

# 패킹(packing) 할당
# v1, *v2 = [1,2,3,4] # vector
# print(v1, '\n', v2)
# *v1, v2 = [1,2,3,4] # vector
# print(v1, '\n', v2)

# print 출력 양식
# print(format(3.15427, '8.3f'))     # 총8자리 소수점3자리
# print(format(102145, '20d'))       # 총 20칸
# print(format(10212334, '3,d'))      # 3개 단위로 찍기

# print 양식 문자
# num1 = 10; num2 = 20
# tot = num1 + num2
# print('%d + %d = %d' %(num1, num2, tot))
# print('%s 입니다. 점수는 %d' %('김지환', 95))
# print('전체 %d%%가 %dcm 입니다' %(60, 173))

# 외부상수 출력
# print("이름은 {} 이고, 나이는 {} 입니다".format('김지환', 22))
# print("이름은 {0} 이고, 나이는 {1} 입니다.".format('김지환', 22))
# print("나이는 {1} 이고, 나이는 {0} 입니다.".format('김지환',22))

# 산술, 관계, 논리 연산자
# 산술 > 관계 >  논리 > 대입연산자
# print('산술연산자 ', 10+3, 10-3, 10*3, 10/3, 10//3, 10%3)
# print('관계연산자 ', 5 > 3, 5 < 3, 5 >= 3, 5==3, 5!=3)
# print('논리연산자 ', 5 > 4 and 5 == 3, 5 > 4 or 5 == 3, not(5==3))

# 카운터 변수 +=
# cnt = 0
# cnt = cnt + 1
# cnt += 1
# print('cnt : ', cnt)

# escape 문자 처리
# print('홍길동')
# print('\n줄바꿈')
# print('\\n줄바꿈')
# print(r'\n줄바꿈')
# print("c:\\\'aa\\\"abc.txt")

# input 키보드 입력
# a = int(input('첫번째 수 입력 : '))
# b = int(input('두번째 수 입력 : '))
# print("%d + %d = %d" %(a, b, a+b))
# c = float(input('실수 입력 : '))
# print("%5.2f" %(c))

# 사각형 넓이 구하기
# w = float(input("가로 : "))
# h = float(input("세로 : "))
# area = w * h
# print("%f" %(area))

# int(숫자), str(문자), bool(T/F)
# print(10, type(10))
# print(10.125, type(10.125))
# print("홍길동", type("홍길동"))
# print(10 >= 5, type(10 >= 5))

# 2(bin), 8(oct), 16(hex) 진법
# print(10, bin(10), oct(10), hex(10))
# print(10, 0b1010, 0o12, 0xa)

# 문자열 처리
# str = "우리나라 대한민국 나의 조국은 대한민국입니다."
# print(str, type(str))
# len (길이)
# print('str 길이 : ', len(str))
# print(str[0:11])
# print('국 글자수 : ', str.count('국'))
# 시작문자 유무
# print(str.startswith('우리'))

# str2 = "김지환"
# result = str2[0];   print(result)
# result = str2[0:3]; print(result)
# result = str2[:3];  print(result)
# result = str2[-1];  print(result)
# result = str2[-3:-2];   print(result)

# split 문자열 나누기
# str3 = "나는 홍길동입니다. 나이는 28세이고 주소는 서울 입니다."
# str4 = str3.split(sep= ' ')
# print('str4 : ', str4)
# join 문자열 합치기
# str5 = ' '.join(str4)
# print('str5 : ', str5)

# 기본 자료구조
# list 자료구조
# list = [1,2,3,4]
# print(type(list))
# print(list)
# print(list[1:2])
# list[2] = 6
# print(list)
# list.append(5)    # node 추가
# print(list)
# print(list[::2])  # 2개씩 건너뛰기

# 튜플(tuple) 자료구조 # 수정이 불가능
# t = (1,2,3,4)
# print(type(t))
# print(t)

# set 자료구조
# 순서가 없어 index 불가능 # 중복불가 # {}로 만든다
# s = {1,2,3,4,5,1,2}
# print(s, type(set)) # 중복은 빼고 출력

# dict
# 순서가 없어 index 불가능 # 출력 순서 랜덤 # 중복 불가 # 원소는 중복가능
# d = {'name':'홍길동', 'age':25, 'address':'서울시'}
# print(d, type(d))
# print(d['age'])     # key 접근

# 자료구조 변환
# set -> list 변환
# s = {1,2,3,4,5,1,2}
# print(s, type(s))
# l = list(s)
# print(l, type(l))

# list -> set 변환
# l   = ['a', 'b', 'c', 'b', 'c']
# print(l, type(l))
# l2  = list(set(l))
# print(l2, type(l2))

# if 조건문
# var = int(input("입력 : "))
# if var >= 50 :
#     print('var는 50 이상')

# N = int(input("숫자입력 : "))
# if N == 0 :
#     print("N은 0")
# elif N % 2 == 0 :
#     print("N은 짝수")
# else :
#     print("N은 홀수")

# while 문
# i = 1 # 카운터 변수
# t = 0 # 누적 변수
# while i <= 5 :
#     print('i= ', i, end= ' ')
#     t += i
#     print('t= ', t)
#     i += 1

# 1 ~ 50 사이의 5의 배수 합 구하기
# i = 1
# total = 0
# while i <= 50 :
#     if i % 5 == 0 :
#         print(i, end=' ')
#         total += i
#     i += 1
# print("total : ", total)

# 3의 배수이면서 2의 배수가 아닌 수의 합
# i = 1;
# while i <= 50 :
#     if i % 3 == 0 and i % 2 != 0 :
#         print(i, end= ' ')
#     i += 1

# while True:
#     a = int(input('data : '))
#     if a == 0 :
#         print("탈출")
#         break
#     print('a : ', a)

import random
# r = random.randint(1,5)
#
# while True :
#     i = int(input("숫자입력 : "))
#     if(i == r) :
#         print("성공")
#         break

