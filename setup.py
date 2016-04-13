from setuptools import setup

setup(name='epitran',
      version='0.0',
      description='Tools for transcribing languages written with Latin script to IPA, complementary to Unitran.',
      url='http://www.davidmortensen.org/epitran',
      author='David R. Mortensen',
      author_email='dmortens@cs.cmu.edu',
      license='MIT',
      install_requires=['setuptools',
                        'unicodecsv',
                        'regex'],
      scripts=['epitran/bin/epitranscribe.py'],
      packages=['epitran'],
      package_dir={'epitran': 'epitran'},
      package_data={'epitran': ['data/*.csv']},
      zip_safe=True
      )
