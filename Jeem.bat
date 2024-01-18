@echo off
echo Installing Requirements...
TIMEOUT /T 3
pip install -r requirements.txt
echo Running Jeem...
python main.py
pause
