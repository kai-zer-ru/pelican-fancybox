# pelican-fancybox

Плагин для активации `Fancybox` в блогах на основе `Pelican`.

## Настройка

```python
PLUGINS = [
	'fancybox'
	]
```

После этого в макет `base.html` перед закрывающимся тегом `</body>` вставить тег `{{fancybox}}`.

Насртойка плагина производится с помощью переменной `FANCYBOX_SETTINGS`. 

Более подробно о ключах и значениях для настройки можно почитать [тут](http://fancyapps.com/fancybox/#docs).

Вот пример простой конфигурации:

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