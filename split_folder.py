import os
import shutil

def split_folder(input_folder, output_folder, images_per_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    total_files = len(files)
    folder_count = 0

    for i in range(0, total_files, images_per_folder):
        folder_count += 1
        new_folder = os.path.join(output_folder, f'folder_{folder_count}')
        os.makedirs(new_folder, exist_ok=True)
        
        for j in range(i, min(i + images_per_folder, total_files)):
            shutil.copy(os.path.join(input_folder, files[j]), new_folder)

input_folder = 'archive (1)\\v_2\\agri\\s2'
output_folder = 's2 data'
images_per_folder = 500 # Adjust this number as needed

split_folder(input_folder, output_folder, images_per_folder)
