from lesson_06.lesson_06_task_01.my_list import MyList


def work_with_list(list_for_check, list_for_check2):
    list_for_check.append(9)
    list_for_check.append(87)
    list_for_check.append(19)
    list_for_check.insert(1, 54)
    list_for_check.insert(2, 'List')
    list_for_check.insert(10, 31)
    list_for_check.pop(10)
    list_for_check.insert(10, 30)
    list_for_check.remove(54)
    list_for_check.clear()

    list_for_check2.append(10)
    list_for_check2.append(5)
    list_for_check2.insert(2, 17)
    list_for_check2.append(89)
    list_for_check2.insert(5, 8)

    # extended_list = MyList(size=len(list_for_check)+len(list_for_check2))
    extended_list = list_for_check + list_for_check2
    extended_list.print_()


if __name__ == "__main__":
    size = 10
    size2 = 6
    # my_type = int
    first_list = MyList()
    other_list = MyList()
    work_with_list(first_list, other_list)
