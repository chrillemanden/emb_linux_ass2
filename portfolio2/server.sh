#!/bin/bash

#bash ./adhoc/adhoc.sh

sudo pigpiod
 
socat tcp-listen:8080,reuseaddr,fork exec:'bash tcp/tcp_commands.sh -s && echo done' &

rm ./distances
touch ./distances

bash /home/pi/git/emb_linux_ass2/portfolio2/getdist.sh &
