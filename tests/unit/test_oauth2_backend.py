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
import httplib

import unittest2
import mock
from requests.models import Response

from st2auth_keystone_backend.keystone import KeystoneAuthenticationBackend


class KeystoneAuthenticationBackendTestCase(unittest2.TestCase):
    def _mock_keystone(self, *args, **kwargs):
        return_codes = {
            'goodv2': httplib.OK,
            'goodv3': httplib.CREATED,
            'bad': httplib.UNAUTHORIZED
        }
        json = kwargs.get('json')
        res = Response()
        try:
            # v2
            res.status_code = return_codes[json['auth']['passwordCredentials']['username']]
        except KeyError:
            # v3
            res.status_code = return_codes[json['auth']['identity']['password']['user']['name']]
        return res

    @mock.patch('requests.post', side_effect=_mock_keystone)
    def test_authenticate(self, mock_post):
        backendv2 = KeystoneAuthenticationBackend(keystone_url="http://fake.com:5000",
                                                  keystone_version=2)
        backendv3 = KeystoneAuthenticationBackend(keystone_url="http://fake.com:5000",
                                                  keystone_version=3)

        # good users
        self.assertTrue(backendv2.authenticate('goodv2', 'password'))
        self.assertTrue(backendv3.authenticate('goodv3', 'password'))
        # bad ones
        self.assertFalse(backendv2.authenticate('bad', 'password'))
        self.assertFalse(backendv3.authenticate('bad', 'password'))

if __name__ == '__main__':
    sys.exit(unittest2.main())
