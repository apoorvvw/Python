#! /bin/bash
#
# $Author: ee364e10 $
# $Date: 2015-01-24 17:50:03 -0500 (Sat, 24 Jan 2015) $ 
# $HeadUrl$ 
# $Revision: 73762 $
num_parameters=$#
if [[ num_parameters == 0 ]]
then
  echo "Usage: check_file.bash $1"
  exit 0
fi
echo "Hello"
Paramas=$@
if [[ -e $1 ]]
then
  echo "$1 exists"
else
  echo "$1 does not exists"
fi
if [[ -d $1 ]]
then
  echo "$1 is a directory"
else
  echo "$1 is not a directory"
fi
if [[ -f $1 ]]
then
  echo "is an ordinary file"
else
  echo " is not an ordinary file"
fi
if [[ -f $1 ]]
then 
  echo "$1 is a readable"
else
  echo "$1 is not readable"
fi
if [[ -w $1 ]]
then
 echo "$1 is writable"
else
  echo "$1 is not a writable"
fi
if [[ -x $1 ]]
then
  echo "$1 is executable"
else
  echo "$1 is not executable"
fi
exit 0
