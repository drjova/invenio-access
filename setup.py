# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio module for common role based access control."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'SQLAlchemy-Continuum>=1.2.1',
    'Werkzeug>=0.11.2',
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.2.2',
    'mock>=1.0.0',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
    'redis>=2.10.3',
]

extras_require = {
    'admin': [
        'invenio-admin>=1.0.0a2',
    ],
    'docs': [
        'Sphinx>=1.4.2',
    ],
    'mysql': [
        'invenio-db[mysql]>=1.0.0b3',
    ],
    'postgresql': [
        'invenio-db[postgresql]>=1.0.0b3',
    ],
    'sqlite': [
        'invenio-db>=1.0.0b3',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name in ('sqlite', 'mysql', 'postgresql'):
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    'Flask>=0.11.1',
    'invenio-accounts>=1.0.0b3',
    'six>=1.10',
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_access', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-access',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio access',
    license='GPLv2',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-access',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'flask.commands': [
            'access = invenio_access.cli:access',
        ],
        'invenio_admin.views': [
            'invenio_access_action_users = '
            'invenio_access.admin:action_users_adminview',
            'invenio_access_action_roles = '
            'invenio_access.admin:action_roles_adminview',
        ],
        'invenio_access.actions': [
            'invenio_access.actions = '
            'invenio_access.permissions:superuser_access',
        ],
        'invenio_base.apps': [
            'invenio_access = invenio_access:InvenioAccess',
        ],
        'invenio_base.api_apps': [
            'invenio_access = invenio_access:InvenioAccess',
        ],
        'invenio_db.alembic': [
            'invenio_access = invenio_access:alembic',
        ],
        'invenio_db.models': [
            'invenio_access = invenio_access.models',
        ],
        'invenio_i18n.translations': [
            'messages = invenio_access',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 4 - Beta',
    ],
)
