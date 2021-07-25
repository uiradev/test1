import re
import subprocess
import os
import shutil
from pathlib import Path

# Configuration
HOME_DIR = str(Path.home())
VISQOL_DIR = HOME_DIR + "/Documents/GitHub/visqol/"
MOS_REGEX = re.compile(r"MOS-LQO:\s*(?P<mos_lqo>[0-9.]+)")

# Based on https://github.com/google/visqol/issues/3
def calculate(reference_file, degraded_file, visqol_dir = VISQOL_DIR, timeout = 60.0):
    visqol_exe = visqol_dir + "bazel-bin/visqol"
    visqol_full_path = shutil.which(visqol_exe, os.X_OK)
    if visqol_full_path is None:
        raise Exception("visql executable not found:" +
                        visqol_exe + "\nGit clone visqol to diretory: " + VISQOL_DIR)

    command_args = [visqol_exe, 
                    "--reference_file", reference_file, 
                    "--degraded_file", degraded_file]

    visqol_output = subprocess.run(
        command_args, timeout=timeout, cwd=visqol_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).stdout.decode("utf-8")

    mos_match = MOS_REGEX.search(visqol_output)
    if mos_match:
        return float(mos_match.group("mos_lqo"))
    else:
        raise Exception(
            "Failed to calculate VISQOL - response does not contain MOS-LQO."
            " Actual response: {}".format(visqol_output)
        )
