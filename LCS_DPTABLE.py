str1 = "abcde"
str2 = "ac"
m,n=len(str1),len(str2)
#print(m,n)
dp=[[0]*(n+1) for _ in range(m+1)]
#print(dp)
for i in range(1,m+1):
    for j in range(1,n+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[i][j])