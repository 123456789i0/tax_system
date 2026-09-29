# Requirement:
# - มี save_taxpayer(profile), load_all(), find_taxpayer(id_card) และ delete_taxpayer(id_card)
# - มี export_summary(profile, tax) สร้างไฟล์สรุปและคืนชื่อไฟล์ .txt
# - จัดเก็บข้อมูลตาม profile schema และรองรับข้อมูลไม่มีไฟล์/ไฟล์ว่าง/ข้อมูลเสียหาย
# - ตรวจสอบเลขบัตรก่อนบันทึก และไม่รับ input หรือแสดงเมนูเอง
### ทำงานที่เกี่ยวข้องกับการจัดการไฟล์ ./data/taxpayer.txt เท่านั้น
import json

def create_profile_dict(id_card="", name="", age="", status="", income=None, deductions=None, tax=None):
    profile = dict()
    profile.setdefault("id_card", id_card)
    profile.setdefault("name", name)
    profile.setdefault("age", age)
    profile.setdefault("status", status)
    profile.setdefault("income", income)
    profile.setdefault("deductions", deductions)
    profile.setdefault("tax", tax)
    return profile

def save_taxpayer(profile: dict) -> bool:
    if profile:
        with open("./data/taxpayer.txt", "a", encoding="utf-8") as file:
            json.dump(profile, file, ensure_ascii=False)
            file.write("\n")
            return True
    return False

def load_all() -> list:
    #โหลดข้อมูลทั้งหมดของ profile
    with open("./data/taxpayer.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        data = [d.strip() for d in data]
    return data

def find_taxpayer(id_card) -> int:
    #เช็คว่า id_card ที่ใส่เข้ามานั้นมีอยู่แล้วใน taxpayer.txt หรือมั้ย แล้ว return ค่า bool
    data = load_all()
    for i in range(len(data)):
        try:
            d = json.loads(data[i])
            if d["id_card"] == id_card:
                return i
        except:
            continue
    return 0

def create_profile(id_card) -> dict:
    """สร้าง dict ของ profile id_card นั้น ๆ จาก taxpayer.txt แล้ว return profile type-data: dict
    ตัวอย่างค่าที่ต้องการให้ return profile = {
    "id_card":    "1234567890123",   # str, 13 หลัก
    "name":       "สมชาย ใจดี",       # str
    "age":        35,                 # int
    "status":     "single",           # "single" / "married"
    "income": [                      # list ของ dict
        {"type": "เงินเดือน", "amount": 480000.0},
        {"type": "ค่าเช่า",   "amount":  60000.0},
    ],
    "deductions": {                   # dict
        "personal":  60000.0,
        "spouse":        0.0,
        "insurance": 25000.0,
        "fund":      50000.0,
    },
    "tax": None
    }"""
    if find_taxpayer(id_card):
        data = load_all()
        line = find_taxpayer(id_card)
        profile = json.loads(data[line])
        return profile
    else:
        return False


def delete_taxpayer(id_card: str) -> bool:
    data = load_all()
    line = find_taxpayer(id_card)
    data.remove(data[line])
    with open("./data/taxpayer.txt", "w", encoding="utf-8") as file:
        for d in data:
            file.write(d)
    return True
        
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
            file.write(f"รายได้:{profile['income']:,}\n")
            file.write(f"ค่าลดหย่อน: {profile['deductions']}\n")
            file.write(f"ภาษีที่ต้องชำระ: {profile['tax']:,}\n")

        return filename
