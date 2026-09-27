# Requirement:
# - มี run_quiz(n) เล่นควิซและคืนคะแนนเป็น int
# - โหลดคำถาม ตัวเลือก และคำตอบจาก data/questions.txt แบบสุ่ม
# - รองรับจำนวนข้อเกินข้อมูล ไฟล์ว่าง หรือไฟล์อ่านไม่ได้
# - แยกการตรวจคำตอบออกจากการแสดงผลเพื่อให้ทดสอบได้ง่าย
# Requirement:
# - มี run_quiz(n) เล่นควิซและคืนคะแนนเป็น int
# - โหลดคำถาม ตัวเลือก และคำตอบจาก data/questions.txt แบบสุ่ม
# - รองรับจำนวนข้อเกินข้อมูล ไฟล์ว่าง หรือไฟล์อ่านไม่ได้
# - แยกการตรวจคำตอบออกจากการแสดงผลเพื่อให้ทดสอบได้ง่าย


from core.deduction import calc_deduction
from core.calculator import calc_net_income,calc_score
import random

incomes = int(random.randrange(25000,80000,1000))
status_ran = ["married","single"]
status = random.choice(status_ran)
parent = random.randrange(0,2)
spouse = 'ไม่มีคู่สมรส'
children = 0
if status == "married":
    spouse_ran = [True,False]
    spouse = random.choice(spouse_ran)
    children = random.randrange(0,4)
    parent = random.randrange(0,4)
insurance = int(random.randrange(10000,100000,1000))
fund = random.randrange(10000,100000,1000)
print(f"""เงินเดือน {incomes} บาท 
สถานะ {status} 
ผู้ปกครอง(มีรายได้ไม่เกิน 30,000 บาท) {parent} คน
คู่สมรสมีรายได้ {spouse} (False = ไม่มีรายได้ , True = มีรายได้) 
บุตร {children} คน
ประกัน {insurance} บาท  
กองทุน {fund} บาท""")


deduction = calc_deduction(spouse, status, children,parent,insurance,fund, incomes)
tax_ans = calc_net_income(incomes,deduction) - deduction
ans = float(input("คำตอบ = "))
score = calc_score(ans,tax_ans)
