import subprocess
import os, stat
import platform
import argparse
import requests
import shutil
import zipfile
import pathlib
from os.path import exists
import PySimpleGUI as sg



#checking os
PLAT = platform.system()

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tools', action='store_true', help='show avalable tools to install')
parser.add_argument('-i', '--install', help='install selected tool')
parser.add_argument('--ip', help='specify ip address of ios device.')
parser.add_argument('-o', '--options', action='store_true', help='displays options for toolkit.')
parser.add_argument('-r', '--run', help='Runs selected option')
parser.add_argument('--gui', help="Opens gui", action='store_true')

args = parser.parse_args()

#functions

#fixes/ other functions
USR = "mobile@"
IP = args.ip
def respring():
    CMD = 'sbreload'
    print('Default password is apline')
    subprocess.run(['ssh', USR+IP, CMD])
    exit

def clear_other():
    CMD = "'rm -rf /var/mobile/Library/Caches/com.apple.CacheDeleteAppContainerCaches.deathrow'"
    print('After running this, reboot your device, may or may not clear some other storage')
    print('Default password is apline')
    subprocess.run(['ssh', USR+IP, CMD])
    exit

def ssh_shell():
    CMD = ''
    print('Default password is apline')
    subprocess.run(['ssh', USR+IP, CMD])
    exit

if args.run == '1':
    respring()

def install_ns():
        if PLAT == 'Windows':
            print('Use Linux or macOS for this tool.')
        else:
            UNURL = 'https://gist.github.com/m1stadev/f1130b066fb1334dccc8bcb596c5b336'
            r = requests.get(UNURL, allow_redirects=True)
            open('nonce-setter.py', 'wb').write(r.content)
            os.chmod('nonce-setter.py', stat.S_IRWXO)
            print("File ready at 'nonce-setter.py'")

def download_iso():
    URL = "put something here"
    r = requests.get(URL, allow_redirects=True)
    open('Odysseyra1n.iso', 'wb').write(r.content)

def install_orain():
        if PLAT == 'Windows':
            print('Odysseyra1n does not support windows, however you can download the OdysseyRa1n iso to flash to a usb\nThis will let you use checkra1n and bootstrap with procursus on your pc but you will need to follow this tutorial.\nhttps://guides.stkc.win/posts/odysseyn1x/')
        else:
            print('Dowloading script...')
            UOURL = 'https://raw.githubusercontent.com/coolstar/Odyssey-bootstrap/master/procursus-deploy-linux-macos.sh'
            r = requests.get(UOURL, allow_redirects=True)
            open('Odysseyra1n-deploy.sh', 'wb').write(r.content)
            print('chmoding...')
            os.chmod('Odysseyra1n-deploy.sh', stat.S_IRWXO)
            YN == input('Saved as "./Odysseyra1n-deploy.sh", would you like to run it now? [y/n]')
            if YN == 'y':
                subprocess.run(['./Odysseyra1n-deploy.sh'])
            elif YN == 'n':
                exit
            else:
                print("ok ig")
                exit

def install_futurerestore():
        if PLAT == 'Linux':
            print('Downloading futurerestore...')
            LFURL = 'https://nightly.link/futurerestore/futurerestore/workflows/ci/test/futurerestore-Linux-x86_64-RELEASE.zip'
            r = requests.get(LFURL, allow_redirects=True)
            open("futurerestore.zip", 'wb').write(r.content)
            print("extracting...")
            with zipfile.ZipFile('futurerestore.zip', 'r') as zip_ref:
                zip_ref.extractall('futurerestore')
            path = pathlib.Path('futurerestore.zip')
            path.unlink()
            for pkg in os.listdir('futurerestore'):
                if pkg.endswith("RELEASE.tar.xz"):
                    continue
            os.chdir('futurerestore')
            print('extracting(again)...')
            subprocess.run(['tar', '-xf', pkg])
            path = pathlib.Path(pkg)
            path.unlink()
            print('chmoding...')
            os.chmod('futurerestore', stat.S_IRWXO)
            print('futurestore binary is ready to run under the directory futurerestore/')
            subprocess.run(['./futurerestore'])
            exit

        elif PLAT == 'Darwin':
            print('Downloading futurerestore...')
            MFURL = 'https://nightly.link/m1stadev/futurerestore/workflows/ci/test/futurerestore-macOS-x86_64-RELEASE.zip'
            r = requests.get(MFURL, allow_redirects=True)
            open("futurerestore.zip", 'wb').write(r.content)
            print('extracting...')
            with zipfile.ZipFile('futurerestore.zip', 'r') as zip_ref:
                zip_ref.extractall('futurerestore')
            path = pathlib.Path('futurerestore.zip')
            path.unlink()
            for PKG in os.listdir('futurerestore'):
                if PKG.endswith("RELEASE.tar.xz"):
                    continue
            os.chdir('futurerestore')
            print("extracting(again)...")
            subprocess.run(['tar', '-xf', PKG])
            path = pathlib.Path(PKG)
            path.unlink()
            print("chmoding...")
            os.chmod('futurerestore', stat.S_IRWXO)
            print('futurestore binary is ready to run under the directory futurerestore/')
            subprocess.run(['./futurerestore'])
            exit

        elif PLAT == "Windows":
            print('There is a windows version of futurerestore but it is very out of date\nit is recommended to use macos or linux for this at the time this script was made.')

def install_checkra1n():
    if PLAT == 'Linux':
        print("Downloading checkra1n...")
        LCURL = 'https://assets.checkra.in/downloads/linux/cli/x86_64/dac9968939ea6e6bfbdedeb41d7e2579c4711dc2c5083f91dced66ca397dc51d/checkra1n'
        r = requests.get(LCURL, allow_redirects=True)
        open('checkra1n', 'wb').write(r.content)
        shutil.move("checkra1n", "/usr/local/bin/checkra1n")
        os.chmod("/usr/local/bin/checkra1n", stat.S_IRWXO)
        print("finished, you can now run 'sudo checkra1n', you might have to restart terminal for it to work")
        yn = input("Would you like to run checkra1n now? [y/n]")
        if yn == "y":
            subprocess.run(['sudo', 'checkra1n'])
            exit
        elif yn == 'n':
            print('ok')
        else:
            print('invalid response')
    elif PLAT == 'Darwin':
        print("Downloading checkra1n...")
        MCURL = "https://assets.checkra.in/downloads/macos/754bb6ec4747b2e700f01307315da8c9c32c8b5816d0fe1e91d1bdfc298fe07b/checkra1n%20beta%200.12.4.dmg"
        r = requests.get(MCURL, allow_redirects=True)
        open('checkra1n.dmg', 'wb').write(r.content)
        print('now open the dmg that was downloaded and install it like normal')
        exit
    elif PLAT == 'Windows':
        print('Checkra1n does not support windows, however you can download the OdysseyRa1n iso to flash to a usb\nThis will let you use checkra1n on your pc but you will need to follow this tutorial.\nhttps://guides.stkc.win/posts/odysseyn1x/')

def run_checkra1n():
        if PLAT == 'Linux':
            file_exists = exists('/usr/local/bin/checkra1n')
        if file_exists == True:
            subprocess.run(['sudo', 'checkra1n', '-c', '-e', 'launchd_missing_exec_no_panic=1'])
        elif file_exists == False:
            YN = input('You do not have checkra1n installed, would you like to install it now?')
            if YN == 'y':
                install_checkra1n()
            elif YN == 'n':
                exit
        elif PLAT == 'Darwin':
            file_exists = exists('/Applications/checkra1n.app/Contents/MacOS/checkra1n')
        if file_exists == True:
            subprocess.run(['sudo','/Applications/checkra1n.app/Contents/MacOS/checkra1n', '-c', '-e', 'launchd_missing_exec_no_panic=1',])
        elif file_exists == False:
            YN = input('You do not have checkra1n installed, would you like to install it now?')
            if YN == 'y':
                install_checkra1n()
            elif YN == 'n':
                exit
        else:
            print("No.")

if args.gui == True:
    sg.theme("Black")
    layout = [

            [sg.Text('Install Tools:')],
            [sg.Button('Checkra1n'), sg.Button('FutureRestore'), sg.Button('Odysseyra1n (Script)'), sg.Button('Nonce-Setter')],
            [sg.Text('Run Fixes/Other Functions')],
            [sg.Button('Remote Respring'), sg.Button('Clear "other" storage'), sg.Button('SSH Shell'), sg.Button('Fix Checkra1n bootloop')],
            [sg.Exit()]

    ]

    window = sg.Window('Jailbreak-toolkit', layout, size=(800, 500))

    event, values = window.read()
    window.close()

    while True:
        #installing tools
        if event == 'Checkra1n':
            install_checkra1n()
            exit
        elif event == 'FutureRestore':
            install_futurerestore()
            exit
        elif event == 'OdysseyRa1n (Script)':
            install_orain()
            exit
        elif event == 'Nonce-Setter':
            install_ns()
            exit
        #running tools
        elif event == 'Remote Respring':
            respring()
            exit
        elif event == 'Clear "Other" Storage':
            clear_other()
            exit
        elif event == 'SSH Shell':
            ssh_shell()
            exit
        elif event == 'Fix Checkra1n bootloop':
            run_checkra1n()
            exit
        elif event == 'Exit':
            window.close()
        window.close()

    window.close()
    self.TKroot.update()


elif args.run == '2':
    clear_other()
elif args.run == '3':
    run_checkra1n()
elif args.run == '4':
    ssh_shell()


if args.options:
    print("[1]Remote respring\n[2]Atempt clearing 'Other' storage\n[3]Atempt to fix checkra1n bootloop\n[4]Run ssh shell")

if args.tools:
    print("Avalable tools:\nCheckra1n\nFuturerestore(latest beta)\nOdysseyra1n (must jailbreak with checkra1n first)\nNonce-setter (m1stadev)")

if args.install == "nonce-setter":
    install_ns()


if args.install == 'checkra1n':
    install_checkra1n()

elif args.install == 'futurerestore':
    install_futurerestore()


elif args.install == 'odysseyra1n':
    install_orain()
