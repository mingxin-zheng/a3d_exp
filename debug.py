import subprocess
import sys
from time import sleep

if __name__ == "__main__":    
    # Launch the main function
    print("Starting", file=sys.stderr)
    sleep(10)
    subprocess.run(['bcprun', '-n', '2', '-p', '8', '-a' '-c', "python hello_world.py"])
    sleep(0.1)
    print("Finished", file=sys.stderr)
