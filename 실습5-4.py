# 사용자로부터 물건 가격을 입력받아, 물건 가격이 6만원 이상인 경우 할인 대상에 포함될 수 있는지를 판별하는 프로그램을 삼항 연산자를 이용하여 작성하시오.

pay = int(input('물건 가격을 입력하시오:'))

over6 = True if pay > 60000 else False

print("상품 가격 ? {}".format(pay))
print("할인대상 :{}".format(over6))
