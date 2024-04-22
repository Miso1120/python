# 정수를 입력 받아 50보다 크고 100보다 작은 경우, 100보다 큰 경우, 50보다 작은 경우의 조건
# 중첩 if 명령을 이용하여 출력할 것.

num = int(input("어떤 수? "))

if num > 100:
 print("입력한 수 {}는 100보다 큽니다.".format(num))
else:
 if num < 100 and num >50:
  print("입력한 수 {}는 50보다 크고 100보다 작습니다.".format(num))
 else:
  if num < 50:
   print("입력한 수 {}는 50보다 작습니다.".format(num))