# importing the module
import os
import time
#importing pyfiglet module for fonts
import pyfiglet

os.system("clear")

# sets the text colour to green
os.system("tput setaf 2")
print("\t\t\t\t\t\tLaunching Terminal User Interface")

# sets the text color to white
os.system("tput setaf 7")

print("\t\t\t\t\t-------------------------------------------------")
print("\t\t\t\t\t\t\tHOLD ON!!!!!!!!!\n\t\t\t\t\t\tYou are entering to the linux world")
print("\t\t\t\t\t-------------------------------------------------")
print("\n")
while True:
          os.system("tput setaf 3")
          result = pyfiglet.figlet_format("\t\t\t\tWelcome to ", font = "bulbhead" )
          result1 = pyfiglet.figlet_format("\t\t\t\t  the World of", font = "bulbhead" )
          os.system("tput setaf 1")
          result2 = pyfiglet.figlet_format("\t\t\t\t   REDHAT LINUX", font = "bulbhead" )
          print(result)
          print(result1)
          print(result2)
          os.system("tput setaf 4")
          print('\t\t\t1.Print date {:<25} 11.Create a folder'.format(''))
          print('\t\t\t2.Print cal {:<25}  12.To see all the folders '.format(''))
          print('\t\t\t3.Configure yum {:<21}  13.To see yum is configured or not '.format(''))
          print('\t\t\t4.To check the status of webserver {:<2}  14.Print Working Directory '.format(''))
          print('\t\t\t5.Install & start docker {:<12}  15.Reference manual pages for commands/programs '.format(''))
          print('\t\t\t6.To check the status of docker {:<5}  16.display the disk space used in the file system '.format(''))
          print('\t\t\t7.To stop docker {:<20}  17.Show previously used commands '.format(''))
          print('\t\t\t8.Add user {:<26}  18.Who you are logged in as '.format(''))
          print('\t\t\t9.Delete user {:<23}  19.Display free and used memory '.format(''))
          print('\t\t\t10.Create a file {:<20}  20.Display CPU information '.format(''))
          print('\t\t\t21.To create a webserver {:<13} 22.To Create Partition'.format(''))
          print('\t\t\t23.To mount a file {:<19} 24.To Create physical volume(pv)'.format(''))
          print('\t\t\t25.To create volume group {:<12} 26.To Create logical volume'.format(''))
          print('\t\t\t27.Exit ')


          os.system("tput setaf 5")
          ch = int(input("Enter your choice:  \t"))
          if (ch == 1):
              os.system("tput setaf 6")
              print("today's date is \n")
              os.system("date")
          elif ch == 2:
              os.system("tput setaf 6")
              print("Here is your calender")
              os.system("cal")
          elif ch == 3:
              os.system("yum install httpd -y")
              print(os.system("systemctl start httpd"))
          elif ch == 4:
              os.system("systemctl status httpd")
          elif ch == 5:
              print("installing docker............")
              print("starting docker...................")
             # os.system("yum install docker-ce -y")
              os.system("systemctl start docker")
          elif ch == 6:
              print(os.system("systemctl status docker"))
          elif ch == 7:
              print("stopping docker.................")
              os.system("systemctl stop docker")
              print(os.system("systemctl status docker"))
          elif ch == 8:
              os.system("tput setaf 6")
              new_user=input("Enter the name of new user: ")
              os.system("useradd {}".format(new_user))
              os.system("id -u {}".format(new_user))
          elif ch == 9:
              del_user=input("Enter the name of the user to delete: ")
              os.system("userdel {}".format(del_user))
          elif ch == 10:
              filename=input("Enter the filename: ")
              f=os.system("touch {}".format(filename))
              if f!=0:
                  print("Some error occurred")
              else:
                  print("File created successfully")
          elif ch == 11:
              os.system("tput setaf 6")
              foldername=input("Enter the foldername: ")
              f=os.system("mkdir {}".format(foldername))
              if f!=0:
                  print("tput setaf 1")
                  print("Some error occurred")
              else:
                  print("Folder created successfully")
          elif ch == 12:
              os.system("tput setaf 6")
              os.system("ls -a")
          elif ch == 13:
              os.system("tput setaf 6")
              os.system("yum repolist")
          elif ch == 14:
              os.system("tput setaf 6")
              os.system("pwd")
          elif ch == 15:
              os.system("tput setaf 6")
              command_name = input("Enter the command whose manual you want to see:")
              os.system("man {}".format(command_name))
          elif ch == 16:
              print("disk space...........")
              os.system("tput setaf 6")
              os.system("df")
          elif ch == 17:
              print("history...........")
              os.system("tput setaf 6")
              print(os.system("history"))
          elif ch == 18:
              os.system("tput setaf 6")
              os.system("whoami")
          elif ch == 19:
              os.system("tput setaf 6")
              os.system("free -h")
          elif ch == 20:
              os.system("tput setaf 6")
              os.system("cat /proc/cpuinfo")
          elif ch == 21:
              os.system("tput setaf 6")
              print("Stoping firewall............")
              os.system("systemctl stop firewalld")
              print("Starting the apache services...........")
              os.system("systemctl start httpd")
              print("STATUS OF THE APACHE WEBSERVER")
              s= os.system("systemctl status httpd")
              print(s)
              os.system("tput setaf 2")
              print("\nCopy your index.html files in /var/www/html/ folder ")
              f = input("Enter your webfile name:")
              os.system("cp {} /var/www/html".format(f) )
              time.sleep(2)
              print("file copied......................")
              print("*********IP ADDRESS*********")
              os.system("ifconfig enp0s3")
              print("Enter the ip in webbrowser for visiting the webpage")
              time.sleep(4)
          elif ch == 22:
              os.system("tput setaf 6")
              disk=input("enter your disk name ")
              os.system("sudo fdisk /dev/{}".format(disk))
          elif ch == 23:
              os.system("tput setaf 6")
              initdisk=input("Enter the destination where to mount ")
              finaldisk=input("Enter the disk path ")
              os.system("sudo mount -t ntfs {}  {}".format(initdisk, finaldisk))
              time.sleep(4)
          elif ch == 24:
              os.system("tput setaf 6")
              initdisk=input("Enter the destination where to mount ")
              finaldisk=input("Enter the disk path ")
              os.system("sudo pvcreate {}  {}".format(initdisk, finaldisk))
              time.sleep(4)
          elif ch == 25:
              os.system("tput setaf 6")
              grname=input("Enter your group name ")
              initdisk=input("Enter the destination where to mount ")
              finaldisk=input("Enter the disk path ")
              os.system("sudo vgcreate {}  {} {}".format(grname,initdisk, finaldisk))
              time.sleep(4)
          elif ch == 26:
              os.system("tput setaf 6")
              l= os.system("sudo lvdisplay")
              print(l)
              time.sleep(4)
          elif ch == 27:
              os.system("tput setaf 6")
              print("\n\t\t\t\t\t\tSEE YOU SOON!!\n")
              os.system("tput setaf 7")
              exit()
          else:
              print("Invalid entry")
          os.system("tput setaf 9")
          input("\n\nPress enter to continue")
          os.system("clear")

