
"""
Created on Sat Nov  3 23:44:37 2018

@author: Gehad
"""
###import numpy as np
import numpy as np
import pandas as pd
from itertools import combinations


def generate_comb(items,n):
    multi_dim_arr=[]
    comb=combinations(items,n)
    #transform comb objects to comb list
    comb_list=list()
    for c in comb:
        for itm in c:
            comb_list.append(itm)
    arr=np.array(comb_list)
    multi_dim_arr=np.reshape(arr,(-1,n))
    return(multi_dim_arr)
       
    
def generate_one_itemset_withsupport(transactions,items):
    items_sup=list()
    count =0
    for item in items:
        for i in range(0,9959):
            for j in range(0,3):
                if (item==transactions[i][j]):
                    count = count +1
        items_sup.append((item,count))
    return(items_sup)
    
#بقارن ايتمست بال ست بتاعة الترانزاكشن واشوف ان كانت جزء منها 
#ولا لا وبريترن ست فيها بيرز بال ايتمست و السبورت كونت بتاعها 
def generate_n_itemset_withsupport(transactions,item_sets):
    items_with_sup=list()
    count =0
    for itemset in item_sets:
        y=set(itemset)
        for trans in transactions:
            z=set(trans)
            if (y.issubset(z)):
                count=count+1
        items_with_sup.append((y,count))
        count=0
    return(items_with_sup)
            
        #items_sup.append((itemset,count))

# بمسح اللي اقل من المينيمم سابورت
# في الست اللي رجعت من الفانكشن اللي فوق دي 
def remove_pair(item_sup_pairs,minsup):
    updated_pairs=list()
    for item,support in item_sup_pairs:
        if support>=minsup:
            updated_pairs.append((item,support))
    return(updated_pairs)
    
    
#----------------------------------------------------------------------------------------- 

dataSet = pd.read_excel('CoffeeShopTransactions.xlsx')
transactions = list()
for i in range (0,9959): #9959
    transactions.append([dataSet.values[i,j] for j in range (3,6)])
#print(transactions)
items=set()
for i in range(0,9959):
    for j in range (0,2):
        items.add(transactions[i][j])
minsup=int(input("Enter Minimum support count "))
minconf=float(input("Enter Minimum confidence "))
item_sup_pairs=generate_one_itemset_withsupport(transactions,items)
updated_pairs=remove_pair(item_sup_pairs,minsup)
item_set=list()
sup_list=list()
for items,sup in updated_pairs:
    item_set.append(items)
    sup_list.append(sup)
n=1
finalsets=list()
finalsup=list()
for i in sup_list:
    if i>=minsup:
        n=n+1
        comb=generate_comb(item_set,n)
        items_with_support=generate_n_itemset_withsupport(transactions,comb)
        up_date=remove_pair(items_with_support,minsup)
        sup_list.clear()
        for itm,sp in up_date:
            sup_list.append(sp)
            finalsets.append(itm)
            finalsup.append(sp)
print("The frequent itemsets")
for i in range(0,len(finalsets)):
    print("set: ",finalsets[i])
    print("Frequent: ",finalsup[i])
print("-------------------------------------------------------------")   

for i in range(0,len(finalsets)):
    comb=combinations(finalsets[i],len(finalsets[i]))
    
temp=list() 
temp1=list()    
for i in range(0,len(finalsets)):
    temp=list(finalsets[i])
    temp1.append(temp[0])
temp2=list()
for item in temp1:
    for itm,sup in item_sup_pairs:
        if item==itm:
            temp2.append(sup)
conf=float()
conf_list=list()
for i in range(0,len(finalsup)):
    conf=(finalsup[i]/temp2[i])*100
    conf_list.append((round(conf,2)))

for i in range(0,len(finalsets)):
    for c in comb:
        print("Rule: ",c)
        print("confidence= ",conf_list[i],"%")
        if conf_list[i]>=minconf:
            print("Strong Rule")





