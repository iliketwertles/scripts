import argparse
import os.path
import shutil
import subprocess
import glob

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="select name for entry")
parser.add_argument("--number", help="specify number of entry (40+ suggested")
parser.add_argument("-f", "--file", help="copy grub file to grub directory", required=False)
parser.add_argument("--grubpath", help="specify path to update grub config to (default is /boot/grub/grub.cfg)")
parser.add_argument("-i", "--image", help="add image to custom grub entry, should have the same name in the entry as a --class specified in the entry ", required=False)


args = parser.parse_args()

if not os.geteuid() == 0:
    exit("\nRun as root\n")

def imagehandler():
    print("checking for images...")
    if args.image == True:
        print("valid image specified\nChoose a path below")
        print(glob.glob("/boot/grub/themes"))
        THEMENAME = input("which theme would you like the icon to go into?")
        shutil.move(args.image, "/boot/grub/themes/{}/icons").format(THEMENAME)
    else:
        print("no immage specified, continuing")

def updategrub():
    if file.exists("/usr/sbin/update-grub"):
        subprocess.Popen("sudo update-grub", shell=True)
        exit("refer to exit msg above")
    else:
        if args.grubpath == True:
            subprocess.Popen("sudo grub-mkconfig -o "+args.grubpath , shell=True)
        if args.grubpath == None:
            exit("file in place, unable to update grub.")

NAME = args.name
if args.name == None:
    NAME == "custom"

if args.number < 40:
    YN = input("numbers below 40 are not suggested, would you like to continue?")
    if YN == "y":
        print("ok")
    elif YN == "n":
        print("ok, setting to '99'")
        args.number = 99
elif args.number > 99: 
    print("setting to '99', numbers above 99 are not supported")
else:
    print("valid number specified")
    

if os.path.exists("/etc/grub.d/40_custom"):
    print("valid custom file found!")
else:
    exit("could not find '40_custom' file at /etc/grub.d/")

YN = input("would you like to continue? [y/n]")
if YN == "y":
    print("ight")
else:
    exit("ok then")

DIR = "/etc/grub.d/{}_"
shutil.copy("/etc/grub.d/40_custom", DIR.format(args.number)+NAME)

if args.file == None:
    print("No file specified, opening nano editor.")
else:
    print("appending contents of file specified into {}_".format(args.number)+NAME)
    with open(args.file,'r') as firstfile, open(args.number+"_"+NAME,'w') as secondfile:
        for line in firstfile:
            secondfile.write(line)
    print("updating grub now")
    imagehandler()
    updategrub()
    

subprocess.Popen("sudo nano /etc/grub.d/{}_".format(args.number)+NAME)
imagehandler()
updategrub()
