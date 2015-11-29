Example Zengine Project for the GDGIzmir

Set the SERVER variable in the settings.py for Riak & Redis server IP's

Create a bucket named "gdg" in the Riak.

riak-admin bucket-type create gdg '{"props":{"last_write_wins":true, "allow_mult":false, "n_val": 1}}'

riak-admin bucket-type activate gdg

Use http://dev.zetaops.io/?backendurl=http://127.0.0.1:9001/ as the frontend
