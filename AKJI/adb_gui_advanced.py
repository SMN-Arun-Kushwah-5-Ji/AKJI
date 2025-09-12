import os
import subprocess
import time
import threading
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

ADB = "adb"  # Agar adb PATH mein nahi hai toh full path daalein

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

def append_output(output_text, text):
    output_text.insert(tk.END, text + "\n")
    output_text.see(tk.END)

def connect_adb(ip, output_text, status_label):
    append_output(output_text, "Setting device to TCP/IP mode...")
    out, err = run_cmd(f"{ADB} tcpip 5555")
    if err:
        append_output(output_text, err)
    time.sleep(2)

    append_output(output_text, f"Connecting to {ip}:5555 ...")
    out, err = run_cmd(f"{ADB} connect {ip}:5555")
    if out:
        append_output(output_text, out)
    if err:
        append_output(output_text, err)

    if "connected" in out.lower():
        messagebox.showinfo("Success", f"Connected to {ip}")
        status_label.config(text=f"Connected: {ip}")
    else:
        messagebox.showerror("Error", f"Failed to connect to {ip}")
        status_label.config(text="Not connected")

def disconnect_device(output_text, status_label):
    out, err = run_cmd(f"{ADB} disconnect")
    if out:
        append_output(output_text, out)
    if err:
        append_output(output_text, err)
    messagebox.showinfo("Info", "Disconnected all devices")
    status_label.config(text="Not connected")

def reboot_device(output_text):
    out, err = run_cmd(f"{ADB} reboot")
    if out:
        append_output(output_text, out)
    if err:
        append_output(output_text, err)
    messagebox.showinfo("Info", "Device reboot command sent")

def launch_scrcpy(output_text):
    append_output(output_text, "Launching scrcpy...")
    def run_scrcpy():
        os.system("scrcpy --bit-rate 4M --max-size 1024")
    threading.Thread(target=run_scrcpy, daemon=True).start()

def push_file(output_text):
    local_path = filedialog.askopenfilename(title="Select file to push")
    if not local_path:
        return
    remote_path = simpledialog.askstring("Remote Path", "Enter remote path (e.g. /sdcard/Download/):")
    if not remote_path:
        return
    append_output(output_text, f"Pushing {local_path} to {remote_path} ...")
    out, err = run_cmd(f'{ADB} push "{local_path}" "{remote_path}"')
    if out:
        append_output(output_text, out)
    if err:
        append_output(output_text, err)

def pull_file(output_text):
    remote_path = simpledialog.askstring("Remote Path", "Enter remote file path (e.g. /sdcard/Download/file):")
    if not remote_path:
        return
    local_path = filedialog.asksaveasfilename(title="Save file as")
    if not local_path:
        return
    append_output(output_text, f"Pulling {remote_path} to {local_path} ...")
    out, err = run_cmd(f'{ADB} pull "{remote_path}" "{local_path}"')
    if out:
        append_output(output_text, out)
    if err:
        append_output(output_text, err)

def list_devices(output_text):
    out, err = run_cmd(f"{ADB} devices")
    if out:
        append_output(output_text, "Connected devices:\n" + out)
    if err:
        append_output(output_text, err)

def run_custom_command(output_text):
    cmd = simpledialog.askstring("Custom Command", "Enter adb command (without 'adb'):")
    if not cmd:
        return
    full_cmd = f"{ADB} {cmd}"
    append_output(output_text, f"Running: {full_cmd}")
    out, err = run_cmd(full_cmd)
    if out:
        append_output(output_text, out)
    if err:
        append_output(output_text, err)

def clear_output(output_text):
    output_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    root.title("Advanced ADB Wireless Control")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="Enter Mobile IP:").grid(row=0, column=0, padx=5)
    ip_entry = tk.Entry(frame, width=20)
    ip_entry.grid(row=0, column=1, padx=5)

    status_label = tk.Label(root, text="Not connected", fg="red")
    status_label.pack()

    output_text = tk.Text(root, height=20, width=70)
    output_text.pack(padx=10, pady=10)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="Connect ADB Wireless", command=lambda: threading.Thread(target=connect_adb, args=(ip_entry.get().strip(), output_text, status_label), daemon=True).start()).grid(row=0, column=0, padx=5, pady=3)
    tk.Button(btn_frame, text="Disconnect Device", command=lambda: disconnect_device(output_text, status_label)).grid(row=0, column=1, padx=5, pady=3)
    tk.Button(btn_frame, text="Reboot Device", command=lambda: reboot_device(output_text)).grid(row=0, column=2, padx=5, pady=3)
    tk.Button(btn_frame, text="Launch scrcpy", command=lambda: launch_scrcpy(output_text)).grid(row=0, column=3, padx=5, pady=3)
    tk.Button(btn_frame, text="Push File", command=lambda: push_file(output_text)).grid(row=1, column=0, padx=5, pady=3)
    tk.Button(btn_frame, text="Pull File", command=lambda: pull_file(output_text)).grid(row=1, column=1, padx=5, pady=3)
    tk.Button(btn_frame, text="List Devices", command=lambda: list_devices(output_text)).grid(row=1, column=2, padx=5, pady=3)
    tk.Button(btn_frame, text="Run Custom Command", command=lambda: run_custom_command(output_text)).grid(row=1, column=3, padx=5, pady=3)
    tk.Button(root, text="Clear Output", command=lambda: clear_output(output_text)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
