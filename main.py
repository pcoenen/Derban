import os
import config_reader
import detectors
import time
from collections import Counter


def main():
    initialize()
    run()


def initialize():
    return


def run():
    # When the algo starts check every ip from that day
    last_check_time = time.strftime("%Y-%m-%d") + " 00:00:00"
    wait_time = float(config_reader.get_setting("General", "frequency"))
    while True:
        new_time = time.strftime("%Y-%m-%d %H:%M:%S")
        check_and_block(collect_ips(last_check_time))
        time.sleep(wait_time)
        last_check_time = new_time


def check_and_block(ip_list):
    block_list = []
    max_failed = float(config_reader.get_setting("General", "max failed login"))
    for ip, amount in ip_list.iteritems():
        if amount > max_failed:
            block_list.append(ip)
    block_all_ips(block_list)


def block_all_ips(ip_list):
    for ip in ip_list:
        block_ip(ip)
        print "Blocked" + ip


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

