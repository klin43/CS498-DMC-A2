import requests
import time

US_CENTRAL = "http://34.70.153.26:8080"
EUROPE_WEST = "http://35.205.21.137:8080"

def measure_latency(region, url, end_point):
    times = []
    for i in range(10):
        start = time.time()
        
        if end_point == "/register":
            requests.post(url + end_point, json={"username": f"user{i}_{int(time.time())}"})
        else:
            requests.get(url + end_point)
        
        end = time.time()
        time_taken = 1000 * (end - start)
        times.append(time_taken)
    
    avg_latency = sum(times) / len(times)
    print(f"{end_point} avg latency on {region}: {avg_latency} ms")
        

def main():
    measure_latency("us-central1", US_CENTRAL, "/register")
    measure_latency("europe-west1", EUROPE_WEST, "/register")
    measure_latency("us-central1", US_CENTRAL, "/list")
    measure_latency("europe-west1", EUROPE_WEST, "/list")
    
if __name__ == "__main__":
    main()
