#Define:
#Variable is a container for storing data values.

full_name = "Abbas Ali"
print(full_name) #Abbas Ali
print(type(full_name)) #<class 'str'>
print(id(full_name)) #Memory Address
print(full_name.upper()) #ABBAS ALI
print(full_name.lower()) #abbas ali
print(full_name.title()) #Abbas Ali
print(full_name.strip()) #Abbas Ali
print(full_name.replace("Ali", "Khan")) #Abbas Khan
print(full_name.find("Ali")) #6
print(full_name.count("Ali")) #1
print(full_name.startswith("Abbas")) #True
print(full_name.endswith("Khan")) #False
print(full_name.split()) #['Abbas', 'Ali']
print(full_name.join(['Abbas', 'Ali'])) #AbbasAli
print(full_name.format("Abbas", "Ali")) #Abbas Ali
print(full_name.fstring("Abbas", "Ali")) #Abbas Ali
