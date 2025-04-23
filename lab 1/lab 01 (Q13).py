#Convert bytes into KB, MB, and GB:

a = int(input("Enter bytes: "))
kb = a / 1024
mb = kb / 1024
gb = mb / 1024
print(a, "bytes is: ", kb, "KB,", mb, "MB, and", gb, "GB")