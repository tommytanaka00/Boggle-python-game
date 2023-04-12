def is_valley(lst):
    min_val = min(lst)
    for i in range(len(lst)):
        if lst[i] == min_val:
            print(i)



lst = [7, 5, 4, 3, 2, 7, 9, 10]
is_valley(lst)