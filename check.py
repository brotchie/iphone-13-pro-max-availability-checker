#!/usr/bin/env python3
import pprint
import requests
import sys
import time


URL_TEMPLATE = "https://www.apple.com/shop/pickup-message-recommendations?cppart=UNLOCKED/US&location={postcode}&product=MLKR3LL/A"
RETRY_DELAY_SECONDS = 30


def main():
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} postcode\n")
        sys.exit(1)

    postcode = sys.argv[1] 
    url = URL_TEMPLATE.format(postcode=postcode)

    while True:
        response = requests.get(url)

        print("Checking for iPhone 13 Max availability...")
        found = False
        for store in response.json()["body"]["PickupMessage"]["stores"]:
            if store["partsAvailability"]:
                found = True
                pprint.pprint(store["partsAvailability"])

        if not found:
            print("No iPhone's found, waiting 30 seconds to retry.")

        time.sleep(RETRY_DELAY_SECONDS)


if __name__ == "__main__":
    main()
