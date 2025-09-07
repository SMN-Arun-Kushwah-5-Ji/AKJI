#!/bin/bash

# ================= Colors =================
colors=(
  "\033[1;31m" # Red
  "\033[1;32m" # Green
  "\033[1;33m" # Yellow
  "\033[1;34m" # Blue
  "\033[1;35m" # Magenta
  "\033[1;36m" # Cyan
)
reset="\033[0m"
color_index=0
width=64

# ================= Banner =================
print_banner() {
  clear
  color_index=$(( (color_index + 1) % ${#colors[@]} ))

  center_multicolor() {
    local text="$1"
    local words=($text)
    local total_len=${#text}
    local pad=$(( (width - total_len) / 2 ))
    printf "%*s" $pad ""
    local i=0
    for w in "${words[@]}"; do
      local c=${colors[$(( i % ${#colors[@]} ))]}
      echo -ne "${c}${w}${reset} "
      ((i++))
    done
    echo ""
  }

  echo -e "${colors[0]}================================================================${reset}"
  center_multicolor "Mega Kali & Parrot OS Tools Installer"
  center_multicolor "(500+ Tools Included)"
  echo -e "${colors[1]}----------------------------------------------------------------${reset}"
  center_multicolor "Developed by Arun Kushwah"
  center_multicolor "SMN-Arun-Kushwah-5-Ji"
  echo -e "${colors[2]}----------------------------------------------------------------${reset}"
  center_multicolor "[SMN]  = Shri Man Narayan / Narayani"
  center_multicolor "[Name] = Arun Kushwah"
  center_multicolor "[5]    = Family Members"
  center_multicolor "[Ji]   = Respect Ke Liye"
  center_multicolor "[AKJI] = Arun Kushwah Ji"
  echo -e "${colors[3]}----------------------------------------------------------------${reset}"
  center_multicolor "}=[|:|[_SMN_AKJI_5_]|:|]~>"
  echo -e "${colors[4]}================================================================${reset}"
  echo ""
}

# ================= Tool Printing =================
multicolor_inline() {
  local text="$1"
  local words=($text)
  local i=0
  for w in "${words[@]}"; do
    local c=${colors[$(( i % ${#colors[@]} ))]}
    echo -ne "${c}${w}${reset} "
    ((i++))
  done
  echo ""
}

# ------------------- Kali Tools -------------------
declare -A kali_tools=(
  ["Information Gathering"]="kali-linux-information-gathering nmap dnsenum theharvester maltego dnsrecon recon-ng masscan netdiscover arp-scan"
  ["Vulnerability Analysis"]="kali-linux-vulnerability-analysis nikto openvas wapiti sqlmap wpscan"
  ["Wireless Attacks"]="kali-linux-wireless aircrack-ng reaver wifite bully fern-wifi-cracker"
  ["Exploitation Tools"]="kali-linux-exploitation metasploit-framework armitage beef-xss exploitdb"
  ["Password Attacks"]="kali-linux-passwords john hydra hashcat medusa"
  ["Forensics"]="kali-linux-forensics autopsy sleuthkit volatility bulk-extractor"
  ["Reverse Engineering"]="kali-linux-reverse-engineering gdb radare2 apktool dex2jar jd-gui"
  ["Reporting Tools"]="kali-linux-reporting dradis faraday"
  ["Hardware Hacking"]="kali-linux-hardware usbutils"
  ["Stress Testing"]="kali-linux-stress-testing slowloris hping3"
  ["Sniffing & Spoofing"]="kali-linux-sdr wireshark ettercap mitmproxy"
  ["Maintainers Tools"]="kali-linux-maintainers-tools"
  ["Social Engineering"]="kali-linux-social-engineering set social-engineer-toolkit"
  ["Top 10 Tools"]="aircrack-ng burpsuite metasploit nmap wireshark sqlmap john hydra hashcat"
)

# Add extra Kali packages
kali_extra_packages=(
  "masscan" "netdiscover" "arp-scan" "wpscan" "fern-wifi-cracker" "exploitdb" "medusa" "bulk-extractor" "dex2jar" "jd-gui"
  "slowloris" "hping3" "ettercap" "mitmproxy" "usbutils" "set"
)

# ------------------- Parrot Tools -------------------
declare -A parrot_tools=(
  ["Information Gathering"]="parrot-tools-info nmap dnsenum theharvester maltego dnsrecon recon-ng masscan netdiscover arp-scan"
  ["Vulnerability Analysis"]="parrot-tools-vuln nikto openvas wapiti sqlmap wpscan"
  ["Wireless Attacks"]="parrot-tools-wireless aircrack-ng reaver wifite bully fern-wifi-cracker"
  ["Exploitation Tools"]="parrot-tools-exploitation metasploit-framework armitage beef-xss exploitdb"
  ["Password Attacks"]="parrot-tools-passwords john hydra hashcat medusa"
  ["Forensics"]="parrot-tools-forensics autopsy sleuthkit volatility bulk-extractor"
  ["Reverse Engineering"]="parrot-tools-re reverse-engineering gdb radare2 apktool dex2jar jd-gui"
  ["Reporting Tools"]="parrot-tools-reporting dradis faraday"
  ["Hardware Hacking"]="parrot-tools-hardware usbutils"
  ["Stress Testing"]="parrot-tools-stress-testing slowloris hping3"
  ["Sniffing & Spoofing"]="parrot-tools-sdr wireshark ettercap mitmproxy"
  ["Maintainers Tools"]="parrot-tools-maintainers-tools"
  ["Social Engineering"]="parrot-tools-social-engineering set social-engineer-toolkit"
  ["Top 10 Tools"]="aircrack-ng burpsuite metasploit nmap wireshark sqlmap john hydra hashcat"
)

# Add extra Parrot packages
parrot_extra_packages=(
  "masscan" "netdiscover" "arp-scan" "wpscan" "fern-wifi-cracker" "exploitdb" "medusa" "bulk-extractor" "dex2jar" "jd-gui"
  "slowloris" "hping3" "ettercap" "mitmproxy" "usbutils" "set"
)

# ---------------- Combine Kali + Parrot Tools ----------------
declare -A combined_tools

combine_tools() {
  combined_tools=()
  for key in "${!kali_tools[@]}"; do
    combined_tools["$key"]="${kali_tools[$key]}"
  done
  for key in "${!parrot_tools[@]}"; do
    if [[ -v combined_tools[$key] ]]; then
      existing="${combined_tools[$key]}"
      new="${parrot_tools[$key]}"
      merged=$(echo -e "$existing\n$new" | tr ' ' '\n' | sort -u | tr '\n' ' ')
      combined_tools[$key]="$merged"
    else
      combined_tools[$key]="${parrot_tools[$key]}"
    fi
  done
}

# ================= Installer =================
install_tools() {
  local os="$1"
  local category="$2"
  local packages="$3"

  multicolor_inline "Installing $category packages for $os..."

  if command -v apt &>/dev/null; then
    sudo apt update
    sudo apt install -y $packages
  elif command -v pkg &>/dev/null; then
    pkg update -y
    pkg install -y $packages
  else
    multicolor_inline "No supported package manager found!"
    return
  fi

  multicolor_inline "$category installation for $os completed!"
  read -p "Press Enter to continue..."
}

# ================= Category Selector =================
select_category() {
  local os="$1"
  local -n tools_ref="$2"

  while true; do
    print_banner
    multicolor_inline "Selected OS: $os"
    echo "Select Tool Category to install:"
    local i=1
    local categories=()
    for cat in "${!tools_ref[@]}"; do
      echo "$i) $cat"
      categories+=("$cat")
      ((i++))
    done
    echo "$i) Back to OS selection"
    echo "================================================================"
    read -p "Choice: " choice

    if [[ "$choice" -ge 1 && "$choice" -le "${#categories[@]}" ]]; then
      local cat_name="${categories[$((choice-1))]}"
      install_tools "$os" "$cat_name" "${tools_ref[$cat_name]}"
    elif [[ "$choice" -eq $i ]]; then
      break
    else
      multicolor_inline "Invalid option! Try again."
      sleep 1
    fi
  done
}

# ================= Main Menu =================
while true; do
  print_banner
  multicolor_inline "Select Operating System tools to install:"
  echo "1) Kali Linux"
  echo "2) Parrot OS"
  echo "3) Linux OS (Kali + Parrot combined)"
  echo "4) Exit"
  echo "================================================================"
  read -p "Choice: " os_choice

  case $os_choice in
    1)
      kali_tools["Extra Kali Packages"]="${kali_extra_packages[*]}"
      select_category "Kali Linux" kali_tools
      ;;
    2)
      parrot_tools["Extra Parrot Packages"]="${parrot_extra_packages[*]}"
      select_category "Parrot OS" parrot_tools
      ;;
    3)
      combine_tools
      select_category "Linux OS" combined_tools
      ;;
    4)
      multicolor_inline "Exiting. Happy hacking!"
      exit 0
      ;;
    *)
      multicolor_inline "Invalid option! Try again."
      sleep 1
      ;;
  esac
done
