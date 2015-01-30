#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import django_social_launch

package_name = 'django_social_launch'
test_package_name = '%s_test_project' % package_name

EXCLUDE_FROM_PACKAGES = ['%s*' % test_package_name]

def runtests():
    import os
    import sys
    
    import django
    from django.core.management import call_command
    
    os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % test_package_name
    django.setup()
    call_command('test')
    sys.exit()

setup(name='django-social-launch',
    version=django_social_launch.__version__,
    description="Social sign up page for Django.",
    author='Seán Hayes',
    author_email='sean@seanhayes.name',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords='django social sign up referrer',
    url='http://seanhayes.name/',
    download_url='https://github.com/SeanHayes/django-social-launch',
    license='GPL',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    install_requires=['Django>=1.7', 'python-social-auth',],
    test_suite='setup.runtests',
)

