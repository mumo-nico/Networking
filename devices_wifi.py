import os

def get_connected_devices():
    # Execute the arp command and capture the output
    result = os.popen("arp -a").read()

    devices = []

    # Parse the output to extract IP and MAC addresses
    for line in result.split('\n'):
        if "dynamic" in line.lower():  # Look for lines with dynamic entries (active devices)
            parts = line.split()
            if len(parts) >= 3:
                devices.append({'ip': parts[0], 'mac': parts[1]})

    return devices

if __name__ == "__main__":
    connected_devices = get_connected_devices()

    if connected_devices:
        print("Devices connected to the same Wi-Fi network:")
        for device in connected_devices:
            print(f"IP: {device['ip']} - MAC: {device['mac']}")
    else:
        print("No devices found on the Wi-Fi network.")
