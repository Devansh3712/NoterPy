#!bin/bash

if ! [ -d "$logs" ];
then
mkdir logs
fi

if ! [ -d "$notes" ];
then
mkdir notes
fi

if ! [ -d "$to-do-list" ];
then
mkdir to-do-list
fi