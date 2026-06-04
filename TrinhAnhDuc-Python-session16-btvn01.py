# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]

# Hàm chuẩn hóa tên bệnh và thêm vào hồ sơ
def add_diagnosis(raw_diagnosis, current_list):
    raw_diagnosis = raw_diagnosis.strip().title()
    current_list.append(raw_diagnosis)
    return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Gọi hàm để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)

'''
Câu 1: Tại sao strip() và title() không làm thay đổi raw_diagnosis?

Trong Python, String là kiểu dữ liệu bất biến (Immutable). 
Điều này có nghĩa là sau khi một chuỗi được tạo ra, nội dung của nó không thể thay đổi trực tiếp.

Câu 2: Cần sửa cú pháp gán như thế nào?

Phải gán kết quả trả về vào biến:

raw_diagnosis = raw_diagnosis.strip()
raw_diagnosis = raw_diagnosis.title()

Hoặc viết gọn:

raw_diagnosis = raw_diagnosis.strip().title()

Câu 3: extend() hoạt động như thế nào với String?

Phương thức extend() dùng để thêm từng phần tử của một iterable vào list.

Chuỗi (String) cũng là một iterable nên:

lst = []
lst.extend("ABC")

sẽ tương đương:

lst.append("A")
lst.append("B")
lst.append("C")

Câu 4: Cần thay extend() bằng gì?

Cần sử dụng:

append()

vì append() thêm nguyên vẹn một phần tử vào cuối list.


'''

