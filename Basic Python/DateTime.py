'''
Date Time 

'''
import datetime



Today_Str = datetime.datetime.now()
#print (Today_Str)                   # all things 
#print (Today_Str.year)
#print (Today_Str.month)
#print (Today_Str.day)
#print (Today_Str.hour)
#print (Today_Str.minute)
#print (Today_Str.second)
#print (Today_Str.strftime("%x"))                # yare/month/date
#print (Today_Str.strftime("%X"))                # hours/min/sec
#print (Today_Str.strftime("%c"))                # day/month/date/time/year
#print (Today_Str.strftime("%H : %M.%C %p %j"))  # hour/min/sec/AM-PM and date in year


#NewDate = datetime.datetime (2020,12,8,9)       # Set Year, Month,Date,Time
#print ("Set New Date Time :", NewDate)

# Date 

Day_Str = Today_Str.strftime ("%A")

if Day_Str == "Monday" :
    pass
elif Day_Str == "Tuesday" :
    print ("Yes")

    


#print (Today_Str.strftime ("%a"))               # Day short name
#print (Today_Str.strftime ("%A"))               # Day full name
#print (Today_Str.strftime ("%w"))               # day in week
#print (Today_Str.strftime ("%d"))               # date
#print (Today_Str.strftime ("%b"))               # Month short name
#print (Today_Str.strftime ("%B"))               # Month full name
#print (Today_Str.strftime ("%Y"))               # Year