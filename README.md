# pelican-fancybox

`Fancybox` plugin for `Pelican`.

The default theme does not include fancybox, but it is pretty easy to add one (on base.html):

```
{{ fancybox }}
```

## Usage

Enable the plugin in your pelicanconf.py:

```python
PLUGINS = [
	.....,
	'fancybox',
	......,
	]
```

## Settings

Example settings:

```python
FANCYBOX_SETTINGS = {
    'helpers':  {
        'thumbs' : {
            'width': 50,
            'height': 50
        }
    }
}
```

For more information about settings you can read [here](http://fancyapps.com/fancybox/#docs).