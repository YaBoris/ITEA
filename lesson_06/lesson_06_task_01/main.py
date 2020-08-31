from lesson_06.lesson_06_task_01.my_list import MyList


def work_with_list(list_for_check, list_for_check2):
    list_for_check.append(9)
    list_for_check.insert(2, 54)
    list_for_check.append('List')
    list_for_check.insert(5, 31)
    list_for_check.append(19)
    list_for_check.pop(7)
    list_for_check.insert(4, 30)
    list_for_check.append(99)
    list_for_check.remove(54)
    # list_for_check.clear()
    list_for_check.print_()

    list_for_check2.append(10)
    list_for_check2.append(5)
    list_for_check2.insert(2, 17)
    list_for_check2.append(89)
    list_for_check2.insert(5, 8)
    list_for_check2.print_()

    extended_list = list_for_check + list_for_check2
    extended_list.print_()


if __name__ == "__main__":
    first_list = MyList([5, 9, 12, 67, 4])
    second_list = MyList([67, 13, 43, 20, 7])
    work_with_list(first_list, second_list)
