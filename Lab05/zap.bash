#! /bin/bash
#
# $Author$
# $Date$ 
# $HeadUrl$ 
# $Revision$
Num_param=$#
param_values=$@
if (( $# == 6 ))
then
    echo "usage: zap.bash <file_name>"
    exit 0
fi
#if [[ ! -r $1 ]]
#then
  #  echo "error $1 is not a readbale file"
   # exit 0
#fi
file="test"
new=$file".sorted" 
echo $new
