# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:36:49 2018

@author: Gogo
"""
import pandas as pd
import random 
import math

        
def laod_file(filename):
    dataset=pd.read_excel(filename)
    students=list()
    for i in range (0,150):
        students.append([dataset.values[i,j] for j in range(0,21)])
    return students


def calc_distance (centriod,stud):
    diff_list=[]
    sumtion=0.0
    distance=0.0
    dis_list=[]
    for i in range(0,len(centriod)):
        for j in range (1,len(stud)):
            x1=float(centriod[i][j])
            x2=float(stud[j])
            diff=x2-x1
            sqr_diff=diff**2
            diff_list.append(sqr_diff)
        sumtion=sum(diff_list)
        distance=math.sqrt(sumtion)
       # print(distance)
        dis_list.append(distance)
        diff_list.clear()
    #print(dis_list)
    return dis_list


def calc_new_centriod (students_cluster):
    t=zip(*students_cluster)
    tlist=[]
    for s in t:
        tlist.append(list(s))
    #calc new centriod
    newcentriod=[]
    for i in range(len(tlist)):
        newcentriod.append(sum(tlist[i])/len(tlist[i]))
    return(newcentriod)
    
def checkImmigration(old,new):
    if old==new:
        return True
    else:
        return False
        
#--------------------------------------------------------------------------------
students=laod_file("Course Evaluation .xlsx")
k=int(input("Enter Number of clusters"))
#choose intial centriod
IntialCentriod=random.sample(students,k)
#print(IntialCentriod)

stud_label_list=list()
for stud in students:
    x=calc_distance(IntialCentriod,stud)
    #assign a label for each student
    label=(x.index(min(x)))+1
    stud_label_list.append((stud,label))
#print(stud_label_list)
#print(x)
clusters=list()
for i in range (0,k):
    clusters.append([])

for i in range(0,len(clusters)):
    for stud,label in stud_label_list:
        if label==i+1:
            clusters[i].append(stud)
            
#end intial 

old=list()
new=list()
newCentriods=list()
for c in clusters:     
    newCentriods.append(calc_new_centriod(c))  
for stud in students:
    x=calc_distance(newCentriods,stud)
    #assign a label for each student
    label=(x.index(min(x)))+1
    old.append((stud,label))
#-------------------------------------------------------------    
    #clear clusters 
for k in clusters:
    k.clear()   
for i in range(0,len(clusters)):
    for stud,label in old:
        if label==i+1:
            clusters[i].append(stud)           
newCentriods.clear()
for c in clusters:     
    newCentriods.append(calc_new_centriod(c))
for stud in students:
    x=calc_distance(newCentriods,stud)
    #assign a label for each student
    label=(x.index(min(x)))+1
    new.append((stud,label))

while (checkImmigration(old,new)!=True):
    old.clear()
    new.clear()
    for c in clusters:     
        newCentriods.append(calc_new_centriod(c))  
    for stud in students:
        x=calc_distance(newCentriods,stud)
    #assign a label for each student
        label=(x.index(min(x)))+1
        old.append((stud,label))
#-------------------------------------------------------------    
    #clear clusters 
    for k in clusters:
        k.clear()   
    for i in range(0,len(clusters)):
        for stud,label in old:
            if label==i+1:
                clusters[i].append(stud)           
    newCentriods.clear()
    for c in clusters:     
        newCentriods.append(calc_new_centriod(c))
    for stud in students:
        x=calc_distance(newCentriods,stud)
    #assign a label for each student
        label=(x.index(min(x)))+1
        new.append((stud,label))

print(new)    
for i in range(0,len(clusters)):
    clen=len(clusters[i])
    print("Cluster",i+1)
    print("*******")
    for j in range(0,clen):
        print(clusters[i][j][0])
    print("-----------------------------------------------------------------------")
    
#outliers
clustered=set()
observed=set() 
for i in range(0,len(clusters)):
    clen=len(clusters[i])
    for j in range(0,clen):
        clustered.add(clusters[i][j][0])
for i in range(0,len(students)):
    for j in range(0,21):
        observed.add(students[i][0])
outliers=observed-clustered
outliers=list()
print("Outliers")
print("*******")
print(outliers)
























