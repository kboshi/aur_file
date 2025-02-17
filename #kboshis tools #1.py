#kboshis tools #1
'basically the basics of a system right when you use the archinstall script it installs everything'


import socket
import sys
import subprocess
import platform
import os
import time

print("Welcome to kboshis tools")
print("")
print("This is a list of toolsets that I use on the daily basis")
print("")

def check_os():    
    try:
        with open('/etc/os-release', 'r') as f:
            os_info = f.read().lower()
            if 'arch' in os_info:
                print("running on Arch Linux! :D")
                return True
            else:
                print("running on Linux, but not Arch Linux :C")
                print("please run Arch Linux")
                sys.exit(1)
    except FileNotFoundError:
        print("could not determine Linux distribution")
        return False

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print("Output:", result.stdout)
        time.sleep(2)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"error executing command: {str(e)}")
def check_sudo():
    return os.geteuid() == 0

if __name__ == "__main__":
    if not check_sudo():
        print("This script must be run with sudo privileges")
        sys.exit(1)
    check_os()
    print("everything is working so far")
    print("quick update")
    run_command("sudo pacman -Syuu git yay neofetch nano")
    print("installing blackarch")
    run_command("curl https://blackarch.org/strap.sh > strap.sh")
    run_command("sudo bash strap.sh")
    print("blackarch is installed")
    run_command("rm -rf /etc/pacman.conf")
    run_command("git clone https://github.com/kboshi/aur_file/blob/main/pacman.conf /etc/")
    run_command("pacman-key --init")
    run_command("pacman-key -r 9D5F1C051D146843CDA4858BDE64825E7CBC0D51")
    run_command("pacman-key --lsign-key 9D5F1C051D146843CDA4858BDE64825E7CBC0D51")
    run_command("pacman -Syuu")
    print("archstrike installed")
    print("one more thing I have to do")
    run_command("wget -q -O chaotic-AUR-installer.bash https://raw.githubusercontent.com/SharafatKarim/chaotic-AUR-installer/main/install.bash && sudo bash chaotic-AUR-installer.bash && rm chaotic-AUR-installer.bash")
    print("chaotic aur installed")
