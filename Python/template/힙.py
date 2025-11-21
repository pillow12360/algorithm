import heapq

hq = [3,2,1]
heapq.heapify(hq)

print(heapq.heappop(hq))
print(hq)


arr3 = [1,2,6,4,2,4,4,3,7,2,4,6,5,42,1]

arr3.sort(key=lambda x: x)

print(arr3)

mapping = { 'A' : 'X', 'B' : 'Y', 'C' : 'Z'}

s = ['A','B','C','D']

s = ''.join(mapping.get(ch, ch) for ch in s)

dic = {1 : "A", 2 : "B"}

print(dic.get(3,"C"))

print(dic.keys())
print(dic.values())

for k,v in dic.items():
  print(k,v)

print(dic.pop(2))
print(dic)

# dic.pop(key)
# dic.get(key,defalut)
# dic.setdefault(key, defalut)

st = "ABCDABCDBAAAAA"

st = st.replace("A","Z")
print(st)

rot = list(zip(*grid[::-1]))

list(zip(*grid[::-1]))