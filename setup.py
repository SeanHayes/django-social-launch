#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import django_social_launch

package_name = 'django_social_launch'
test_package_name = '%s_test_project' % package_name

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
	packages=[
		'django_social_launch',
		'django_social_launch_test_project',
	],
	include_package_data=True,
	install_requires=['Django>=1.4', 'django-pagination',],
	test_suite = '%s.runtests.runtests' % test_package_name,
)

