# -*- coding: utf-8 -*-
# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from setuptools import setup, find_packages

from dist_utils import check_pip_version
from dist_utils import fetch_requirements
from dist_utils import parse_version_string

check_pip_version()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(BASE_DIR, 'requirements.txt')
INIT_FILE = os.path.join(BASE_DIR, 'st2auth_oauth2_backend', '__init__.py')

version = parse_version_string(INIT_FILE)
install_reqs, dep_links = fetch_requirements(REQUIREMENTS_FILE)

setup(
    name='st2-auth-backend-oauth2',
    version=version,
    description='StackStorm authentication backend which reads from an Oauth2/OpenID Identity Provider.',
    author='Pearson Technology, Inc.',
    author_email='peter.idah@pearson.com',
    url='https://github.com/pidah/st2-auth-backend-oauth2',
    license='Apache License (2.0)',
    download_url='https://github.com/pidah/st2-auth-backend-oauth2/tarball/master',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
    platforms=['Any'],
    scripts=[],
    provides=['st2auth_oauth2_backend'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_reqs,
    dependency_links=dep_links,
    test_suite='tests',
    entry_points={
        'st2auth.backends.backend': [
            'oauth2 = st2auth_oauth2_backend.oauth2:Oauth2AuthenticationBackend',
        ],
    },
    zip_safe=False
)
