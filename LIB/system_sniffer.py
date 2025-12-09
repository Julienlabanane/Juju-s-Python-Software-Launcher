import platform
import re
from xml.etree import ElementTree
from LIB import minbetter_command
from LIB.minbetter_command import min_better_command as minbetter_command
import subprocess
import re
from xml.etree import ElementTree
from pathlib import Path
def _log(msg: str, level: str = "info"):
    try:
        print(f"[{level.upper()}] {msg}")
    except Exception:
        pass
try:
    from LIB import tempfolder_scheduler
except Exception:
    tempfolder_scheduler = None
    minbetter_command("Cannot import tempfolder scheduler", "error")

# -----------------------------
# CPU
# -----------------------------
def get_cpu_name():
    system = platform.system()

    # macOS
    if system == "Darwin":
        return subprocess.check_output(
            ["sysctl", "-n", "machdep.cpu.brand_string"]
        ).decode().strip()

    # Linux
    if system == "Linux":
        try:
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":")[1].strip()
        except Exception:
            pass
        minbetter_command("Unknown CPU", "error")
        return "Unknown CPU"

    # Windows
    if system == "Windows":
        try:
            import winreg  # type: ignore
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
            )
            name, _ = winreg.QueryValueEx(key, "ProcessorNameString")
            return name
        except Exception:
            minbetter_command("Unknown CPU", "error")
            return "Unknown CPU"

    minbetter_command("Unknown CPU", "error")
    return "Unknown CPU"
minbetter_command("CPU : " + get_cpu_name(), "info")

# -----------------------------
# GPU
# -----------------------------
def get_gpu_name():
    system = platform.system()

    # macOS
    if system == "Darwin":
        output = subprocess.check_output(
            ["system_profiler", "SPDisplaysDataType"]
        ).decode()
        match = re.search(r"Chipset Model: (.+)", output)
        return match.group(1).strip() if match else "Unknown GPU"

    # Linux
    if system == "Linux":
        try:
            output = subprocess.check_output("lspci", shell=True).decode()
            for line in output.split("\n"):
                if "VGA compatible controller" in line or "3D controller" in line:
                    parts = line.split(":")
                    if len(parts) >= 3:
                        return parts[2].strip()
                    return parts[-1].strip()
        except Exception:
            pass
        return "Unknown GPU"

    # Windows
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
        except Exception:
            return "Unknown GPU"
    return "Unknown GPU"
minbetter_command("VGA : " + get_gpu_name(), "info")

# -----------------------------
# RAM
# -----------------------------
def get_ram():
    system = platform.system()

    # macOS
    if system == "Darwin":
        bytes_ram = int(subprocess.check_output(
            ["sysctl", "-n", "hw.memsize"]
        ))
        return f"{bytes_ram / (1024**3):.2f} GB"

    # Linux
    if system == "Linux":
        try:
            with open("/proc/meminfo") as f:
                for line in f:
                    if "MemTotal:" in line:
                        kb = int(line.split()[1])
                        return f"{kb / (1024**2):.2f} GB"
        except Exception:
            pass
        return "Unknown RAM"

    # Windows
    if system == "Windows":
        try:
            output = subprocess.check_output(
                    [
                        "powershell",
                        "-Command",
                        "Get-CimInstance Win32_ComputerSystem | Select-Object -ExpandProperty TotalPhysicalMemory"
                    ]
                ).decode().strip()
            first_line = output.splitlines()[0] if output.splitlines() else output
            bytes_ram = int(first_line.replace(',', '').strip())
            return f"{bytes_ram / (1024**3):.2f} GB"
        except Exception:
            return "Unknown RAM"
    minbetter_command("Unknown RAM", "error")
    return "Unknown RAM"
minbetter_command("RAM : " + get_ram(), "info")

# -----------------------------
# OS VERSION + DISTRIBUTION
# -----------------------------
def get_os_info():
    system = platform.system()

    # macOS
    if system == "Darwin":
        version = platform.mac_ver()[0]
        return ("macOS", version)

    # Linux
    if system == "Linux":
        try:
            with open("/etc/os-release") as f:
                info = {}
                for line in f:
                    if "=" in line:
                        k, v = line.strip().split("=", 1)
                        info[k] = v.strip('"')
            distro = info.get("PRETTY_NAME", "Unknown Linux")
        except Exception:
            distro = "Unknown Linux"

        version = platform.release()
        return (distro, version)

    # Windows
    if system == "Windows":
        version = platform.version()
        return ("Windows", version)

    minbetter_command("Unknown OS", "error")
    return ("Unknown OS", "Unknown Version")
minbetter_command("OS : " + str(get_os_info()), "info")
# If executed directly, print summary (safe)
if __name__ == "__main__":
    os_name, os_version = get_os_info()
    print(f"OS: {os_name} {os_version}")