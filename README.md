# shudder-py

An **unofficial** Python API client for horror streaming service [Shudder](https://www.shudder.com)

## Example code

```python
from shudder.session import ShudderSession

shudder = ShudderSession()
shudder.login()

for feature in shudder.my_list():
    print("%(title)s [%(year)s]" % feature)
    print("%(short)s\n" % feature["description"])
```

Output:

```
Host [2020]
During an online séance, six friends accidentally invite the attention of a demonic presence.

Missions [2017]
The first team to successfully land on Mars are pulled into a supernatural mystery.

```

## API Documentation

The API requires client authentication parameters passed either as parameters to `login()` or as the following environment variables:
* `SHUDDER_EMAIL`
* `SHUDDER_PASSWORD`

### Get "My List"

```python
from shudder.session import ShudderSession

shudder = ShudderSession()
shudder.login()

print(shudder.my_list())
```

### Search for a film or series

```python
from shudder.session import ShudderSession

shudder = ShudderSession()
shudder.login()

shudder.search("it follows")
# [ <Movie [id=..., title=It Follows]>, ... ]
```

### Get reviews for a film or series

```python
from shudder.session import ShudderSession

shudder = ShudderSession()
shudder.login()

film = shudder.search("it follows")[0]

shudder.reviews(film)

# [<shudder.models.Review ... ]
```
