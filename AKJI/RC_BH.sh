#!/bin/bash
# Local Network ADB Remote Control + Bug Hunting Features

AVAILABLE_DEVICES=()

run_cmd() {
    echo -e "\n> Running: $1"
    eval "$1"
}

scan_network() {
    echo "🔍 Scanning local network for devices with open ADB (5555)..."
    NETWORK=$(ip route | grep -oP 'src \K\S+')
    if [ -z "$NETWORK" ]; then
        read -p "Enter network prefix (e.g., 192.168.1): " NETWORK
    else
        NETWORK=$(echo $NETWORK | awk -F. '{print $1"."$2"."$3}')
    fi

    AVAILABLE_DEVICES=()
    for i in $(seq 1 254); do
        ip="$NETWORK.$i"
        timeout 1 bash -c "echo > /dev/tcp/$ip/5555" &>/dev/null
        if [ $? -eq 0 ]; then
            AVAILABLE_DEVICES+=("$ip")
        fi
    done

    if [ ${#AVAILABLE_DEVICES[@]} -eq 0 ]; then
        echo "❌ No devices found on network with ADB enabled."
    else
        echo "✅ Found devices:"
        for ip in "${AVAILABLE_DEVICES[@]}"; do
            echo " - $ip"
        done
    fi
}

connect_device() {
    if [ ${#AVAILABLE_DEVICES[@]} -eq 0 ]; then
        echo "No scanned devices. Run scan first."
        return
    fi

    echo "Select device to connect:"
    select IP in "${AVAILABLE_DEVICES[@]}"; do
        if [ -n "$IP" ]; then
            echo "Connecting to $IP..."
            adb tcpip 5555
            sleep 2
            adb connect "$IP:5555"
            break
        else
            echo "Invalid selection."
        fi
    done
}

list_devices() {
    adb devices
}

bug_hunt_report() {
    read -p "Enter device IP: " IP
    echo "Generating Bug Hunting Report for $IP..."
    REPORT="bug_report_$IP.txt"
    echo "Device: $IP" > $REPORT

    # Check if USB debugging enabled
    DEBUG=$(adb -s $IP:5555 shell getprop persist.service.adb.enable)
    echo "USB Debugging: ${DEBUG:-disabled}" >> $REPORT

    # List installed packages
    echo "Installed Packages:" >> $REPORT
    adb -s $IP:5555 shell pm list packages >> $REPORT

    # Check for common insecure settings
    DEV_MODE=$(adb -s $IP:5555 shell getprop ro.debuggable)
    echo "Device Debuggable Mode: ${DEV_MODE:-0}" >> $REPORT

    echo "Bug Hunting Report saved to $REPORT"
}

# Push, Pull, Reboot, Custom Command functions same as previous script
# ... (reuse previous push_file, pull_file, reboot_device, custom_command functions)

# ----- Menu -----
while true; do
    echo -e "\n====== Local ADB Remote + Bug Hunting ======"
    echo "1) Scan Local Network for ADB Devices"
    echo "2) Connect to Device"
    echo "3) Disconnect Device"
    echo "4) Reboot Device"
    echo "5) Push File"
    echo "6) Pull File"
    echo "7) List Connected Devices"
    echo "8) Run Custom Command"
    echo "9) Bug Hunting Report"
    echo "10) Exit"
    echo "=============================================="

    read -p "Choose option: " CHOICE

    case $CHOICE in
        1) scan_network ;;
        2) connect_device ;;
        3) adb disconnect ;;
        4) read -p "Enter device IP (or Enter for all): " IP; if [ -z "$IP" ]; then adb reboot; else adb -s "$IP:5555" reboot; fi ;;
        5) read -p "Enter device IP: " IP; read -p "Local file: " L; read -p "Remote path: " R; adb -s "$IP:5555" push "$L" "$R" ;;
        6) read -p "Enter device IP: " IP; read -p "Remote file: " R; read -p "Local save path: " L; adb -s "$IP:5555" pull "$R" "$L" ;;
        7) list_devices ;;
        8) read -p "Enter device IP: " IP; read -p "Command: " CMD; adb -s "$IP:5555" $CMD ;;
        9) bug_hunt_report ;;
        10) echo "Exiting..."; break ;;
        *) echo "❌ Invalid option" ;;
    esac
done
