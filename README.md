# Blockchain Sonar's Explorer Backend
## Quick Start
* Launch backend
```shell
python3.10 -m venv .venv
source .venv/bin/activate
pip install --requirement requirements-dev.txt
FLASK_APP=blockchain_sonar_backend python -m flask run
```
* In a browser, open [http://127.0.0.1:5000/webapp/](http://127.0.0.1:5000/webapp/)

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


## Explorer API

### Addresses

#### Fetch address info

Path: `/v1/address/<address>`

```
curl --verbose --request GET --header 'Accept: application/json' http://127.0.0.1:5000/explorer/v1/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e
curl --verbose --request GET --header 'Accept: application/json' http://127.0.0.1:5000/explorer/v1/address/DQvuJB3eHEUmdB2wi2K9B6Vdimq9DNJU7Z
```
