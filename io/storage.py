# Requirement:
# - มี save_taxpayer(profile), load_all(), find_taxpayer(id_card) และ delete_taxpayer(id_card)
# - มี export_summary(profile, tax) สร้างไฟล์สรุปและคืนชื่อไฟล์ .txt
# - จัดเก็บข้อมูลตาม profile schema และรองรับข้อมูลไม่มีไฟล์/ไฟล์ว่าง/ข้อมูลเสียหาย
# - ตรวจสอบเลขบัตรก่อนบันทึก และไม่รับ input หรือแสดงเมนูเอง
### ทำงานที่เกี่ยวข้องกับการจัดการไฟล์ ./data/taxpayer.txt เท่านั้น

def save_taxpayer(profile: dict) -> bool:
    pass

def load_all() -> list:
    #โหลดข้อมูลทั้งหมดของ profile
    pass

def find_taxpayer(id_card) -> bool:
    #เช็คว่า id_card ที่ใส่เข้ามานั้นมีอยู่แล้วใน taxpayer.txt หรือมั้ย แล้ว return ค่า bool
    pass

def create_profile(id_card) -> dict:
    #สร้าง dict ของ profile id_card นั้น ๆ จาก taxpayer.txt แล้ว return profile type-data: dict
    #ตัวอย่างค่าที่ต้องการให้ return profile = {
    # "id_card":    "1234567890123",   # str, 13 หลัก
    # "name":       "สมชาย ใจดี",       # str
    # "age":        35,                 # int
    # "status":     "single",           # "single" / "married"
    # "incomes": [                      # list ของ dict
    #     {"type": "เงินเดือน", "amount": 480000.0},
    #     {"type": "ค่าเช่า",   "amount":  60000.0},
    # ],
    #"deductions": {                   # dict
    #     "personal":  60000.0,
    #     "spouse":        0.0,
    #     "insurance": 25000.0,
    #     "fund":      50000.0,
    # },
    # "tax": None
    # }
    pass

def delete_taxpayer(id_card: str) -> bool:
    pass

def export_summary_profile(id_card: str):
    pass