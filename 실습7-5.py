# animal=["dog","duck","pony","donkey","giraffe","elephant","cat"]가 기억되어 있다.
# 문자열이 5글자 이내인 동물만 출력하는 프로그램을 작성하시오.


animal=["dog","duck","pony","donkey","giraffe","elephant","cat"]
x=len(animal)

for i in animal:
 if len(i) < 5:
  print(i)
