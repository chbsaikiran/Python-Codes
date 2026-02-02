def partion_lists(input_list, pivot):
    less_than_pivot = []
    greater_than_pivot = []
    for item in input_list:
        if item < pivot:
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)
    return less_than_pivot, greater_than_pivot

def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    pivot = input_list[0]
    less_than_pivot, greater_than_pivot = partion_lists(input_list[1:], pivot)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

#Example usage:
# if __name__ == "__main__":
#     sample_list = [38, 27, 43, 3, 9, 82, 10]
#     sorted_list = quick_sort(sample_list)
#     print("Sorted List:", sorted_list)