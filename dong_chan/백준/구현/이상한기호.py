def strange(A, B):
  return (A+B)*(A-B)
A, B = map(int,input().split())
print(strange(A,B))