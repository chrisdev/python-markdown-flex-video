#!/usr/bin/env python

"""
Supports the responsive embedding of web videos URLs (currently YouTube and Vimeo are supported) using 
the flex-video method.  Flex-video provides an
 intrinsic ratio that will properly scale your video on any device.  Currently
**div.flex-video** is supported by zurb.foundation but you can use the included CSS
with other frameworks such as twitter-bootstrap. 
Any For instance, if a URL to an youtube video is
found in the text submitted to markdown and it isn't enclosed in parenthesis
like a normal link in markdown, then the URL will be swapped with a embedded
youtube video. 


>>> import markdown


Test Youtube

>>> s = "http://www.youtube.com/watch?v=E88d4e1gYh0&feature=g-logo-xit"
>>> markdown.markdown(s, ['flex_video']) #doctest: +NORMALIZE_WHITESPACE
    u'<p>\\n<div class="flex-video">\\n<iframe frameborder="0" height="315" src="http://www.youtube.com/v/E88d4e1gYh0&amp;feature=g-logo-xit" width="420"></iframe>\\n</div>\\n</p>'

>>> markdown.markdown(s, ['flex_video(orientation=widescreen)']) #doctest: +NORMALIZE_WHITESPACE
    u'<p>\\n<div class="flex-video">\\n<iframe frameborder="0" height="315" src="http://www.youtube.com/v/E88d4e1gYh0&amp;feature=g-logo-xit" width="560"></iframe>\\n</div>\\n</p>'
        
"""

import markdown

try:
    from markdown.util import etree
except:    
    from markdown import etree

version = "0.0.1"

class VideoExtension(markdown.Extension):
    def __init__(self, configs): 
        self.config = {
            'orientation':['Normal','screen orientation widescreen or None'],
            'provider':['YouTube','Provider youtube or vimeo']

        }

        # Override defaults with user settings
        for key, value in configs:
            self.setConfig(key, value)

    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(md, 'vimeo', Vimeo,
            r'([^(]|^)http://(www.|)vimeo\.com/(?P<vimeoid>\d+)\S*')
        self.add_inline(md, 'youtube', Youtube,
            r'([^(]|^)http://www\.youtube\.com/watch\?\S*v=(?P<youtubeargs>[A-Za-z0-9_&=-]+)\S*')

class Vimeo(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com' % m.group('vimeoid')
        width = self.ext.config['vimeo_width'][0]
        height = self.ext.config['vimeo_height'][0]
        return flex_video(url, width, height)


class Youtube(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.youtube.com/v/%s' % m.group('youtubeargs')
        orientation=self.ext.config['orientation'][0]
        provider=self.ext.config['provider'][0]
        if provider.lower() == 'youtube':
            if orientation.lower() == 'widescreen':
                width = "560"
                height = "315"
            else:
                width = "420"
                height = "315"  
        else:
            width="560"
            height="225"
                
        return flex_video(url, width, height)
    
def flex_video(url,width,height):
    """
    <div class="flex-video">
     <iframe width="420" height="315" src="http://www.youtube.com/embed/9otNWTHOJi8" frameborder="0" allowfullscreen></iframe>
   </div>    
    """
    obj=etree.Element('div')
    obj.set('class',"flex-video")
    iframe=etree.Element('iframe')
    iframe.set('width',width)
    iframe.set('height',height)
    iframe.set('src',url)
    iframe.set('frameborder',"0")
    obj.append(iframe)
    return obj
    

def makeExtension(configs=None) :
    return VideoExtension(configs=configs)

   