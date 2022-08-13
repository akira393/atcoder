import os
import shutil
url=str(input("urlを入力してください:"))
_folder_file_name_list = [a for a in url.split("/") if a != '']
folder_file_name_list=_folder_file_name_list[-1].split("_")
folder_name="_".join(folder_file_name_list[0:-1])
file_name=folder_file_name_list[-1]

os.makedirs(folder_name, exist_ok=True)

target_path=folder_name+"/"+file_name+".py"
if not os.path.isfile(target_path):
    shutil.copyfile("tools/templatefile.py", target_path)
else:
    print("already exists this file")
print(target_path)