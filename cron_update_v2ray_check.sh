#!/bin/sh

# change to your specific folder for cron job
TOP_DIR=/home/felix/docker/v2ray_check

# rm workdir & restart from github
rm -fr ${TOP_DIR}
git clone git@github.com:feishengfei/check.git --recursive ${TOP_DIR}
if [ $? -eq 0 ]; then
    # cron check and update
    pushd ${TOP_DIR}
    ./iter_v2.py free/v2 && git add README.md config && git commit --allow-empty -m "update_at $(date '+%m-%d %H:%M')" && git push origin HEAD:main
    popd
fi
