from setuptools import setup

setup(name='epitran',
      version='0.0',
      description='Tools for transcribing languages into IPA.',
      url='http://www.davidmortensen.org/epitran',
      author='David R. Mortensen',
      author_email='dmortens@cs.cmu.edu',
      license='MIT',
      install_requires=['setuptools',
                        'unicodecsv',
                        'regex',
                        'panphon>=0.3'],
      scripts=['epitran/bin/epitranscribe.py',
               'epitran/bin/detectcaps.py',
               'epitran/bin/word2pfvectors.py',
               'epitran/bin/connl2ipaspace.py',
               'epitran/bin/testvectorgen.py'],
      packages=['epitran'],
      package_dir={'epitran': 'epitran'},
      package_data={'epitran': ['data/*.csv', 'data/*.json']},
      zip_safe=True
      )
