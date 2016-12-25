#!/bin/bash

systemctl stop derban.service
chmod +x *
rm -rf /etc/derban
cp -r ../source /etc/derban
rm -rf /usr/bin/derban.sh
cp derban.sh /usr/bin/derban.sh
rm -rf /lib/systemd/system/derban.service
cp derban.service /lib/systemd/system/derban.service
rm -rf /etc/systemd/system/derban.service
ln -s /lib/systemd/system/derban.service /etc/systemd/system/derban.service


systemctl daemon-reload
systemctl enable derban.service
systemctl start derban.service
