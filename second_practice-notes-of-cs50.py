#!/usr/bin/env python
# coding: utf-8

# In[8]:


s='cs50p2'
for i in range(len(s)):
    if s[i].isdigit():
        ind=s.index(s[i])
        break

print(s[ind:])


# In[ ]:


s='cs50p2'
i=0
while i<=len(s):
    if s[i].isdigit()


# In[11]:


def main(s):
    price=50
    us=int(input(f"Amount Due: {price}")
    if us==price:
        print("Change Owed")
def amount(us):
           
    
        
    if us!=price:
        print(f"Insert Due: {price-us})
        coke()


# In[3]:


s=[1,2,3,4,5]
# s.reverse()
s.pop(2)
s.
s


# In[ ]:


a=int(input("etn1"))
b=int(input("etn2"))
t=a
a=b
print(a)
print(b)
print(t)


# In[ ]:





# In[2]:


s=12
size_arr=int(input("enter the array size"))
temp_arr=[]
lst=[]
delete=[]
for i in range(size_arr):
    input_elm=int(input())
    temp_arr.append(input_elm)
for j in range(size_arr):
    lst.append(temp_arr[j])
    if sum(lst)>s:
        var=sum(lst)-s
        delete.append(var)
        
    else:
        pass
if delete in lst:
    lst.remove(delete)
else:
    pass
# lst
temp_arr
# delete

    


# In[1]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car.values())


#before the change

car["color"] = "red"

print(car["brand"]) #after the change


# In[11]:


s="LVIII"
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
count=0
for i in range(len(s)):
    if s[i] in d:
        count+=d[s[i]]
#         print("yes")
print(count)


# In[29]:


s="IV"
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
count=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if d[s[i]] > d[s[j]]:
            count+=d[s[i]]
#             print(count)
        else:
            var=d[s[j]]-d[s[i]]
#             print(d[s[j]],d[s[i]])
            count+=var
#             print(count)
#         print("yes")
print(count)


# In[34]:


s="MCMXCIV"
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
count=0
for i in range(len(s)):
    for j in range(i):
        if d[s[i]] > d[s[j]]:
            count+=d[s[i]]
            print(count)
        else:
            var=d[s[j]]-d[s[i]]
#             print(d[s[j]],d[s[i]])
            count+=var
#             print(count)
#         print("yes")
print(count)


# In[9]:


s="MCMXCIV"
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
count=0
i=0

    for j in range(i+1):
        if d[s[i]] > d[s[j]]:
            count+=d[s[i]]
            print(count)
            i+=1
        else:
            var=d[s[j]]-d[s[i]]
            count+=var
            i+=1
print()
    


# In[18]:


s="MCMXCIV"
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
count=0
for i in range(len(s)-1):
    
    
    if d[s[i]] > d[s[i+1]]:
        count+=d[s[i]]
        print(count)
    else:
        var=d[s[i+1]]-d[s[i]]
#             print(d[s[j]],d[s[i]])
        count+=var
    
#             print(count)
#         print("yes")
print("/",count)


# In[19]:


s="MCMXCIV"
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
count=0
i=0
while i>=0:
    if d[s[i]]>d[s[i+1]]:
        count+=d[s[i]]
        i+=1
        print("*",count)
    else:
        temp=d[s[i+1]]-d[s[i]]
        count+=temp
        i+=1
        print("%",count)

print(count)       
    


# In[ ]:


def main():
    var=us()
    for i in range(len(var)):
        print(f"{i} {var[i]}")
    
def us():
    found=True
    while found:
        lst=[]
        try:
            user=input()
            if user.upper() not in lst:
                lst.append(user)
                found=True
        except EOFError:
            found=False
            
#         break
    return lst
            
            
    
    
main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


def solve(arr,tar):
    re=[]
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i]+arr[j]==tar:
                re.append(i)
                re.append(j)
            else:
                pass
    return re
                
arr=[2,7,11,15]
tar=9


# In[6]:


arr=[3,2,4]
tar=6
re=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==tar:
            re.append(i)
            re.append(j)
        else:
            pass
print(re)


# In[1]:


l1=[2,4,3]
l2=[5,6,8]
to=[]
temp=0
while temp==0:
    
    for i in range(len(l1)):
        for j in range(i):
            var=l1[i]+l2[j]
            if var<10:
                to.append(var)
            else:
                temp+=var
#                 var=temp
print(to)


# In[11]:


l1=[2,4,3]
l2=[5,6,8]
to=[]
temp=0
while temp==0:
    
    for i,j in range(len(l1)):
        var=l1[i]+l2[j]
        if var<10:
            to.append(var)


# In[24]:


l1=[2,4,3]
l2=[5,6,4]
to=[]
temp=0
while temp==0:
    
    for i in range(len(l1)):
        for j in range(i,i+1):
            var=var+int(var1[0])
            var=l1[i]+l2[j]
#             var=var+int(var1[0])
            if var<10:
                to.append(var)
            else:
                
                temp+=var
                var1=str(temp)
                
                to.append(int(var1[1]))
#                 var=int(var1[0])
print(to)


# In[49]:


l1=[2,4,3]
l2=[5,6,4]
to=[]
var1=l1[::-1]
var2=l2[::-1]
con1=''
con2=''
for i in range(len(var1)):
    con1+=str(l1[i])
print(con1)
for j in range(len(var1)):
    con2+=str(l2[j])
print(con2)
result=int(con1)+int(con2)
# print(result)
str_result=str(result)
for z in range(len(str_result)):
    to.append(int(str_result[z]))
print(to[::-1])


# In[50]:


l1=[0]
l2=[0]
to=[]
var1=l1[::-1]
var2=l2[::-1]
con1=''
con2=''
for i in range(len(var1)):
    con1+=str(l1[i])
print(con1)
for j in range(len(var1)):
    con2+=str(l2[j])
print(con2)
result=int(con1)+int(con2)
# print(result)
str_result=str(result)
for z in range(len(str_result)):
    to.append(int(str_result[z]))
print(to[::-1])


# In[52]:


l1=[9,9,9,9,9,9,9]
l2=[9,9,9,9]
to=[]
var1=l1[::-1]
var2=l2[::-1]
con1=''
con2=''
for i in range(len(var1)):
    con1+=str(l1[i])
print(con1)
for j in range(len(var2)):
    con2+=str(l2[j])
print(con2)
result=int(con1)+int(con2)
# print(result)
str_result=str(result)
for z in range(len(str_result)):
    to.append(int(str_result[z]))
print(to[::-1])


# In[62]:


s=['p','w','w','k','e','w']
count=0
temp=[]
for i in range(len(s)):
    if s[i] not in temp:
        temp.append(s[i])
    else:
        var=i
        i=var
        count+=1
print(count)


# In[69]:


# s=['p','w','w','k','e','w']
s='pwwkew'
count=0
temp=[]
for i in range(len(s)):
    if s[i] in temp:
        count=0
        temp.clear()
#         temp.append(s[i])
#         count+=1
    else:
        temp.append(s[i])
        count+=1
print(count)


# In[105]:



def findMedianSortedArrays(nums1, nums2):
    
    nums1.extend(nums2)
    print(nums1)
    
    length=len(nums1)
    if length%2==0:
        re=(nums1[nums1/2]+nums1[nums/2]+1)/2
        
    return re
findMedianSortedArrays(nums1=[1,2],nums2=[3,4])


# In[106]:


len([1,2,3,4])


# In[ ]:





# In[130]:


num1=[1,2]
num2=[3,4]
tem=[]
num1.extend(num2)
tem.extend(num1)
tem.sort()
print(tem)
length=len(tem)
print(length)
if length%2==0:
    var1=length/2
#     var2=var1+1
    add=tem[int(var1)-1]+tem[int(var1)]
    re=add/2
    
print(re)


# In[133]:


num1=[1,3]
num2=[2]
tem=[]


num1.extend(num2)
tem.extend(num1)
tem.sort()
print(tem)
length=len(tem)
print(length)
if length%2==0:
    var1=length/2
#     var2=var1+1
    add=tem[int(var1)-1]+tem[int(var1)]
    re=add/2
    print(re)
else:
    t=tem[int(length/2)]
    print(t)
    


# In[12]:


def heloo():
    var=us()
    for i in range(len(var)):
        print(f"{i} {var[i]}")
    
def us():
    while True:
        lst=[]
        try:
            user=input()
            if user.upper() not in lst:
                lst.append(user)
        except EOFError:
        break
#         break
#         else:
#             pass
    return lst
            
            
    
    
    
heloo()


# In[ ]:





# In[ ]:





# In[ ]:




