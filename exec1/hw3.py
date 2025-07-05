from dataclasses import dataclass

fields = [
        ('stu_id', '学号'),
        ('name', '姓名'),
        ('address', '地址'),
        ('birthday', '生日'),
        ('telephone', '电话号码'),
        ('email', '电子邮件'),
    ]

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

def register_student():
    print("学生信息录入")

    responses = {field: input(f"请输入{label}: ").strip() for field, label in fields}
    student = Student(**responses)

    print("\n学生信息录入完成!")
    print(student)