import glob, os

path = input("path daxil edin ")
os.chdir(path)
dir_list = os.listdir(path)
print(dir_list)

for file in dir_list:
    if file.endswith(".txt"):
        os.remove(file)
        print('All viruses removed from your device')
    else:
        print('No virus detected on your device')