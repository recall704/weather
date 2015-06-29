#encoding:utf-8

from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='weather',
      version=version,
      description="Linux Windows 下的一个天气查询小程序",
      long_description="""方便在终端查询天气的小程序""",
      classifiers=[],
      keywords='python　weather terminal',
      author='recall',
      author_email='tk657309822@gmail.com',
      url='https://github.com/recall704',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      entry_points={
        'console_scripts':[
            'weather = weather.weather:main'
        ]
      },
)