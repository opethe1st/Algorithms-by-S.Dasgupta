def f(n):
    if n > 1:
        print 'going', n
        f(n / 2)
        f(n / 2)


f(16)
print 'here'
