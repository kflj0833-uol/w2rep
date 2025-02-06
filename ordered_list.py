def get_ordered_list(lst=None):
    if lst==None:
        input_lst = input('enter list of integers separated by commas:')
        number_lst = input_lst.split(',')
        integer_lst = [int(num.strip())for num in number_lst]
    return sorted(integer_lst)