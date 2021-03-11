#!bin/bash

if [ -d "$logs" ];
then
    echo "logs file present"
else
    mkdir logs
fi

if [ -d "$notes" ];
then
    echo "notes file present"
else
    mkdir notes
fi

if [ -d "$to-do-list" ];
then
    echo "to-do-list file present"
else
    mkdir to-do-list
fi
