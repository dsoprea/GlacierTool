import setuptools
import os.path

import gt

app_path = os.path.dirname(gt.__file__)

with open(os.path.join(app_path, 'resources', 'README.rst')) as f:
      long_description = f.read()

with open(os.path.join(app_path, 'resources', 'requirements.txt')) as f:
      install_requires = list(map(lambda s: s.strip(), f.readlines()))

setuptools.setup(
      name='glacier_tool',
      version=gt.__version__,
      description="Do concurrent, multipart uploads of massive archives to Amazon Glacier.",
      long_description=long_description,
      classifiers=[],
      keywords='glacier concurrent',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/GlacierTool',
      license='GPL 2',
      packages=setuptools.find_packages(exclude=['dev']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      package_data={
          'gt': [
            'resources/README.rst',
            'resources/requirements.txt',
            'resources/scripts/*',
          ],
      },
      scripts=[
          'gt/resources/scripts/gt_upload_large',
      ],
)
