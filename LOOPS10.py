def fibonacci(n):
  fib1 = 0
  fib2 = 1
  print(fib1,fib2,end = " ")
  for i in range(2,n):
    next_term = fib1+fib2
    print(next_term,end = " ")
    fib1 = fib2
    fib2 = next_term

x = int(input("ENTER NUMBER OF TERMS : "))
fibonacci(x)
