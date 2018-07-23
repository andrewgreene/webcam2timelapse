import os
import os.path
import datetime
import shutil

rightNow = datetime.datetime.now()
yesterday = rightNow - datetime.timedelta(days=1)
yesterdayString = yesterday.strftime("%y%m%d")
path = "/path/to/directory/" + yesterdayString + "/*.jpg"
filename = yesterdayString + ".mp4"
output = "/path/to/output/" + filename

command = "cd /c; /path/to/ffmpeg -framerate 30 -pattern_type glob -i '" + path + "' -c:v libx264 -p ix_fmt yuv420p " + output

os.system(command)

deleteCommand = "rm -rf /path/to/directory/" + yesterdayString

os.system(deleteCommand)

shutil.rmtree(path)
