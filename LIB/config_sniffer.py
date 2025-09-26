import os
import xml.etree.ElementTree as ET
import logging
logging.basicConfig(level=logging.INFO)
if not os.path.exists('ETC/JPSLconfig.xml'):
    theme_choice = "light"
    language_code = "en"
    button_launch_text = "Launch"
    button_about_text = "About"
    button_market_text = "Market"
    button_close_text = "Close"
    logging.warning("Configuration file not found, default configuration loaded")
else:
    config_tree = ET.parse('ETC/JPSLconfig.xml')
    config_root = config_tree.getroot()
    language_code = config_root[0][0].text
    theme_choice = config_root[0][1].text
    if os.path.exists('LOCAL/local-' + language_code + '.xml'):
        lang_tree = ET.parse('LOCAL/local-' + language_code + '.xml')
        lang_root = lang_tree.getroot()
        localization = lang_root.find('localization')
        button_launch_text = localization.find('button_launch').text
        button_about_text = localization.find('button_about').text
        button_market_text = localization.find('button_market').text
        button_close_text = localization.find('button_close').text
    else:
        button_launch_text = "Launch"
        button_about_text = "About"
        button_market_text = "Market"
        button_close_text = "Close"