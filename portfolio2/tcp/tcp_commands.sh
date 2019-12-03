
#!/bin/bash

while getopts "s" option; do

	case "${option}" in
		s)
			#str_cmd=$OPTARG
			s=1
			;;
		*)
			;;
	esac
done


if [ -t 1 ]; then
     	read c
elif [ "x$s" != "x" ]; then
     	read c
else
    	c=$1
	if [ "$#" = 0 ]; then
		echo "Pass an argument." > /dev/stderr
		exit 1
	fi
fi

#read c
#c=$1

echo "hay"

if [ $c = getdist ]; then
	echo "distance: "
	tail -n1 distances
fi

exit 0
