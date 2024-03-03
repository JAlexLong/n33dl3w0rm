from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

console_scripts = '''
[console_scripts]
n33dl3w0rm=n33dl3w0rm:main
'''

setup(
    name = 'n33dl3w0rm',
    version = '0.1.0',
    author = 'J. Alex Long',
    license = 'GPLv3',
    description = 'An experimental malware library.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/JAlexLong/n33dl3w0rm',
    py_modules = ['n33dl3w0rm'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points=console_scripts,
)