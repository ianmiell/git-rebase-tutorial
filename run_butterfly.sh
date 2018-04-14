#!/bin/bash

set -eu

# Designed to be run when called from butterfly

# butterfly.server.py --host=0.0.0.0 --port=57575 --shell='/space/git/git-rebase-tutorial/run_butterfly.sh'

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cd $(dirname ${BASH_SOURCE[0]})
echo 'LOADING... please wait'
shutit build -d docker -l info
