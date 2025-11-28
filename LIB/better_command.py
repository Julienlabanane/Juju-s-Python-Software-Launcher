import time
import LIB.system_sniffer as system_sniffer
from docx import Document
from docx.shared import RGBColor
log_file_name = "LOG/JPSL_log_" + time.strftime("%Y%m%d-%H%M%S") + ".docx"
log_file = Document()
log_file.add_heading("JPSL Log File", 0) 
log_file.add_paragraph("Log created on: " + time.asctime())
system_sniffer_result = (
    ('CPU', system_sniffer.get_cpu_name()),
    ('GPU', system_sniffer.get_gpu_name()),
    ('RAM', system_sniffer.get_ram()),
    ('OS', system_sniffer.get_os_info()),
)
table = log_file.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Component'
hdr_cells[1].text = 'Model'
for id, desc in system_sniffer_result:
    row_cells = table.add_row().cells
    row_cells[0].text = id
    row_cells[1].text = desc
def better_command(txt, context):
    yellow_warning = '\033[33m'
    error_warning = '\033[91m'
    succes = '\033[32m'
    base = '\033[0m'
    libname = "Juju's Python Better Command"
    libver = '1'
    if context == "hello":
        print(yellow_warning + "◼" + error_warning + "◼" + succes + "◼" + base + "  " + libname + " v" + libver)
    if context == "error":
        print(error_warning + "[" + time.asctime() + "] → " + txt)
        error_indoc = log_file.add_paragraph(time.asctime() + " → " + txt + "\n")
        error_indoc.runs[0].font.color.rgb = RGBColor(255, 0, 0)
    if context == "warning":
        print(yellow_warning + "[" + time.asctime() + "] → " + txt)
        warning_indoc = log_file.add_paragraph(time.asctime() + " → " + txt + "\n")
        warning_indoc.runs[0].font.color.rgb = RGBColor(255, 255, 0)
    if context == "success":
        print(succes + "[" + time.asctime() + "] → " + txt)
        success_indoc = log_file.add_paragraph(time.asctime() + " → " + txt + "\n")
        success_indoc.runs[0].font.color.rgb = RGBColor(0, 255, 0)
    if context == "info":
        print(base + "[" + time.asctime() + "] → " + txt)
        log_file.add_paragraph("[INFO] " + time.asctime() + " → " + txt + "\n")
    log_file.save(log_file_name)
better_command("", "hello")