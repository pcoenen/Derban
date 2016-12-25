#!/bin/bash

chmod +x *
yes | cp -rf ../source /etc/derban
yes | cp -rf derban.sh /usr/bin/derban.sh
yes | cp -rf derban.service /lib/systemd/system/derban.service
rm -rf /etc/systemd/system/derban.service
ln -s /lib/systemd/system/derban.service /etc/systemd/system/derban.service


systemctl daemon-reload
systemctl enable derban.service
systemctl start derban.service
