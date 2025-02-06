search_ordered_list(x,y):
    sorted_lst=get_ordered_list(x)
    low=0
    high=len(sorted_lst)-1
    while low<=high:
        mid=(low+high)//2
        if sorted_lst(mid)=y:
            return True
        elif sorted_lst(mid)<y:
            low=mid+1
        else:
            high=mid-1
    return false

