# Requirement:
# - มี show_menu() รับตัวเลือกเมนูจากผู้ใช้
# - มี input_number(prompt, min, max) ตรวจรูปแบบและช่วงของตัวเลข
# - มี print_table(), print_summary() และ print_bar_chart() สำหรับแสดงผล
# - ปัดเศษเงินเฉพาะตอนแสดงผล และรองรับข้อมูลว่างโดยไม่ทำให้โปรแกรมหยุด

def show_menu() -> input:
    print("\n===== Tax System =====")
    print("1. เพิ่มข้อมูลผู้เสียภาษี")
    print("2. คำนวณภาษี")
    print("3. สร้างข้อมูลผู้เสียภาษีในรูปแบบไฟล์ .txt")
    print("4. ลบข้อมูลผู้เสียภาษี")
    print("5. เล่นควิซ")
    print("0. ออกจากโปรแกรม")

    return input("เลือกเมนู: ")

###หมายเหตุ ในการ input ต้อง ใช้ function strip ทุกครั้ง
def input_menu(chioce: str) -> str:
    #เช็คว่า user กรอกข้อมูลใน show_menu() ถูกต้องมั้ย ถ้าไม่ให้กรอกใหม่ แต่ถ้าถูก return chioce: str
    pass

def input_id(data: str) -> bool:
    #เช็คว่า id_card ถูกต้องมั้ย รูปแบบที่ต้องการคือ id_card = "1234567891234" ถ้าไม่ให้กรอกใหม่จนกว่าจะถูก และ เก็บข้อมูลเป็น id_card = "1-2345-67891-23-4"
    pass

def input_text(data: str) -> str:
    #ใข้เช็คข้อมูลใน profile ที่ต้องกรอกเป็น str ได้แก่ ชื่อ สถานภาพ เป้าหมายคือต้องเมคเซนส์ ไม่เอาแบบ เทพซ่า777 อิอิ ถ้าไม่ให้กรอกใหม่จนกว่าจะถูก
    pass

def input_num(data: str) -> float:
    #ใข้เช็คข้อมูลใน profile ที่ต้องกรอกเป็น num ได้แก่ อายุ รายได้ เป้าหมายคือต้องเมคเซนส์ ไม่เอาแบบ สิบเจ็ด จะเอา ("17.0") และ return (data: float) ถ้าไม่ให้กรอกใหม่จนกว่าจะถูก
    pass

def input_choice(data: str, valid_choice: list) -> str:
    #ใช้เช็คข้อมูลใน profile ที่ต้องกรอกเป็น ตัวเลือกที่มีเท่านั้น เช่น list("single", "married")
    pass