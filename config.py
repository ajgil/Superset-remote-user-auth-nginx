
from flask_appbuilder.security.manager import AUTH_DB, AUTH_LDAP, AUTH_REMOTE_USER
# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# Uncomment to setup Full admin role name
# AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = False

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Gamma"

# imports
from superset.security import SupersetSecurityManager
from flask import redirect, g, flash, request, session
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.security.views import AuthDBView, AuthRemoteUserView
from flask_appbuilder.security.views import expose
from flask_appbuilder.security.manager import BaseSecurityManager
from flask_appbuilder import base
from flask_login import login_user, logout_user

# ----------------------------------------------------------------
# Login AUTH_REMOTE_USER
# ----------------------------------------------------------------
# 1.- Definir una clase middleware
# 2.- Actualizar ADDITIONAL_MIDDLEWARE
# 3.- override vista auth
# 4.- Manager de seguridad
# 5.- AUTH_USER_REGISTRATION = False (If you do not want auto self registration)

class RemoteUserMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        user = environ.pop('HTTP_PROXY_REMOTE_USER', None)
        environ['REMOTE_USER'] = user
        return self.app(environ, start_response)

ADDITIONAL_MIDDLEWARE = [RemoteUserMiddleware, ]

class MiCustomRemoteUserView(AuthRemoteUserView):
    # Leave blank
    login_template = ''

    @expose('/login/')
    def login(self):
        # headers
        username = request.headers.get('HTTP_PROXY_REMOTE_USER')
        if g.user is not None and g.user.is_authenticated():
        	return redirect(self.appbuilder.get_url_for_index)

        sm = self.appbuilder.sm
        session = sm.get_session
        user = session.query(sm.user_model).filter_by(username=username).first()
        if user is None and username:
            msg = ("User not allowed, {}".format(username))
            flash(as_unicode(msg), 'error')
            return redirect(self.appbuilder.get_url_for_login)

        if username:
            user = self.appbuilder.sm.auth_user_remote_user(username)
            if user is None:
                flash(as_unicode(self.invalid_login_message), 'warning')
            else:
                login_user(user)
        else:
            flash(as_unicode(self.invalid_login_message), 'warning')

        return redirect(self.appbuilder.get_url_for_index)

class MiCustomSecurityManager(SupersetSecurityManager):
    authremoteuserview = MiCustomRemoteUserView

AUTH_TYPE = AUTH_REMOTE_USER
CUSTOM_SECURITY_MANAGER = MiCustomSecurityManager
