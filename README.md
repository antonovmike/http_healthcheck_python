# http_healthchecker

Install and activate Python virtual environment:
```bash
apt install python3.10-venv
```
```bash
source venv/bin/activate
```
Upgrade package installer for Python and install packages:
```bash
python3 -m pip install --upgrade pip
```

Start with args
```bash
python main.py 1 http://httpstat.us/
```
```bash
python main.py 2 http://httpstat.us/500
```
```bash
python main.py 3 not_an_address
```