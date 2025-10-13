from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import os
import xml.etree.ElementTree as ET
def show_settings_main():
    settings_already_open = True
    config_path = 'ETC/JPSLconfig.xml'
    if os.path.exists(config_path):
        tree = ET.parse(config_path)
        root = tree.getroot()
        cfg = root.find('cfg')
        current_lang = cfg.find('localization').text
        current_theme = cfg.find('theme_choice').text
    else:
        current_lang = 'en'
        current_theme = 'light'
    if os.path.exists('LOCAL/' + current_lang + '.xml'):
        lang_tree = ET.parse('LOCAL/' + current_lang + '.xml')
        lang_root = lang_tree.getroot()
        localization = lang_root.find('localization')
        lang_list_text = localization.find('lang_list_text').text
        theme_label_text = localization.find('theme_label_text').text
        confirmation_settings_message_text = localization.find('confirmation_settings_message').text
        settings_window_title_text = localization.find('settings_window_title').text
    settings_window = Tk()
    settings_window_size = "400x250"
    settings_window.geometry(settings_window_size)
    settings_window.title(settings_window_title_text)
    settings_window.tk.call("source", "ASSET/AZURE/azure.tcl")
    settings_window.tk.call("set_theme", current_theme)
    ttk.Label(settings_window, text=lang_list_text).pack(pady=5)
    lang_var = ttk.Combobox(settings_window, values=["English", "Français", "Español", "Deutsch", "Italiano", "Русский", "Dansk", "العربية"])
    lang_var.set(current_lang)
    lang_var.pack(pady=5)
    ttk.Label(settings_window, text=theme_label_text).pack(pady=5)
    theme_var = ttk.Combobox(settings_window, values=["light", "dark"])
    theme_var.set(current_theme)
    theme_var.pack(pady=5)
    def save_config():
        if os.path.exists(config_path):
            tree = ET.parse(config_path)
            root = tree.getroot()
            cfg = root.find('cfg')
            cfg.find('localization').text = lang_var.get()
            cfg.find('theme_choice').text = theme_var.get()
            tree.write(config_path, encoding='utf-8', xml_declaration=True)
        else:
            root = ET.Element('data')
            cfg = ET.SubElement(root, 'cfg')
            ET.SubElement(cfg, 'localization').text = lang_var.get()
            ET.SubElement(cfg, 'theme_choice').text = theme_var.get()
            tree = ET.ElementTree(root)
            tree.write(config_path, encoding='utf-8', xml_declaration=True)
        messagebox.showinfo("Settings", confirmation_settings_message_text)
        settings_window.destroy()
    save_btn = ttk.Button(settings_window, text="Save", command=save_config)
    save_btn.pack(pady=15)
    settings_window.mainloop()