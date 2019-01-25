#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv 
from sklearn import tree
import graphviz


# In[4]:



gender = []
data = []


# In[5]:


#csvfile=pd.read_csv(r'D:\STT PELITA BANGSA 2016\SEMESTER 7\mk2\tugas\dataset.csv')
with open('D:/STT PELITA BANGSA 2016/SEMESTER 7/mk2/tugas/data1.csv','r',newline='',encoding='utf-8')as csvfile:
    r = csv.reader(csvfile,delimiter=',')
    for row in r:
        gendertemp =[]
        datatemp =[]
        for i in range (len(row)):
            if i ==0 : 
                gendertemp = row[0]
            elif i == 1 : 
                TB =int(row[1])
                datatemp.append(TB)
            elif i == 2 :
                BB =int(row[2])
                datatemp.append(BB)
            else : 
                US= int (row[3])
                datatemp.append(US)
            
        gender.append(gendertemp)
        data.append(datatemp)
    csvfile.close()
        


# In[34]:


print('\nData set Training :')
print('Data Gender', end='')
print(gender)
print('Data Karakter :', end='')
print(data)


# In[6]:


klasifikasi = tree.DecisionTreeClassifier()


# In[7]:


klasifikasi = klasifikasi.fit(data,gender)


# In[9]:


klasifikasi=tree.export_graphviz(klasifikasi,out_file=None)
graph=graphviz.Source(klasifikasi)
graph


# In[14]:


databaru =[158,50,39]
prediksi=klasifikasi.predict([databaru])


# In[15]:


print('\n data test baru :',end='' )
print(databaru,end='')
print(', ',end='')
print('Hsil',end='')
print(prediksi)


# In[ ]:





# In[ ]:





# In[ ]:




