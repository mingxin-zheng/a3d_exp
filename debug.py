import subprocess

if __name__ == "__main__":    
    # Launch the main function
    subprocess.run(['bcprun', '-n', '2', '-p', '8', '-c', "python debug.py"])
