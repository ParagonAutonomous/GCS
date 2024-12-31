"""Single MAVLink drone client."""
from sim.simulator import simulate_drone
from sim.config import GCS_IP, GCS_PORT

if __name__ == "__main__":
    GCS_ADDRESS = (GCS_IP, GCS_PORT)
    simulate_drone(sysid=1, compid=1, gcs_address=GCS_ADDRESS)