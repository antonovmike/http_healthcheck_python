import argparse
import time
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse


class HealthChecker:
    @staticmethod
    def check_url(url):
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("URL parsing error")

        try:
            with urlopen(url, timeout=3) as connection:
                code = connection.getcode()
                return f"Checking '{url}'. Result: OK({code})"
        except HTTPError as e:
            return f"Checking '{url}'. Result: ERR({e.code})"
        except URLError as e:
            return f"Checking '{url}'. Result: ERR({e.reason})"
        except Exception as e:
            return f"Checking '{url}'. Result: ERR({str(e)})"



def main():
    parser = argparse.ArgumentParser(description='HTTP Health Checker')
    parser.add_argument('interval', type=int, help='Interval between checks in seconds')
    parser.add_argument('url', help='URL to check')
    args = parser.parse_args()

    checker = HealthChecker()

    while True:
        try:
            result = checker.check_url(args.url)
            print(result)
            time.sleep(args.interval)
        except ValueError as e:
            print(str(e))
            break

if __name__ == '__main__':
    main()

