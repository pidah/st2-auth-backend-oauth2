# Oauth2 authentication plugin for StackStorm Community edition

**NOTE**: This oauth2 backend __ONLY__ supports the  `Resource Owner Password Credential Grant` as specified in https://tools.ietf.org/html/rfc6749


### Configuration Options

| option           | required | default | description                                              |
|------------------|----------|---------|----------------------------------------------------------|
| token_url     | yes      |         |Oauth2 token endpoint url (i.e."http://example.com:5000/token") |
| client_id     | yes      |         |client_id for the client obtained from the Identity Provider    |
| client_secret | yes      |         |client_secret for the client obtained from the Identity Provider|

### Configuration Example

Please refer to the authentication section in the StackStorm
[documentation](http://docs.stackstorm.com) for basic setup concept. The
following is an example of the auth section in the StackStorm configuration file for the oauth2 backend:

```
[auth]
mode = standalone
backend = oauth2
backend_kwargs = {"token_url": "http://example.com:5000/token", "client_id": "demo", "client_secret": "1a9ada23-d527-46eb-9230-d068ac3bc161"}
enable = True
use_ssl = True
cert = /path/to/ssl/cert/file
key = /path/to/ssl/key/file
logging = /path/to/st2auth.logging.conf
api_url = https://myhost.example.com:9101
debug = False
```

### Oauth2 Identity Provider Server

To validate this Oauth2 backend, you can use the the following Identity Provider https://github.com/pidah/yoloAPI/ which supports Resource Owner Password Credentials Grant. This provider is based on https://github.com/brunsgaard/yoloAPI.

### Tests

To run both unit and integration tests:

```
pip install -r test-requirements.txt

python setup.py test
```
or 

```
python -m  unittest discover
```



## Copyright, License, and Contributors Agreement

Copyright 2015 StackStorm, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in
compliance with the License. You may obtain a copy of the License in the [LICENSE](LICENSE) file,
or at: [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

By contributing you agree that these contributions are your own (or approved by your employer) and 
you grant a full, complete, irrevocable copyright license to all users and developers of the
project, present and future, pursuant to the license of the project.
