def fib(n):
    mem = [0] * (n + 1)

    def fib_helper(n, mem):
        if n == 0 or n == 1:
            return n
        if mem[n] == 0:
            mem[n] = fib(n - 1) + fib(n - 2)
        return mem[n]

    return fib_helper(n, mem)

print(fib(20))
