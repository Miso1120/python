# 사용자로부터 어떤 숫자 하나를 입력 받아, 입력한 숫자가 3의 배수인지를 판별하는 프로그램을 삼항 연산자를 이용하여 작성하시오.

in_num = int(input("숫자를 입력하시오: "))

ask =("당신이 입력한 숫자{}는(은) 3의 배수입니다.".format(in_num)) if in_num %3 == 0 else ("당신이 입력한 숫자{}는(은) 3의 배수가 아닙니다.".format(in_num))

print(ask)