
#!/bin/bash
#Portfolio 1

url=$1

identifier="id="

doc_id=${url##*$identifier}

echo "doc_id:"
echo $doc_id


#wget --no-check-certificate -q 'https://docs.google.com/uc?export=download&id=1FqECEPZ-HRPpLiErtXQqMqgJY5EPH3-O' -O inputfile

wget --no-check-certificate -q 'https://docs.google.com/uc?export=download&id='$doc_id -O inputfile


tr a-z A-Z < inputfile > inputfileCAPS


#The chars we are looking for in the frequency analysis
chars=ABCDEFGHIJKLMNOPQRSTUVWXYZ
num_chars=26

#Declaring an array to save the results
freqs=()

for i in $(seq 0 $(($num_chars-1)))
do
	
	cur_char=${chars:$i:1}

	value=$(grep -o $cur_char inputfileCAPS | wc -l)

	freqs[$i]=$value

	echo "$cur_char" $'\t' "$value"
done


