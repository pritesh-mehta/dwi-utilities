"""
@author: pritesh-mehta
"""

from setuptools import setup, find_packages

setup(name='dwi_utilities',
      version='1.0',
      description='Diffusion-weighted MRI utilities',
      url='https://github.com/pritesh-mehta/dwi_utilities',
      python_requires='>=3.6',
      author='Pritesh Mehta',
      author_email='pritesh.mehta@kcl.ac.uk',
      license='Apache 2.0',
      zip_safe=False,
      install_requires=[
      'numpy',
      'scipy',
      'pathlib',
      'argparse'
      ],
      entry_points={
        'console_scripts': [
            'adc_map=dwi_utilities.adc_map:process',
            'comp_high_b=dwi_utilities.comp_high_b:process',
            ],
      },
      packages=find_packages(include=['dwi_utilities']),
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
      ]
      )