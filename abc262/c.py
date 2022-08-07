N=int(input())
an=list(map(int, input().split()))
result=0

# ai=i,aj=jの組み合わせ(=ak=k の総和)
same=0
for n in range(1,N+1):
    if an[n-1]==n:
        same+=1

ans=same*(same-1)/2

# ai=j,aj=iの組み合わせ


for i in range(N):
    j=an[i]-1
    if an[j]==i+1 and an[i]==j-1:
    # if i+1==an[i]-1 and an[an[i]-1]==i+1:
        ans+=1
print(ans)
# for i,ai in enumerate(an):
#     print("ai:",ai)
#     for _j,aj in enumerate(an[i+1:N]):
#         print("aj:",aj)
#     print("-")
# print(result)

