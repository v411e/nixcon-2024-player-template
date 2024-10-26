from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
  name='garnixapi',
  #packages=['someprogram'],
  version='0.0.1',
  #author='...',
  #description='...',
  install_requires=install_requires,
  scripts=[
    'main.py',
  ],
  entry_points={
    # example: file some_module.py -> function main
    'console_scripts': ['garnixapi=garnixapi:main']
  },
)