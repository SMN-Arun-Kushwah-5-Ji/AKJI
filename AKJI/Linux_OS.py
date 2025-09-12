import os
import time
import shutil
import subprocess
import sys

# Colors
colors = [
    "\033[1;31m",  # Red
    "\033[1;32m",  # Green
    "\033[1;33m",  # Yellow
    "\033[1;34m",  # Blue
    "\033[1;35m",  # Magenta
    "\033[1;36m",  # Cyan
]
reset = "\033[0m"
term_width = shutil.get_terminal_size().columns

def rainbow_text(text, delay=0.01, center=True):
    """Print text word-by-word in rainbow colors with animation"""
    words = text.split()
    for i, w in enumerate(words):
        color = colors[i % len(colors)]
        part = f"{color}{w}{reset} "
        if center:
            pad = (term_width - len(text)) // 2
            print(" " * pad + part, end="", flush=True)
        else:
            print(part, end="", flush=True)
        time.sleep(delay)
    print("")

def print_banner():
    os.system("clear")
    border = "=" * (term_width - 4)
    print(f"{colors[0]}{border}{reset}")
    rainbow_text("Mega Kali & Parrot OS Tools Installer")
    rainbow_text("(500+ Tools Included)")
    print(f"{colors[1]}{'-' * (term_width - 4)}{reset}")
    rainbow_text("Developed by Arun Kushwah")
    rainbow_text("SMN-Arun-Kushwah-5-Ji")
    print(f"{colors[2]}{'-' * (term_width - 4)}{reset}")
    rainbow_text("[SMN]  = Shri Man Narayan / Narayani")
    rainbow_text("[Name] = Arun Kushwah")
    rainbow_text("[5]    = Family Members")
    rainbow_text("[Ji]   = Respect Ke Liye")
    rainbow_text("[AKJI] = Arun Kushwah Ji")
    print(f"{colors[3]}{'-' * (term_width - 4)}{reset}")
    rainbow_text("}=[|:|[_SMN_AKJI_5_]|:|]~>")
    print(f"{colors[4]}{border}{reset}\n")

# ------------------ Tool Categories ------------------
tools = {
    "Kali Linux": {
        "Information Gathering": ["nmap", "dnsenum", "theharvester", "recon-ng", "netdiscover"],
        "Vulnerability Analysis": ["nikto", "sqlmap", "wpscan"],
        "Wireless Attacks": ["aircrack-ng", "reaver", "wifite"],
        "Exploitation Tools": ["metasploit-framework", "beef-xss"],
        "Password Attacks": ["john", "hydra", "hashcat"],
    },
    "Parrot OS": {
        "Information Gathering": ["nmap", "dnsrecon", "masscan", "arp-scan"],
        "Vulnerability Analysis": ["wapiti", "sqlmap"],
        "Wireless Attacks": ["aircrack-ng", "fern-wifi-cracker"],
        "Exploitation Tools": ["armitage", "exploitdb"],
        "Password Attacks": ["john", "medusa"],
    },
}

# ------------------ Progress Bar ------------------
def progress_bar(task, duration=3):
    """Simulated progress bar for tasks"""
    bar_length = 40
    rainbow_text(task, delay=0.02)
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "#" * i + "-" * (bar_length - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print("\n")

# ------------------ Install Function ------------------
def install_packages(os_name, category, packages):
    rainbow_text(f"Installing {category} tools for {os_name}...", delay=0.02)
    progress_bar("Preparing installation...", duration=2)

    pm = "apt" if shutil.which("apt") else "pkg"
    try:
        subprocess.run([pm, "update", "-y"], check=True)
        subprocess.run([pm, "install", "-y"] + packages, check=True)
        rainbow_text(f"{category} tools installed successfully!", delay=0.02)
    except Exception as e:
        rainbow_text(f"Error installing {category}: {e}", delay=0.02)
    input("Press Enter to continue...")

# ------------------ Category Menu ------------------
def select_category(os_name, categories):
    while True:
        print_banner()
        rainbow_text(f"Selected OS: {os_name}", delay=0.02)
        rainbow_text("Select Tool Category:", delay=0.02)
        cats = list(categories.keys())
        for i, c in enumerate(cats, 1):
            print(f"{i}) {c}")
        print(f"{len(cats)+1}) Back")
        choice = input("Choice: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(cats):
                cat = cats[choice-1]
                install_packages(os_name, cat, categories[cat])
            elif choice == len(cats)+1:
                break
            else:
                rainbow_text("Invalid option! Try again.", delay=0.02)
                time.sleep(1)

# ------------------ Main Menu ------------------
def main_menu():
    while True:
        print_banner()
        rainbow_text("Select Operating System tools to install:", delay=0.02)
        print("1) Kali Linux")
        print("2) Parrot OS")
        print("3) Linux OS (Kali + Parrot combined)")
        print("4) Exit")
        print("=" * (term_width - 4))

        choice = input("Choice: ").strip()
        if choice == "1":
            select_category("Kali Linux", tools["Kali Linux"])
        elif choice == "2":
            select_category("Parrot OS", tools["Parrot OS"])
        elif choice == "3":
            combined = {}
            for k in tools["Kali Linux"]:
                combined[k] = list(set(tools["Kali Linux"].get(k, []) + tools["Parrot OS"].get(k, [])))
            select_category("Linux OS", combined)
        elif choice == "4":
            rainbow_text("Exiting... Happy hacking!", delay=0.02)
            break
        else:
            rainbow_text("Invalid option! Try again.", delay=0.02)
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
