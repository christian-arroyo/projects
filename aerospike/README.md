Module to learn and practice Aerospike

# Basic read and write operations
```
import aerospike
from aerospike import exception as ex
import sys

config = {
    'hosts': [ ('127.0.0.1', 3000)]
}

# Create a client and connect it to the cluster
try:
    client = aerospike.client(config).connect()
    client.truncate('test', "demo", 0)
except ex.ClientError as e:
    print("Error: {0} [{1}]".format(e.msg, e.code))
    sys.exit(1)

# Record key tuple: (namespace, set, key)
keyTuple = ('test', 'demo', 'key')

# Write a record
client.put(keyTuple, {'name': 'John Doe', 'age': 32})

# Read a record
(key, meta, record) = client.get(keyTuple)
```