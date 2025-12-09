import platform
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
import os

from LIB.tempfolder_scheduler import *
from LIB.minbetter_command import min_better_command as minbetter_command

xml_path = Path("TEMP/systemconf.xml")

if xml_path.exists():
    tree = ET.parse(xml_path)
    root = tree.getroot()

    def get_xml_value(tag_name):
        elem = root.find(tag_name)
        return elem.text if elem is not None else "Unknown"
    def get_cpu_name():
        return get_xml_value("cpu")
    def get_vga_name():
        return get_xml_value("vga")
    def get_ram():
        return get_xml_value("ram")
    def get_os_info():
        return get_xml_value("os")
    minbetter_command("CPU : " + get_xml_value("cpu"), "info")
    minbetter_command("VGA : " + get_xml_value("vga"), "info")
    minbetter_command("RAM : " + get_xml_value("ram"), "info")
    minbetter_command("OS : " + get_xml_value("os"), "info")

else:

    # ============================
    #             CPU
    # ============================

    def get_cpu_name():
        system = platform.system()

        if system == "Darwin":
            return subprocess.check_output(
                ["sysctl", "-n", "machdep.cpu.brand_string"]
            ).decode().strip()

        if system == "Linux":
            try:
                with open("/proc/cpuinfo") as f:
                    for line in f:
                        if "model name" in line:
                            return line.split(":")[1].strip()
            except:
                pass
            return "Unknown CPU"

        if system == "Windows":
            try:
                import winreg
                key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
                )
                name, _ = winreg.QueryValueEx(key, "ProcessorNameString")
                return name.strip()
            except:
                return "Unknown CPU"

        return "Unknown CPU"
    cpu = get_cpu_name()
    minbetter_command(f"CPU : {cpu}", "info")

    # ============================
    #             VGA
    # ============================

    def get_vga_name():
        system = platform.system()

        if system == "Darwin":
            output = subprocess.check_output(
                ["system_profiler", "SPDisplaysDataType"]
            ).decode()
            import re
            match = re.search(r"Chipset Model: (.+)", output)
            return match.group(1).strip() if match else "Unknown GPU"

        if system == "Linux":
            try:
                output = subprocess.check_output("lspci", shell=True).decode()
                for line in output.split("\n"):
                    if "VGA compatible controller" in line or "3D controller" in line:
                        parts = line.split(":")
                        return parts[-1].strip()
            except:
                pass
            return "Unknown GPU"

        if system == "Windows":
            try:
                output = subprocess.check_output(
                    [
                        "powershell",
                        "-Command",
                        "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"
                    ]
                ).decode().splitlines()
                gpus = [line.strip() for line in output if line.strip()]
                return gpus[0] if gpus else "Unknown GPU"
            except:
                return "Unknown GPU"

        return "Unknown GPU"
    vga = get_vga_name()
    minbetter_command(f"VGA : {vga}", "info")


    # ============================
    #             RAM
    # ============================

    def get_ram():
        system = platform.system()

        if system == "Darwin":
            bytes_ram = int(subprocess.check_output(
                ["sysctl", "-n", "hw.memsize"]
            ))
            return f"{bytes_ram / (1024**3):.2f} GB"

        if system == "Linux":
            try:
                with open("/proc/meminfo") as f:
                    for line in f:
                        if "MemTotal:" in line:
                            kb = int(line.split()[1])
                            return f"{kb / (1024**2):.2f} GB"
            except:
                pass
            return "Unknown RAM"

        if system == "Windows":
            try:
                output = subprocess.check_output(
                    [
                        "powershell",
                        "-Command",
                        "Get-CimInstance Win32_ComputerSystem | Select-Object -ExpandProperty TotalPhysicalMemory"
                    ]
                ).decode().strip()
                bytes_ram = int(output.replace(',', ''))
                return f"{bytes_ram / (1024**3):.2f} GB"
            except:
                return "Unknown RAM"

        return "Unknown RAM"
    ram = get_ram()
    minbetter_command(f"RAM : {ram}", "info")

    # ============================
    #        OS INFORMATION
    # ============================

    def get_os_info():
        system = platform.system()

        if system == "Darwin":
            return f"macOS {platform.mac_ver()[0]}"

        if system == "Linux":
            try:
                with open("/etc/os-release") as f:
                    info = {}
                    for line in f:
                        if "=" in line:
                            k, v = line.strip().split("=", 1)
                            info[k] = v.strip('"')
                distro = info.get("PRETTY_NAME", "Unknown Linux")
            except:
                distro = "Unknown Linux"

            version = platform.release()
            return f"{distro} ({version})"

        if system == "Windows":
            return f"Windows {platform.version()}"

        return "Unknown OS"
    os_full = get_os_info()
    minbetter_command(f"OS : {os_full}", "info")

    # ============================
    # XML SAVE
    # ============================

    # Create XML
    xml_content = f"""<?xml version="1.0"?>
<data>
    <cpu>{cpu}</cpu>
    <vga>{vga}</vga>
    <ram>{ram}</ram>
    <os>{os_full}</os>
</data>
"""

    TempFolder.put('systemconf.xml', xml_content)
