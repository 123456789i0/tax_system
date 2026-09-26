
from core.calculator import cal_tax, calc_net_income
from core.deduction import calc_dection
from io.display import show_menu, input_menu, input_id, input_text, input_num, input_choice
from io.storage import save_taxpayer, find_taxpayer, delete_taxpayer, export_summary_profile

def menu1_add_taxpayer(id_card):
    #เพิ่มข้อมูลในไฟล์ taxpayer.py
    ### หมายเหตุเข้าไปดู requirment ค่าที่ต้องการในไฟล์ taxpayer.txt
    #ใช้งานคู่กับ save taxpayer
    pass

def menu2_calculate_tax(id_card):
    #หาค่าภาษีที่เคยมีใน taxpayer.txt แต่หากไม่เคยให้คำนวณภาษี และบันทึก tax ลงในไฟล์ taxpayer.txt
    pass

def menu3_create_id_txt(id_card):
    #ออกแบบ และสร้างไฟล์ .txt ของ id_card ที่ user กรอก โดยใช้ชื่อไฟล์ ex. 1-2345-67891-23-4.txt
    pass

def menu4_delete_taxpayer(id_card):
    #ลบข้อมูล profile ของ id_card ที่ user กรอก
    pass


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