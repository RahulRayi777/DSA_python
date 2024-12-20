#spaces=0,1,2
#stars=5,3,1
'''n=5
for i in range(n):
    row = " " * i + "*" * (2 * (n - i) - 1)
    print(row)'''

#side_spaces=4,3,2,1,0
#mid_space=1,3,5
'''
n=5
for i in range(n):
    if i==0:
        print(' '*(n-1)+'*'*(i+1)+' '*(n-i))
    elif i==n-1:
        print('*'*((2*n)-1))
    else:
        print(' '*(n-i-1)+'*'+' '*(2*i)+'*')
 
'''
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print('')

'''
'''
n=5
for i in range(n):
    if i==0:
        print('*'*(n))
    elif i==n:
        print(' '*(n)+'*')
    else:
        print(' '*(i)+'*'+' '*(n-1-i)+'*')

        
'''
'''
a=[3, 8, 2, 10, 5]
s=0
for i in a:
    if i>s:
        s=i
print(s)
'''

'''
a=[1, 2, 2, 3, 4, 4, 5]
l=[]
for i in a:
    if i in l:
        pass
    else:
        l.append(i)
print(l)
'''

'''
a=[1, 2, 3, 3, 4, 5]
l=[]
b=[]
for i in a:
    if i not in l:
        l.append(i)
        #print(l)
    else:
        b.append(i)
        #print(b)
if b==[]:
    print('false')
else:
    print('True')
        
'''
'''
lst = [1, 2, 3, 4, 5]
a=0
b=len(lst)-1
for i in range(len(lst)):
    if a<b:
        lst[a],lst[b]=lst[b],lst[a]
    a=a+1
    b=b-1
print(lst)
    '''

'''
lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]
c=0
for i in lst1:
     
    for j in lst2:
        if i==j:
            c=c+1
            break
if c==len(lst1):
    print('True')
else:
    print('False')
'''
'''
lst = [1, 7, 3, 10, 5]
diff=0
for i in range(len(lst)-1):
    a=abs(lst[i]-lst[i+1])
    if a>diff:
        diff=a
print(a)
        
'''
'''
list1=[1, 4, 7]
list2 = [2, 3, 5, 8]
list3=sorted(list1+list2)
print(list3)
'''

'''
lst = [1, 2, 3, 4, 5]
k = 2
for  _ in range(k):
    digit=lst.pop()
    lst.insert(0,digit)
print(lst)
'''


'''

keys = ['x', 'y', 'z']
values = [10, 20, 30]
a={}
for i in range(len(keys)):
    a[keys[i]]=[values[i]]
print(a)

'''

'''
a="hello world hello"
d={}
words=a.split()
for word in words:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
    
print(d)
'''



'''
def is_palindromic_tuple(tup):
    start = 0
    end = len(tup) - 1
    
    # Loop until the start pointer is less than or equal to the end pointer
    while start <= end:
        # If elements at start and end pointers are not equal, it's not a palindrome
        if tup[start] != tup[end]:
            return False
        # Move the pointers towards the center
        start += 1
        end -= 1
    
    # If all elements matched, it is a palindrome
    return True
    
is_palindromic_tuple((1, 2, 3, 2, 1))

'''

'''
s="Hello, World!"
a=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in s:
    if i in a:
        c=c+1
print(c)
'''



'''
s="A man a plan a canal Panama"
ss=''
for char in s:
    if char.isalnum():
        char=char.lower()
        ss=ss+char
print(ss)
'''

'''
s = "anagram"
t = "nagaram"
#if len(s)!=len(t):
#  print('false')
if sorted(s)==sorted(t):
    print('True')

print('False')
'''

'''
s="A man a plan a canal Panama"
ss=''
for i in s:
    if i.isalnum():
        i=i.lower()
        ss=ss+i
#print(ss)
if ss==ss[::-1]:
    print('True')
'''
'''
a="Hello, World!"
b=a.split()
c=0
for i in b:
    c=c+1
print(c)

'''

'''
s="'Hello, World!'"
ss=''
for i in s:
    if i not in ss:
        ss=ss+i
print(ss)
'''

'''
s = "abcde"
t = "ace"
j=0
for i in range(len(s)):
    if j<len(t) and s[i]==t[j]:checking it will not cross if it reaches len
        j=j+1
if j==len(t):
    print('sbs')
'''      


'''
s = "hello worlds"
t = "world"
ss=s.split()
c=0
for i in ss:
     if i==t:
        c=c+1
        print('True')
else:
    print('False')
        
'''

'''
s = "The quick brown fox jumps over the lazy dog"
ss=s.split()
l=[]
for i in ss:
    l.append(len(i))

print(max(l))

'''


'''
Intersection of Two Lists
n1= [4, 9, 5]
n2= [9, 4, 9, 8, 4]
n3=set(n2)&set(n1)
print(list(n3))
'''
'''
a=[1, 0, 1, 1, 0, 1, 1, 1, 1]
c=0
max_c=0
for i in a:
    if i==1:
        c=c+1
        max_c=max(max_c,c)
    else:
        c=0
print(max_c)
'''

'''
class product:
    def __init__(self,iid,name):
        self.iid=iid
        self._name=name

    def get_name(self):
        print(self._name)
    def get_iid(self):
        print(self.iid)
        
a=product(3,'Rahul')
a.get_name()
a.get_iid()
'''
'''
class car:
    def __init__(self,color,wheel):
        self.color=color
        self._wheel=wheel
    @staticmethod
    def greet():
        print('good morning')
        
    def get_color(self):
        print(self._wheel)
c=car('white',4)
c.greet()
c.get_color()

'''


'''
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
dog=Dog()
dog.sound()

'''


'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_employee_info(self):
        print(f"Salary: {self.salary}")
        print(f"Salary: {self.name}")

        
class manager(Employee):
    def __init__(self,name,age,salary,department):
        super().__init__(name,age,salary)
        self.department=department
def display_manager_info(self):
        print(f"Salary: {self.salary}")
        print(f'{self.name}')
        print(f'self.department')

e=manager("Alice", 35, 80000,'DS')
e.display_manager_info()
'''


'''
Inheritance
class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Deal Price: {self.deal_price}")
        print(f"You Saved: {self.you_save}")
        print(f"Ratings: {self.ratings}")

class ElectronicItem(Product):
     
    
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months
    
    def get_warranty(self):
        return self.warranty_in_months
    
    def display_product_details(self):
        super().display_product_details()
        print(f"Warranty: {self.warranty_in_months} months")

e = ElectronicItem("Laptop", 45000, 40000, 3.5)
e.set_warranty(10)
e.display_product_details()

'''

'''
Char Count
s = 'AAAABBBBCCCCDDDDEEEEeeee'
d={}
for char in s:
    if char in d:
        d[char]=d[char]+1
    else:
        d[char]=1
print(d)

'''


'''
s="hello, this is a sample sentence."
ss=s.split()
sss=''
for i in ss:
    a=i[0].capitalize()+i[1:]
    sss=sss+a+' '
print(sss)
'''


'''
s="hello, this is a sample sentence."
ss=s.split()
b=ss[::-1]
bb=' '.join(b)
print(bb)
#sss=' '.join(ss[::-1])
#print(sss)
'''



































'''
class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def get_name(self):
        print(self.name)
        print(self.color)

class vehicle(car):
    def __init__(self,name,color,doors):
        super().__init__(name,color)
        self.doors=doors

    def get_name(self):
        super.get_names()
        print(self.doors)

#c=car('rahul','white')
#c.get_name()
v=vehicle('rahul','white',4)
v.get_name()

 
'''












 


