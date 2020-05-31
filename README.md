# SpaceChallenge_Server

### Getting started
`python -m venv venv`

`source venv/bin/activate`

`python run.py`

#### Requests

##### Add infected hashes into the database
Request:

`url = host:port/insert_contacts`
```
request type = POST
key = hashes
value = {"data": ["hash1", "hash2", ...]}
```

Response:
```
{
    "response": bool
}
```


##### Find hashes in the database
Request:

`url = host:port/check_contacts`
```
request type = POST
key = hashes
value = {"data": ["hash1", "hash2", ...]}
```

Response:
In case of recent interaction (less them two weeks ago)
```
{
    "response": "High risk"
}
```

In case of long-ago interaction (more then two weeks ago)
```
{
    "response": "Low risk"
}
```

In case of zero interactions with infected people.
```
{
    "response": "No risk"
}
```
