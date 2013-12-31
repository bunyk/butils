butils
======

This is package of my python utils useful in debugging or for performing other tasks.

Installation
------------

```
pip install https://github.com/bunyk/butils/archive/master.zip
```


Contents
--------

- `butils.config_parser.config_to_dict(filename)` - read config file and return it content as dictionary of dictionaries.
- `butils.whereis(object)` - return location of object in code. 
- `butils.from_where_called()` - returns location in code from where function which calles this is called
- `butils.add_watched_attribute(name, watch_get=False)` - when called in class (for example `add_watched_attribute('name')`) - instances of that class will log every change to the attribute. And log every access if `watch_get` is `True`.
- `butils.watch_for_output(condition=lambda x: True, stream='stdout')` - log location in code where some output is performed.
