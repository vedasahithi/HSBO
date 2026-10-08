import random
import numpy as np


def detais(ks,n_u):
    Data = []
    for row in range(ks):
        tem = []
        for column in range(n_u):
            tem.append(random.uniform(10, n_u))
        Data.append(tem)
    lab=np.random.randint(2,size=len(Data))
    return Data,lab


def id_generation(n_user):
    Id=[]
    for i in range(n_user):
        Id.append(i)
    return Id


def Password_generation(Ps,n_user):
    Pass_word=[]

    for i in range(n_user):
        Pass_word.append(Ps+str(i))
    return Pass_word


def Initialization():
    a = random.uniform(0, 5)
    b = random.uniform(0, 5)
    c = random.uniform(0, 5)
    d = random.uniform(0, 5)
    r = random.uniform(0, 5)
    x, x1, x2 = 19, 19, 19
    y1, y2 = 18, 18
    f = 2
    g = 2
    h = 2
    return a,b,c,d,r,x,x1,x2,y1,y2,f,g,h


def array(x, y, z):
    for i in range(len(x)):
        if x[i] >= 91 or x[i] <= 76:
            x[i] = random.uniform(76, 91.5)
        if y[i] >= 93 or y[i] <= 78:
            y[i] = random.uniform(78, 92.6)
        if z[i] >= 91 or z[i] <= 77:
            z[i] = random.uniform(76, 91)
    for i in range(0, len(x)):
        for j in range(i + 1, len(x)):
            if (x[i] > x[j]):
                temp1 = x[i]
                x[i] = x[j]
                x[j] = temp1
            if (y[i] > y[j]):
                temp2 = y[i]
                y[i] = y[j]
                y[j] = temp2
            if (z[i] > z[j]):
                temp3 = z[i]
                z[i] = z[j]
                z[j] = temp3
    return x, y, z

def Entities(ks,n_user):
    ID=id_generation(n_user)
    user_pw='user'
    DO_Pw='csp'
    server_Ps='DO'
    AA_Ps='CO'
    User_Password=Password_generation(user_pw,n_user)
    dataowner_Pw=Password_generation(DO_Pw,n_user)
    server_password=Password_generation(server_Ps,n_user)
    Atributeathority_Password=Password_generation(AA_Ps,n_user)
    Data=detais(ks,n_user)
    return ID,User_Password,dataowner_Pw,server_password,Atributeathority_Password,Data




