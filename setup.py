from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'viihdexdash',
    description = 'Command line tool for downloading Elisa Viihde DASH streams with FFmpeg',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/Qotscha/viihdexdl',
    author = 'Qotscha',
    version = '0.2.0',
    packages = ['viihdexdash'],
    package_dir = {'viihdexdash': 'src'},
    install_requires = [
        'requests',
        'langcodes',
        'pycaption'
        ],
    entry_points = {
        'console_scripts': [
            'viihdexdash = viihdexdash.__main__:main'
            ]
        },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'
        ]
    )
