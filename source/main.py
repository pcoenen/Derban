import firewallD
import config_reader
import detectors
import time
from collections import Counter
import datetime
import sys


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
        collect_ips(last_check_time)
        check_and_block()
        deblock_ips()
        time.sleep(wait_time)
        last_check_time = new_time


def deblock_ips():
    global blocked_ip_list
    block_time = datetime.timedelta(seconds= int(config_reader.get_setting("General", "block time")))
    for [ip, time_blocked] in blocked_ip_list:
        if time_blocked + block_time < datetime.datetime.now():
            return
        else :
            firewallD.deblock_ip(ip)
            blocked_ip_list.remove([ip, time_blocked])


def check_and_block():
    global ip_fail_counter
    print ip_fail_counter
    block_list = []
    max_failed = float(config_reader.get_setting("General", "max failed login"))
    for ip, amount in ip_fail_counter.iteritems():
        if amount > max_failed:
            block_list.append(ip)
    block_all_ips(block_list)


def block_all_ips(ip_list):
    global blocked_ip_list
    global ip_fail_counter
    for ip in ip_list:
        if firewallD.block_ip(ip) :
            blocked_ip_list.append([ip,datetime.datetime.now()])
            del ip_fail_counter[ip]
            print "Blocked " + ip
            sys.stdout.flush()
        else :
            print "Failed to block"


def collect_ips(check_time):
    global ip_fail_counter
    collected = []
    if config_reader.get_bool_setting('Detection Methods','SSH'):
        ssh_ips = detectors.ips_ssh_login_fails(check_time)
        collected.append(ssh_ips)
    if config_reader.get_bool_setting('Detection Methods', 'dovecot'):
        dovecot_ips = detectors.ips_mail_login_fails(check_time)
        collected.append(dovecot_ips)
    ip_fail_counter = sum((Counter(dict(x)) for x in collected), ip_fail_counter)

blocked_ip_list = []
ip_fail_counter = Counter()

if __name__ == "__main__":
    main()

