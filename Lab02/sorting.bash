#! /bin/bash
#
# $Author: ee364e10 $
# $Date: 2015-01-28 11:20:16 -0500 (Wed, 28 Jan 2015) $ 
# $HeadUrl$ 
# $Revision: 74374 $
Num_param=$#
param_values=$@
if (( $# == 0 ))
then
    echo "Usage: ./sorting.bash <input file>"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readbale file."
    exit 2
fi
    echo "Your choices are:" 
    echo "1) First 10 people"
    echo "2) Last 5 names by highest zipcode"
    echo "3) Address of the 6th-10thby reverse e-mail"
    echo "4) First 12 companies"
    echo "5) Pick a number of people"
    echo "6) Exit"
    read a
while (( a != 6 ))
do
    if (( $a == 1 ))
    then #1) First 10 people
    	tail -n +2 $1 | sort -t"," -k7,7 -k5,5 -k2,2 -k1,1 | head -n 2
    elif (( $a == 2 ))
    then #2) Last 5 names by highest zipcode
    	sort -t"," -nk8,8 $1 | tail -n 5 | cut -d"," -f1,2
    elif (( $a == 3 ))
    then #3) Address of the 6th-10thby reverse e-mail
    	sort -t"," -r -k11 $1 | tail -n +7 | head -n5 | cut -d"," -f4
    elif (( $a == 4 ))
    then #4) First 12 companies
    	sort -t"," -k3 $1 | head -n12 | cut -d"," -f3
    elif (( $a == 5 ))
    then #5) Pick a number of people
	echo "Enter number of people"
	read nmn
    	sort -t"," -k2,2 -k1,1 $1 | head -n $nmn
    fi	
    echo "Your choices are:" 
    echo "1) First 10 people"
    echo "2) Last 5 names by highest zipcode"
    echo "3) Address of the 6th-10thby reverse e-mail"
    echo "4) First 12 companies"
    echo "5) Pick a number of people"
    echo "6) Exit"
    read a
done
exit 0
# 1. FirstName, 2. LastName, 3. Company, 4. Address, 5. City,6.County,7.State,8.ZIP,9.Phone,10.Fax,11Email,12Web
