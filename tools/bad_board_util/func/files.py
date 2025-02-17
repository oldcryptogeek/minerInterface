import ipaddress
import os
import re
import xlsxwriter

import aiofiles

from tools.bad_board_util.func.ui import update_ui_with_data
from tools.bad_board_util.layout import window
from tools.bad_board_util.func.decorators import disable_buttons
from miners.miner_factory import MinerFactory


@disable_buttons
async def save_report(file_location):
    data = {}
    workbook = xlsxwriter.Workbook(file_location)
    sheet = workbook.add_worksheet()
    for line in window["ip_table"].Values:
        data[line[0]] = {
            "Model": line[1],
            "Total Chips": line[2],
            "Left Chips": line[3],
            "Center Chips": line[5],
            "Right Chips": line[7],
            "Nominal": 1,
        }

    async for miner in MinerFactory().get_miner_generator([key for key in data.keys()]):
        if miner:
            data[miner.ip]["Nominal"] = miner.nominal

    list_data = []
    for ip in data.keys():
        new_data = data[ip]
        new_data["IP"] = ip
        list_data.append(new_data)

    data = sorted(data, reverse=True, key=lambda x: x["Total Chips"])

    headers = [
        "IP",
        "Miner Model",
        "Total Chip Count",
        "Left Board Chips",
        "Center Board Chips",
        "Right Board Chips",
    ]
    print(data)
    row = 0
    col = 0
    for item in headers:
        sheet.write(row, col, item)
        col += 1

    row = 1
    for line in data:
        col = 0
        for point in line:
            sheet.write(row, col, point)
            col += 1
        row += 1

    workbook.close()


async def import_iplist(file_location):
    await update_ui_with_data("status", "Importing")
    if not os.path.exists(file_location):
        return
    else:
        ip_list = []
        async with aiofiles.open(file_location, mode="r") as file:
            async for line in file:
                ips = [
                    x.group()
                    for x in re.finditer(
                        "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",
                        line,
                    )
                ]
                for ip in ips:
                    if ip not in ip_list:
                        ip_list.append(ipaddress.ip_address(ip))
    ip_list.sort()
    window["ip_table"].update([[str(ip), "", "", "", ""] for ip in ip_list])
    await update_ui_with_data("ip_count", str(len(ip_list)))
    await update_ui_with_data("status", "")


async def export_iplist(file_location, ip_list_selected):
    await update_ui_with_data("status", "Exporting")
    if not os.path.exists(file_location):
        return
    else:
        if ip_list_selected is not None and not ip_list_selected == []:
            async with aiofiles.open(file_location, mode="w") as file:
                for item in ip_list_selected:
                    await file.write(str(item) + "\n")
        else:
            async with aiofiles.open(file_location, mode="w") as file:
                for item in window["ip_table"].Values:
                    await file.write(str(item[0]) + "\n")
    await update_ui_with_data("status", "")
