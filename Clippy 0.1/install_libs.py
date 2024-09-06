import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    with open('requirements.txt') as f:
        packages = f.read().splitlines()

    for package in packages:
        try:
            install(package)
            print(f"Successfully installed {package}")
        except Exception as e:
            print(f"Error installing {package}: {e}")
