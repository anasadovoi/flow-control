
start_n = int(input('Introduce the first number>>>'))
end_n = int(input('Introduce the last number>>>'))

if start_n < end_n:
    while start_n <= end_n:
        print(start_n)
        start_n += 1
elif start_n > end_n:
    while start_n >= end_n:
        print(start_n)
        start_n -= 1
    