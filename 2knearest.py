# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:15:25 2018

@author: Gehad
"""
import pandas as pd
import math 
from statistics import mode




def loaddata(filename):
    dataSet=pd.read_csv(filename)
    dataSetLen=len(dataSet)
    carsdata=[]
    for i in range(0,dataSetLen):
        carsdata.append([dataSet.values[i,j] for j in range(0,7)])
    #price feature
    for i in range (0,dataSetLen):
        if carsdata[i][0]=='low':
            carsdata[i][0]=1
        if carsdata[i][0]=='med':
            carsdata[i][0]=2
        if carsdata[i][0]=='high':
            carsdata[i][0]=3
        if carsdata[i][0]=='vhigh':
            carsdata[i][0]=4
      #maintance price feature
    for i in range (0,dataSetLen):
        if carsdata[i][1]=='low':
            carsdata[i][1]=1
        if carsdata[i][1]=='med':
            carsdata[i][1]=2
        if carsdata[i][1]=='high':
            carsdata[i][1]=3
        if carsdata[i][1]=='vhigh':
            carsdata[i][1]=4
      # no. of doors feature
    for i in range (0,dataSetLen):
        if carsdata[i][2]=='2':
            carsdata[i][2]=2
        if carsdata[i][2]=='3':
            carsdata[i][2]=3
        if carsdata[i][2]=='4':
            carsdata[i][2]=4
        if carsdata[i][2]=='5more':
            carsdata[i][2]=5
     # capacity feature
    for i in range (0,dataSetLen):
        if carsdata[i][3]=='2':
            carsdata[i][3]=2
        if carsdata[i][3]=='4':
            carsdata[i][3]=4
        if carsdata[i][3]=='more':
            carsdata[i][3]=5
    # lug feature
    for i in range (0,dataSetLen):
        if carsdata[i][4]=='small':
            carsdata[i][4]=1
        if carsdata[i][4]=='med':
            carsdata[i][4]=2
        if carsdata[i][4]=='big':
            carsdata[i][4]=3
    #safty
    for i in range (0,dataSetLen):
        if carsdata[i][5]=='low':
            carsdata[i][5]=1
        if carsdata[i][5]=='med':
            carsdata[i][5]=2
        if carsdata[i][5]=='high':
            carsdata[i][5]=3  
    return(carsdata)
    
def calc_distance(traindata,test):
    diff_list=[]
    sumtion=0.0
    distance=0.0
    dis_list=[]
    for i in range(0,len(traindata)):
        for j in range (0,len(test)):
            x1=float(traindata[i][j])
            x2=float(test[j])
            diff=x2-x1
            sqr_diff=diff**2
            diff_list.append(sqr_diff)
        sumtion=sum(diff_list)
        distance=math.sqrt(sumtion)
       # print(distance)
        dis_list.append((distance,traindata[i][6]))
        diff_list.clear()
    return dis_list


def get_nearest(dis):
    nearest=[]
    for i in range(0,5):
        nearest.append(dis[i])
    return nearest

            
def majority_voting(classes):
    clsFreq=[]
    cls=set()
    for c in classes:
        cls.add(c)
    my_cls=list(cls)
    count=0
    for i in range(0,len(my_cls)):
        for j in range(0,len(classes)):
            if my_cls[i]==classes[j]:
                count=count+1
        clsFreq.append((my_cls[i],count))
        count=0
    clsFreq.sort()
    sortCls=[]
    for x,y in clsFreq:
        sortCls.append(x)
    resCls=sortCls[-1]
    return (resCls)


def calc_accurcy(test,orgTest):
    count=0
    for i in range (0,len(test)):
        if test[i][6]==orgTest[i][6]:
            count=count+1
    return (count/len(orgTest))*100

def main():
    carsdata=loaddata("car.data.csv")
    dataSetLen=len(carsdata)
    testData=[]
    trainData=[]
    trainingDataSize=int(.75*dataSetLen)
    for i in range(0,trainingDataSize):
        trainData.append([carsdata[i][j] for j in range(0,7)])
    for i in range (trainingDataSize,dataSetLen):
        testData.append([carsdata[i][j] for j in range(0,6)])
    for testTuple in testData:
        dis=calc_distance(trainData,testTuple)
        dis.sort()
        #print(dis)
        nearest=get_nearest(dis)
            #print(nearest)
        classes=[]
        for x,y in nearest:
            classes.append(y)
        expCls=majority_voting(classes)
        testTuple.append(expCls)
    originalTest=[]
    for i in range (trainingDataSize,dataSetLen):
        originalTest.append([carsdata[i][j] for j in range(0,7)])
    accurcy=calc_accurcy(testData,originalTest)
    print(testData)
    print("Classifier accurcy:",round(accurcy,2),"%")
    
            
if __name__ =='__main__':
    main()
