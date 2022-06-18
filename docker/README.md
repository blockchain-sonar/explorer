
### Build
```shell
docker build --tag  ghcr.io/blockchain-sonar/explorer/snapshot \
    --file docker/Dockerfile .
```

### Run

```shell
export BSE_MONGO_URL=mongodb+srv://<user>:<password>@<host>:<port>/<database>
docker run --rm --interactive --tty \
    --env BSE_MONGO_URL \
    --publish 8080:8080 \
     ghcr.io/blockchain-sonar/explorer/snapshot
```

### Debug

```shell
docker run --rm --interactive --tty \
    --entrypoint /bin/sh \
     ghcr.io/blockchain-sonar/explorer/snapshot
```
