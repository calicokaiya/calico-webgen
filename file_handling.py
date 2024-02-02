from shutil import rmtree
from os import walk, path, makedirs

def get_files_and_dirs(root_path):
    file_list = {
        "folders": [],
        "files": [],
    }
    for root, dirs, files in walk(root_path):
        relative_root = path.relpath(root, root_path)

        # get the relative root of all files
        for file in files:
            try:
                # makes current path not show up as "."
                if relative_root != ".":
                    file_path = path.normpath(path.join(relative_root, file))
                else:
                    file_path = file
                file_list["files"].append(file_path)
            except Exception as e:
                print(f"Error while getting file directory {file_path}, {e}")

        # get the relative root of all directories
        for directory in dirs:
            try:
                if relative_root != ".":
                    dir_path = path.normpath(path.join(relative_root, directory))
                else:
                    dir_path = directory
                file_list["folders"].append(dir_path)
            except Exception as e:
                print(f"Error while getting folder {dir_path} {e}")

    return file_list

# gets a list of folders and creates them in the "resources" folder
def create_directories(folders, result_root_dir):
    for folder in folders:
        path_to_check = path.join(result_root_dir, folder)
        path_to_check = path.normpath(path_to_check)
        try:
            if not path.exists(path_to_check):
                makedirs(path_to_check, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory {path_to_check} {e}")
    

# deletes the "result" folder and creates it again to reset program
def reset_result_folder(result_root_dir):
    try:
        if path.exists(result_root_dir):
            rmtree(result_root_dir)
            makedirs(result_root_dir, exist_ok=True)
    except Exception as e:
        print(f"Error removing or creating {result_root_dir}, {e}")

def get_page_title(content):
    if len(content) < 0:
        return "calicocali.co" # must be set via settings
    if content[0].strip().startswith("$title"):
        title = content[0].split("=")
        title = title[-1].strip()
        content.pop(0) # remove first line (title line) from file
    else:
        title = "calicocali's corner" # must add default page title in settings
    return title

# returns the data of a list of files
def load_content_files_data(file, root_dir):
    file_path = path.normpath(root_dir + "/" + file)
    with open(file_path, "r") as content_file:
        content = content_file.readlines()
    # determine if we have a custom title
    title = get_page_title(content)

    #should return the page title and the content of the file
    data = {
        "title": title,
        "content": content
    }
    return data

if __name__ == "__main__":
    files = get_files_and_dirs("./pages")
    print(files)
    print("directories: ", files["files"])
    print("files: ", files["folders"])