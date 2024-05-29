import os
from shutil import copytree, ignore_patterns
from googletrans import Translator

def translate_and_copy_folders(root_folder, new_folder):
    translator = Translator()

    # Sao chép cấu trúc thư mục và các tệp từ thư mục gốc sang thư mục mới
    copytree(root_folder, new_folder, ignore=ignore_patterns('*.pyc'))

    # Dịch tên thư mục và đổi tên
    for foldername in os.listdir(new_folder):
        folderpath = os.path.join(new_folder, foldername)
        if os.path.isdir(folderpath):
            translated_name = translator.translate(foldername, src='en', dest='vi').text
            os.rename(folderpath, os.path.join(new_folder, translated_name))
            print(f"Dịch {foldername} sang {translated_name} thành công!")

# Thay đổi đường dẫn root_folder và new_folder thành đúng đường dẫn của thư mục gốc và thư mục mới
root_folder = r"D:\HCSDLDPT\HCSDLDPT_birds_classification\Bird_dataset_OZ_1"
new_folder = r"D:\HCSDLDPT\HCSDLDPT_birds_classification\Bird_dataset_OZ_1_1"
translate_and_copy_folders(root_folder, new_folder)
