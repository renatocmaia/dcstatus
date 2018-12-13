from setuptools import setup


setup(name="dcstatus",
     packages=[],
     license="MIT",
     install_requires=["Flask", "gunicorn", "PyYAML", "f5-sdk", "f5-icontrol-rest"],
     version='0.1',
     description='',
     author='Renato Maia',
     author_email='renatocsmaia@gmail.com',
     url='https://github.com/stone-payments/dcstatus',
     zip_safe=False)
