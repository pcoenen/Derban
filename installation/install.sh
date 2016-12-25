#!/bin/bash

chmod +x *
cp -rf ../source /etc/derban
cp -f derban.sh /usr/bin/derban.sh
cp -f derban.service /lib/systemd/system/derban.service
ln -s -f /lib/systemd/system/derban.service /etc/systemd/system/derban.service


systemctl daemon-reload
systemctl enable derban.service
systemctl start derban.service
