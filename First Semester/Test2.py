# N자리수의 각 자리 숫자 합 구하기

print("자연수를 입력하세요.")
n=input()
sum=0

for i in n:
  sum+=int(i)

print(sum)