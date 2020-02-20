#QUick sort
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
Time complexity analysis:
   Best: o(logn)
   Average and most case: o(nlogn)
   Worst: o(n2)

"""

#-------------------------------------------------------------------------------
#    Implementation
#-------------------------------------------------------------------------------
def partition(the_list, start_index, end_index):
    pivot = the_list[end_index]

    left_index = start_index
    right_index = end_index - 1

    while left_index <= right_index:
        while left_index <= end_index and the_list[left_index] < pivot:
            left_index += 1
        while right_index >= start_index and the_list[right_index] > pivot:
            right_index += 1
        if left_index < right_index:
            the_list[right_index], the_list[left_index] = \
                the_list[left_index], the_list[right_index]
        # Unless we've looked at all the elements in the list and are
        # done partitioning. In that case, move the pivot element into
        # its final position.
        else:
            the_list[end_index], the_list[left_index] = the_list[left_index],
            the_list[end_index]
    return left_index

def quick_sublist(the_list, start_index, end_index):
    #list with o or 1 elements
    if start_index >= end_index:
        return
    # Divide the list into sublists
    pivot_index = partition(the_list, start_index, end_index)
    # Sort sublist recursively
    quick_sublist(the_list, start_index, pivot_index -1)
    quick_sublist(the_list, pivot_index, end_index)

def quicksort(the_list):
    quicksort_sublist(the_list, 0, len(the_list) - 1)

