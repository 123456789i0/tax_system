
from core.calculator import cal_tax, calc_net_income
from core.deduction import calc_dection
from io.display import show_menu, input_menu, input_id, input_text, input_num, input_choice
from io.storage import save_taxpayer, find_taxpayer, delete_taxpayer, export_summary_profile


def menu1_add_taxpayer(id_card):
    name_input = input("กรอกชื่อ: ")
    name = input_text(name_input)

    age_input = input("กรอกอายุ: ")
    age = int(input_num(age_input))

    status_input = input("กรอกสถานภาพ (single/married):")
    status = input_choice(status_input, ["single","married"])

    income_input = input("กรอกรายได้ต่อเดือน: ")
    income = input_num(income_input)

    spouse_input = input("มีคู่สมรสไหม? (y/n): ").strip().lower()
    spouse = input_num(spouse_input == "y")

    children_input = input("จำนวนบุตร: ")
    children = int(input_num(children_input))

    parent_input = input("จำนวนบิดามารดาที่ต้องเลี้ยงดู: ")
    parent = int(input_num(parent_input))

    insurance_input = input("ค่าเบี้ยประกัน (ถ้าไม่มีใส่ 0 ): ")
    insurance = input_num(insurance_input)

    fund_input = input("เงินกองทุน (ถ้าไม่มีใส่ 0 ): ")
    fund = input_num(fund_input)

    deductions = calc_dection(spouse, status, children, parent, insurance, fund, income)

    profile = create_profile()
    save_taxpayer(profile)
    print("เพิ่มข้อมูลภาษีเรียบร้อยเเล้ว\n")
    #เพิ่มข้อมูลในไฟล์ taxpayer.py
    ### หมายเหตุเข้าไปดู requirment ค่าที่ต้องการในไฟล์ taxpayer.txt
    #ใช้งานคู่กับ save taxpayer
    # รายได้ต่อเดือน
    

def menu2_calculate_tax(id_card):
    #หาค่าภาษีที่เคยมีใน taxpayer.txt แต่หากไม่เคยให้คำนวณภาษี และบันทึก tax ลงในไฟล์ taxpayer.txt
    pass

def menu3_create_id_txt(id_card):
    filename = export_summary_profile(id_card)
    print(f"สร้างไฟล์ {filename} เรียบร้อยเเล้ว\n")
    #ออกแบบ และสร้างไฟล์ .txt ของ id_card ที่ user กรอก โดยใช้ชื่อไฟล์ ex. 1-2345-67891-23-4.txt

def menu4_delete_taxpayer(id_card):
    delete_taxpayer(id_card)
    print("ลบข้อมูลผู้เสียภาษีเรียบร้อยเเล้ว\n")
    #ลบข้อมูล profile ของ id_card ที่ user กรอก



def menu5_quiz():
    #สุ่มคำถามจาก ./data/question.txt
    pass

while True:

    choice = show_menu()

    input_menu(choice)

    if choice == "0":
        print("จบการทำงานของระบบคำนวณและจัดการภาษีเงินได้บุคคลธรรมดา\n")
        break

    elif choice == "1":
        id_card = input_id()
        if not find_taxpayer(id_card):
            menu1_add_taxpayer() #เรียกใช้งานฟังก์ชันที่ทำหน้าที่รับข้อมูลจาก user ให้ถูกต้อง และเพิ่มข้อมูล profile ลงใน taxpayer.py
        else:
            print("เลขบัตรประจำตัวประชาชนนี้มีการบันทึกข้อมูลเอาไว้แล้ว\n")
            continue

    elif choice == "2":
        id_card = input_id()
        if find_taxpayer(id_card):
            menu2_calculate_tax(id_card)
        else:
            print("ไม่พบข้อมูลของเลขบัตรประจำตัวประชาชนนี้ในระบบ โปรดเพิ่มข้อมูลผู้เสียภาษีก่อนคำนวณภาษี\n")
            continue

    elif choice == "3":
        id_card = input_id()
        if find_taxpayer(id_card):
            menu3_create_id_txt(id_card)
        else:
            print("ไม่พบข้อมูลของเลขบัตรประจำตัวประชาชนนี้ในระบบ\n")
            continue

    elif choice == "4":
        id_card = input_id()
        if find_taxpayer(id_card):
            menu4_delete_taxpayer(id_card)
        else:
            print("ไม่พบข้อมูลของเลขบัตรประจำตัวประชาชนนี้ในระบบ\n")
            continue

    elif choice == "5":
        menu5_quiz()

    else:
        print("ERROR!")
        break
