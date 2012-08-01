#!/usr/bin/env python

"""
Embeds web videos using URLs.  For instance, if a URL to an youtube video is
found in the text submitted to markdown and it isn't enclosed in parenthesis
like a normal link in markdown, then the URL will be swapped with a embedded
youtube video.

All resulting HTML is XHTML Strict compatible.

>>> import markdown


Test Youtube

>>> s = "http://www.youtube.com/watch?v=u1mA-0w8XPo&hd=1&fs=1&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" height="344" type="application/x-shockwave-flash" width="425"><param name="movie" value="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" /><param name="allowFullScreen" value="true" /></object></p>'


Test Youtube with argument

>>> markdown.markdown(s, ['video(youtube_width=200,youtube_height=100)'])
u'<p><object data="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" height="100" type="application/x-shockwave-flash" width="200"><param name="movie" value="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" /><param name="allowFullScreen" value="true" /></object></p>'


Test Youtube Link

>>> s = "[Youtube link](http://www.youtube.com/watch?v=u1mA-0w8XPo&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1)"
>>> markdown.markdown(s, ['video'])
u'<p><a href="http://www.youtube.com/watch?v=u1mA-0w8XPo&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1">Youtube link</a></p>'


Test Vimeo Video

>>> s = "http://www.vimeo.com/1496152"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com" height="321" type="application/x-shockwave-flash" width="400"><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com" /><param name="allowFullScreen" value="true" /></object></p>'

Test Vimeo Video with some GET values

>>> s = "http://vimeo.com/1496152?test=test"
>>> markdown.markdown(s, ['video'])
u'<p><object data="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com" height="321" type="application/x-shockwave-flash" width="400"><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com" /><param name="allowFullScreen" value="true" /></object></p>'

"""

import markdown

try:
    from markdown.util import etree
except:    
    from markdown import etree

version = "0.0.1"

class VideoExtension(markdown.Extension):
    def __init__(self, configs):
        #markdown.markdown(s, ['video(youtube_width=200,youtube_height=100)'])
        #video(provider=youtube,format=widescreen)
        #self.config = {
            #'bliptv_width': ['480', 'Width for Blip.tv videos'],
            #'bliptv_height': ['300', 'Height for Blip.tv videos'],
            #'dailymotion_width': ['480', 'Width for Dailymotion videos'],
            #'dailymotion_height': ['405', 'Height for Dailymotion videos'],
            #'gametrailers_width': ['480', 'Width for Gametrailers videos'],
            #'gametrailers_height': ['392', 'Height for Gametrailers videos'],
            #'metacafe_width': ['498', 'Width for Metacafe videos'],
            #'metacafe_height': ['423', 'Height for Metacafe videos'],
            #'veoh_width': ['410', 'Width for Veoh videos'],
            #'veoh_height': ['341', 'Height for Veoh videos'],
            #'vimeo_width': ['400', 'Width for Vimeo videos'],
            #'vimeo_height': ['321', 'Height for Vimeo videos'],
            #'yahoo_width': ['512', 'Width for Yahoo! videos'],
            #'yahoo_height': ['322', 'Height for Yahoo! videos'],
            #'youtube_width': ['425', 'Width for Youtube videos'],
            #'youtube_height': ['344', 'Height for Youtube videos'],
        #}
        
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
        #self.add_inline(md, 'bliptv', Bliptv,
            #r'([^(]|^)http://(\w+\.|)blip.tv/file/get/(?P<bliptvfile>\S+.flv)')
        #self.add_inline(md, 'dailymotion', Dailymotion,
            #r'([^(]|^)http://www\.dailymotion\.com/(?P<dailymotionid>\S+)')
        #self.add_inline(md, 'gametrailers', Gametrailers,
            #r'([^(]|^)http://www.gametrailers.com/video/[a-z0-9-]+/(?P<gametrailersid>\d+)')
        #self.add_inline(md, 'metacafe', Metacafe,
            #r'([^(]|^)http://www\.metacafe\.com/watch/(?P<metacafeid>\S+)/')
        #self.add_inline(md, 'veoh', Veoh,
            #r'([^(]|^)http://www\.veoh\.com/\S*(#watch%3D|watch/)(?P<veohid>\w+)')
        self.add_inline(md, 'vimeo', Vimeo,
            r'([^(]|^)http://(www.|)vimeo\.com/(?P<vimeoid>\d+)\S*')
        #self.add_inline(md, 'yahoo', Yahoo,
            #r'([^(]|^)http://video\.yahoo\.com/watch/(?P<yahoovid>\d+)/(?P<yahooid>\d+)')
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
    
def flash_object(url, width, height):
    """
     <object data="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" height="344" type="application/x-shockwave-flash" width="425"><param name="movie" value="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" /><param name="allowFullScreen" value="true" /></object></p>'
    """
    obj = etree.Element('object')
    obj.set('type', 'application/x-shockwave-flash')
    obj.set('width', width)
    obj.set('height', height)
    obj.set('data', url)
    param = markdown.etree.Element('param')
    param.set('name', 'movie')
    param.set('value', url)
    obj.append(param)
    param = markdown.etree.Element('param')
    param.set('name', 'allowFullScreen')
    param.set('value', 'true')
    obj.append(param)
    #param = markdown.etree.Element('param')
    #param.set('name', 'allowScriptAccess')
    #param.set('value', 'sameDomain')
    #obj.append(param)
    return obj

def makeExtension(configs=None) :
    return VideoExtension(configs=configs)

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    s = "http://www.youtube.com/watch?v=u1mA-0w8XPo&hd=1&fs=1&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1"
    print markdown.markdown(s, ['flex_video'])    
    
