from setuptools import setup, find_packages

setup(
    name='pygist',
    version='0.3',
    description='Easy to use interface for github\'s gists.',
    url='http://github.com/kanales/pygist',
    author='Iván Canales',
    license='MIT',
    packages=find_packages(),
    scripts=['bin/pygist'],
    zip_safe=False,
    install_requires=[
        'click>=6.7',
        'requests>=2.18',
    ],
    keywords="click gist github share code",
)

