#!/bin/bash
# platform = multi_platform_ubuntu,multi_platform_rhel
# packages = openssl-pkcs11

{{% if 'ubuntu' in product %}}
tmpdir=$(mktemp -d)
cd $tmpdir; apt download libpam-pkcs11
cd /; dpkg-deb --fsys-tarfile $tmpdir/libpam-pkcs11*.deb | tar -x ./usr/share/doc/libpam-pkcs11/examples/pam_pkcs11.conf.example
rm -rf $tmpdir
{{% endif %}}



if [ ! -f /etc/pam_pkcs11/pam_pkcs11.conf ]; then
    cp /usr/share/doc/libpam-pkcs11/examples/pam_pkcs11.conf.example /etc/pam_pkcs11/pam_pkcs11.conf
fi

sed -i "/^\s*#/! s/cert_policy.*/# cert_policy = ca,signature,ocsp_on;/g" /etc/pam_pkcs11/pam_pkcs11.conf
