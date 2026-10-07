# Requirement:
# - มี save_taxpayer(profile), load_all(), find_taxpayer(id_card) และ delete_taxpayer(id_card)
# - มี export_summary(profile, tax) สร้างไฟล์สรุปและคืนชื่อไฟล์ .txt
# - จัดเก็บข้อมูลตาม profile schema และรองรับข้อมูลไม่มีไฟล์/ไฟล์ว่าง/ข้อมูลเสียหาย
# - ตรวจสอบเลขบัตรก่อนบันทึก และไม่รับ input หรือแสดงเมนูเอง
### ทำงานที่เกี่ยวข้องกับการจัดการไฟล์ ./data/taxpayer.txt เท่านั้น

HEAD_TABLE = ("id_card", "age", "status", "income", "expenses", "deductions", "tax", "name")
DECTION_KEYS = ("spouse", "parent", "child", "insurance", "fund")

def head_table():
    dection = f"{"spouse":<10}{"parent":<10}{"child":<10}{"insurance":<15}{"fund":<10}"
    head = f"{"id_card":^25}| {"age":^5}| {"status":^10}| {"income":^15}| {"expenses":^15}|  {"deductions: "+dection:<60}|  {"tax":<15}| {"name"}"
    print(head)
    with open("./data/taxpayer.txt", "a") as file:
        file.write(head+"\n")
# head_table()

def form_taxpayer(id_card="", name="", age="", status="", income=0, expenses=0, deductions=0, tax="waiting"):
    #สร้าง str ของ profile ใช้งานร่วมกับหการรับตัวแปรของ menu1 เพื่อเตรียมบันทึกลงในระบบ
    dection = f"{deductions["spouse"]:<10}{deductions["parent"]:<10}{deductions["child"]:<10}{deductions["insurance"]:<15}{deductions["fund"]:<10}"
    taxpayer = f"{id_card:^25}| {age:^5}| {status:^10}| {income:^15}| {expenses:^15}|  {(" "*len("deductions: "))+dection:<60}|  {tax:<15}| {name}\n"
    return taxpayer

def save_taxpayer(taxpayer: dict) -> bool:
    if taxpayer:
        with open("./data/taxpayer.txt", "a", encoding="utf-8") as file:
            file.write(taxpayer)
            return True
    return False

def load_all() -> list:
    #โหลดข้อมูลทั้งหมดของ profile
    with open("./data/taxpayer.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
    return data

def find_taxpayer(id_card) -> tuple:
    #เช็คว่า id_card ที่ใส่เข้ามานั้นมีอยู่แล้วใน taxpayer.txt หรือมั้ย แล้ว return ค่า int
    data = load_all()
    for i in range(len(data)):
        if data[i].find(id_card) != -1:
            index = i
            return (index, data[index])
    return None

def create_profile(id_card) -> dict:
    #สร้าง dict profile ของ taxpayer id_card นั้น ๆ จาก taxpayer.txt แล้ว return profile type-data: dict
    """ตัวอย่างค่าที่ต้องการให้ return profile = {
    "id_card":    "1234567890123",   # str, 13 หลัก
    "age":        35,                 # int
    "status":     "single",           # "single" / "married"
    "income":      400000.0           # float
    "expenses"     20000.0            #float
    "deductions": {                   # dict
        "personal":  60000.0,
        "spouse":        0.0,
        "insurance": 25000.0,
        "fund":      50000.0,
    },
    "tax": 5000.0
    "name":       "สมชาย ใจดี",       # str
    }"""
    try:
        index, data = find_taxpayer(id_card)
        data = [x.strip() for x in data.split("|")]
    except:
        taxpayer_q = id_card
        data = [x.strip() for x in taxpayer_q.split("|")] #ใช้ร่วมกับ quiz.py
    finally:
        profile = dict()
        for i in range(len(HEAD_TABLE)):
            if HEAD_TABLE[i]=="deductions":
                dection = [x.strip() for x in data[i].split()]
                deductions = dict()
                for j in range(len(DECTION_KEYS)):
                    deductions[DECTION_KEYS[j]] = float(dection[j])
                profile.setdefault(HEAD_TABLE[i], deductions)
            else:
                try:
                    profile.setdefault(HEAD_TABLE[i], float(data[i]))
                except:
                    profile.setdefault(HEAD_TABLE[i], data[i])
    return profile

def delete_taxpayer(id_card) -> bool:
    data = load_all()
    index, data_index = find_taxpayer(id_card)
    with open("./data/taxpayer.txt", "w", encoding="utf-8") as file:
        for i in range(len(data)):
            if i != index:
                file.write(f"{data[i]}")
        return True
    return False
        
def export_summary_profile(id_card: str):
    profile = create_profile(id_card)
    if not profile:
        return None
    
    if profile:
        filename = f"./data/summary_{id_card}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"สรุปข้อมูลผู้เสียภาษี\n")
            file.write(f"="*30+ "\n")
            file.write(f"เลขบัตรประชาชน: {profile['id_card']}\n")
            file.write(f"ชื่อ-นามสกุล: {profile['name']}\n")
            file.write(f"อายุ: {profile['age']}\n")
            file.write(f"สถานะ: {profile['status']}\n")
            file.write(f"รายได้: {profile['income']:,}\n")
            file.write(f"ค่าใช้จ่ายตามกฎหมาย: {profile['expenses']:,}\n")
            file.write("ค่าลดหย่อน: \n")
            for key, value in profile['deductions'].items():
                if key == "personal":
                    name = "ส่วนตัว"
                elif key == "spouse":
                    name = "คู่สมรส"
                elif key == "parent":
                    name = "บิดามารดา"
                elif key == "child":
                    name = "บุตร"
                elif key == "insurance":
                    name = "ประกันชีวิต"
                elif key == "fund":
                    name = "กองทุน"
                else:
                    name = key
                file.write(f' \t{name}: {value:,.2f}\n')
            file.write(f"ภาษีที่ต้องชำระ: {profile['tax']:,}\n")

        return filename
