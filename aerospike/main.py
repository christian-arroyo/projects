""" Simple example of reading and writing into Aerospike"""

import sys

import aerospike
from aerospike import exception as ex


def main():
    address = "127.0.0.1"   # Aerospike address
    port = 3000             # Aerospike port
    namespace = "test"      # Cluster namespace
    setname = "test_set"         # Set name within namespace
    client = aerospike.client(
        {'hosts': [(address, port)]}
    )

    read_policy = {'total_timeout': 5000}
    write_policy = {'total_timeout': 5000}
    key = (namespace, setname, "bar")
    bins = {'myBin': 'Hello World!'}

    # Write record
    try:
        client.put(key, bins, policy=write_policy)
    except ex.ClientError as e:
        print(e)
    
    # Read record
    try:
        (key_, meta, bins) = client.get(key, policy=read_policy)
        print ('Keys: ', key_)
        print('Metadata: ', meta)
        print('Bins: ', bins)
    except ex.ClientError as e:
        print(e)
        sys.exit(1)
    finally:
        client.close()

if __name__ == '__main__':
    main()
