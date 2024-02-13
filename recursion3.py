# Python program to display the Fibonacci sequence usinf recursion

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms=int(input("Enter sequence upto which you want to print fibonacci series: "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i),end=" ")
