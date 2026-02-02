def merge_lists(left,right):
    mergered_list = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            mergered_list.append(left[left_index])
            left_index += 1
        else:
            mergered_list.append(right[right_index])
            right_index += 1
    # If there are remaining elements in left or right, extend them to the merged list
    mergered_list.extend(left[left_index:])
    mergered_list.extend(right[right_index:])
    return mergered_list

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    mid_index = len(input_list) // 2
    left_half = merge_sort(input_list[:mid_index])
    right_half = merge_sort(input_list[mid_index:])
    return merge_lists(left_half, right_half)

# Example usage:
# if __name__ == "__main__":
#     sample_list = [38, 27, 43, 3, 9, 82, 10]
#     sorted_list = merge_sort(sample_list)
#     print("Sorted List:", sorted_list)

