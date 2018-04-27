def bmi(kg,m):
    return kg/ (m*m)
def check(kg,m=2,name="guest"):
    b=bmi(kg,m)
    print(name,'BMI=',b)
check(43,1.53,name="me")
check(43,1.53)

