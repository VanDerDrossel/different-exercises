# Task 1. solution 1
def transform_list(arg: list) -> str:
    text_before_last = ''
    for i in arg[0:-1]:
        text_before_last += f'{i}, '
    return f'{text_before_last}and {arg[-1]}'


# Task 1. solution 2
def transform_list_join(arg: list) -> str:
    arg[-1] = 'and ' + arg[-1]
    return ', '.join(arg)
