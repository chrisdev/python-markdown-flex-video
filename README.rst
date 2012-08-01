Responsive Video Extension for Python-Markdown
===============================================

Wraps and embeds your web videos (currently YouTube and Vimeo) so as to create an 
intrinsic ratio that will properly scale your video on any device.  Currently
**div.flex-video** is currently supported by zurb.foundation but you can use the included CSS
with other frameworks such as twitter-bootstrap.


Contributors
-------------
* `Christopher Clarke <https://github.com/chrisdev>`_
* `Kewsi Aguillera <https://github.com/kaguillera>`_
* `Lendl Smith <https://github.com/ilendl2>`_

Install
-----------
Create a virtual environment for your project and activate it::

    $ virtualenv mysite-env
    $ source mysite-env/bin/activate
    (mysite-env)$
    
Next install Pinax::

    (mysite-env)$ pip install git+git://github.com/chrisdev/python-markdown-flex-video
    
    
Usage
______

::
    >>> import markdown    
    >>> txt = "http://www.youtube.com/watch?v=u1mA-0w8XPo&hd=1&fs=1&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1"
    >>> print markdown.markdown(txt, ['video'])
    <p>
    

