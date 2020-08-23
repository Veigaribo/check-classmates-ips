# ipcheck.py

`ipcheck.py` is a Python 2 script designed to scan a range of IPv4 addresses looking for possible TCP connections.

The script assumes the connections will be stablished in 0.01s or less.

### Options

The script accepts the following argument options:

- `-bip <base-ip>`: Specify the first 3 octets of the IP address, like "1.2.3". The given string may or may not end with a dot. The default value is "192.168.0"
- `-port <port>`: The port where the connection will be attempted, like "443". The default value is "80"
- `--details` or `-d`: Make it so more information is printed out.
