import os
import requests
from time import sleep

def ping_url(website_url, delay, max_trials):
    number_of_trials = 0
    while number_of_trials < max_trials:
        try:
            url_response = requests.get(website_url)
            if requests.status_code == 200:
                print(f"Website {website_url} is reachable")
                return True
        except ConnectionError:
            print(f"Website {website_url} is not reachable... retrying in {delay} seconds...")
            sleep(delay)
            number_of_trials += 1
        except requests.exceptions.MissingSchema:
            print(f"Invalid URL format: {website_url}. Make sure the URL has a valid schema (e.g., http:// or https://)")
            return False
        
    return False

if __name__ == "__main__":
    website_url = os.getenv("INPUT_URL")
    max_trials = int(os.getenv("INPUT_MAX_TRIALS"))
    delay = int(os.getenv("INPUT_DELAY"))

    website_reachable = ping_url(website_url, delay, max_trials)
    
    if not website_reachable:
        raise Exception(f"Website {website_url} is malformed or unreachable.")

    print(f"Website {website_url} is reachable.")