import os
import subprocess

a=subprocess.Popen(["stat","."], stdout=subprocess.PIPE)
o,err=a.communicate()
print (o)

