import os
import time
import sys
import smtplib

def main():
    intialize()

def intialize():


def blockip(ip):
    os.system("firewall-cmd --permanent --add-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"")

settings = {}
if __name__ == "__main__":
    main()

