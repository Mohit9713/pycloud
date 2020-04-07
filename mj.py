#python3
import os

import subprocess

a=subprocess.Popen(["stat","."], stdout=subprocess.PIPE)
o,err=a.communicate()
print (o)

mydict={"tried":"Hey"}
print (mydict)

