from distutils.core import setup

VERSION = '0.1'

desc = """l client implementation using selnium drivers."""

name = 'httpy_client'

setup(name=name,
      version=VERSION,
      author='Stefano Dipierro',
      author_email='dipstef@github.com',
      url='http://github.com/dipstef/{}/'.format(name),
      description=desc,
      packages = ['httpy.client.selenium'],
      requires=['selenium', 'httpy', 'httpy_client'],
      platforms=['Any']
)
