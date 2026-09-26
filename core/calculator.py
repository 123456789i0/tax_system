# Requirement:
# - มี calc_tax(net_income) คำนวณภาษีตามขั้นบันไดจาก config
# - มี calc_net_income(profile) คำนวณเงินได้สุทธิหลังหักค่าลดหย่อน
# - เป็น pure function คืนค่าเป็น float/list และห้ามใช้ input, print

# from io.storage import create_profile
from deduction import calc_dection

profile  = {
        "id_card":    "1234567890123",   # str, 13 หลัก
        "name":       "สมชาย ใจดี",       # str
        "age":        35,                 # int
        "status":     "single", 
        "child" : 0 ,           # "single" / "married" children = ?
        "incomes": 48000.0,
        
        "deductions": {                   # dict
            "personal":  60000.0,
            "spouse":        0,
            "insurance": 25000.0,
            "fund":      50000.0,
        },
        "tax": None
        }

def calc_net_income(profile: dict) -> float:
    total_dection = 0
    for dection in profile["deductions"].values():
          total_dection += dection
    net_income = (profile["incomes"]*12) - total_dection
    return net_income


    # profile = create_profile()
    # Dection = calc_dection()
    # net_income = (profile["incomes"] * 12) - sum(Dection.values())
    # return net_income
    
def cal_tax(net_income: float) -> float:
    if net_income <= 150000:
            tax = 0
    elif net_income <= 300000:
            tax = (net_income - 150000) * 0.05
    elif net_income <= 500000:
            tax = 7500 + (net_income - 300000) * 0.10
    elif net_income <= 750000:
            tax = 27500 + (net_income - 500000) * 0.15
    elif net_income <= 1000000:
            tax = 65000 + (net_income - 750000) * 0.20
    elif net_income <= 2000000:
        tax = 115000 + (net_income - 1000000) * 0.25
    elif net_income <= 5000000:
        tax = 365000 + (net_income - 2000000) * 0.30
    else:
        tax = 1265000 + (net_income - 5000000) * 0.35
    
    return tax



net_income = calc_net_income(profile)
tax = cal_tax(net_income)
print(net_income)
print(tax)

