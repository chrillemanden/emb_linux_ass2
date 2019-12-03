#!/bin/bash

#sudo service network-manager stop

sudo ip link set wlan0 down
sudo iw wlan0 set type ibss
sudo ip link set wlan0 up
sudo iw wlan0 ibss join pibot 2412
sudo ip addr add 192.168.99.16/24 dev wlan0


