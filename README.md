# Asynchronous Lichess Python SDK

This package is meant to be an unofficial Python API Client for lichees.org.  
For information about the API please refer to https://lichess.org/api  
Every API endpoint uses async Python methods (asyncio).

# Dependencies
To use this package you need to install all of the dependencies located under `requirements.txt`.  
```bash
pip install requirements.txt
```
Supported python versions: `python >= 3.6`
# How to build
Building script is located under `build.sh`.  
Steps:  
```bash
sh build.sh
pip install -U .
```

# Implemented Lichess Endpoints
* account
* boards
* bots
* broadcast
* challenges
* games
* messages
* relations
* simulations
* studies
* teams
* tournaments
* users

# Sample usage
### Client initialization
```python
from lichess_client import APIClient

client = APIClient(token="lichess_account_token")
```
  
### Call an endpoint
```python

response = await client.account.get_my_profile()
print(response)

{'metadata': 
    {'method': <RequestMethods.GET: 'GET'>, 
     'url': 'https://lichess.org/api/account/kid', 
     'content_type': 'application/json', 
     'timestamp': b'Fri, 13 Mar 2020 19:05:27 GMT'}, 
 'entity': 
    {'code': 200, 
     'reason': 'OK', 
     'status': <StatusTypes.SUCCESS: 'success'>, 
     'content': {'kid': False}
     }
}
```

### Access to the response properties
```python

print(response.metadata.timestamp)
b'Fri, 13 Mar 2020 19:11:32 GMT'

print(response.entity.content)
{'kid': False}
```
