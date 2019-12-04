# emb_linux_ass2
Portfolio Assignment 2 in 5th semester elective course Linux for Embedded Objects

## Adhoc network
An adhoc network is set up on the pi zero by running the bash script /adhoc/adhoc.sh
The ssid of the network is pibot and the frequency 2412 MHz.

## TCP server
The pi zero listens to a TCP server with socat on port 8080 by running the script server.sh
inside the script we run 
```tcp-listen:8080,reuseaddr,fork exec:'bash tcp/tcp_commands.sh```
when a connection is made the ``tcp_commands.sh`` is run. This script determines which pyth
on scripts to run. With this we can get distance from the distance sensor and make the robot follow the wall. However it is not implemented yet that the robot can be stopped
