from distutils.core import setup
setup(
  name = 'chartsfigures',
  packages = ['chartsfigures'],
  version = '0.02',
  license='MIT',
  description = 'Social Science data analysis',
  author = 'Daniel He',
  author_email = 'danielhe2024@u.northwestern.edu',
  url = 'https://github.com/danielhe-chartsfigures/chartsfigures',
  download_url = 'https://github.com/danielhe-chartsfigures/chartsfigures',
  keywords = ['charts', 'figures', 'social science'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)