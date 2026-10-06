
# Requirement:
# - มี run_quiz(n) เล่นควิซและคืนคะแนนเป็น int
# - โหลดคำถาม ตัวเลือก และคำตอบจาก data/questions.txt แบบสุ่ม
# - รองรับจำนวนข้อเกินข้อมูล ไฟล์ว่าง หรือไฟล์อ่านไม่ได้
# - แยกการตรวจคำตอบออกจากการแสดงผลเพื่อให้ทดสอบได้ง่าย


from core.deduction import calc_dection
from core.calculator import calc_net_income, cal_tax
from io_utils.storage import create_profile_input
import random

def quiz():
    income_q = int(random.randrange(25000,80000,1000))
    status_ran = ["married","single"]
    status_q = random.choice(status_ran)
    parent_q = random.randrange(0,2)
    spouse_q = False
    children_q = 0
    if status_q == "married":
        spouse_ran = [True,False]
        spouse_q = random.choice(spouse_ran)
        children_q = random.randrange(0,4)
        parent_q = random.randrange(0,4)
    insurance_q = int(random.randrange(10000,100000,1000))
    fund_q = random.randrange(10000,100000,1000)
    print(f"""เงินเดือน {income_q} บาท 
    สถานะ {status_q} 
    ผู้ปกครอง(มีรายได้ไม่เกิน 30,000 บาท) {parent_q} คน
    คู่สมรสมีรายได้ {spouse_q} (False = ไม่มีรายได้ , True = มีรายได้) 
    บุตร {children_q} คน
    ประกัน {insurance_q} บาท  
    กองทุน {fund_q} บาท""")

                # calc_dection(spouse, status, children, parent,insurance,fund, income)
    deductions_q = calc_dection(spouse_q, status_q, children_q,parent_q,insurance_q,fund_q, income_q)
    profile = create_profile_input(status=status_q, income=income_q, deductions=deductions_q)
    tax_ans = cal_tax(calc_net_income(profile))
    profile["tax"] = tax_ans
    return profile
