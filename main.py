import file_handling
from os import path
from shutil import copyfile
from jinja2 import Environment, FileSystemLoader

# TODO
# create github page
# add variables file for settings


template_dir = 'templates' # should be set in a variable config file
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('template.html') # change this to be local later
# these should come f a vars file for settings
root_dir = path.normpath("./pages")
result_root_dir = path.normpath("./result")

def format_content(content):
    blacklist = ["</li>", "<ul>", "</ul>", "</h"]
    return_content = []
    append_br = True
    if not isinstance(content, list):
        return content
    
    for line in content:

        append_br = True
        for black in blacklist:
            if black in line:
                append_br = False
        if append_br:
            return_content.append(line.replace("\n", "<br>\n"))
        else:
            return_content.append(line)
    return return_content


# generate an html file if filename ends in .txt, copies file otherwise
def generate_file(filename, data):
    
    file_extension = path.splitext(filename)[1]
    if file_extension != ".txt":
        file_source = path.join(root_dir, filename)
        file_destination = path.join(result_root_dir, filename)
        print(file_destination, " ", file_source) 
        copyfile(file_source, file_destination)
        return
    
    filename = filename.replace(".txt", ".html")
    result_path = path.join(result_root_dir, filename)

    data = {
        "page_title": data["title"],
        "content": format_content(data["content"])
    }

    rendered_html = template.render(data)
    with open(result_path, "w") as html_file:
        html_file.write(rendered_html)

def get_page_title(page_content):
    if len(page_content) > 0 and page_content[0].startswith("$title"):
        html_title = page_content[0].split(" ")[-1].replace("\n", "")
        page_content.pop(0)
    else:
        html_title = "Untitled_Page"

    return html_title


# will generate the whole website
def generate_website():
    # wipe all current files in the "result" folder
    # (deletes the folder and recreates it)
    file_handling.reset_result_folder(result_root_dir)

    # get list of all folders and files
    website_tree = file_handling.get_files_and_dirs(root_dir)
    folders = website_tree["folders"]
    files = website_tree["files"]

    # creates all folders in the "result" folder
    file_handling.create_directories(folders, result_root_dir)

    # loads all content files and generates website tree
    for file in files:
        data = file_handling.load_content_files_data(file, root_dir)
        generate_file(file, data)


def main():
    generate_website()
    
if __name__ == "__main__":
    main()