import subprocess
import pkg_resources

def upgrade_packages():
    # Get all installed packages
    packages = [pkg.key for pkg in pkg_resources.working_set]
    # Upgrade each package
    for package in packages:
        subprocess.check_call(["pip", "install", "--upgrade", package])

if __name__ == "__main__":
    upgrade_packages()
