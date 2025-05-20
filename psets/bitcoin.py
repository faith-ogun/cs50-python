import sys
import json
import requests

# Error handling - handle these before the correct case scenario
### No argument handling
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

### Too many arguments handling
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
### Argument IS number handling
    bitcoins = float(sys.argv[1])

except (ValueError):
    sys.exit("Command-line argument is not a number")

except (requests.RequestException):
    sys.exit("Invalid request.")

# CoinCap Request
response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=myKey")
# dont forget https://

o = response.json()

result = float(o["data"]["priceUsd"])

calc = result * bitcoins

print(f"${calc:,.4f}")
