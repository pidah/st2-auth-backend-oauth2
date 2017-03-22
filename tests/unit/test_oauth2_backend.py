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

import sys

import unittest2
import mock
from st2auth_oauth2_backend.oauth2 import Oauth2AuthenticationBackend


def _mock_fetch_token(**kwargs):
    access_token = {"access_token": "asdfoiw37850234lkjsdfsdf"}

    if kwargs['username'] == 'good' and kwargs['password'] == 'password':
        return access_token


class Oauth2AuthenticationBackendTestCase(unittest2.TestCase):

    @mock.patch(
        'st2auth_oauth2_backend.oauth2.OAuth2Session.fetch_token',
        side_effect=_mock_fetch_token)
    def test_authenticate(self, mock_post):
        backend = Oauth2AuthenticationBackend(
            token_url="http://fakeidentityprovider.com:8080/token",
            client_id="demo",
            client_secret="1a9ada23-d527-46eb-9230-d068ac3bc161")

        # good users and wrong password
        self.assertEqual(backend.authenticate('good', 'badpassword'), False)
        # good users and correct password
        self.assertEqual(backend.authenticate('good', 'password'), True)
        # bad users
        self.assertEqual(backend.authenticate('bad', 'badpassword'), False)

if __name__ == '__main__':
    sys.exit(unittest2.main())
