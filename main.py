
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

    incomes = []
    while True:
        income_type_input = input("ประเภทรายได้ (เช่น เงินเดือน , ค่าเช่า): ")
        income_type = input_text(income_type_input)

        amount_input = input("จำนวนเงิน: ")
        amount = input_num(amount_input)

        incomes.append({"type": income_type, "amount": amount})
        more = input("เพิ่มรายได้อีกไหม? (y/n): ").strip().lower()
        if more != "y":
            break

    personal_deduction = 60000.0
    spouse_deduction = 60000.0 if status == "married" else 0.0
    insurance_input = input("ค่าเบี้ยประกัน (ถ้าไม่มีใส่ 0 ): ")
    insurance = input_num(insurance_input)

    fund_input = input("เงินกองทุน (ถ้าไม่มีใส่ 0 ): ")
    fund = input_num(fund_input)

    profile = {
        "id_card": id_card,
        "name": name,
        "age": age,
        "status": status,
        "incomes": incomes,
        "deductions": {
            "personal": personal_deduction,
            "spouse": spouse_deduction,
            "insurance": insurance,
            "fund": fund,
        },
        "taxt":None
    }

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
    profile = create_profile(id_card)

    File_name = f"{id_card}.txt"
    with open(File_name, "w",) as f:
        f.write(f"เลขบัตรประจำตัวประชาชน: {profile['id_card']}\n")
        f.write(f"ชื่อ: {profile['name']}\n")
        f.write(f"อายุ: {profile['age']}\n")
        f.write(f"สถานภาพ: {profile['status']}\n")
        f.write("รายได้:\n")
        for income in profile['incomes']:
            f.write(f"  -{income['type']}:{income['amount']}\n")
        f.write("ค่าลดหย่อน:\n")
        for key, value in profile ['deductions'].items():
            f.write(f"   -{key}: {value}\n")

    print(f"สร้างไฟล์ {File_name} เรียบร้อยเเล้ว\n")

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
