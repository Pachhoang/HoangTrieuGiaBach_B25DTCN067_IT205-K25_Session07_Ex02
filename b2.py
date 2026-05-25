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

#C1 Vì strip() trả về chuỗi mới nên không thay đổi trực tiếp biến transaction.

#C2 Chuỗi giao dịch được phân tách bằng ký tự "|".

#C3 Vì split("-") sẽ tách theo dấu "-" thay vì dấu "|" nên dữ liệu bị sai cấu trúc.

#C4 Khi split("-"), course_code như PYTHON-01 sẽ bị tách thành nhiều phần làm lệch dữ liệu.

#C5 Vì sau split() các phần vẫn còn khoảng trắng thừa nên cần strip() lại từng phần.

#C6 Vì amount ban đầu là chuỗi nên cần đổi sang số để định dạng tiền bằng dấu phẩy.
