from os import listdir,mkdir,rename
from os.path import isfile, join, exists

source = '/Users/shahriyer/Downloads'
files = listdir(source)

files_to_folder_map = {
    'jpg jpeg png gif svg' : 'Images',
    'app dmg pkg' : 'Applications',
    'txt doc docx xls xlsx pages pdf csv' : 'Documents',
    'zip zar gz bz2 iso' : 'Archives',
    'mp3': 'Audio',
    'mp4 avi flv mov mpeg': 'Videos',
    'sketch' : 'Sketch',
    'ai' : 'Illustrator',
    'psd' : 'PSD'
}

def get_file_extension(file_name):
    split_name = file_name.split('.')
    return split_name[-1]

def create_folder(name):
    if not exists(join(source,name)):
        mkdir(join(source,name))

def move_file_to_folder(file_name,folder_name):
    old_path = join(source, file_name)
    new_path = join(source, folder_name, file_name)
    rename(old_path,new_path)

def map_file_to_folder(extention,name):
    folder_name = 'Others'

    for extensions,destination in files_to_folder_map.items():
        if extention in extensions.split(' '):
            folder_name = destination
            break

    create_folder(folder_name)
    move_file_to_folder(name,folder_name)

def main():
    for file_name in files:
        if isfile(join(source,file_name)):
            extension = get_file_extension(file_name)
            map_file_to_folder(extension,file_name)

if __name__ == "__main__":
    main()
    print("Done!")