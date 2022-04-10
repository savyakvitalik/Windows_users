import openpyxl
import os
import random


CHARS = 'abcdefghijklnop1234567qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcde'
password = ""
wb = openpyxl.load_workbook('exel.xlsx')
wb1 = openpyxl.Workbook()

wb1.create_sheet(title = 'Password', index = 0)

sheet_users = wb['Users']
sheet_group = wb['Group']
sheet_password = wb1['Password']

print("Enter number of users:")
rows_2 = int(input())
cols_2 = sheet_users.max_column

print("Enter number of groups:")
rows_1 = int(input())
cols_1 = sheet_group.max_column

print("Enter length of password")
chars_password = int(input())

for i in range(2, rows_1 + 2):
    for j in range(1, cols_1 + 1):
        if(j == 1):
            group_name = sheet_group.cell(row = i, column = j).value
        elif(j == 2):
            description_group = sheet_group.cell(row = i, column = j).value
    os.system(f"net localgroup \"{group_name}\" /add")
    os.system(f"net localgroup \"{group_name}\" /comment:\"{description_group}\"")


for n in range(2,rows_2 + 2):
    for m in range(1, cols_2 + 1):
        for k in range(1, chars_password):
            password += random.choice(CHARS)
        if(m == 1):
            user_name = sheet_users.cell(row = n,column = m).value
            sheet_password.cell(row = n - 1, column = m).value = f"{user_name}"
        elif(m == 2):
            full_name = sheet_users.cell(row = n,column = m).value
            sheet_password.cell(row = n - 1, column = m).value = f"{password}"
        elif(m == 3):
            description = sheet_users.cell(row = n,column = m).value
        elif(m == 4):
            group_add = sheet_users.cell(row = n,column = m).value
    os.system(f"net user \"{user_name}\" {password} /ADD /yes")
    os.system(f"wmic UserAccount where Name=\"{user_name}\" set PasswordExpires=False")
    os.system(f"net user \"{user_name}\" /fullname:\"{full_name}\"")
    os.system(f"net user \"{user_name}\" /comment:\"{description}\"")
    os.system(f"net localgroup \"{group_add}\" \"{user_name}\" /add")
    password = ""
if (os.path.exists("Passwaord.xlsx")):
    os.remove("Password.xlsx")
    
wb1.save('Password.xlsx')

exit()