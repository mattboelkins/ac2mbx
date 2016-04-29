import glob
import os
files = glob.glob("*.py")
for file in files:
    os.system("python " + file)
