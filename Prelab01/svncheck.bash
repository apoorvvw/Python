#! /bin/bash
#
# $Author: ee364e10 $
# $Date: 2015-01-25 17:45:49 -0500 (Sun, 25 Jan 2015) $ 
# $HeadUrl$ 
# $Revision: 73834 $
number_params=$#
input="file_list"
while read line
do
  echo "Reading $line"
  svnStatus=$(svn status $line)
  if [[ $svnStatus == ?* ]]
  then   
    if [[ -e $line ]]
    then
	if [[ -x $line ]]
	then
	  echo "Do you want to make the file executable? (y/n)"
	  read answer
	  if (( answer == "y" ))
	  then
	    chmod +x $line
	  fi
	fi
	svn add $line
    else
	echo "File does not exist"
    fi
  elif [[ $svnStatus != ?* ]]
  then
    if [[ ! -x $line ]]
    then
      svn propset svn:executable ON $line
    fi
  fi
done <"$input"
svn commit -m "auto commiting code"
