#!/bin/bash

if ![ -d "$logs" ];
    mkdir logs
fi

if ![ -d "$notes" ];
    mkdir notes
fi

if ![ -d "$to-do-list" ];
    mkdir to-do-list
fi

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
clear

echo "Finished NoterPy setup"
