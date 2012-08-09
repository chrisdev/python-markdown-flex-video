A Responsive Video Extension for Python-Markdown
===============================================
Supports the responsive embedding of web videos URLs (currently only YouTube and Vimeo? are supported) using 
the flex-video method.  Flex-video provides an
 intrinsic ratio that will properly scale your video on any device.  Currently
**div.flex-video** is supported by zurb.foundation but you can use the included CSS
with other frameworks such as twitter-bootstrap. 
Currently, if  the URL to an youtube video is
found in the markdown text submitted it isn't enclosed in parenthesis then the URL will be swapped with a embedded
youtube video. 

Contributors
-------------
- `Christopher Clarke <https://github.com/chrisdev>`_
- `Lendl Smith <https://github.com/ilendl2>`_

Install
-----------
Create a virtual environment for your project and activate it::

    $ virtualenv mysite-env
    $ source mysite-env/bin/activate
    (mysite-env)$ pip install Markdown
    (mysite-env)$ pip install git+git://github.com/chrisdev/python-markdown-flex-video
    
    
Usage
------

::
    >>> import markdown    
    >>> txt = "http://www.youtube.com/watch?v=E88d4e1gYh0&feature=g-logo-xit"
    >>> print markdown.markdown(txt, ['video'])
    <p>
    <div class="flex-video">
    <iframe frameborder="0" height="315" src="http://www.youtube.com/v/E88d4e1gYh0&amp;feature=g-logo-xit" width="420"></iframe>
    </div>
    </p>
     
    

