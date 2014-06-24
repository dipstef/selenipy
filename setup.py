from distutils.core import setup

VERSION = '0.1'

desc = """Wrapper for selenium drivers using the interfaces defined in the httpy_client module"""

name = 'selenipy'

setup(name=name,
      version=VERSION,
      author='Stefano Dipierro',
      author_email='dipstef@github.com',
      url='http://github.com/dipstef/{}/'.format(name),
      description=desc,
      packages=['httpy_client.selenium'],
      requires=['selenium', 'httpy'],
      platforms=['Any']
)
