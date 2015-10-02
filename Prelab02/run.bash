#! /bin/bash
#
# $Author: ee364e10 $
# $Date: 2015-01-26 23:55:57 -0500 (Mon, 26 Jan 2015) $ 
# $HeadUrl$ 
# $Revision: 74137 $
if (( $# != 2 ))
then
    echo "usage: run.bash"
   exit 0
fi
gcc $1 -o quick_sim
if (( $? ))
then
    echo "error: $1 could not be compiled!"
    exit 0
fi
name=$2
if [[ -e $2 ]]
then
    read -p "$2 exists. Would you like to delete it? (y/n)" ans
    if [[ ($ans == "y") || ($ans == "yes") ]]
    then 
        rm -f $2
    	name=$2
    else
        #Code for Non exixtant file
	read -p "Enter new file name: " name
    fi
fi
echo "" > $name
#touch $name
#At this point the name of the file is "name" and only the file has been created with nothing in it
sTime=$(quick_sim 1 1 i | cut -d":" -f10)
for P in a i
do
    for C in 1 2 4 8 16 32
    do
	for W in 1 2 4 8 16
	do
	 pName=$(quick_sim $C $W $P | cut -d":" -f2)
	 cSize=$(quick_sim $C $W $P | cut -d":" -f4)
    	 iWidth=$(quick_sim $C $W $P | cut -d":" -f6)
	 CPI=$(quick_sim $C $W $P | cut -d":" -f8)
	 eTime=$(quick_sim $C $W $P | cut -d":" -f10)
   	echo "$pName:$cSize:$iWidth:$CPI:$eTime" >> $name 
         if (( $sTime > $eTime ))
         then
		sName=$pName
		sSize=$cSize
		sWidth=$iWidth
		sCPI=$CPI
		sTime=$eTime
         fi
        done    
   done
done
echo "Fastest run time achieved by $sName with cache size $sSize and issue width $sWidth was $sTime"
exit 0
