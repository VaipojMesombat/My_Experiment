'''
File Management

'''
'''
try :

    File_name = "File_Management_data.txt"
    Read_File = open (File_name ,"r",encoding = "utf8")   # "encoding = utf8" is used for read Thai charector
    print ("Read the whole file \n",Read_File.read())                     # read the whole file 
    # print ("Read just only 5 char in file \n", File_String.read(5))         # In case you need just only 5 char in file if the previous command read the whole then the pointer still at the end of ile thus it will be print none   
    Read_File.close ()                                     # Must closed after use a file
except  FileNotFoundError :
     print ("File not found")

'''

# Create new file 
# Define vavriable 

import os                   # import "os" library 

New_File = "New_File.txt"
Delete_File = "Delete_File.txt"
Data_in_New_File = "New File\n"
Second_Line = "Second Line\n"
Third_Line = "Thrid Line\n"
Fourth_Line = "Fourth Line\n"


#Ceate_File = open(New_File,"x",encoding="utf8")    # "x" = only create new file , "w" = create and write the date in to file 
'''
Write_File = open (New_File,"w",encoding="utf8")
Write_File.writelines (Data_in_New_File)
Write_File.writelines (Second_Line)
Write_File.writelines (Third_Line)
Write_File.writelines ("XXXxx\n")
Write_File.close ()
Write_File = open (New_File,"a",encoding="utf8")    # "a" append file 
Write_File.writelines (Fourth_Line)
Write_File = open (New_File,"r",encoding="utf8")
Read_File = Write_File.read()
print ("Data in new file is\n", Read_File)
Write_File.close ()

'''
 
Delete_File_Open = open (Delete_File,"w",encoding="utf8")
Delete_File_Open.writelines (Data_in_New_File)
Delete_File_Open.writelines (Second_Line)
Delete_File_Open.writelines (Third_Line)
Delete_File_Open.writelines (Fourth_Line)
Delete_File_Open.close ()
Delete_File_Read = open (Delete_File,"r",encoding="utf8")

print ("Before\n")
for Line in Delete_File_Read.readlines() :
    Content = Line [0:11]
    print (Content)

Delete_File_Read.close()


Delete_File_Open = open (Delete_File,"a",encoding="utf8") # "w" mode will be replace all data in file
Delete_File_Open.writelines ("Last Line")
Delet_File_Open = open (Delete_File,"r",encoding="utf8")
Read_After_INsert_Last_line = Delet_File_Open.read()
print ("After\n",Read_After_INsert_Last_line)

# Delete Text file 
'''
try :

    os.remove ("Delete_File")
    Delet_File_Read = open (Delete_File,"r",encoding="utf8")

except FileNotFoundError :

    print ("File not Found")

'''


