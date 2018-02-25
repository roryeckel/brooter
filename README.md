# brooter
Easy and extensible brute force algorithms and utilities framework for Python

Please use responsibly. I, do not take responsibility for misuse or damages.
This software comes with no warranty. Don't do evil stuff.

Planned features:
+ Session saving (somewhat already implemented)
+ FileGenerator
+ Distributed processing

Concurrent example:
```python
import br00ter

def test_password(password):
    print('testing ' + password)
    return (password, password == '12345')

if __name__ == '__main__':
    with br00ter.FileGenerator('passlist.txt') as x:
    # with br00ter.TableGenerator('12345', 5, 5) as x:
        pool = br00ter.BrutePool(x, test_password)
        pool.start()
        pool.join()
        print(pool.get_positive_results())

```
