#Scripted by Therealmip

#MW-CE script


safemode = ("")

devmode = ("")

#Trys in import "OS" if it fails the script is put to a stop
try:
  import os
except:
  print("ERROR!")
  print("OS import error")
  print("Please retry starting MW-CE, if that fails report this code to support")
  print("ERROR CODE: H-07-F-0001")
  exit()


#Checks if the logging.log file is in MW-CE's working folder
file_existsmain = os.path.exists('bin')
if file_existsmain == False:
  try:
    f123 = open('logging.log', 'w')
    f123.close()
  except:
    print("ERROR!")
    exit()
elif file_existsmain == True:
  pass




#Trys to import "logging", if it fails the script is put to a stop until fixed
try:
  import logging
  logging.basicConfig(filename="logging.log", format='%(asctime)s %(message)s', filemode='w')
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
except:
  print("ERROR!")
  print("Logging import error")
  print("Please retry starting MW-CE, if that fails report this code to support")
  print("ERROR CODE: H-09-F-0001")
  exit()


#Trys to print MW-CE 'textart' in color
try:
  class startupcolors:
      BLUE = '\033[94m'
      ENDC = '\033[0m'
      italic = '\x1B[3m'
      italicnorm = '\x1B[0m'
  from art import *
  print(f"{startupcolors.BLUE}")
  tprint("MW-CE")
  print(f"{startupcolors.ENDC}")
  import sys
  import time
  import threading

  

  #Loads the older daemon system, this is used as an backup.
  class Spinner:
      busy = False
      delay = 0.05

      @staticmethod
      def spinning_cursor():
          while 1: 
              for cursor in '/-\|' : yield cursor

      def __init__(self, delay=None):
          self.spinner_generator = self.spinning_cursor()
          if delay and float(delay): self.delay = delay

      def spinner_task(self):
          while self.busy:
            
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

      def __enter__(self):
          self.busy = True
          threading.Thread(target=self.spinner_task).start()

      def __exit__(self, exception, value, tb):
          self.busy = False
          time.sleep(self.delay)
          if exception is not None:
              return False

except:
  logging.error('Failed to load main loading daemon')
  pass

try:
  print("Loading imports. . .")
  with Spinner():
    import os
    import os.path
    import subprocess
    import time
    import sys
    import climage
    import zipfile
    import socket
    import pyshorteners
    import random
    import requests, json
    import requests
    import whois
    from os import system, name
    from os import listdir
    from datetime import datetime
    from time import sleep
    from tqdm import tqdm
    from art import *
    import time
    import socket
    import shutil
    import sys
    import platform
    import os
    import socket
    from itertools import product
    from importlib import reload
    from zipfile import ZipFile, BadZipFile
    import string
    from random import *
    start_time = time.time()
    logger.info('Imported all imports')
    logging.error('Test error')
  
#If imports fail then the script is stopped with a error
except:
  logging.critical('FAILED TO LOAD IMPORTS')
  import time
  import os
  import sys
  from time import sleep
  print()
  safemode = ("Safe-Mode")
  print("ERROR!")
  print("Logging import error")
  print("Please retry starting MW-CE, if that fails report this code to support")
  print("ERROR CODE: H-08-F-0002")
  print()
  print("Starting Safe Mode in:")
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  pass



#Checks if 'bin' exists
file_exists = os.path.exists('bin')
def check2343234():
  if file_exists == False:
    print()
    print("WARNING: 'bin' not found. Please redownload a new version of MW-CE")
    print()
    exit()
  elif file_exists == True:
    pass

check2343234()

  

#states text colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ROOTRED = ' \u001b[31m'

rootcolor = (bcolors.BOLD)

taskkill1 = ("ok")

def easteregg321():
  print(f"{bcolors.ROOTRED}ERR0R 008: Process termination needed{bcolors.ENDC}")
  time.sleep(0.7)
  exit


from cryptography.fernet import Fernet
#Loads the enc key
#for enc-ing files and stuff
key="lbeiXBZ1gIVWtTAlbXCACKEIT7B3AppqxZib-35LmQo="


fernet=Fernet(key)

#Def's the "screen_clear" function to clear the screen
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

#if there is any problems with text colors at first
#this should fix it
print("calibrating text colors. . .")
print(f"{bcolors.HEADER}calibrating. . .{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}Text colors calibration complete!{bcolors.ENDC}")

def exitthing3():
  screen_clear()
  exit

    
  
#Current verion of MW-CE
version = ("0.1.9.1 Beta PE")

screen_clear()
#defs the info screen
print(f"MIPWARE Command Executor {bcolors.HEADER}=OVERHAUL-PB={bcolors.ENDC}")
print(version)
print(f"{bcolors.OKGREEN}MW-CE loaded!{bcolors.ENDC}")
print(safemode)
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
def MainCommandline():
  command,info = input(f"{bcolors.ROOTRED} (ROOT) {bcolors.ENDC} Command: ").split()
  #Commands

  if command == ("echo"):
    print(info)


  
  MainCommandline()
MainCommandline()
