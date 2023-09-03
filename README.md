# xpost-update

Create a post on x.com (Twitter) and update this post again.

## usage

### create new post and update this post again

docker run -e SECRETS_FILE=secrets.json --volume ./secrets.json:/secrets.json --volume ./data:/data xpost-update "this is a post"

docker run -e SECRETS_FILE=secrets.json --volume ./secrets.json:/secrets.json --volume ./data:/data xpost-update "this is a post edited"

### update existing post with known POST ID again

docker run -e POST_ID=123123123123 -e SECRETS_FILE=secrets.json --volume ./secrets.json:/secrets.json --volume ./data:/data xpost-update "this is a post edited again"

### pass all paramets as environment variables

docker run -e POST_TEST="this is a post" -e CONSUMER_KEY=123 -e CONSUMER_SECRET=123 -e ACCESS_TOKEN=123 -e ACCESS_TOKEN_SECRET=123 --volume ./data:/data xpost-update
