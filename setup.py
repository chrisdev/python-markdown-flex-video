from distutils.core import setup

setup(name='mdx_flex_video',
    version="0.0.2",
    description="Markdown 2.2 extension for responsive video embedding using flex-video as supported by zurb-foundation",
    author="Chris Clarke",
    author_email="cclarke@chrisdev.com",
    url="http://code.tylerlesmann.com/mdx_video2",
    py_modules = ["mdx_flex_video"],
    install_requires=[
        "Markdown >= 2.1.1",
    ],  
)
