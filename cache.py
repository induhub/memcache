from time import sleep
cache={}
def square(number):
    total=number*number
    sleep(5)
    return total


def square_cache(number):
    if number in cache.keys():
        result=cache[square]#(number)
    return result

print square_cache(2)
