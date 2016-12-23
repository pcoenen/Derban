import os


def ips_ssh_login_fails(since_time):
    result = {}
    stream = os.popen("journalctl -u sshd -a --no-pager --since='" + since_time + "'")
    line = stream.readline()
    while line != "":
        if "Failed password for" in line:
            ip = line.split("from ", 1)[1]
            ip = ip.split(" ", 1)[0]
            result[ip] = dict.get(ip, 0) + 1
        line = stream.readline()
    return result


def ips_mail_login_fails(since_time):
    result = {}
    stream = os.popen("journalctl -u dovecot -a --no-pager --since='" + since_time + "'")
    line = stream.readline()
    while line != "":
        if "Password mismatch" in line:
            ip = line.split(",")[1]
            result[ip] = dict.get(ip, 0) + 1
        line = stream.readline()
    return result