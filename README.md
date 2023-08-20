# http_healthcheck_python
This app sends an HTTP GET request at specified intervals

The check is performed in a cycle with a specified interval.

There are three possible test results:
1. `OK(200)`, in case the request returned HTTP status code `200`.
2. `ERR({HTTP_CODE})`, in case the request returned an HTTP status code other than `200`.
3. `URL parsing error`, in case the second argument is not a valid HTTP URL. Then the application ends.
 
The utility takes two arguments:
1. Integer value of the interval in seconds.
2. HTTP URL to be checked.

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

```bash
deactivate
```