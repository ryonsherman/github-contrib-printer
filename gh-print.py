#!/usr/bin/env python2

import os
import shutil
import tempfile
import argparse
import subprocess

# parse script arguments
parser = argparse.ArgumentParser()
parser.add_argument('user', help="github user")
parser.add_argument('repo', help="github repo")
parser.add_argument('density', 
    type=int, nargs='?', default=20, 
    help="commit density (default: %(default)s)")
args = parser.parse_args()

# create temp dir
path = tempfile.mkdtemp()

# determine repo url
url = "https://"
repo = args.repo.split('@')
if len(repo) > 1:
    url += "%s@" % repo[0]
    repo = repo[1]
else: repo = repo[0]
url += "github.com/%s.git" % repo

# helper to make subprocess calls
def call(cmd):
    cmd = "cd %s; %s" % (path, cmd)
    subprocess.call(cmd, shell=True)

# clone repo
call("git clone %s %s" % (url, path))
# configure repo
call("git config user.email 'gh-printer-debug@secretco.de.com'")

# commit bit density
for i in range(0, args.density):
    with open(os.path.join(path, 'file'), 'wb') as f:
        f.write(os.urandom(1024))
    call("git add file")
    call("git commit file -m 'gh-printer'")

# push commits
call("git push %s" % url)

# remove temp dir
shutil.rmtree(path)
