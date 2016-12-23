import os
import config_reader
import detectors
import datetime
import time
from collections import Counter


def main():
    initialize()
    run()


def initialize():
    return


def run():
    last_check_time = datetime.datetime.now().time()
    wait_time = float(config_reader.get_setting("General", "frequency"))
    while True:
        new_time = datetime.datetime.now().time()
        print collect_ips(last_check_time)
        time.sleep(wait_time)
        last_check_time = new_time


def collect_ips(check_time):
    collected = []
    if config_reader.get_bool_setting('Detection Methods','SSH'):
        ssh_ips = detectors.ips_ssh_login_fails(check_time)
        collected.append(ssh_ips)
    if config_reader.get_bool_setting('Detection Methods', 'dovecot'):
        dovecot_ips = detectors.ips_mail_login_fails(check_time)
        collected.append(dovecot_ips)
    return sum((Counter(dict(x)) for x in collected), Counter())


def block_ip(ip):
    os.system("firewall-cmd --permanent --add-rich-rule=\"rule family='ipv4' source address='" + ip + "' reject\"")

if __name__ == "__main__":
    main()

