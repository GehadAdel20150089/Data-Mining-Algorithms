# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:10:18 2018

@author: Gehad
"""

import pandas as pd
from itertools import combinations 

def calc_p_class(trainingData,Class):
    count=0
    for i in range(0,len(trainingData)):
        for j in range(0,7):
            if trainingData[i][j]==Class:
               count=count+1
    prop=count/len(trainingData)
    return prop
    
    
def calc_p_feature_class(trainingData,Class,feature,fno):
    count=0
    counter=1
    for i in range(0,len(trainingData)):
        for j in range(0,7):
            if trainingData[i][j]==Class:
               count=count+1
            if  trainingData[i][j]==Class and trainingData[i][fno]==feature:
                counter=counter+1
    prop=counter/count
    return prop


def calssifier(trainingData,test):
    p_unacc=calc_p_class(trainingData,'unacc')
    p_acc=calc_p_class(trainingData,'acc')
    p_good=calc_p_class(trainingData,'good')
    p_vgood=calc_p_class(trainingData,'vgood') 
    cls=[p_unacc,p_acc,p_good,p_vgood]
    #print(p_unacc)
    #print(p_acc)
    #print(p_good)
    #print(p_vgood)
    classes=['unacc', 'acc', 'good', 'vgood']
    feature1=['vhigh', 'high', 'med', 'low']
    feature2=['vhigh', 'high', 'med', 'low']
    feature3=['2','3', '4', '5more']
    feature4=['2','4','more']
    feature5=['small', 'med', 'big']
    feature6=['low', 'med', 'high']
    
    #price feature fno=0
    p_price=[]
    #print("price feature")
    for c in classes:
        for f in feature1:
            #print(c,f)
            p_price.append((c,f,calc_p_feature_class(trainingData,c,f,0)))
    #mprice feature fno=1
    p_mprice=[]
    #print("mantience price feature")
    for c in classes:
        for f in feature2:
            #print(c,f)
            p_mprice.append((c,f,calc_p_feature_class(trainingData,c,f,1)))
    #no. of doors feature fno=2
    p_doorsnum=[]
    #print("no. of doors feature")
    for c in classes:
        for f in feature3:
            #print(c,f)
            p_doorsnum.append((c,f,calc_p_feature_class(trainingData,c,f,2)))
    #Capacity in terms of persons to carry fno=3
    p_capacity=[]
    #print("Capacity in terms of persons to carry")
    for c in classes:
        for f in feature4:
            #print(c,f)
            p_capacity.append((c,f,calc_p_feature_class(trainingData,c,f,3)))
    #the size of luggage boot
    p_lug=[]
    #print("the size of luggage boot")
    for c in classes:
        for f in feature5:
            #print(c,f)
            p_lug.append((c,f,calc_p_feature_class(trainingData,c,f,4)))
    #Estimated safety of the car
    p_safty=[]
    #print("Estimated safety of the car")
    for c in classes:
        for f in feature6:
            #print(c,f)
            p_safty.append((c,f,calc_p_feature_class(trainingData,c,f,5)))
    #print(p_price)
    #print(p_mprice)
    #print(p_doorsnum)
    #print(p_capacity)
    #print(p_lug)
    #print(p_safty)
    
    #TESTING
    p_props=[]
    for c in classes:
        for x,y,z in p_price:
            if x==c and y==test[0]:
                p_props.append(z)
    #print(p_props)
    mp_props=[]
    for c in classes:
        for x,y,z in p_mprice:
            if x==c and y==test[1]:
                mp_props.append(z)
    #print(mp_props)
    d_props=[]
    for c in classes:
        for x,y,z in p_doorsnum:
            if x==c and y==test[2]:
                d_props.append(z)
    #print(d_props)
    c_props=[]
    for c in classes:
        for x,y,z in p_capacity:
            if x==c and y==test[3]:
                c_props.append(z)
    #print(c_props)
    l_props=[]
    for c in classes:
        for x,y,z in p_lug:
            if x==c and y==test[4]:
                l_props.append(z)
    #print(l_props)
    s_props=[]
    for c in classes:
        for x,y,z in p_safty:
            if x==c and y==test[5]:
                s_props.append(z)
    #print(s_props)
    res=[]
    for i in range(0,4):
        r=cls[i]*p_props[i]*mp_props[i]*d_props[i]*c_props[i]*l_props[i]*s_props[i]
        res.append(r)
    #print(res)
    res_cls=(res.index(max(res)))
    return classes[res_cls]
        

def calc_accurcy(test,orgTest):
    count=0
    for i in range (0,len(test)):
        if test[i][6]==orgTest[i][6]:
            count=count+1
    return (count/len(orgTest))*100
                
    
def main():
    #loading the dataset and split it 
    trainingData=list()
    testData=list()
    dataSet=pd.read_csv("car.data.csv")
    dataSetLen=len(dataSet)
    trainingDataSize=int(.75*dataSetLen)
    for i in range(0,trainingDataSize):
        trainingData.append([dataSet.values[i,j] for j in range(0,7)])
    for i in range (trainingDataSize,dataSetLen):
        testData.append([dataSet.values[i,j] for j in range(0,6)])
    #call classifier
    for test_tuple in testData:
        cls=calssifier(trainingData,test_tuple)
        test_tuple.append(cls)
    print(testData)
    #clac accurcy
    originalTest=[]
    for i in range (trainingDataSize,dataSetLen):
        originalTest.append([dataSet.values[i,j] for j in range(0,7)])
    accurcy=calc_accurcy(testData,originalTest)
    print("Classifier accurcy:",round(accurcy,2),"%")
    
    
if __name__ =='__main__':
    main()
