import sys

def numbers_sum(number):
    values = []
    for num in range(1, number+1):
        if number - num >= num + 1:
            number = number - num
            values.append(num)
            continue
        else:
            values.append(number)
            break
    
    k = len(values)
    
    return k, values
            
        


def main():
    reader = (int(x) for x in sys.stdin)
    n  = next(reader)
    
    k , values = numbers_sum(n)
    print(k)
    print(*values)



if __name__ = __main__:
  main()

