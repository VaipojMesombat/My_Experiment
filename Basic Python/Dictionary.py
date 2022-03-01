'''
Dictionary Syntax

Variable = { index [string,boolean,number] : value [string,boolean,number] }

'''


Dictionary_Varable_1 = {1:"Vaipoj",2:"Pojjana",3:"Pojjnaee",4:"Tripub"} # Index will be number, string. 
Dictionary_Varable_2 = {"Vaipoj":"ไวพจน์","Pojjanee":"พจนี","Pojjana":"พจนา","Tripub":"ไตรภพ"}
Dictionary_Contruct = dict ({1:100,2:200,3:300})
'''''
print (Dictionary_Varable_1)
print (Dictionary_Varable_2)
print (Dictionary_Varable_1 [1])
print (Dictionary_Varable_2 ["Pojjana"])
print (Dictionary_Varable_2.get (3))
print (Dictionary_Contruct)
'''
# Update = update value (exits element) or insert new element in dictionary
'''
Dictionary_Varable_1.update ({1:"Mr. Vaipoj"})
print (Dictionary_Varable_1)
Dictionary_Varable_2.update ({"Mesombat":"Surname"})
print (Dictionary_Varable_2)
'''
'''
for item in Dictionary_Varable_1 : # print only key
    print (item)

for value in Dictionary_Varable_2.values () : # print only value
    print (value)

for item,value in Dictionary_Varable_2.items () : # print key, value 
    print (item,value)

'''

# Delete element in Dictionary
'''
Dictionary_Contruct.pop(2) # delete element with define by index
print (Dictionary_Contruct)
Dictionary_Varable_1.popitem() # delete the last element
print (Dictionary_Varable_1)
'''

# Clear & release dictionary 
'''
Dictionary_Varable_1.clear()
print (Dictionary_Varable_1)

del Dictionary_Varable_1  # remove this variable and release memory

'''
# Copy Dic
'''
New_Dic = Dictionary_Varable_1.copy() 
print (New_Dic)

'''

# Neted DIc 

Address_Dic = {
                "Country" : {1:"Thainland",2:"Japan",3:"USA"},
                "City" : {"First_City":"Bangkok","Second_City":"Tokyo","Third_City":"Newyork"},
                "Road" : {100: "Road 1",200:"Road 2",300:"Road 3"},
                "House_Hold"  : {11:"Vaipoj",12:"Pojajana",13:"Pojjanee"}
            }



print (Address_Dic)
print (Address_Dic ["Country"][1])
print (Address_Dic["City"] ["First_City"])
print ("Bangkok" in Address_Dic ["Country"])  # find element in neted dic then it will be return true/false


