#!/bin/bash
sudo ps -A|grep mysql
sudo pkill mysql
sudo ps -A|grep mysqld
sudo pkill mysqld
sudo service mysql restart
sudo mysql -hlocalhost -uroot -p
