import subprocess

if __name__ == "__main__":    
    # Launch the main function
    print("Starting")
    subprocess.run(['bcprun', '-n', '2', '-p', '8', '-c', "python hello_world.py"])
    print("Finished")
