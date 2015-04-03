django-ladon
=======================

.. image:: https://travis-ci.org/TargetHolding/django-ladon.svg?branch=master
    :target: https://travis-ci.org/TargetHolding/django-ladon
.. image:: https://coveralls.io/repos/TargetHolding/django-ladon/badge.svg
  :target: https://coveralls.io/r/TargetHolding/django-ladon


A fairly simple wrapper for including ladon in your django projects.

Just add `django_ladon` to your `INSTALLED_APPS`, write your webservice-classes in `ladon.py` in your app(s) in the usual ladon way, and point a urlpattern to `django_ladon.urls`.

