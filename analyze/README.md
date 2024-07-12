# Summary

Below is the payload files. I crawled theirs contents by querying the urls I found. 
One thing to note here is I crawled them 1 week after my wallet was hacked. So these may be the new version.

Only `payload_1 (1).py` is from my local laptop. It was originally `~/.n2/pay`.

# payload_original.js

This is the entry file of everything. It was obfuscated. This file is the original one, but prettified.

It was tucked way below the regular-looking codes in this file: `/dice_front-end_user/authentication/middlewares/helpers/error.js`.
You must scroll down to spot the malicious codes.

# payload_after_deobfuscated.js

The original file was deobfuscated with: https://obf-io.deobfuscate.io/

# payload_1.py

This file was fetched by `payload.js` from http://95.164.17.24:1224/client/5346

# payload_1 (1).py

This file was fetched by `payload.js` from http://95.164.17.24:1224/client/5346

# payload_2.py

This file was fetched by `payload_1.py` from http://95.164.17.24:1224/payload/5346/root

# payload_3.py

This file was fetched by `payload_2.py` from http://95.164.17.24:1224/brow/5346/root
