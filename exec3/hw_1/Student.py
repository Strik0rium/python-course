from dataclasses import dataclass
from typing import Any


@dataclass
class Student:
    stu_id: str
    name: str
    address: str
    birthday: str
    telephone: str
    email: str

    def __str__(self):
        return (f"学号: {self.stu_id}, "
                f"姓名: {self.name}, "
                f"地址: {self.address}, "
                f"生日: {self.birthday}, "
                f"电话号码: {self.telephone}, "
                f"电子邮件: {self.email}")


student_list = [
    Student("2022303324", "Strik0r", "XC516", "2002-08-10", "13987786171", "strik0rium@gmail.com"),
    Student("2022300001", "Alice", "XC101", "2003-05-17", "13900001111", "alice@example.com"),
    Student("2022300002", "Bob", "XC102", "2002-11-03", "13900002222", "bob@example.com"),
    Student("2022300003", "Charlie", "XC103", "2001-09-22", "13900003333", "charlie@example.com"),
    Student("2022300004", "Diana", "XC104", "2003-02-28", "13900004444", "diana@example.com"),
]

fields = [
        ('stu_id', '学号'),
        ('name', '姓名'),
        ('address', '地址'),
        ('birthday', '生日'),
        ('telephone', '电话号码'),
        ('email', '电子邮件'),
    ]

def register_student():
    print("学生信息录入")

    responses = {field: input(f"请输入{label}: ").strip() for field, label in fields}
    student = Student(**responses)
    student_list.append(student)

    print("\n学生信息录入完成!")
    print(student)


def _query() -> Any | None:
    id_to_find = str(input("请输入需要查询的学号: ")).strip()
    for student in student_list:
        if student.stu_id == id_to_find:
            return student
    return None


def query_student():
    student = _query()
    if student is None:
        print("未能查询到学生信息")
        return

    print("学生信息查询成功!")
    print(student)


def delete_student():
    student = _query()
    if student is None:
        print("未能查询到学生信息")
        return

    student_list.remove(student)
    print("删除成功!")


def modify_student():
    student = _query()
    if student is None:
        print("未能查询到学生信息")
        return

    for field, label in fields[1:]:  # 跳过学号
        current_value = getattr(student, field)
        input_str = input(f"请输入{label} (当前值: {current_value})，不输入表示不改动: ").strip()
        if input_str:
            setattr(student, field, input_str)

    print("修改完成!")
    print(student)


def list_all_students():
    for student in student_list:
        print(student)
