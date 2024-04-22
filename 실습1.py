
i = 0
oddcnt = 0

for i in range(5):
 num = int(input("어떤 수:"))
 if num %2 != 0:
  print("{}은(는) 홀수입니다.".format(num))
  oddcnt += 1
 else:
  print("{}은(는) 짝수입니다.".format(num))
print("홀수 개수 : {}".format(oddcnt))



