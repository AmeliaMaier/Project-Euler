max = 4000000
fibonacci_num_low = 1
fibonacci_num_high = 2
fibonacci_sum = 0
sum = 2
while(fibonacci_num_high <= max):
    fibonacci_sum = fibonacci_num_low + fibonacci_num_high
    fibonacci_num_low = fibonacci_num_high
    fibonacci_num_high = fibonacci_sum
    if(fibonacci_num_high % 2 == 0):
        sum = sum + fibonacci_num_high
print (sum)
