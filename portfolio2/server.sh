#!/bin/bash

#bash ./adhoc/adhoc.sh 
socat tcp-listen:8080,fork exec:'bash tcp/tcp_commands.sh' &
