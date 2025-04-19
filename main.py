import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        print("Enter the username like : main.py benzine12")
        return
    
    name = sys.argv[1]
    response = requests.get(f"https://api.github.com/users/{name}/events")
    if response.status_code == 404:
        print("Username not found, try another one")
        return
    json_data = response.json()
    print(json.dumps(json_data, indent=4))
    
if __name__ == "__main__":
    main()