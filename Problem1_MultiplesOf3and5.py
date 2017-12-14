max = 1000
count = 1
sum = 0
while(count <= max):
  if(count%3 == 0 or count%5 == 0):
    sum = sum + count
  count = count +1
print (sum)
