import subprocess


def block_ip(ip):
    output = subprocess.check_output("firewall-cmd --add-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"", shell=True)
    if(output == "success" or output == "Warning: ALREADY_ENABLED"):
        return True
    return False

def deblock_ip(ip):
    output = subprocess.check_output("firewall-cmd --remove-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"", shell=True)
    if(output == "success"):
        return True
    return False


def restart():
    output = subprocess.check_output("firewall-cmd --reload", shell=True)
    if (output == "success"):
        return True
    return False