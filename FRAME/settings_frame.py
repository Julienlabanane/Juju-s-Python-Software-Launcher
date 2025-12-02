import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import os
import xml.etree.ElementTree as ET
from pathlib import Path

#main function to show settings window
def show_settings_main():
    
    # create all the fonctions and variables
    settings_already_open = True
    where_is_lang_folder = Path("LOCAL/")
    lang_folder = [item.name for item in where_is_lang_folder.iterdir()]
    config_path = 'ETC/JPSLconfig.xml'
    if os.path.exists(config_path):
        tree = ET.parse(config_path)
        root = tree.getroot()
        cfg = root.find('cfg')
        current_lang = cfg.find('localization').text
    else:
        current_lang = 'en'
    if os.path.exists('LOCAL/' + current_lang):
        lang_tree = ET.parse('LOCAL/' + current_lang)
        lang_root = lang_tree.getroot()
        localization = lang_root.find('localization')
        lang_list_text = localization.find('lang_list_text').text
        confirmation_settings_message_text = localization.find('confirmation_settings_message').text
        settings_window_title_text = localization.find('settings_window_title').text
    def save_config():
        if os.path.exists(config_path):
            tree = ET.parse(config_path)
            root = tree.getroot()
            cfg = root.find('cfg')
            cfg.find('localization').text = lang_var.get()
            tree.write(config_path, encoding='utf-8', xml_declaration=True)
        else:
            root = ET.Element('data')
            cfg = ET.SubElement(root, 'cfg')
            ET.SubElement(cfg, 'localization').text = lang_var.get()
            tree = ET.ElementTree(root)
            tree.write(config_path, encoding='utf-8', xml_declaration=True)
        messagebox.showinfo("Settings", confirmation_settings_message_text)
        settings_window.destroy()
    
    # Create and configure settings window
    settings_window = tk.Toplevel()
    settings_window_size = "400x250"
    settings_window.geometry(settings_window_size)
    settings_window.title(settings_window_title_text)
    settings_window.config()

    # Define UI elements
    lang_label = ttk.Label(settings_window, text=lang_list_text)
    lang_var = ttk.Combobox(settings_window, values=lang_folder)
    save_btn = ttk.Button(settings_window, text="Save", command=save_config)
    
    # Set UI elements
    lang_var.set(current_lang)

    # Place UI elements
    lang_label.pack(pady=5)
    lang_var.pack(pady=5)
    save_btn.pack(pady=15)
