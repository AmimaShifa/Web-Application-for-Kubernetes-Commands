  
#!/usr/bin/python3

import cgi
import subprocess

print("content: text/html")
print()

f = cgi.FieldStorage()

query = f.getvalue("x")

if "show pods" in query:
    cmd = "kubectl get pods --kubeconfig admin.conf"
    o=sp.getoutput(cmd)
    print(o)

elif "show deployment" in query:
    cmd = "kubectl get deployments --kubeconfig admin.conf"
    o = sp.getoutput(cmd)
    print(o)
