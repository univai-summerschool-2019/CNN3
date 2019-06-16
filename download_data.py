import os
import glob
import subprocess


if not os.path.exists("../dogcat-data"):
    print("Downloading dog/cat dataset...")
    subprocess.check_output("curl https://storage.googleapis.com/wandb-production.appspot.com/qualcomm/dogcat-data.tgz | tar xvz", shell=True)
    subprocess.check_output("rm ../dogcat-data/train/dog/._dog* ../dogcat-data/train/cat/._cat* ../dogcat-data/validation/cat/._cat* ../dogcat-data/validation/dog/._dog*", shell=True)