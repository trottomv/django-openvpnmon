
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
0. Install from pip:

```
  pip install git+https://github.com/trottomv/openvpnmon.git
```

1. Add "openvpnmon" to INSTALLED_APPS in `settings.py`:

```
  INSTALLED_APPS = {
  ...
  'openvpnmon'
  }
```

2. Include the myblog URLconf in `urls.py`:

```
  url(r'^openvpnmon/', include('openvpnmon.urls'))
```
0. Download `extras` directory on your `../your/django-project/`: (if you have `svn` installed)

```
  svn export https://github.com/trottomv/openvpnmon.git/trunk/extras
```
0. In your `settings.py` insert this follow lines:

```
#OpenVPNmon settings
EASY_RSA_DIR = os.path.join(BASE_DIR, "extras", "easy-rsa")
EASY_RSA_KEYS_DIR = os.path.join(EASY_RSA_DIR, "keys")
EASY_RSA_VARS_FILE = os.path.join(EASY_RSA_DIR, "vars")
CA_CERT = os.path.join(EASY_RSA_KEYS_DIR, 'ca.crt')
URL_PREFIX = ""
```

3. Run `python manage.py migrate` to create openvpnmon models.

4. Run the development server and access to manage openvpnmon `http://127.0.0.1:8000/openvpnmon/`.


