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