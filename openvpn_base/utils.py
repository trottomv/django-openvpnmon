from django.conf import settings
import os, datetime, time, zipfile, zlib

import os
import subprocess
import random
import string

from django.utils import six
from django.conf import settings


class CalledShellCommandError(Exception):
    """Exception raised for errors in shell command execution

    Attributes:
        shell_cmd -- shell command
        output  -- command output
        returncode -- error code
    """

    DEFAULT_OUTPUT = "no output provided (using python 2.6?)"

    def __init__(self, shell_cmd, returncode, output=DEFAULT_OUTPUT):
        self.shell_cmd = shell_cmd
        self.returncode = returncode
        self.output = output


def call_shell(shell_cmd, stdin=None):
    """Call shell command and normalize exception output."""
    towrite = ''

    if isinstance(stdin, six.text_type) or isinstance(stdin, str):
        towrite = stdin
        stdin = subprocess.PIPE

    try:
        if stdin is not subprocess.PIPE:
            rv = subprocess.check_output(shell_cmd,
                                         stdin=stdin,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        else:
            process = subprocess.Popen(shell_cmd,
                                       stdin=stdin,
                                       stderr=subprocess.STDOUT,
                                       shell=True,
                                       stdout=subprocess.PIPE)
            process.stdin.write(towrite + '\n')
            output, unused_err = process.communicate()
            retcode = process.poll()
            if retcode:
                raise subprocess.CalledProcessError(
                    retcode, shell_cmd, output=output)
            return output
    except subprocess.CalledProcessError as e:
        raise CalledShellCommandError(shell_cmd, e.returncode, e.output)
    except AttributeError:  # python 2.6
        try:
            rv = subprocess.check_call(shell_cmd, stdin=stdin, shell=True)
        except subprocess.CalledProcessError as e:
            raise CalledShellCommandError(shell_cmd, e.returncode)
    except OSError as e:
        raise CalledShellCommandError(shell_cmd, e.errno, e)
    return rv


def gen_difficult_password(length=10):

    SPECIAL_CHARS = '*()!&,.<:'
    SPECIAL_CHARS = '@.+-_'  # Limitazione applicazione SPES
    total = string.ascii_letters + SPECIAL_CHARS + string.digits
    password = ''.join(random.sample(total, length))
    return password


def get_manage_shell_cmd(cmd, *args, **kw):

    ENVIRONMENT_VARIABLE = "DJANGO_SETTINGS_MODULE"
    settings_module = os.environ[ENVIRONMENT_VARIABLE]
    kw_expanded = ""
    for k, v in kw.items():
        kw_expanded += "--%s=%s" % (k, v)
    args_expanded = " ".join(args)
    cmd = "%s/manage.py %s --settings=%s %s %s" % (settings.PROJECT_ROOT, cmd,
                                                   settings_module,
                                                   kw_expanded, args_expanded)
    if os.environ.get("VIRTUAL_ENV"):
        cmd = ". %s/bin/activate && %s" % (os.environ["VIRTUAL_ENV"], cmd)
    return cmd

def zipfile_info(zf):
    rv = ""
    for info in zf.infolist():
        rv += "%s" % info.filename
        rv += "%s %s" % ('\tComment:\t', info.comment)
        rv += "%s %s" % ('\tModified:\t', datetime.datetime(*info.date_time))
        rv += "%s %s %s" % ('\tSystem:\t\t', info.create_system,
                            '(0 = Windows, 3 = Unix)')
        rv += "%s %s" % ('\tZIP version:\t', info.create_version)
        rv += "%s %s %s" % ('\tCompressed:\t', info.compress_size, 'bytes')
        rv += "%s %s %s" % ('\tUncompressed:\t', info.file_size, 'bytes')
        rv += '\n'
    return rv


def zipfile_print_info(zf):
    print zipfile_info(zf)


def get_certs_zipfile(client, zipfilename):

    # Create ZIP file and serve
    compression = zipfile.ZIP_DEFLATED
    zf = zipfile.ZipFile(zipfilename, mode='w', compression=compression)
    zf.writestr("%s.crt" % settings.DOWNLOAD_CERT_CLIENT_BASENAME, client.cert)
    zf.writestr("%s.key" % settings.DOWNLOAD_KEY_CLIENT_BASENAME, client.key)
    zf.writestr("%s.crt" % settings.DOWNLOAD_CERT_CA_BASENAME, client.ca)
    if client.subnet.config_client:
        zf.writestr("%s.ovpn" % settings.DOWNLOAD_OPENVPNCONF_BASENAME_WIN,
                    client.subnet.config_client)
        zf.writestr("%s.conf" % settings.DOWNLOAD_OPENVPNCONF_BASENAME_GNU,
                    client.subnet.config_client)
    zf.close()
    return zf


def get_certs_zip_content_and_notes(client):

    zipfilename = '/tmp/zipc%s-%s.zip' % (client.pk, time.time())
    zf = get_certs_zipfile(client, zipfilename)

    f = file(zipfilename, mode="r")
    zipcontent = f.read()
    f.close()

    zipnotes = zipfile_info(zf)

    # Remove just created zipfile
    os.remove(zipfilename)
    return zipcontent, zipnotes
