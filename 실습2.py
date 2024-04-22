bunza = int(input("분자 값을 입력하시오: "))
bunmo = int(input("분모 값을 입력하시오: "))

part = bunza // bunmo
last = bunza  % bunmo

print("나눗셈 몫 = {:d}".format(part))
print("나눗셈 나머자 = {:d}".format(last))