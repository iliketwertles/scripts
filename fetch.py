import subprocess
import platform
from pathlib import Path

logo = f'''  .~.
  /V\\   Hello {subprocess.getoutput('whoami')}
 // \\\\
/(   )\\
 ^`~'^'''

if platform.system() == "Linux":
    if Path('/etc/pacman.d').exists() == True:
        distro = 'Arch'
        pkgs = subprocess.getoutput('pacman -Q | wc -l')
    elif Path('/etc/apt').exists() == True:
        distro = 'Debian'
        pkgs == subprocess.getoutput('dpkg --list | wc -l')
    elif Path('/etc/dnf').exists() == True:
        distro = 'Fedora'
        pkgs == subproces.getoutput('dnf list installed | wc -l')

elif platform.system() == "Darwin":
    distro = 'MacOS'
    if Path('/opt/homebrew/Cellar') or Path('/usr/local/Cellar') == True:
        pkgs == subprocess.getoutput('ls -1 $(brew --cellar) | wc -l')
    elif Path('/opt/homebrew/Cellar') and Path('/usr/local/Cellar') == False:
        pkgs = "no"

kernel = subprocess.getoutput('uname -r')

print(logo)
print(f'You have {pkgs} packages on kernel {kernel}, have fun {distro} user!')
