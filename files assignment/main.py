__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
""" You need to master the following to complete this assignment:
        Importing and using Python modules;     Reading and understanding Python standard library documentation.
After running the above wincpy start you should have the following files:
        __init__.py (ignore this)       main.py      data.zip"""


"""clean_cache: takes no arguments and creates an empty folder named cache in the current directory.
If it already exists, it deletes everything in the cache folder."""


import fileinput
import os
import shutil


def clean_cache():
    current_directory = os.getcwd()
    total_filepath=os.path.join(current_directory,"files")
    new_folder=os.path.join(total_filepath,"cache")
    if os.path.exists(new_folder):
        print("new folder does exist and is replaced")
        shutil.rmtree(new_folder)
    os.makedirs(new_folder)
    print("current_directory=", current_directory,"\n", "total path=",total_filepath, "\n new_folder=",new_folder)



"""cache_zip:
takes a zip file path (str) and a cache dir path (str) as arguments, in that order.
The function then unpacks the indicated zip file into a clean cache folder.
You can test this with data.zip file."""

def cache_zip(zip_file_path, cache_dir_path):
    from zipfile import ZipFile
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)



"""cached_files:
takes no arguments and returns a list of all files in the cache.
File paths should be specified in absolute terms. Search the web for what this means!
No folders should be included in the list. You do not have to account for files within folders within the cache directory."""


def cached_files():
    lijst=[]
    path = os.path.abspath("files/cache") 
    dir_list=os.listdir(path)
    for name in dir_list:
        new_name=os.path.join(path,name)
        lijst.append(new_name)
    #print ("lijst is", lijst)
    return lijst 


"""find_password:
takes the list of file paths from cached_files as an argument.
This function should read the text in each one to see if the password is in there.
Surely there should be a word in there to indicate the presence of the password?
Once found, find_password should return this password string."""

def find_password(lijst):
    tekst=""
    for file in lijst:         #lees de tekst van de file in
        with fileinput.input(file, encoding="utf-8") as f:
            for line in f:            
                if "password" in line:  #controleer of het woord password er in voorkomt en lever dan de hele tekst
                    tekst= line
                    print(tekst)
                    wachtwoord_start= tekst.find(" ") +1
                    wachtwoord_eind=tekst.find("\n")
                    print(wachtwoord_start, wachtwoord_eind)
                    wachtwoord=tekst[wachtwoord_start:wachtwoord_eind] #zit nog witregel achter de laatste letter, had ik ook kunnen wissen met replace
                    print(wachtwoord)
    return wachtwoord


if __name__ == "__main__":
    clean_cache()
    cache_zip( r"C:\Users\marja\Documents\mijnDocumenten\Data Analytics\Winc\files\data.zip", r"C:\Users\marja\Documents\mijnDocumenten\Data Analytics\Winc\files\cache" )
    cached_files()
    find_password(cached_files())