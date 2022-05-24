# KAD

`Keys as Dots` is a simple Python package that allows usage of dots in place of dictionary keys.

# Usage

```python
import kad

dictionary = {'a': 5, 'b': True}

kad_object = kad.to_kad(dictionary)

assert(kad_object.b)
assert(kad_object.a == 5)
```
