transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction = transaction.strip()

student_name, course_code, amount, status = transaction.split("|")

student_name = student_name.strip().title()
course_code = course_code.strip()
amount = int(amount.strip())
status = status.strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền: {:,} VND".format(amount))
print("Trạng thái:", status)