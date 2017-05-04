
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

import logging

import os
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from passlib.apache import HtpasswdFile

__all__ = [
    'Oauth2AuthenticationBackend'
]

LOG = logging.getLogger(__name__)


class Oauth2AuthenticationBackend(object):
    """
    Backend which connects to an Oauth2/OpeniD Connect Identitiy provider.

    This backend depends on the "requests", "oauthlib" and "requests_oauthlib libraries.

    **NOTE**: This oauth2 backend ONLY supports the  `Resource Owner Password Credential Grant` as specified in https://tools.ietf.org/html/rfc6749

    """

    def __init__(
            self,
            token_url,
            client_id,
            client_secret="",
            exclude_list=None,
            file_path=None):
        """
        :param token_url: token endpoint url for the Oauth2/OpenID connect Identity Provider.
        :type token_url: ``str``
        """
        self._token_url = token_url
        self._client_id = client_id
        self._client_secret = client_secret
        self._exclude_list = exclude_list
        self._file_path = file_path

    def authenticate(self, username, password):

        if username in self._exclude_list:
            htpasswd_file = HtpasswdFile(path=self._file_path)
            result = htpasswd_file.check_password(username, password)

            if result is None:
                LOG.info('User "%s" doesn\'t exist' % (username))
            elif result is False:
                LOG.info('Invalid password for user "%s"' % (username))
            elif result is True:
                LOG.info(
                    'Authentication for user "%s" successful' %
                    (username))

            return bool(result)

        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
        oauth = OAuth2Session(
            client=LegacyApplicationClient(
                client_id=self._client_id))

        try:
            token = oauth.fetch_token(
                token_url=self._token_url,
                username=username,
                password=password,
                client_id=self._client_id,
                client_secret=self._client_secret,
                verify=False)
        except Exception as e:
            LOG.info(
                'Authentication for user "{}" failed: {}'.format(
                    username, str(e)))
            return False
        if token is not None:
            LOG.info('Authentication for user "{}" successful'.format(username))
            return True

        return False

    def get_user(self, username):
        pass
