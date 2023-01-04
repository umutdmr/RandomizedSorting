from numpy import random

def create_input_with_type(n,int_type):
    if int_type==1:
        return list(random.randint(10*n,size=(n,)))
    elif int_type==2:
        return list(random.randint(int(n*(3/4)),size=(n,)))
    elif int_type==3:
        return list(random.randint(int(n/4),size=(n)))
    elif int_type==4:
        return [1] * n
    else:
        raise "Wrong type"
