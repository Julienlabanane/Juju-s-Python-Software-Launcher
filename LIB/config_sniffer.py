import os
import xml.etree.ElementTree as ET
from LIB.better_command import better_command
if not os.path.exists('ETC/JPSLconfig.xml'):
    language_code = "en"
    button_launch_text = "Launch"
    button_about_text = "About"
    button_market_text = "Market"
    button_close_text = "Close"
    settings_button_text = "Settings"
    confirmation_settings_message_text = "Configuration saved!"
    better_command("No config file found, defaulting to English localization.", "warning")
else:
    config_tree = ET.parse('ETC/JPSLconfig.xml')
    config_root = config_tree.getroot()
    language_code = config_root[0][0].text
    if os.path.exists('LOCAL/' + language_code):
        lang_tree = ET.parse('LOCAL/' + language_code)
        lang_root = lang_tree.getroot()
        langpack_info = lang_root.find('infodata')
        author = langpack_info.find('author').text
        contact = langpack_info.find('contact').text
        version = langpack_info.find('version').text
        day = langpack_info.find('day').text
        month = langpack_info.find('month').text
        year = langpack_info.find('year').text
        additionalnotes = langpack_info.find('additionalnotes').text
        localization = lang_root.find('localization')
        button_launch_text = localization.find('button_launch').text
        button_about_text = localization.find('button_about').text
        button_market_text = localization.find('button_market').text
        button_close_text = localization.find('button_close').text
        settings_button_text = localization.find('button_settings').text
        confirmation_settings_message_text = localization.find('confirmation_settings_message').text
        settings_window_title_text = localization.find('settings_window_title').text
        market_placeholder_text = localization.find('market_placeholder_text').text
        market_window_title_text = localization.find('market_window_title').text
        better_command(f"Localization loaded: {language_code}", "success")
    else:
        button_launch_text = "Launch"
        button_about_text = "About"
        button_market_text = "Market"
        button_close_text = "Close"
        settings_button_text = "Settings"
        confirmation_settings_message_text = "Configuration saved!"
        settings_window_title_text = "Settings"
        market_placeholder_text = "Market Placeholder"
        market_window_title_text = "Market"
        better_command(f"Localization file for '{language_code}' not found, defaulting to English.", "error")
better_command(f"Configuration loaded. Language: {language_code}", "info")