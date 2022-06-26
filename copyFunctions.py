import os
import shutil
from distutils.dir_util import copy_tree
from shutil import copyfile, copy
from datetime import date

def copyFilesToDir(source_files, dest):
    result = {"error": False, "message": "Deploy executed successfully."}
    try:
        if len(source_files) < 1 or dest is None or dest == "":
            result = {"error": True, "message": "Deploy not executed. Source files or desination are not present. "}
            return result
        # create dest foldes if not exists
        if not os.path.exists(dest):
            os.makedirs(dest)
        # copy files
        for file in source_files:
            if '.' not in file:
                copy_tree(file, dest)
            else:
                copy(file, dest)

    # If source and destination are same
    except shutil.SameFileError:
        result = {"error": True, "message": "Source and destination represents the same file."}
        print("Source and destination represents the same file.")

    # If file exists.
    except FileExistsError:
        result = {"error": True, "message": "One or more file already exists in destination directory."}
        print("One or more file already exists in destination directory.")

    # If there is any permission issue
    except PermissionError:
        result = {"error": True, "message": "Permission denied."}
        print("Permission denied.")

    # For other errors
    except Exception as ex:
        result = {"error": True, "message": str(ex)}
        print("Error occurred while copying files: " + str(ex))

    return result

def backupFolder(source_folder, backup_path):
    result = {"error": False, "message": "Backup executed successfully."}
    d = date.today()
    year = str(date.today().year)
    month = str(f"{d:%m}")
    day = str(date.today().day)
    zip_suffix_date = year + month + day
    try:
        zip_name = backup_path + '/backup_' + zip_suffix_date
        directory_name = source_folder

        # Create 'path\to\zip_file.zip'
        shutil.make_archive(zip_name, 'zip', directory_name)

    # If source and destination are same
    except shutil.SameFileError:
        result = {"error": True, "message": "Source and destination represents the same file."}
        print("Source and destination represents the same file.")

    # If file exists.
    except FileExistsError:
        result = {"error": True, "message": "One or more file already exists in destination directory."}
        print("One or more file already exists in destination directory.")

    # If there is any permission issue
    except PermissionError:
        result = {"error": True, "message": "Permission denied."}
        print("Permission denied.")

    # For other errors
    except Exception as ex:
        result = {"error": True, "message": str(ex)}
        print("Error occurred while copying files: " + str(ex))

    return result