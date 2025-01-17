import requests
import time
import threading

def analyze_url():
    response = requests.post(
        "http://localhost:8000/api/analyze",
        json={"topic": "AI LLMs"}
    )
    task_data = response.json()
    print(f"Task created: {task_data}")

    # Check status with retry
    task_id = task_data['task_id']
    for _ in range(5):  # retry 5 times
        status = requests.get(f"http://localhost:8000/api/task/{task_id}")
        status_data = status.json()
        print(f"Task status: {status_data}")
        
        if status_data['status'] in ['COMPLETED', 'FAILED']:
            break
            
        time.sleep(2)  # wait 2 seconds between checks

def test_url_insight_bot():
    threads = []
    for _ in range(10):  # create 10 threads
        thread = threading.Thread(target=analyze_url)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # wait for all threads to complete

if __name__ == "__main__":
    test_url_insight_bot()