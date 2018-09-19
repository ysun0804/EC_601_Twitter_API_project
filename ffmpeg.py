import os
import subprocess
path=os.getcwd()

strcmd = "ffmpeg -framerate 1 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p out.mp4"
subprocess.call(strcmd,shell=True)
