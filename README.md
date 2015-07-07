# Wagtail-OpenShift
Wagtail CMS project ready to use on OpenShift

# Getting started
* login with your openshift credentials  `rhc setup -l username`
* create your python/sqlite openshift app  `rhc app create appname python-2.7 --from-code https://github.com/dennyb87/wagtail-openshift.git`
* go to `www.yourappname.com/admin` and login with username `wagtail` and password `openshift`
* change username and password of the account!

# Media files & Database
Your media files and database will be on OpenShift in a persistent directory called `$OPENSHIFT_DATA_DIR` in this way:
```
$OPENSHIFT_DATA_DIR/
    db.sqlite3
    media/
```
Don't worry... they will not be affected by `git push`.
