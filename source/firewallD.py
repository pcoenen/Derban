import subprocess
import os
import re
import sys


def block_ip(ip):
    output = subprocess.check_output("firewall-cmd --add-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"", shell=True).strip()
    if("success" == output or "Warning: ALREADY_ENABLED" == output):
        return True
    return False

def deblock_ip(ip):
    output = subprocess.check_output("firewall-cmd --remove-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"", shell=True).strip()
    if("success" == output):
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
    print "Al permanent blocked ip's will be removed"
    print "Be patient this can take really long (in some cases some hours)"
    sys.stdout.flush()
    count = 0
    stream = os.popen("firewall-cmd --list-all")
    line = stream.readline().strip()
    while line != "":
        p = re.compile("rule family=\"ipv4\" source address=\"(.*)\" reject")
        result = p.search(line)
        if result :
            ip = result.group(1)
            if permanent_deblock_ip(ip):
                count += 1
            if count % 100 == 0:
                print "Already " + str(count) + "ip's deblocked"
        line = stream.readline().strip()
    print "Deblocked " + str(count) + " ip's"
    restart()