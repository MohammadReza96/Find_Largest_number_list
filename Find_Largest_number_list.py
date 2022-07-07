def Find_Largest_number_list(*args):
    max_index=args[0]
    index_number=0
    for index in range(len(args)):
        if args[index]>max_index:
            max_index=args[index]
            index_number=index
    return f'largest data:{max_index} largest data index:{index_number}'


li=[5,2,7,1,6,9,13,31,43,34,23,11,55,23,12,11,5,-1]
print(Find_Largest_number_list(*li))

print(Find_Largest_number_list(4,5,6,3,4,5,2,8,9,5,6))