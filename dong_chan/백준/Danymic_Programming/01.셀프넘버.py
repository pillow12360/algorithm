set1 = set(range(1,10001))
remove_set = set()
for i in set1:
    for num in str(i):
        i += int(num)
    remove_set.add(i)

self_numbers = set1 - remove_set

for i in sorted(self_numbers):
    print(i)