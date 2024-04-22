# 5과목의 점수를 입력하여 과목 40점 이상, 전과목 평균 60점 이상이면 "합격" 출력
#그렇지 않다면 불합격을 출력하도록 프로그램을 작성하시오.

c1 = int(input("소프트웨어 설계 : "))
c2 = int(input("소프트웨어 개발 : "))
c3 = int(input("데이터베이스 구축 : "))
c4 = int(input("프로그래밍언어 활용 : "))
c5 = int(input("정보시스템 구축 관리 : "))
tot = c1+c2+c3+c4+c5
averge = tot / 5


if averge >= 60 and (c1 >= 40 and c2 >= 40 and c3 >= 40 and c4 >= 40 ):
  print("평균 :{}".format(averge))
  print("결과 :합격")
else:
  print("평균 :{}".format(averge))
  print("결과 :불합격")
