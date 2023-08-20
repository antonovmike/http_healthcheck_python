import argparse
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


class HealthChecker:
    @staticmethod
    def check_url(url):
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
    parser.add_argument('url', help='URL to check')
    args = parser.parse_args()

    checker = HealthChecker()
    result = checker.check_url(args.url)
    print(result)


if __name__ == '__main__':
    main()
