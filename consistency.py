import requests
import uuid

US_CENTRAL = "http://34.70.153.26:8080"
EUROPE_WEST = "http://35.205.21.137:8080"

def measure_consistency():
    count = 0
    for i in range(100):
        username = str(uuid.uuid4())
        
        requests.post(US_CENTRAL + "/register", json={"username": username})
        username_list = requests.get(EUROPE_WEST + "/list").json()
   
        if username not in str(username_list):
            count += 1
    
    print(f"Number of usernames not found in list immediately: {count} times")
        
    
def main():
    measure_consistency()
    
if __name__ == "__main__":
    main()

