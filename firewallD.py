import subprocess
import os
import re


def block_ip(ip):
    output = subprocess.check_output("firewall-cmd --add-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"", shell=True)
    if("success" in output or "Warning: ALREADY_ENABLED" in output):
        return True
    return False

def deblock_ip(ip):
    output = subprocess.check_output("firewall-cmd --remove-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"", shell=True)
    if(output == "success"):
        return True
    return False

def permanent_deblock_ip(ip):
    output = subprocess.check_output(
        "firewall-cmd --permanent --remove-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"", shell=True)
    if ("success" in output):
        return True
    print "failed"
    print output
    return False


def restart():
    output = subprocess.check_output("firewall-cmd --reload", shell=True)
    if (output == "success"):
        return True
    return False

def remove_all_permanent():
    count = 0
    stream = os.popen("firewall-cmd --list-all")
    line = stream.readline()
    while line != "":
        matchObj = re.match(r'rule family=\"ipv4\" source address=\"(.*)\" reject', line, re.M | re.I)
        if matchObj:
            ip = matchObj.group(1)
            if permanent_deblock_ip(ip):
                count += 1
        line = stream.readline()
    print "Deblocked " + count + "ip's"