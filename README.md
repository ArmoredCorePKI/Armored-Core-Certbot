# Certbot with Armored Core

Certbot is a widely used client program for web domains to interact with a Let's Encrypt CA.
We have implemented the certificate validation function of armored core in Certbot's workflow

## File Structure


- **certbot/acore**: contain most armored core functions for certificate parsing, PUF entry parsing, verification, so on.
- **certbot/trillianclient**: provide the operations of the trillian log server using protobuf(-grpc) API
- **certbot/internal/main.py**: the actual entry point file where we add a `acorefunc` function in Certbot's option.


## Deployment

> make sure that >=Python3.8 environment. we recommend using some python virtual environment.


```bash
`cd project_dir/certbot`

sudo your_virtual_python3_bin main.py certonly --standalone -d mydomain.test --server https://localhost:14000/dir --email you@example.com --agree-tos --no-verify-ssl --http-01-port=5002
```

Now prepare a root terminal to acquire the root certificates for verification.

```bash
curl -k -s -o /etc/letsencrypt/live/mydomain.test/roots.pem https://localhost:15000/roots/0
```

Then switch to the terminal before to perform the validation operation.

(make sure first edit the `BASEINDEX` in `trillianclient/tclient_util.pp` as the AppendEntry `treesize - 4`, we will improve this workflow later :-) )

```bash

sudo your_virtual_python3_bin main.py main.py acorefunc --verify-puf-cert --test-domain mydomain.test
```

The whole procedure can see the how-to-run
