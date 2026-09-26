# Requirement:
# - เก็บค่าคงที่ของระบบ เช่น TAX_BRACKETS และ DEDUCTION_RULES
# - เก็บ RETIREMENT_GROUP และ RETIREMENT_GROUP_CAPเ
# - ใช้เป็นแหล่งกฎกลางของระบบ และไม่แก้ค่าระหว่างโปรแกรมทำงาน
# - ห้ามรับ input แสดงผล

TAX_BRACKETS = (
    # (เพดานบนของขั้น, อัตราภาษี %)
    (150000, 0),
    (300000, 5),
    (500000, 10),
    (750000, 15),
    (1000000, 20),
    (2000000, 25),
    (5000000, 30),
    (float("inf"), 35),
)

DEDUCTION_RULES = {
    "personal": {"type": "fixed", "amount": 60000},
    "spouse":   {"type": "fixed", "amount": 60000},
    "child":    {"type": "per_unit", "unit_amount": 30000, "max_units": 3},
    "parent":   {"type": "per_unit", "unit_amount": 30000, "max_units": 4},
    "health_insurance": {"type": "percent_capped", "cap": 25000},
    "donation": {"type": "percent_of_net", "percent": 10},
}
