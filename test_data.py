import requests
import json

# Fetch tickets
print("=== TICKETS ===")
resp = requests.get('https://hackutd2025.eog.systems/api/Tickets')
tickets = resp.json()
print(f"Type: {type(tickets)}")
if isinstance(tickets, list):
    print(f"Total tickets: {len(tickets)}")
    print("Sample ticket:")
    print(json.dumps(tickets[0], indent=2))
    print("\nAnother sample:")
    print(json.dumps(tickets[10], indent=2))
else:
    print("Tickets is a dict:")
    print(json.dumps(tickets, indent=2))

# Fetch cauldrons
print("\n=== CAULDRONS ===")
resp = requests.get('https://hackutd2025.eog.systems/api/Information/cauldrons')
cauldrons = resp.json()
print(f"Total cauldrons: {len(cauldrons)}")
print("Sample cauldron:")
print(json.dumps(cauldrons[0], indent=2))
print(f"\nCauldron keys: {list(cauldrons[0].keys())}")
print(f"Has fill_rate? {'fill_rate' in cauldrons[0]}")
print(f"Has generation_rate? {'generation_rate' in cauldrons[0]}")
