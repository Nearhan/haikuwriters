#!/bin/bash
PROJ="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
$PROJ/manage.py test --settings="tests.test_settings"
