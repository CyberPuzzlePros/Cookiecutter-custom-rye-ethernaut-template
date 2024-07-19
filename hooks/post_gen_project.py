#!/usr/bin/python3
import subprocess

def is_rye_installed():
    """
    Check if rye is installed
    """
    try:
        subprocess.run(["rye", "--version"], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def install_rye():
    """
    Install rye using curl
    """
    # First part of the command
    curl_command = ["curl", "-sSf", "https://rye.astral.sh/get"]

    # Second part of the command
    bash_command = ["bash"]

    # Run the curl command and pipe its output to the bash command
    curl_process = subprocess.Popen(curl_command, stdout=subprocess.PIPE)
    bash_process = subprocess.run(bash_command, stdin=curl_process.stdout, capture_output=True, text=True)

    # Close the stdout pipe of curl_process to signal that no more data will be written
    curl_process.stdout.close()

    # Wait for curl_process to finish
    curl_process.wait()

    # Print the output and errors
    if bash_process.stderr:
        print(bash_process.stderr)

def setup_env():
    """
    Set up rye environment
    """
    try:
        subprocess.run(["rye", "init"], check=True)
        subprocess.run(["rye", "add", "eth-ape", "--pre"], check=True)
        subprocess.run(["rye", "sync", "--pre"], check=True)
        subprocess.run(["rye", "run", "ape", "plugins", "install", "."], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("Make sure to manually set up a git repository which is necessary for `hatch-vcs`")

def main():
    if not is_rye_installed():
        install_rye()
    setup_env()

if __name__ == "__main__":
    main()
