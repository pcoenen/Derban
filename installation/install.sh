#!/bin/bash

cp -r /source /etc/derban
cp derban.sh /usr/bin/derban.sh
cp derban.service /lib/systemd/system/derban.service
ln -s /lib/systemd/system/derban.service /etc/systemd/system/derban.service


systemctl enable derban.service
systemctl start derban.service
