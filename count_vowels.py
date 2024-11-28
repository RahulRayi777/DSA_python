my_list = [
    "apple",
    "banana",
    "grape",
    "watermelon",
    "strawberry"
]
'''
for i in my_list:
    c=0
    b=list(i)
    print(b)
    for j in b:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            c=c+1
    print(c)'''

ovels='aeiou'
for word in my_list:
     c=0
     for char in word:
        if char in ovels:
            c=c+1
     print(c)
    
        
