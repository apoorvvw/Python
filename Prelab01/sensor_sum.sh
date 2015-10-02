#! /bin/bash
#
# $Author$
# $Date$ 
# $HeadUrl$ 
# $Revision$
Num_param=$#
param_values=$@
if (( $# == 0 ))
then
    echo "usage: sesor_sum.sh <file_name>"
    exit 0
fi
if [[ ! -r $1 ]]
then
    echo "error $1 is not a readbale file"
    exit 0
fi
while read line
do
    sum=0
    v=($line)
    ((sum = v[1] + v[2] + v[3]))
    file=$(echo "$line" | head -c2)
    echo  -n "$file "
    echo "$sum"
done < "$1"
exit 0
