import os
import shutil
            
#Get the type of the file based on its extension
def getting_type_of_file(file_name):
    extension_file = os.path.splitext(file_name)[1].lower()
    if extension_file in ['.jpg', '.jpeg', '.png', '.gif']:
        return 'Images'
    elif extension_file in ['.pdf', '.docx', '.txt','.xlsx','.pptx','.ppt']:
        return 'Documents'
    elif extension_file in ['.mp4', '.avi', '.mov']:
        return 'Videos'
    elif extension_file in ['.mp3', '.wav', '.mov']:
        return 'Audios'
    elif extension_file in ['.exe']:
        return 'Executable Files'
    elif extension_file in ['.c++']:
        return 'C++ Files'
    elif extension_file in ['.py']:
        return 'Python Files'
    elif extension_file in ['.c']:
        return 'C Files'
    elif extension_file in ['.java']:
        return 'Java Files'
    elif extension_file in ['.html']:
        return 'HTML Files'
    elif extension_file in ['.css']:
        return 'CSS Files'
    elif extension_file in ['.js']:
        return 'Javascript Files'
    elif extension_file in ['.zip']:
        return 'Zip_Files'
    else:
        return 'Others'
    
#Create folders
def creating_folders(directory, folders):
    for folder_name in folders:
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
#Organize files in the specified directory into separate folders
def organize_files(directory):
    folders = ['Images', 'Documents', 'Videos','Audios','Executable Files','C++ Files','Python Files','C Files','Java Files','HTML Files','CSS Files',
               'Javascript Files','Zip_Files','Others']
    creating_folders(directory, folders)
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        for file_name in files:
            file_type = getting_type_of_file(file_name)
            source_path = os.path.join(directory, file_name)
            destination_path = os.path.join(directory, file_type, file_name)
            shutil.move(source_path, destination_path)
        print("Files organized successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        directory = input("Enter the directory to organize: ")
        organize_files(directory)
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("The given task is executed")
