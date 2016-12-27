# Derban

### Installation

Derban can be installed easly by cloning this repository and running the following commands

```bash
$ cd Derban
$ cd installation
$ sudo chmod +x install.sh
$ sudo ./install.sh
```
You can check if the service is running using the following command

```bash
$ systemctl status derban
```

###Configuration

You can configurate the service by changing /etc/derban/settings.ini

```
[General]
frequency : 1
max failed login : 5
block time : 86400

[Detection Methods]
SSH : true
dovecot : true
```

More information about these settings:
* **frequency** : the response time of the script in seconds, it is advised to check for failed logins every second
* **max failed login** : the amount of failed logins that are allowed for one ip adress
* **block time** : the time in seconds that an ip adress needs to be blocked, generaly 86400 seconds (one day)

