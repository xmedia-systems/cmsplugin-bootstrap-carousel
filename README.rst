========================================
Bootstrap carousel plugin for Django CMS
========================================

This plugin lets you easily add *carousel* components (ie. slideshows)
into django-cms pages using `Bootstrap
<http://twitter.github.com/bootstrap/>`_.

Requirements
============

* `Django CMS >= 2.2 <http://django-cms.org>`_
* `Bootstrap <http://twitter.github.com/bootstrap/>`_

Installation
============

To use it into your project, just follow this procedure:

#. Open the *settings.py* file and add ``cmsplugin_bootstrap_carousel`` to the
   ``INSTALLED_APPS`` variable

#. Run the following command::

    $ ./manage.py syncdb

Images embedded into carousels are automaticaly resized. The default
size is 800x600. To change it, define the following variable into your
configuration file::

  BOOTSTRAP_CAROUSEL_IMGSIZE = (1024, 768)

.. note::

    Bootstrap is not included with this plugin.
