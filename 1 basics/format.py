def prStr():
    s="num1:{0} num2:{1} num3:{2}" .format(100,200,300)
    print (s)
    s="{0:<10}{1:<10}{2:<10}".format("appleapple","banana","grape")
    print(s)
    s="{0:>10.2f}".format(3.1415926)
    print(s)
prStr()    