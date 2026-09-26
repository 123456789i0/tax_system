# Requirement:
# - มี calc_deduction(profile) คำนวณค่าลดหย่อนรวมเป็น float
# - รองรับ fixed, per-unit, percent-capped และเพดานกองทุนเกษียณ
# - ไม่ให้ค่าลดหย่อนติดลบ และห้ามใช้ input, print

# from io.storage import create_profile

def calc_dection() -> dict:
    #คำนวณค่าลดหย่อน และค่าลดหย่อนรวม ของแต่ละ profile id_card แล้ว return ข้อมูลที่เก็บ
    personal = 60000
    child = 0
    cal_spouse = 0

    if spouse == False:
        cal_spouse = 60000

    if status.lower() == "married":
        child = min(children,3)  * 30000

    
    cal_parent = min(parent,4) * 60000
    
    cal_insurance = min(insurance,100000)

    cal_fund = min(fund , (incomes*12)*0.3)
    
    dection_dict = {"personal": 60000.0,
                "spouse": cal_spouse,
                "parent": cal_parent, 
                "child": child,
                "insurance": cal_insurance ,
                  "fund":      cal_fund,}
    
    return dection_dict

profile  = {
        "id_card":    "1234567890123",   # str, 13 หลัก
        "name":       "สมชาย ใจดี",       # str
        "age":        35,                 # int
        "status":     "single", 
        "child" : 0 ,           # "single" / "married" children = ?
        "incomes": 480000.0,
        
        "deductions": {                   # dict
            "personal":  60000.0,
            "spouse":        0.0,
            "insurance": 25000.0,
            "fund":      50000.0,
        },
        "tax": None
        }
calc_dection(profile)
