import argparse
import time
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


class HealthChecker:
    @staticmethod
    def check_url(interval, url):
        try:
            with urlopen(url, timeout=interval) as connection:
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
        result = checker.check_url(args.interval, args.url)
        print(result)
        time.sleep(args.interval)


if __name__ == '__main__':
    main()
