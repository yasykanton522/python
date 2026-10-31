text1 = input("введите первый набор чисел: ")
text2 = input("введите второй набор чисел: ")

nums1 = []
for p in text1.split():
    nums1.append(float(p))

nums2 = []
for p in text2.split():
    nums2.append(float(p))

print("есть в обоих наборах:")
for n in nums1:
    if n in nums2 and nums1.count(n) == 1:
        print(n, " ")

print("только в первом:")
for n in nums1:
    if n not in nums2:
        print(n, " ")

print("только во втором:")
for n in nums2:
    if n not in nums1:
        print(n, " ")

print("все остальные:")
for n in nums1:
    if n not in nums2:
        print(n, " ")
for n in nums2:
    if n not in nums1:
        print(n, " ")



























