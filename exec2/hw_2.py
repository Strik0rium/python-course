import textwrap

def print_func_list():
    func_list_text = textwrap.dedent("""\
        **********************************************
        1. 学生信息录入
        2. 学生信息查询
        3. 学生信息删除
        4. 学生信息修改
        5. 列出所有学生信息
        6. 退出系统
        **********************************************
        """)
    print(func_list_text)

def register_student():
    print("Registering student")

def query_student():
    print("Querying student")

def delete_student():
    print("Deleting student")

def modify_student():
    print("Modifying student")

def list_all_students():
    print("Listing all students")

actions = {
    '1': register_student,
    '2': query_student,
    '3': delete_student,
    '4': modify_student,
    '5': list_all_students,
    '6': exit
}

if __name__ == '__main__':
    while True:
        print_func_list()
        choice = input('请输入功能编号 (1-6): ').strip()

        action = actions.get(choice)
        if action:
            action()
        else:
            print("无效输入，请重新输入")