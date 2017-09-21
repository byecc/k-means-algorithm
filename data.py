from random import *
from matplotlib import pyplot

rand = Random()
rand.seed(0)
vari = 0.2
x1num = 100
x1 = [rand.normalvariate(2,vari) for i in range(0,x1num)]
y1 = [rand.normalvariate(2,vari) for i in range(0,x1num)]
l1 = [0 for i in range(0,x1num)]

x2num = 100
x2 = [rand.normalvariate(1,vari) for i in range(0,x2num)]
y2 = [rand.normalvariate(1,vari) for i in range(0,x2num)]
l2 = [1 for i in range(0,x2num)]

x3num = 100
x3 = [rand.normalvariate(1,vari) for i in range(0,x3num)]
y3 = [rand.normalvariate(2,vari) for i in range(0,x3num)]
l3 = [2 for i in range(0,x3num)]

x = x1+x2+x3
y = y1+y2+y3
label = l1+l2+l3

total = x1num+x2num+x3num
colors = ['red','green','blue','black']
data_color = [colors[i] for i in label]
pyplot.scatter(x,y,color=data_color,alpha=0.8)
pyplot.show()

pyplot.scatter(x,y,color=colors[3],alpha=0.8)
pyplot.show()

# zx=[0.2,0.3,0.4,0.5]
# zy=[0.2,0.3,0.4,0.5]
# pyplot.scatter(x,y,color=colors[3],alpha=0.8)
# pyplot.scatter(zx,zy,color=colors,s=250,alpha=0.8)
# pyplot.show()

zx=[1.25,1.5,1.75]
zy=[1.25,1.5,1.75]

nzx = [0,0,0]
nzy = [0,0,0]

while zx!=nzx and zy!=nzy:

    pl=[]
    for i in range(0,total):
        minj,mind=-1,-1
        for j in range(len(zx)):
            dist = (x[i]-zx[j])*(x[i]-zx[j])+(y[i]-zy[j])*(y[i]-zy[j])
            if mind<0 or dist<mind:
                minj,mind=j,dist
        pl.append(minj)
    data_color = [colors[l] for l in pl]
    pyplot.scatter(x,y,color=data_color,alpha=0.8)
    pyplot.scatter(zx,zy,color=colors,s=250,alpha=0.8)
    pyplot.show()

    for l in range(3):
        N,sumx,sumy=0,zx[l],zy[l]
        for i in range(0,total):
            if pl[i]==l:
                N+=1
                sumx += x[i]
                sumy += y[i]
        zx[l],zy[l] = sumx/N,sumy/N
    print(zx,zy)
    pyplot.scatter(x,y,color=data_color,alpha=0.8)
    pyplot.scatter(zx,zy,color=colors,s=250,alpha=0.8)
    pyplot.show()

