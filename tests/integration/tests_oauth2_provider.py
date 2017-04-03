import unittest2
import requests
from flask import Flask
from flask_testing import LiveServerTestCase
from yolo.app import db, create_app
from bs4 import BeautifulSoup
from st2auth_oauth2_backend.oauth2 import Oauth2AuthenticationBackend


class Config(object):
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    LIVESERVER_TIMEOUT = 2
    LIVESERVER_PORT = 8943


class Oauth2ProviderIntegrationTests(LiveServerTestCase):

    def create_app(self, **kwargs):

        config = Config()
        config.__dict__.update(kwargs)
        app = create_app(config)
        with app.app_context():
            self.app = app.test_client()
            db.drop_all()
            db.create_all(app=app)
        return app

###########################################################
####################### tests #############################
###########################################################

    def test_authenticate(self):

        username = "test_user"
        password = "password"

        # create a new user
        base_url = self.get_server_url()
        new_user = requests.post(base_url,
                                 data={
                                     "submit": "Add User",
                                     "username": username,
                                     "password": password})
        # create a new client
        new_client = requests.post(base_url, data={"submit": "Add Client"})
        soup = BeautifulSoup(new_client.content, 'html.parser')
        client_id = soup.find(
            'td', text='public').find_previous_sibling("td").text

        token_url = base_url + "/oauth/token"

        #authenticate
        backend = Oauth2AuthenticationBackend(
            token_url=token_url,
            client_id=client_id,
            client_secret="")

        # new user created
        self.assertEqual(new_user.status_code, 200)
        # new client created
        self.assertEqual(new_client.status_code, 200)
        # good users and wrong password
        self.assertEqual(backend.authenticate('good', 'badpassword'), False)
        # good users and correct password
        self.assertEqual(backend.authenticate(username, password), True)
        # bad users
        self.assertEqual(backend.authenticate('bad', 'badpassword'), False)


if __name__ == "__main__":
    unittest2.main()
