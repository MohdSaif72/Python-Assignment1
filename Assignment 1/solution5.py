def fib(n):
    #inititialize the series with 0,1
    series = [0, 1]  
    if n <= 1:
        return series[:n]   
    #Iterate until length of series becomes equal to n
    while len(series) < n:
        #calculating the next Fibonacci number
        next = series[-1] + series[-2] 
        #appending next number to the series
        series.append(next)  
    return series

n = int(input("Enter the number: "))
fibonacci = fib(n)
print(*fibonacci)