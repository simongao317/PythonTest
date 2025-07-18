# Windows版本程序

import tkinter as tk
from tkinter import filedialog
import pyperclip

def get_file_path():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

if __name__ == "__main__":
    file_path = get_file_path()
    if file_path:
        pyperclip.copy(file_path)
        print(f"文件路径已复制到剪贴板：{file_path}")
    else:
        print("未选择文件。")
# Windows版本程序
'''
# Mac版本程序
import subprocess

def get_file_path():
    cmd = """
    osascript -e 'tell application "Finder"
        activate
        set myFile to choose file
        POSIX path of (myFile as alias)
    end tell'
    """
    path = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
    return path

print(get_file_path())
# Mac版本程序
'''