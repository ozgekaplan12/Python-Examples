# 0-10000 arasındaki tek sayıların toplamı

toplam=0
x=0

while x<=10000:
  if x % 2 == 1:
    toplam += x
  x += 1
print(toplam)