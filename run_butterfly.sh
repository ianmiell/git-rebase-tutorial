#!/bin/bash

set -eu

# Designed to be run when called from butterfly

# butterfly.server.py --host=0.0.0.0 --port=57575 --shell='/space/git/git-rebase-tutorial/run_butterfly.sh'

(
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cd $(dirname ${BASH_SOURCE[0]})
echo 'LOADING... please wait'
sleep 2 && echo && echo "If you see a 'Closed' message, then you may have adblockers or similar on your client" &
sleep 4 && echo && echo "Do not resize your window. If you want a different sized window, resize and then reload the page." &
sleep 6 && echo && echo 'STILL LOADING... please wait' &
shutit build -d docker -l critical
) 2>/dev/null
