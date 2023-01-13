def two_sum(numbers, target):
    len_of_num = len(numbers)
    for i in range(0,len_of_num):
        for j in range(i+1,len_of_num):
            if((numbers[i] + numbers[j]) == target):
                l = [i,j]
                break
    return l


def main():
    print(two_sum([1, 2, 3], 4))


main()