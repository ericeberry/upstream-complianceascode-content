#!/bin/bash
# platform = Oracle Linux 7

. $SHARED/auditd_utils.sh
prepare_auditd_test_enviroment
set_parameters_value {{{ audisp_conf_path }}}/plugins.d/syslog.conf "active" "yes"
