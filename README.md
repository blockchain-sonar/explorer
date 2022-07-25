# Backend of blockchain sonar
## Quick Start
* Launch backend
```shell
python3.10 -m venv .venv
source .venv/bin/activate
pip install --requirement requirements-dev.txt
FLASK_APP=blockchain_sonar_backend python -m flask run
```
* In a browser, open [http://127.0.0.1:5000/explorer](http://127.0.0.1:5000/explorer)

## Run tests

```shell
python3.10 -m unittest -v
```

## Image name convension

| Image Tag Name                                             | Build Configuration  | Build Source                                                                    |
|------------------------------------------------------------|----------------------|---------------------------------------------------------------------------------|
| ghcr.io/blockchain-sonar/explorer                          | release              | latest git tag (same as previous, just copy into production image repository)   |
| ghcr.io/blockchain-sonar/explorer:x.y.z                    | release              | git tag `x.y.z` (same as previous, just copy into production image repository)  |
| ghcr.io/blockchain-sonar/explorer/snapshot                 | snapshot             | latest git tag                                                                  |
| ghcr.io/blockchain-sonar/explorer/snapshot:x.y.z           | snapshot             | git tag `x.y.z`                                                                 |
| ghcr.io/blockchain-sonar/explorer/snapshot:bbbbb.xxxxxxxx  | snapshot             | git branch `bbbbb` on commit `xxxxxxxx` (short sha1)                            |
| ghcr.io/blockchain-sonar/explorer/snapshot:bbbbb           | snapshot             | git branch `bbbbb` on latest commit                                             |
