@echo off
echo Installing Requirements...
TIMEOUT /T 3
pip install -r requirements.txt
echo Running Script...
python main.py
pause
