"""Multiple MAVLink drone clients."""
import threading
from drone_client.simulator import simulate_drone
from drone_client.config import GCS_IP, GCS_PORT, DEFAULT_DRONES

if __name__ == "__main__":
    GCS_ADDRESS = (GCS_IP, GCS_PORT)
    threads = []

    for drone in DEFAULT_DRONES:
        thread = threading.Thread(target=simulate_drone, args=(drone["sysid"], drone["compid"], GCS_ADDRESS))
        thread.daemon = True
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()