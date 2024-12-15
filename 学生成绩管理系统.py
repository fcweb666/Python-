#
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  - /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#           佛祖保佑       永不宕机     永无BUG
#
#       佛曰:
#               写字楼里写字间，写字间里程序员；
#               程序人员写程序，又拿程序换酒钱。
#               酒醒只在网上坐，酒醉还来网下眠；
#               酒醉酒醒日复日，网上网下年复年。
#               但愿老死电脑间，不愿鞠躬老板前；
#               奔驰宝马贵者趣，公交自行程序员。
#               别人笑我忒疯癫，我笑自己命太贱；
#               不见满街漂亮妹，哪个归得程序员？
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#    程序说明：
#            1、本程序将管理员与用户权限分割，执行功能1、3、4、7、8时需要管理员权限，执行功能2、5、6时只需要用户权限。
#            2、本成绩管理系统Python程序设计、WEB设计与应用、C语言程序设计、数据结构为基础科目，基础科目无法删除，其他科目需管理员新增。
#            3、本程序学生信息储存在students.txt文件中，科目信息储存在subjects.txt文件中。
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#            姜海主页：www.fcbook.cn    本程序Github项目地址：https://github.com/fcweb666/xscj.git
#                  特别鸣谢：马晟昊老师、海螺AI、CSDN、Github。
#版权所有2024姜海版权所有
#                  本程序部分代码借鉴于网络，不存在侵权可能！
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


进口操作系统（Operating System）

# 文件名常量
学生_档案=students.txt '
SUBJECTS_FILE =subjects.txt '

# 基础科目（不可删除）
BASE_SUBJECTS = ['Python程序设计', 'WEB设计与应用', 'C语言程序设计', '数据结构']

# 学生数据存储
students = []

# 管理员账号和密码
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = '123456'

# 当前用户权限，默认为普通用户
current_user = {
    'username': None,
    'is_admin': False
}

def load_subjects():
    """从文件加载新增的科目"""
    subjects = BASE_SUBJECTS.copy()
    if not os.path.exists(SUBJECTS_FILE):
        return subjects
    with open(SUBJECTS_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            subject = line.strip()
            if subject and subject not in subjects:
                subjects.append(subject)
    return subjects

def save_subjects(subjects):
    """将新增的科目保存到文件"""
    with open(SUBJECTS_FILE, 'w', encoding='utf-8') as file:
        for subject in subjects:
            if subject not in BASE_SUBJECTS:
                file.write(f"{subject}\n")

def load_students():
    """从文件加载学生数据"""
    if not os.path.exists(STUDENTS_FILE):
        return
    with open(STUDENTS_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 5:  # 学号, 姓名, 年龄, + 各科成绩
                continue  # 跳过格式不正确的行
            student = {
                'id': parts[0],
                'name': parts[1],
                'age': int(parts[2]),
            }
            for i in range(3, len(parts), 2):
                subject = parts[i]
                try:
                    score = float(parts[i+1])
                    student[subject] = score
                except (IndexError, ValueError):
                    continue  # 跳过格式不正确的成绩
            students.append(student)

def save_students():
    """将学生数据保存到文件"""
    with open(STUDENTS_FILE, 'w', encoding='utf-8') as file:
        for student in students:
            line = f"{student['id']},{student['name']},{student['age']}"
            for subject in student:
                if subject not in ['id', 'name', 'age']:
                    line += f",{subject},{student[subject]}"
            line += '\n'
            file.write(line)

def login():
    """管理员登录"""
    print("\n=== 管理员登录 ===")
    username = input("请输入管理员用户名: ")
    password = input("请输入管理员密码: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        current_user['username'] = username
        current_user['is_admin'] = True
        print("登录成功！")
    else:
        print("登录失败！用户名或密码错误。")

def add_student():
    """添加新学生"""
    if not current_user['is_admin']:
        print("需要管理员权限才能执行此操作。")
        return
    try:
        student_id = input("请输入学生学号: ")
        # 检查学号是否已存在
        for s in students:
            if s['id'] == student_id:
                print("学号已存在！")
                return
        name = input("请输入学生姓名: ")
        age = int(input("请输入学生年龄: "))
        student = {
            'id': student_id,
            'name': name,
            'age': age
        }
        subjects = load_subjects()
        for subject in subjects:
            while True:
                try:
                    score = float(input(f"请输入{subject}的成绩: "))
                    student[subject] = score
                    break
                except ValueError:
                    print("输入格式错误！请输入有效的数字成绩。")
        students.append(student)
        print("学生信息添加成功！")
    except ValueError:
        print("输入格式错误！请确保年龄和成绩为数字。")

def view_students():
    """查看所有学生信息"""
    if not students:
        print("没有学生信息。")
        return
    subjects = load_subjects()
    print(f"{'学号':<10}{'姓名':<10}{'年龄':<10}", end='')
    for subject in subjects:
        print(f"{subject:<20}", end='')
    print("\n" + "-" * (10 + 10 + 10 + 20 * len(subjects)))
    for s in students:
        print(f"{s['id']:<10}{s['name']:<10}{s['age']:<10}", end='')
        for subject in subjects:
            score = s.get(subject, 'N/A')
            print(f"{score:<20}", end='')
        print()

def update_student():
    """更新学生成绩"""
    if not current_user['is_admin']:
        print("需要管理员权限才能执行此操作。")
        return
    student_id = input("请输入要更新的学生学号: ")
    for student in students:
        if student['id'] == student_id:
            print(f"当前学生: {student['name']}, 年龄: {student['age']}")
            subjects = load_subjects()
            for subject in subjects:
                if subject in student:
                    while True:
                        try:
                            new_score = float(input(f"请输入新的{subject}成绩（当前: {student[subject]}）: "))
                            student[subject] = new_score
                            break
                        except ValueError:
                            print("输入格式错误！请输入有效的数字成绩。")
                else:
                    while True:
                        try:
                            new_score = float(input(f"请输入{subject}的成绩: "))
                            student[subject] = new_score
                            break
                        except ValueError:
                            print("输入格式错误！请输入有效的数字成绩。")
            print("学生成绩更新成功！")
            return
    print("未找到该学号的学生。")

def delete_student():
    """删除学生信息"""
    if not current_user['is_admin']:
        print("需要管理员权限才能执行此操作。")
        return
    student_id = input("请输入要删除的学生学号: ")
    for i, student in enumerate(students):
        if student['id'] == student_id:
            del students[i]
            print("学生信息删除成功！")
            return
    print("未找到该学号的学生。")

def find_student():
    """查找学生信息"""
    keyword = input("请输入要查找的学生学号或姓名: ")
    found = False
    subjects = load_subjects()
    for student in students:
        if keyword == student['id'] or keyword == student['name']:
            print(f"学号: {student['id']}, 姓名: {student['name']}, 年龄: {student['age']}")
            for subject in subjects:
                score = student.get(subject, 'N/A')
                print(f"{subject}: {score}")
            found = True
    if not found:
        print("未找到匹配的学生信息。")

def view_subjects():
    """查看所有科目"""
    subjects = load_subjects()
    print("\n=== 当前科目列表 ===")
    for subject in subjects:
        print(f"- {subject}")

def add_subject():
    """添加新科目"""
    if not current_user['is_admin']:
        print("需要管理员权限才能执行此操作。")
        return
    new_subject = input("请输入要添加的科目名称: ")
    subjects = load_subjects()
    if new_subject in subjects:
        print("该科目已存在！")
        return
    subjects.append(new_subject)
    save_subjects(subjects)
    print(f"科目 '{new_subject}' 添加成功！")

def delete_subject():
    """删除科目"""
    if not current_user['is_admin']:
        print("需要管理员权限才能执行此操作。")
        return
    subjects = load_subjects()
    print("当前科目列表:")
    for subject in subjects:
        print(f"- {subject}")
    subject_to_delete = input("请输入要删除的科目名称: ")
    if subject_to_delete in BASE_SUBJECTS:
        print("基础科目不能删除！")
        return
    if subject_to_delete not in subjects:
        print("该科目不存在！")
        return
    subjects.remove(subject_to_delete)
    save_subjects(subjects)
    # 删除学生中该科目的成绩
    for student in students:
        if subject_to_delete in student:
            del student[subject_to_delete]
    save_students()
    print(f"科目 '{subject_to_delete}' 删除成功！")

def main_menu():
    """显示主菜单"""
    while True:
        print("\n=== 兰州现代职业学院理工学院学生成绩管理系统 ===\n        === 作者：JSJ2.4 姜海 ===")
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 更新学生成绩")
        print("4. 删除学生信息")
        print("5. 查找学生信息")
        print("6. 查看所有科目")
        print("7. 添加科目")
        print("8. 删除科目")
        print("9. 保存数据")
        print("10. 退出")
        choice = input("请输入您的选择: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            find_student()
        elif choice == '6':
            view_subjects()
        elif choice == '7':
            add_subject()
        elif choice == '8':
            delete_subject()
        elif choice == '9':
            save_students()
            print("数据已保存。")
        elif choice == '10':
            save_students()
            print("退出系统。")
            break
        else:
            print("无效的选择，请重新输入。")

def main():
    """主函数"""
    load_subjects()
    load_students()
    while True:
        print("\n=== 兰州现代职业学院理工学院学生成绩管理系统 ===\n        === 作者：JSJ2.4 姜海 ===")
        print("1. 管理员登录")
        print("2. 以普通用户身份使用")
        print("3. 退出")
        choice = input("请输入您的选择: ")
        if choice == '1':
            login()
            if current_user['is_admin']:
                main_menu()
        elif choice == '2':
            current_user['username'] = 'user'
            current_user['is_admin'] = False
            main_menu()
        elif choice == '3':
            save_students()
            print("退出系统。")
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()
