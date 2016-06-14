# coding: utf-8
from pelican import signals
from os import path
import shutil

def initialized(pelican):
    from pelican.settings import DEFAULT_CONFIG
    DEFAULT_CONFIG.setdefault('FANCYBOX_ENABLED', True)
    if pelican:
        pelican.settings.setdefault('FANCYBOX_ENABLED', True)

def fancybox(generator):
	generator.fancybox = '<script type=\"text/javascript\" src=\"//code.jquery.com/jquery-latest.min.js\">'
	generator.fancybox += '</script>'
	generator.fancybox += '<script type="text/javascript" src="/fancybox/lib/jquery.mousewheel-3.0.6.pack.js">'
	generator.fancybox += '</script>'
	generator.fancybox += '<link rel="stylesheet" href="/fancybox/source/jquery.fancybox.css?v=2.1.5" type="text/css" media="screen" />'
	generator.fancybox += '<script type="text/javascript" src="/fancybox/source/jquery.fancybox.pack.js?v=2.1.5">'
	generator.fancybox += '</script>'
	generator.fancybox += '<link rel="stylesheet" href="/fancybox/source/helpers/jquery.fancybox-buttons.css?v=1.0.5" type="text/css" media="screen" />'
	generator.fancybox += '<script type="text/javascript" src="/fancybox/source/helpers/jquery.fancybox-buttons.js?v=1.0.5">'
	generator.fancybox += '</script>'
	generator.fancybox += '<script type="text/javascript" src="/fancybox/source/helpers/jquery.fancybox-media.js?v=1.0.6">'
	generator.fancybox += '</script>'
	generator.fancybox += '<link rel="stylesheet" href="/fancybox/source/helpers/jquery.fancybox-thumbs.css?v=1.0.7" type="text/css" media="screen" />'
	generator.fancybox += '<script type="text/javascript" src="/fancybox/source/helpers/jquery.fancybox-thumbs.js?v=1.0.7">'
	generator.fancybox += '</script>'
	generator.fancybox += '<script type="text/javascript" src="/js/fancybox.js">'
	generator.fancybox += '</script>'
	generator.fancybox += '<script>'
	generator.fancybox += '$( document ).ready(function(){activate_fancybox();$(".fancybox").fancybox();});'
	generator.fancybox += '</script>'
	generator.fancybox += '<link rel="stylesheet" href="/css/fancybox.css" type="text/css"/>'	
	generator._update_context(['fancybox'])


def copy(pelican, writer):
	cp_js(pelican, writer)
	cp_css(pelican, writer)

def cp_css(pelican, writer):
	src = path.join(path.dirname(__file__), "static", "css")
	dest = path.join(pelican.settings['OUTPUT_PATH'], 'css')
	try:
		shutil.rmtree(dest)
	except OSError:
		pass
	try:
		shutil.copytree(src, dest)
	except OSError:
		error('''Copy "%s" to "%s" does not work.''' % (
			src, dest
		))

def cp_js(pelican, writer):
    src = path.join(path.dirname(__file__), "static", "js")
    dest = path.join(pelican.settings['OUTPUT_PATH'], 'js')
    try:
        shutil.rmtree(dest)
    except OSError:
        pass
    try:
        shutil.copytree(src, dest)
    except OSError:
        error('''Copy "%s" to "%s" does not work.''' % (
            src, dest
        ))

def register():
    signals.initialized.connect(initialized)
    signals.article_generator_finalized.connect(fancybox)
    signals.article_writer_finalized.connect(copy)