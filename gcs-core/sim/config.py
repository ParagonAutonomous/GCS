"""MAVLink drone client configuration.
GCS_IP: IP address of the GCS
GCS_PORT: Port of the GCS
HEARTBEAT_INTERVAL: Interval to send heartbeat message
RECEIVE_INTERVAL: Interval to receive messages
DEFAULT_DRONES: Default drone configurations for multiple drone clients
"""
GCS_IP = "127.0.0.1"
GCS_PORT = 14550
HEARTBEAT_INTERVAL = 1
RECEIVE_INTERVAL = 0.1
DEFAULT_DRONES = [
    {"sysid": 1, "compid": 1},
    {"sysid": 2, "compid": 1},
    {"sysid": 3, "compid": 1},
]