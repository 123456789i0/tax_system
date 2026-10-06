# Requirement:
# - มี show_menu() รับตัวเลือกเมนูจากผู้ใช้
# - มี input_number(prompt, min, max) ตรวจรูปแบบและช่วงของตัวเลข
# - มี print_table(), print_summary() และ print_bar_chart() สำหรับแสดงผล
# - ปัดเศษเงินเฉพาะตอนแสดงผล และรองรับข้อมูลว่างโดยไม่ทำให้โปรแกรมหยุด
import re
def show_menu() -> input:
    print("\n===== Tax System =====")
    print("1. เพิ่มข้อมูลผู้เสียภาษี")
    print("2. คำนวณภาษี")
    print("3. สร้างข้อมูลผู้เสียภาษีในรูปแบบไฟล์ .txt")
    print("4. ลบข้อมูลผู้เสียภาษี")
    print("5. เล่นควิซ")
    print("0. จบการทำงาน")

    return input("เลือกเมนู: ")

###หมายเหตุ ในการ input ต้อง ใช้ function strip ทุกครั้ง
def input_menu(chioce: str) -> str:
    valid_choices = ["0","1","2","3","4","5"]

    if chioce.strip() not in valid_choices:
        print("กรุณากรอกเมนูให้ถูกต้อง(1-5)")
        chioce = input_menu(input("เลือกเมนู:"))
    return chioce
    #เช็คว่า user กรอกข้อมูลใน show_menu() ถูกต้องมั้ย ถ้าไม่ให้กรอกใหม่ แต่ถ้าถูก return chioce: str

def input_id(data: str) -> bool:
    data = data.strip()
    while not (data.isdigit() and len(data)==13):
        print("กรุณากรอกเลขบัตรประจำตัวประชาชนให้ถูกต้อง 13 หลัก")
        data = input("กรอกเลขบัตรประจำตัวประชาชน:")
    id_card = f"{data[0]}-{data[1:5]}-{data[5:10]}-{data[10:12]}-{data[12]}"
    return id_card
    #เช็คว่า id_card ถูกต้องมั้ย รูปแบบที่ต้องการคือ id_card = "1234567891234" ถ้าไม่ให้กรอกใหม่จนกว่าจะถูก และ เก็บข้อมูลเป็น id_card = "1-2345-67891-23-4"

def input_text(data: str) -> str:
    data = data.strip()
    pattern = r'^[a-zA-Zก-๙\s]+$'
    while not (data != "" and re.match(pattern, data)):
        print("กรุณากรอกข้อมูลให้ถูกต้อง (เฉพาะตัวอักษรเท่านั้น ห้ามมีตัวเลขหรือสัญลักษณ์)")
        data = input("กรอกชื่อใหม่อีกครั้ง: ").strip()
        data = data.strip()
    return data
    #ใข้เช็คข้อมูลใน profile ที่ต้องกรอกเป็น str ได้แก่ ชื่อ สถานภาพ เป้าหมายคือต้องเมคเซนส์ ไม่เอาแบบ เทพซ่า777 อิอิ ถ้าไม่ให้กรอกใหม่จนกว่าจะถูก

def input_num(data: str) -> float:
    data = data.strip()

    while not (data != "" and data.replace("-","", 1).isdigit() and float(data) >=0 ):
        print("กรุณากรอกข้อมูลให้ถูกต้อง (เฉพาะตัวเลขเท่านั้น เช่น 17 หรือ 17.0)")
        data = input("กรอกข้อมูลใหม่อีกครั้ง: ").strip()
    return float(data)
    #ใข้เช็คข้อมูลใน profile ที่ต้องกรอกเป็น num ได้แก่ อายุ รายได้ เป้าหมายคือต้องเมคเซนส์ ไม่เอาแบบ สิบเจ็ด จะเอา ("17.0") และ return (data: float) ถ้าไม่ให้กรอกใหม่จนกว่าจะถูก

def input_choice(data: str, valid_choice: list) -> str:
    data = data.strip()

    while data not in valid_choice:
        print("กรุณาเลือกจากตัวเลือกที่กำหนดเท่านั้น", valid_choice)
        data = input("กรอกข้อมูลใหม่อีกครั้ง: ").strip()

    if valid_choice == ["y", "n"]:
        if data == "y": return True
        else: return False
    return data
    #ใช้เช็คข้อมูลใน profile ที่ต้องกรอกเป็น ตัวเลือกที่มีเท่านั้น เช่น list("single", "married")
