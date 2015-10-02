#! /bin/bash
#
# $Author: ee364e10 $
# $Date: 2015-01-21 11:17:42 -0500 (Wed, 21 Jan 2015) $ 
# $HeadUrl$ 
# $Revision: 73341 $
#
#Declarations
all_inputs=$@
array=($all_inputs)
number_of_inputs=$#
out_file=${array[0]}
#
# Code input validation
if (( number_of_inputs < 1 ))
then
echo 'Invalid input'
exit 0
fi
#
for ((i=1;i<$#;i++))
do
	while read -a Data
	do
	echo -n ${Data[1]} ' '
	done < expr2
echo ${Data[*]}
done
exit 0
