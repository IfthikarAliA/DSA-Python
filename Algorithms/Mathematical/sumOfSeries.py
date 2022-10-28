from unittest import result


def seriesSum(n):
    return int(n*(n+1)/2)

if __name__ == "__main__":
    num=int(input("Enter the value of N: "))
    result = seriesSum(num)
    print(result)