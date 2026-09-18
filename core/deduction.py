# Requirement:
# - มี calc_deduction(profile) คำนวณค่าลดหย่อนรวมเป็น float
# - อ่านกฎจาก config.DEDUCTION_RULES ไม่กระจายกฎแบบ hard-code
# - รองรับ fixed, per-unit, percent-capped และเพดานกองทุนเกษียณ
# - ไม่ให้ค่าลดหย่อนติดลบ และห้ามใช้ input, print หรือไฟล์
