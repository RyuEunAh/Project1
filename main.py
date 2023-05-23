## 함수 선언부 (=메서드)
def add_func(n1,n2) :
    result = n1+n2
    return result

def sub_func(n1,n2) :
    return n1-n2


## 전역 변수부 (=인스턴스 변수)
num1, num2, res = 100, 200, 0


## 메인 코드부 (=main()메서드)
res = add_func(num1,num2)
print(num1,'+', num2,'=',res)

res = sub_func(num1, num2)
print(num1,'-',num2,'=',res)
