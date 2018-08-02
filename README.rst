
# OpenVPN config

OpenVPN config is an OpenVPN web interface built on top of Django that makes OpenVPN admins able to:

* Define networks and corresponding OpenVPN conf files
* Add clients to OpenVPN network
    * Get configuration files
    * Create new certificates
    * Revoke certificates
* Register OpenVPN connections: log active and recent OpenVPN connections

Default uses sqlite but you can use PostgreSQL or other if you want.

OpenVPN is released with AGPLv3 License
Author is Luca Ferroni <fero@befair.it>

It includes easy-rsa which is free software made by OpenVPN technologies Inc. <sales@openvpn.net>


Quick start
-----------
1. Install from pip:

```
  pip install git+https://github.com/trottomv/django-openvpnmon.git
```

2. Add the folllow lines in `settings.py`:

```
  from django.conf.urls import include

  INSTALLED_APPS = {
  ...
  'openvpnmon',
  'base',
  'mon',
  }
```

3. Include the openvpnmon URLconf in `urls.py`:

```
  from django.conf.urls import include

  url(r'^openvpnmon/', include('openvpnmon.urls'))
```
4. Download `extras` directory on your `../your/django-project/`: (if you have `svn` installed)

```
  svn export https://github.com/trottomv/openvpnmon.git/trunk/extras
```
5. In your `settings.py` insert this follow lines:

```
#OpenVPNmon settings
EASY_RSA_DIR = os.path.join(BASE_DIR, "extras", "easy-rsa")
EASY_RSA_KEYS_DIR = os.path.join(EASY_RSA_DIR, "keys")
EASY_RSA_VARS_FILE = os.path.join(EASY_RSA_DIR, "vars")
CA_CERT = os.path.join(EASY_RSA_KEYS_DIR, 'ca.crt')
URL_PREFIX = ""
```

6. Run `python manage.py migrate` to create openvpnmon models.

7. Run the development server and access to manage openvpnmon `http://127.0.0.1:8000/openvpnmon/`.


