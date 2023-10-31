import requests
import csv
from tqdm import tqdm  # Import tqdm

# Read URLs from 'input.txt'
with open('input.txt', 'r') as f:
    urls = [line.strip() for line in f]

# Get status codes
results = []
# Use tqdm as an iterator to track progress
for url in tqdm(urls, desc="Processing URLs", unit="URL"):
    try:
        response = requests.get(url)
        results.append((url, response.status_code))
    except requests.exceptions.RequestException as e:
        results.append((url, str(e)))

# Write results to 'output.csv'
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Status Code'])
    writer.writerows(results)
