# Oauth2 authentication plugin for StackStorm Community edition

### Configuration Options

| option           | required | default | description                                              |
|------------------|----------|---------|----------------------------------------------------------|
| token_url     | yes      |         | Oauth2 token endpoint url (i.e. "http://example.com:5000")     |

### Configuration Example

Please refer to the authentication section in the StackStorm
[documentation](http://docs.stackstorm.com) for basic setup concept. The
following is an example of the auth section in the StackStorm configuration file for the flat-file
backend.

```
[auth]
mode = standalone
backend = oauth2
backend_kwargs = {"token_url": "http://identity.example.com:5000/"}
enable = True
use_ssl = True
cert = /path/to/ssl/cert/file
key = /path/to/ssl/key/file
logging = /path/to/st2auth.logging.conf
api_url = https://myhost.example.com:9101
debug = False
```

## Copyright, License, and Contributors Agreement

Copyright 2015 StackStorm, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in
compliance with the License. You may obtain a copy of the License in the [LICENSE](LICENSE) file,
or at: [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

By contributing you agree that these contributions are your own (or approved by your employer) and 
you grant a full, complete, irrevocable copyright license to all users and developers of the
project, present and future, pursuant to the license of the project.
