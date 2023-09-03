# xpost-update

Create a post on x.com (Twitter) and update this post by deleting the old one and create a updated one.

## Usage

### Create new post and update this post again

Create new post:

`docker run -e SECRETS_FILE=secrets.json --volume ./secrets.json:/secrets.json --volume ./data:/data xpost-update "this is a post"`

Update this post again:

`docker run -e SECRETS_FILE=secrets.json --volume ./secrets.json:/secrets.json --volume ./data:/data xpost-update "this is a post edited"`

secrets.json looks like:

```
{
  "consumer_key": "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890",
  "consumer_secret": "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890",
  "access_token": "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890",
  "access_token_secret": "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890"
}
```

### Update existing post with known POST ID again

If you start xpost-update for the first time and want to update an existing post set the POST_ID as environment variable:

`docker run -e POST_ID=123123123123 -e SECRETS_FILE=secrets.json --volume ./secrets.json:/secrets.json --volume ./data:/data xpost-update "this is a post edited again"`

If xpost-update has a persistent volume on /data, it will save the new post id in /data/lastpost_id. When you start xpost-update again, it will use this saved post id instead of the POST_ID given.

### pass all needed parameters as environment variables

`docker run -e POST_TEST="this is a post" -e CONSUMER_KEY=123 -e CONSUMER_SECRET=123 -e ACCESS_TOKEN=123 -e ACCESS_TOKEN_SECRET=123 --volume ./data:/data xpost-update`

### use docker swarm, docker secrets and swarm-cronjob to start container regularly

Add docker secret with your secret.json:

```
docker secret create xpost-update-secrets secrets.jsons
```

Add swarm-cronjob as new service:

```
version: "3.8"
services:
  swarm-cronjob:
    image: crazymax/swarm-cronjob
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    environment:
      - "TZ=Europe/Berlin"
      - "LOG_LEVEL=info"
      - "LOG_JSON=false"
    deploy:
      placement:
        constraints:
          - node.role == manager
```

Add new stack for xpost-update:

```
version: "3.8"

services:
  xpost-update:
    image: bkendinibilir/xpost-update
    deploy:
      mode: replicated
      replicas: 0
      labels:
        - "swarm.cronjob.enable=true"
        - "swarm.cronjob.schedule=${CRON_SCHEDULE}"
        - "swarm.cronjob.skip-running=false"
      restart_policy:
        condition: none
    environment:
      - SECRETS_FILE=/run/secrets/xpost-update-secrets
      - POST_TEXT=${POST_TEXT}
    volumes:
      - xpost-update_data:/data
    secrets:
      - xpost-update-secrets

volumes:
  xpost-update_data:

secrets:
  xpost-update-secrets:
    external: true
```

Replace ${CRON_SCHEDULE} with "0 15 \* \* \*" to start it daily at 3 pm and ${POST_TEXT} with your post text.
