import streamlit as st
from pathlib import Path
import os
import shutil

st.set_page_config(page_title="CRUD File Manager", layout="centered")

st.title("📁 CRUD File Handling System")

# ---------------- FILE FUNCTIONS ---------------- #

def create_file(file_name, content):
    p = Path(file_name)

    if p.exists():
        return "FILE ALREADY EXISTS!"

    with open(file_name, 'w') as file:
        file.write(content)

    return "FILE CREATED SUCCESSFULLY!"


def read_file(file_name):
    p = Path(file_name)

    if p.exists() and p.is_file():
        with open(file_name, 'r') as file:
            return file.read()

    return "FILE NOT FOUND!"


def update_file(file_name, content, mode):
    p = Path(file_name)

    if p.exists():
        if mode == "Overwrite":
            with open(file_name, 'w') as file:
                file.write(content)

        elif mode == "Append":
            with open(file_name, 'a') as file:
                file.write(content)

        return "FILE UPDATED!"

    return "FILE NOT FOUND!"


def delete_file(file_name):
    p = Path(file_name)

    if p.exists():
        os.remove(file_name)
        return "FILE DELETED!"

    return "FILE NOT FOUND!"


def rename_file(old_name, new_name):
    p = Path(old_name)

    if p.exists():
        p.rename(new_name)
        return "FILE RENAMED!"

    return "FILE NOT FOUND!"


# ---------------- FOLDER FUNCTIONS ---------------- #

def create_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        return "FOLDER ALREADY EXISTS!"

    p.mkdir()
    return "FOLDER CREATED!"


def delete_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        shutil.rmtree(folder_name)
        return "FOLDER DELETED!"

    return "FOLDER NOT FOUND!"


# ---------------- UI ---------------- #

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

# CREATE FILE
if menu == "Create File":
    st.header("Create File")

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter content")

    if st.button("Create"):
        result = create_file(file_name, content)
        st.success(result)

# READ FILE
elif menu == "Read File":
    st.header("Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read"):
        result = read_file(file_name)

        if result == "FILE NOT FOUND!":
            st.error(result)
        else:
            st.text_area("File Content", result, height=300)

# UPDATE FILE
elif menu == "Update File":
    st.header("Update File")

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter new content")

    mode = st.radio("Select Update Mode", ["Overwrite", "Append"])

    if st.button("Update"):
        result = update_file(file_name, content, mode)
        st.success(result)

# DELETE FILE
elif menu == "Delete File":
    st.header("Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete"):
        result = delete_file(file_name)
        st.success(result)

# RENAME FILE
elif menu == "Rename File":
    st.header("Rename File")

    old_name = st.text_input("Enter old file name")
    new_name = st.text_input("Enter new file name")

    if st.button("Rename"):
        result = rename_file(old_name, new_name)
        st.success(result)

# CREATE FOLDER
elif menu == "Create Folder":
    st.header("Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):
        result = create_folder(folder_name)
        st.success(result)

# DELETE FOLDER
elif menu == "Delete Folder":
    st.header("Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):
        result = delete_folder(folder_name)
        st.success(result)