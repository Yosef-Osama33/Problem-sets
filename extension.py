x = input("File name: ")

x = x.lower()

if ".gif" in x:
    print("image/gif")
elif ".jpg" in x:
    print("image/jpeg") 
elif ".jpeg" in x:
    print("image/jpeg") 
else:
    print("application/octet-stream")