#slicing way which uses [start:stop:step] syntax setting step to -1 tell walk backward
arr = [3, 2, 4, 5, 1]
# reverse_arr = arr[::-1]
# print(reverse_arr)

#reverse() method. It modifies the existing array in memory without creating new one.
# arr.reverse()
# print(arr)

#reversed() function (the iterator way) that reads list backward
for x in reversed(arr):
    print(x, end=" ")