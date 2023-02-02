
from typing import List
# def two_sum(numbers, target):
#     # len_of_num = len(numbers)
#     # for i in range(0,len_of_num):
#     #     for j in range(i+1,len_of_num):
#     #         if((numbers[i] + numbers[j]) == target):
#     #             l = [i,j]
#     #             break
#     # return l


def two_sum2(numbers: List, target: int) -> List:
    left = 0
    right = len(numbers)-1
    to_return = []
    while left < right:
        if(numbers[left] + numbers[right] == target):
            to_return = [left,right]
            break
        else:
            # left+=1
            right-=1
    return to_return



def two_sumVincent(numbers: List, target: int) -> List:
    # numbers.sort()
    # print(numbers)
    left = 0
    right = len(numbers)-1
    to_return = []
    while(left< right):
        the_sum = numbers[left] + numbers[right]
        if the_sum  == target:
            to_return = [left,right]
        if the_sum > target:
            right -=1
        else:
            left +=1
    return to_return




def main():
    # print(two_sumVincent([1, 2, 3,4,5], 8))
    # print(two_sum2([5, 1, 2,3], 5))
    print(two_sumVincent([5, 1, 2,3], 5))

main()