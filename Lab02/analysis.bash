#! /bin/bash
#
# $Author: ee364e10 $
# $Date: 2015-01-28 11:17:53 -0500 (Wed, 28 Jan 2015) $ 
# $HeadUrl$ 
# $Revision: 74365 $
num_params=$#
param_values=$@
input=$1
if (( $# != 1 ))
then
    echo "Usage: analysis.bash <input file>"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readbale file."
    exit 2
fi
while read -a line
do
    #echo ${line[2]}
    ((length=${#line[*]}-1))
    sum=0
    for (( I=2; I < length; I++ ))
    do
        (( sum=$sum+${line[I]} ))
    done       
    ((avg=$sum/($length-2)))
    #if (( ${line[1]} = 2800 ))
    for (( I=2; I < length; I++ ))
    do
	(( av=(90*avg)/100 ))
	#echo -n $avg
	#echo "   $av"
        if (( ${line[I]} < av ))
        then
	    (( a = $I - 1 ))
            echo "Run $a for the ${line[0]} ${line[1]} with the score ${line[$I]} was 90% less than averge $av"
        fi
    done  
    #echo ${sum[*]}
    echo "${line[0]} ${line[1]} scored an average of $avg"
done < "$1"

