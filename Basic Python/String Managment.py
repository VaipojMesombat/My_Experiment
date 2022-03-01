'''
String Management 

'''

My_Name = "vaipoj Mesombat "

print ("How long string : ", len (My_Name), "Charector")
print ("Print string with sequence from front ==> ", My_Name [0:5])
print ("Print string with sequence from back ==>", My_Name [-5:-1])
print ("Print with lower charector",My_Name.lower())
print ("Print with Upper charector", My_Name.upper())
print ("Print with out space", My_Name.strip())
print ("Delete  space on left", My_Name.lstrip())
print ("Delete spacce on right", My_Name.rstrip())
print ("Replace old string with new string", My_Name.replace ("Vaipoj", "Pojjanee"))
print ("Change the first charector to upper case", My_Name.capitalize())

Checking_Word = "Vaipoj" in My_Name # Retrun value with True/Flase 

print (Checking_Word)