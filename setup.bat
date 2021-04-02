@echo off

IF NOT EXIST logs\ (mkdir logs)
IF NOT EXIST notes\ (mkdir notes)
IF NOT EXIST to-do-list\ (mkdir to-do-list) 
python -m venv venv
venv\Scripts\activate.bat & pip install -r requirements.txt
