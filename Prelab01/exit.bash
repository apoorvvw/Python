number of arghuments = $#
for ind in {1..$#}
do
    if[[-e && -r $ind]]
    then
        printf "File %s is readable\n" $ind 
    else
        touch -f $ind
    fi
done
exit 0
