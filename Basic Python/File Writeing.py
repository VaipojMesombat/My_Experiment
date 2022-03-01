f = open("employees.txt", "w")
for i in range(1, 6):
     print('Employee', i)
     name = input("Name: ")
     language = input("Language: ")
     f.write(name + "," + language + "\n")
print("Writing to file completed")
f.close() 
