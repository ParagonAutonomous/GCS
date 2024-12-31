"""Test listener for heartbeat messages."""
import time
from pymavlink import mavutil
from sim.config import GCS_IP, GCS_PORT, RECEIVE_INTERVAL

def listen_for_hearbeats(gcs_address: tuple) -> None:
    """Listen for heartbeat messages from a drone.
    
    Parameters:
    - sysid: System ID of the drone
    - compid: Component ID of the drone
    - gcs_address: Address of the GCS (IP, port)
    """
    gcs = mavutil.mavlink_connection(f"udp:{gcs_address[0]}:{gcs_address[1]}")

    while True:
        try:
            msg = gcs.recv_match(type="HEARTBEAT", blocking=True, timeout=5)

            if msg:
                print(f"[GCS] Received heartbeat from SYSID: {msg.get_srcSystem()} COMID: {msg.get_srcComponent()}")
                print(f" MAV_TYPE: {msg.type} MAV_AUTOPILOT: {msg.autopilot} MAV_STATE: {msg.system_status}")

            time.sleep(RECEIVE_INTERVAL)
        except Exception as e:
            print(f"[GCS] Error: {str(e)}")
            break

if __name__ == "__main__":
    GCS_ADDRESS = (GCS_IP, GCS_PORT)
    listen_for_hearbeats(GCS_ADDRESS)