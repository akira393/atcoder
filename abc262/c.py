N=int(input())
an=list(map(int, input().split()))
result=0
# for i in range(N):
#     for j in range(i+1,N):
#         # if an[i]<=an[j] and (an[i]==i+1 or an[j]==i+1):
#         if (an[i]<=an[j] and an[i]==i+1) or( an[i]>=an[j] and an[j]==i+1):
#             if (an[i]>=an[j] and an[i]==j+1) or( an[i]<=an[j] and an[j]==j+1):
            
#                 result+=1

for i,ai in enumerate(an):
    print("ai:",ai)
    for _j,aj in enumerate(an[i+1:N]):
        print("aj:",aj)
    print("-")
print(result)