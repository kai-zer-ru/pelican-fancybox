# pelican-fancybox

Плагин для активации `Fancybox` в блогах на основе `Pelican`.

## Настройка

```python
PLUGINS = [
	'fancybox'
	]
```

И после этого добавить в макет `base.html` перед закрывающимся тегом `</body>` `{{fancybox}}`.
