# wagtail-openshift
Wagtail CMS project ready to use on OpenShift

# Getting started
* login with your openshift credentials  `rhc setup -l username`
* create your python/sqlite openshift app  `rhc app create appname python-2.7 --from-code https://github.com/dennyb87/wagtail-openshift.git`
* go to 'www.yourappname.com/admin' and login with username `wagtail' password 'openshift'
* change username and password of the account!
