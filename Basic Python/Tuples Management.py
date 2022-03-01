'''
Tuple Data Type: The value is this data type is the same with list but it can not change then it like 
instance variable. The value in tuple it should be contrain number, boolean, floting point and string.

'''
# Define Tuple 
#   Normal
from typing import Tuple


Tuple_Variable = ("ID Number: 123456789", "Driver_Licenses: 34567", "Social Security Number: 1111",
                    1999, True, 999.99)

List_Variable = [1,2,3,False,"Vaipoj", 11.99]

# Define Tuple with only one value 

Tuple_Only_One_Value = ("Bangkok",) 

#print ("Normal Define: ", Tuple_Variable, "\n", List_Variable)

#   Contruct Define

Tuple_Contruct = tuple (("Vaipoj Mesombat", 57, 789.89, False, ))
List_Contruct = list (["Pojjanee",False, 123, 999,999])
#print ("Contruct Define: ", Tuple_Contruct, "\n",List_Contruct)

# Converse Tuple to List 

Conver_Tuple2List = list (Tuple_Variable) 
#print (Conver_Tuple2List)
Conver_Tuple2List[0] = "Change Value"
#print (Conver_Tuple2List)

# Conver List to Tuples

Conver_List2Tuple = tuple (Conver_Tuple2List) 
# print (Conver_List2Tuple)

# Reverse Tuple

Country = "Thailand"
Tuple_Country = tuple (Country)
print (Tuple_Country)
Reverse_Tuple = tuple (reversed(Tuple_Country))
print (Reverse_Tuple)

# Join Tupe
Tuple_City = ("Bangkok",)
Tuple_Province = ("Sapanseang",)
Address = Tuple_City + Tuple_Province
print (Address)
