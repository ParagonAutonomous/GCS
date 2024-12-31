"""MAVLink drone client simulator."""
import threading
import time
from pymavlink import mavutil
from drone_client.config import RECEIVE_INTERVAL

def simulate_drone(sysid: int, compid: int, gcs_address: tuple, heartbeat_interval: int = 1) -> None:
    """Simulate a MAVLink drone client.
    
    Parameters:
    - sysid: System ID of the drone
    - compid: Component ID of the drone
    - gcs_address: Address of the GCS (IP, port)
    - heartbeat_interval: Interval to send heartbeat message
    """
    drone = mavutil.mavlink_connection(
        f"udpout:{gcs_address[0]}:{gcs_address[1]}", 
        source_system=sysid, 
        source_component=compid
    )
    print(f"[DRONE {sysid}] Drone client active")

    heartbeat_thread = threading.Thread(target=send_heartbeat, args=(drone, sysid, heartbeat_interval))
    message_thread = threading.Thread(target=receive_message, args=(drone, sysid))

    heartbeat_thread.daemon = True
    message_thread.daemon = True

    heartbeat_thread.start()
    message_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        return

def send_heartbeat(drone, sysid: int, heartbeat_interval: int = 1) -> None:
    """Send heartbeat message to the GCS.
    
    Parameters:
    - drone: MAVLink drone connection
    - sysid: System ID of the drone
    - heartbeat_interval: Interval to send heartbeat message
    """
    while True:
        try:
            drone.mav.heartbeat_send(
                mavutil.mavlink.MAV_TYPE_QUADROTOR,
                mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA,
                0, 0, mavutil.mavlink.MAV_STATE_ACTIVE
            )
            # print(f"[DRONE {sysid}] Heartbeat sent")
            time.sleep(heartbeat_interval)
        except Exception as e:
            print(f"[DRONE {sysid}] Error: {str(e)}")
            break

def receive_message(drone, sysid: int) -> None:
    """Receive messages from the GCS.
    
    Parameters:
    - drone: MAVLink drone connection
    - sysid: System ID of the drone
    """
    while True:
        try:
            msg = drone.recv_match(type="COMMAND_LONG", blocking=False)
            if msg:
                print(f"[DRONE {sysid}] Command received: {msg}")
            time.sleep(RECEIVE_INTERVAL)
        except Exception as e:
            print(f"[DRONE {sysid}] Error: {str(e)}")
            break