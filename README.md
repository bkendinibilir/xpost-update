# xpost-update

Create a post on x.com (Twitter) and update this post again.

## usage

### create new post and update this post again

create new post:

`docker run -e SECRETS_FILE=secrets.json --volume ./secrets.json:/secrets.json --volume ./data:/data xpost-update "this is a post"`

update this post again:

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

### update existing post with known POST ID again

if you start xpost-update for the first time and want to update an existing post set the POST_ID as environment variable:

`docker run -e POST_ID=123123123123 -e SECRETS_FILE=secrets.json --volume ./secrets.json:/secrets.json --volume ./data:/data xpost-update "this is a post edited again"`

### pass all needed parameters as environment variables

`docker run -e POST_TEST="this is a post" -e CONSUMER_KEY=123 -e CONSUMER_SECRET=123 -e ACCESS_TOKEN=123 -e ACCESS_TOKEN_SECRET=123 --volume ./data:/data xpost-update`
