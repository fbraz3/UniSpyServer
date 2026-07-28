#!/bin/sh
set -e

# If running as root, fix permissions on mounted volumes and drop privileges to unispy user
if [ "$(id -u)" = '0' ]; then
    mkdir -p /unispy-server/log
    chown -R unispy:unispy /unispy-server/log 2>/dev/null || true
    exec gosu unispy "$@"
fi

exec "$@"
