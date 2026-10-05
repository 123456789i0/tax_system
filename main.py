from core.calculator import calc_net_income, cal_tax 
from core.deduction import calc_dection
from io_utils.display import show_menu, input_text, input_num, input_menu, input_id, input_choice
from io_utils.storage import save_taxpayer,create_profile_input, create_profile, find_taxpayer, delete_taxpayer, export_summary_profile
from extra.quiz import quiz

def menu1_add_taxpayer(id_card):
    name_input = input("กรอกชื่อ: ")
    name = input_text(name_input)

    age_input = input("กรอกอายุ: ")
    age = int(input_num(age_input))

    status_input = input("กรอกสถานภาพ (single/married):")
    status = input_choice(status_input, ["single","married"])

    income_input = input("กรอกรายได้ทั้งปี: ")
    income = input_num(income_input)

    expenses_input = input("กรอกค่าใช้จ่ายตามกฎหมาย: ")
    expenses = input_num(expenses_input)

    spouse_input = input("คู่สมรสมีรายได้ใช่หรือไม่ (y=มีรายได้ / n=ไม่มีรายได้): ").strip().lower()
    spouse = input_choice(spouse_input, ["y", "n"])

    children_input = input("จำนวนบุตรที่ชอบด้วยกฎหมาย: ")
    children = int(input_num(children_input))

    parent_input = input("จำนวนบิดามารดาที่ต้องเลี้ยงดู(อายุมากกว่า 60 มีเงินได้พึงประเมินรวมทั้งปี ไม่เกิน 30,000 บาท): ")
    parent = int(input_num(parent_input))

    insurance_input = input("ค่าเบี้ยประกัน (ถ้าไม่มีใส่ 0 ): ")
    insurance = input_num(insurance_input)

    fund_input = input("เงินกองทุน (ถ้าไม่มีใส่ 0 ): ")
    fund = input_num(fund_input)

    deductions = calc_dection(spouse, status, children, parent, insurance, fund, income)
    profile = create_profile_input(id_card, name, age, status, income, expenses, deductions)
    net_income = calc_net_income(profile)
    tax = cal_tax(net_income)
    profile["tax"] = tax
    isSave = save_taxpayer(profile)
    if isSave: print("เพิ่มข้อมูลภาษีเรียบร้อยเเล้ว\n")
    else: print("Error!")
    #เพิ่มข้อมูลในไฟล์ taxpayer.py
    ### หมายเหตุเข้าไปดู requirment ค่าที่ต้องการในไฟล์ taxpayer.txt
    #ใช้งานคู่กับ save taxpayer
    # รายได้ต่อเดือน

def menu2_calculate_tax(id_card):
    #หาค่าภาษีที่เคยมีใน taxpayer.txt แต่หากไม่เคยให้คำนวณภาษี และบันทึก tax ลงในไฟล์ taxpayer.txt
    profile = create_profile(id_card)
    tax = cal_tax(profile["tax"])
    print(f"จำนวนภาษีที่ต้องชำระ = {tax:,.2f} บาท\n")

def menu3_create_id_txt(id_card):
    filename = export_summary_profile(id_card)

    if filename is None:
        print("ไม่พบเลขบัตรประจำตัวประชาชนนี้ในระบบ\n")
    else:
        print(f"สร้างไฟล์ {filename} เรียบร้อยเเล้ว\n")
    #ออกแบบ และสร้างไฟล์ .txt ของ id_card ที่ user กรอก โดยใช้ชื่อไฟล์ ex. 1-2345-67891-23-4.txt

def menu4_delete_taxpayer(id_card):
    if delete_taxpayer(id_card):
        print("ลบข้อมูลผู้เสียภาษีเรียบร้อยเเล้ว\n")
    else:
        print(delete_taxpayer(id_card))
        print("ไม่พบข้อมูลผู้เสียภาษี ลบไม่สำเร็จ\n")
    #ลบข้อมูล profile ของ id_card ที่ user กรอก

def menu5_quiz():
    #สุ่มคำถามจาก ./data/question.txt
    profile = quiz()
    ans_u = input("คำตอบ = ")
    ans = input_num(ans_u)

 
    print(f"เฉลยภาษีที่ต้องจ่าย {profile["tax"]} บาทส่วนต่าง {abs(profile["tax"]-ans)} บาทคลาดเคลื่อน {min(((abs(profile["tax"]-ans)/max(profile["tax"],1)*100)),100):.2f}% ")

while True:

    choice = show_menu()
    choice = input_menu(choice)
    # input_menu(choice)

    if choice == "1":
        id_card = input("กรอกเลขบัตรประชาชนของคุณ: ")
        id_card = input_id(id_card)
        if not find_taxpayer(id_card):
            menu1_add_taxpayer(id_card) #เรียกใช้งานฟังก์ชันที่ทำหน้าที่รับข้อมูลจาก user ให้ถูกต้อง และเพิ่มข้อมูล profile ลงใน taxpayer.py
        else:
            print("เลขบัตรประจำตัวประชาชนนี้มีการบันทึกข้อมูลเอาไว้แล้ว\n")

    elif choice == "2":       
        id_card = input("กรอกเลขบัตรประชาชนของคุณ: ")
        id_card = input_id(id_card)
        if find_taxpayer(id_card):
            menu2_calculate_tax(id_card)
        
        else:
            print("ไม่พบข้อมูลของเลขบัตรประจำตัวประชาชนนี้ในระบบ โปรดเพิ่มข้อมูลผู้เสียภาษีก่อนคำนวณภาษี\n")

    elif choice == "3":
        id_card = input("กรอกเลขบัตรประชาชนของคุณ: ")
        id_card = input_id(id_card)
        if find_taxpayer(id_card):
            menu3_create_id_txt(id_card)
        else:
            print("ไม่พบข้อมูลของเลขบัตรประจำตัวประชาชนนี้ในระบบ\n")

    elif choice == "4":
        id_card = input("กรอกเลขบัตรประชาชนของคุณ: ")
        # id_card = input_id(id_card)
        id_card = input_id(id_card)
        if find_taxpayer(id_card):
            menu4_delete_taxpayer(id_card)
        else:
            print("ไม่พบข้อมูลของเลขบัตรประจำตัวประชาชนนี้ในระบบ\n")

    elif choice == "5":
        menu5_quiz()

    else:
        print("ERROR!")
        break

    isContinue = input_choice(input("continue program (y/n) : "), ['y', 'n'])
    if not isContinue:
        print("จบการทำงานของระบบคำนวณและจัดการภาษีเงินได้บุคคลธรรมดา")
        print("โปรแกรมนี้เป็นการคำนวณคร่าวๆโปรดปรึกษาผู้เชี่ยวชาญ\n")
        break
