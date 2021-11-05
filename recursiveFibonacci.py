import time
def recur_fibo(n):
    
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 0
while nterms < 30:
    nterms = nterms + 5
    print ('nterms = ', nterms)

    start_time = time.time()
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
    stop_time = time.time()

final_time = stop_time - start_time

print(final_time)