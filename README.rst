A Responsive Video Extension for Python-Markdown
===============================================
Supports the responsive embedding of web videos URLs (currently only YouTube and Vimeo are supported) using 
the ``flex-video`` technique.  Flex-video provides an intrinsic ratio that will properly scale 
the video on any device.  
The ``flex-video`` method is supported by `Zurb Foundation`_  but you can use the flex-video CSS from Foundation 
with other UI frameworks such as twitter-bootstrap. 

Note, there is no need to use the Markdown link synthax you can just paste in the YouTube or Vimeo URL. 

.. _`Zurb Foundation` : http://foundation.zurb.com
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

    >>> import markdown    
    >>> txt = "http://www.youtube.com/watch?v=E88d4e1gYh0&feature=g-logo-xit"
    >>> print markdown.markdown(txt, ['flex_video'])
    <p>
    <div class="flex-video">
    <iframe frameborder="0" height="315" src="http://www.youtube.com/v/E88d4e1gYh0&amp;feature=g-logo-xit" width="420"></iframe>
    </div>
    </p>
     
    

