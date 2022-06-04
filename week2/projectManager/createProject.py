import os
import json
import  tempateEditor
import settings

project_file = ".project"

def make_folder(path):
    try:
        os.mkdir(path)
        return True
    except:
        return False

def create_project(data):
    template = json.load(open(tempateEditor.templateFile))
    path = settings.Settings().load()["path"]
    if os.path.exists(path):
        prj_name = valid_name(data["name"])
        prj_path = os.path.join(path, prj_name)
        if make_folder(prj_path):
            build_folders(prj_path, template)
        make_project_file(prj_path, data)

def build_folders(root, folders):
    for f in folders:
        full = os.path.join(root, f["name"])
        make_folder(full)
        build_folders(full, f["content"])

def make_project_file(path, data):
    filepath = os.path.join(path, project_file)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def valid_name(name):
    return name

def get_project_info(path):
    filepath = os.path.join(path, project_file)
    with open(filepath) as f:
        return json.load(f)
