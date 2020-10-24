def fun(number):
    return str(number).count('0')


if __name__ == "__main__":
    print(fun(10**1000000))
