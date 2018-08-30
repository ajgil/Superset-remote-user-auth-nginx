# Apache Superset remote user authentication

This code is easiest way to configure AUTH_REMOTE_USER on Superset and Flask_AppBuilder framework, enables automatic login on superset.

ToDo: Integrate SAML python library to manage token.

We suposse that you have Apache superset running as well. Let's do it

## AUTH_REMOTE_USER Login
There are four steps to do here

* Define middleware class, this will capture environment var 
* Updating global ADDITIONAL_MIDDLEWARE
* Define Security Manager (extends SupersetSecurityManager)
* New Custom View class extends AuthRemoteUserView

## Postman tests

## Ngnix config

Links:
[Flask_AppBuilder](https://flask-appbuilder.readthedocs.io/en/latest/security.html#your-custom-security)
[Werkzeug project](http://werkzeug.pocoo.org/docs/0.14/wrappers/)
[Sairamkrish on Medium](https://medium.com/@sairamkrish/apache-superset-custom-authentication-and-integrate-with-other-micro-services-8217956273c1)
[Yamyamyuo on GitHub](https://github.com/yamyamyuo/superset-development)
[Mistercrunch on GitHub](https://gist.github.com/mistercrunch/6d31af4a11c47edcedc1ba6ceb5f5fab#file-supersetlogin-py)

