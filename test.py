from random import randint

# def function(num):

#     result = 1

#     for n in range(1, num+1):
#         result *= n

#     return result

# m = int(input('m = '))
# n = int(input('n = '))

# print(function(m) // function(n) // function(m-n))


# def roll_dice(n=2):
    
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total

# def add(a=0, b=0, c=0):
#     return a + b + c

# print(roll_dice())
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))
# print(add(c=50, a=100, b=200))

# def foo():
#     pass
# def bar():
#     pass

# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()

# print('0503')


def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    # 計算列表長度(元素個數)
    print(len(list1))
    # 下標(索引)運算
    print(list1[0])
    print(list1[4])
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])
    print(list1[-3])
    list1[2] = 300
    print(list1)
    # 添加元素
    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000]
    print(list1)
    print(len(list1))
    # 刪除元素
    list1.remove(200)
    if 1000 in list1:
        list1.remove(1000)
    del list1[0]
    print(list1)
    # 清空列表元素
    list1.clear()
    print(list1)


if __name__ == '__main__':
    main()