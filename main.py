import tasks


def main():
    test_task_1()


def test_task_1():
    expected = 'one, two, three, and four'
    list_for_check = ['one', 'two', 'three', 'four']
    fact = tasks.transform_list_join(list_for_check)
    print(f'Result: {expected == fact}\n'
          f'Str_fact: {fact}\n'
          f'Str_expected: {expected}')


if __name__ == '__main__':
    main()
