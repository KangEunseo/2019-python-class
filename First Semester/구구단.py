for i in range(2, 9+1):
  if i>7:
    break
  if i%2==0:
    continue
  print("--- "+str(i)+"단 ---")
  for j in range(1, 9+1):
    print("{} x {} = {}".format(i, j, i*j))
  print()

array=[]
for i in range(1, 10, 2):
  array.append(i)
print(array)

array2=[i for i in range(1, 10, 2)]
print(array2)

array3=[i*i for i in range(1, 10, 2)]
print(array3)

array4=[i*i for i in range(1, 10, 2) if i*i > 30]
print(array4)