from setuptools import setup

setup(name='broccoli',
      version='0.2',
      description='Bro Communication Library',
      url='http://github.com/tschan/broccoli-package',
      author='tschan',
      author_email='tschan@bla.de',
      license='MIT',
      packages=['broccoli'],
      zip_safe=False,
      package_data={
        'broccoli': ['_broccoli_intern.so', 'libbroccoli.a', 'libbroccoli.so.5']
      })