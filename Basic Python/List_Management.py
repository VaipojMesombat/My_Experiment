'''
List Managment 

'''

# Define empty
Empty_List = []

# Define Variable 

Number_List = [1,2,3,4,5,6,7,7,8,8,10]
String_List = ["Bangkok","Chonburi","Nonthabuti","Samui"]
String_List2 = ["Air", "Sea","Land"]
Item = ["Bag", "Shoe", "Shirt"]
Pric = [100,200,300]

# print all member of list

# print (Number_List)  
# print (String_List)

# print (len(Number_List))

# How to access to List

''' Access by index of Lsit

for Member_of_list in range (len (String_List)) :
    print (Number_List [Member_of_list])
    print (String_List [Member_of_list])

'''

# Assige value in list to variable 
'''
for Member_of_list in String_List :
    print (Member_of_list)
   
Loop = 0
while Loop < len (Number_List) :
    print (Number_List[Loop])
    Loop+=1

'''

# Insert new item to List
'''
String_List.append ("Bangkok") # append at the end of list
String_List.insert (1,"Chanthaburi") # insert after item 1
print (String_List)

'''

# Remove member of list

# String_List.remove ("Bangkok") # remove by exactly word
# print (String_List)

'''
String_List.pop () # Remoce at lasted of List 
print (String_List)

'''
# del String_List # remove variable String_List from memory

# String_List.claer() # Clear all member in list

'''
Counting 

'''

# Counting = Number_List.count(7)
# print (Counting)

'''
Concatination List

'''

# All_Group = Number_List + String_List
# print (All_Group)

# Number_List = Number_List + String_List
# print (Number_List)

# Number_List.extend (String_List)
# print (Number_List)

'''
Sorting (number and string) 

'''

# Number_List.sort () # น้อยไปมาก
# print (Number_List) 

# Number_List.reverse () # มากไปน้อย
# print (Number_List)

'''
Find Max & Min value from List

'''
# print (max(Number_List))
# print (min(Number_List))

'''
Sorting element in the from back to front

'''

# String_List = String_List [::-1]
# print (String_List)

'''


'''
# for Number in range (len(Number_List)) :
# for Number in range (0,10,1) : # 0 = starting, 10 = loop number, 1 = increase by 1
# Number_List [Number] = Number_List [Number]**2

# Number_List = [Number**2 for Number in Number_List] # for loop แบบลดรูป
# print (Number_List)
  
# New_List = [ String_1 + " " + String_2 for String_1 in String_List for String_2 in String_List2]
# print (New_List)

'''
Function zip : ใช้ในการจัยคู่สมาชิกใน List สองตัว

'''

# for Good, Pricing in zip (Item,Pric) :
#    print (Good," ", Pricing)

#for Good, Pricing in zip (Item,Pric[::-1]) : # [::-1] การนำสมาชิกตัวหลังสุดไปตัวหน้า
#    print (Good," ", Pricing)

