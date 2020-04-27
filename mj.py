#! /usr/bin/python3
import os
import json

import subprocess

a=subprocess.Popen(["stat","."], stdout=subprocess.PIPE)
o,err=a.communicate()
#print (o)

#print ("Test end")

mydict={"tried":"Hey"}
print (json.dumps(mydict))
