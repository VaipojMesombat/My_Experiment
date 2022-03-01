'''
Set Management : Can nit duplicate and non sequence

'''
# Define Set

Set_Variable = {"Bangkok", "Nonthaburi", "Chanthaburi","Trad","Chonburi"}
Set_II_Variable = {"Bangkok","Chonburi","Trad"}
Contruct_Set_Variable = ([1,4,7,11,19,201,222])
#print (Set_Variable)
#print (Contruct_Set_Variable)

# Add the element set
'''
Set_Variable.add ("Changmai")
print (Set_Variable)
Second_Set = [7777,888,999]
Set_Variable.update(Second_Set)
print (Set_Variable)
'''
# Delete the element in set
'''
Set_Variable.remove ("Bangkok") # "remove" In case "Bangkok" is not in this set thenerror occure
print (Set_Variable)
Set_Variable.discard ("Bangkok") # "discard" In case "Bangkok" is not in this set then no error occure

'''
# Clear set 
'''
Set_Variable.clear ()
print (Set_Variable)
'''
# Remove variable and release memory
'''
del Set_Variable
'''

# Union Set
'''
Union_Set = Set_Variable.union(Set_II_Variable)
print (Union_Set)
Copy_Set = Union_Set.copy()
print (Copy_Set)

'''
# Diferrence 
'''
Diferrence_Set = Set_Variable.difference(Set_II_Variable)
print (Diferrence_Set)

'''
# Intersection 
'''
Intersection_Set = Set_Variable.intersection(Set_II_Variable)
print (Intersection_Set)

'''
# Superset & Subset ==> boolean 

print (Set_II_Variable.issubset(Set_Variable))
print (Set_Variable.issuperset(Set_II_Variable))

# Find Min & Max Value

print (min(Contruct_Set_Variable))
print (max(Contruct_Set_Variable))