s='AAAABBBBCCCCDDDDEEEEeeee'
result=[]
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count=count+1
    else:
        result.append(f'{s[i-1]}{count}')
        count=1
result.append(f'{s[i-1]}{count}')
output=' '.join(result)
print(output)
