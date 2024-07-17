#!/usr/bin/python3
import subprocess

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
    # print(bash_process.stdout)
    if bash_process.stderr:
        print(bash_process.stderr)


try:
    install_rye()
    subprocess.call(["rye", "init"])
    subprocess.call(["rye", "add", "eth-ape", "--pre"])
    subprocess.call(["rye", "sync", "--pre"])
    subprocess.call(["rye", "run", "ape", "plugins", "install", "."])
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
    print(
        "Makre sure to manually set up a git repository which is necessary for `hatch-vcs`"
    )