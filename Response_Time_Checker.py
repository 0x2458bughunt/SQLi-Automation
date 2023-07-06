import argparse
import requests
from colorama import Fore, Style

def measure_response_time(urls_file, min_response_time):
    try:
        with open(urls_file, 'r') as file:
            urls = [line.strip() for line in file.readlines()]

        for url in urls:
            try:
                response = requests.get(url)
                response_time = response.elapsed.total_seconds()

                if response_time >= min_response_time:
                    # Print URL and response time
                    print(f"URL: {url} | Response Time: ", end='')

                    # Print response time in green color
                    print(Fore.GREEN + f"{response_time:.2f} seconds" + Style.RESET_ALL)
            except requests.exceptions.RequestException as e:
                print(f"Error occurred while accessing the URL: {url} - {e}")
    except FileNotFoundError:
        print(f"URLs file '{urls_file}' not found.")

# Create command-line argument parser
parser = argparse.ArgumentParser(description='Measure response time of URLs')
parser.add_argument('-l', '--urls-file', help='File containing URLs')
parser.add_argument('-rt', '--min-response-time', type=float, default=0,
                    help='Minimum response time threshold in seconds (default: 0)')

# Parse the command-line arguments
args = parser.parse_args()

# Get the URLs file and minimum response time threshold from the arguments
urls_file = args.urls_file
min_response_time = args.min_response_time

if not urls_file:
    print('No URLs file provided.')
    exit()

measure_response_time(urls_file, min_response_time)
