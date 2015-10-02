#! /bin/bash
#
# $Author: ee364e10 $
# $Date: 2015-02-18 11:22:20 -0500 (Wed, 18 Feb 2015) $ 
# $HeadUrl$ 
# $Revision: 76030 $
Num_param=$#
param_values=$@
if (( $# == 0 ))
then
    echo "Usage: sort.bash  -f <file_name> --column_number=<value>"
    exit 1
fi
if (( $# < 3 ))
then
    echo "Error: Insufficient Information"
    exit 1
fi
val=1
while getopts f:-: thisopt
do
        case $thisopt in
          f)file=$OPTARG
          	if [[ ! -r $file ]]
		then
    			echo "Error: $file is not a readable file"
    			exit 1
		fi
		if [[ ! -r $file ]]
		then
    			echo "Error: $file File does not exist."
    			exit 1
		fi;;
          -)val=$(echo $OPTARG  | cut -d'=' -f2)
          	if (( val < 1))
          	then
          		val=1
          	fi ;;
          *)echo "Unknown Option."
          	exit 1;;
        esac
done
len=0
while read line
do
    data[i]=$line
    v=($line)
    len=${#v[*]} 	
done < "$file"
if (( len < val ))
then 
	echo "Error: Column number $val does not exist."
	exit 1
fi	
fileNew=$file".sorted"
sort -r -k$val,$val $file > $fileNew
echo "File Sorted."
exit 0
