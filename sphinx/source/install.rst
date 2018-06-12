==========
Installing
==========

``FLUIDAsserts`` is hosted on `PyPI <https://pypi.org/project/FLUIDAsserts/>`_,
so you can install it easily using ``pip3``
on a system with ``Python 3``: ::

   $ pip3 install -U fluidasserts

For normal/interactive usage,
you should set the environment variable ``FA_STRICT`` to false
(see below). In an ``UNIX``-like ``OS``: ::

   $ export FA_STRICT="false"

In Windows:

.. code-block:: none

   > set FA_STRICT="false"

Now you're ready to begin :doc:`testing<usage>` vulnerabilities' closure.

-----------------------------------------------
Usage in a CI (Continuous Integration) pipeline
-----------------------------------------------

If you have an application subscribed to our
Continuous Hacking Service
which includes the use of ``Asserts``,
you can integrate it into
your ``CI`` pipeline to
ensure that your software builds and ships
with no open vulnerabilities.
We will provide a custom ``Dcoker`` container
with the specific tests you need
and maintain the build-breaking exploit.

To achieve this, follow these steps:

#. Add the required environment variables
   ``USER``, ``PASS``, ``ORG`` and ``APP``.
   Don't worry, the values will be provided by us!:

   * ``USER``: Name of the user from our Container Registry
   * ``PASS``: The password of the user
   * ``ORG``: The name of the organization
   * ``APP``: The name of the application

   For example, in Gitlab, your environment would look like this:

   .. image:: _static/vars.png

#. Add a job to run ``FLUIDAsserts``.
   For example, in Gitlab,
   you would add these three lines to
   your ``.gitlab-ci.yml``:

   .. code-block:: yaml

      fluidasserts:
        script:
          - docker login registry.gitlab.com -u $USER -p $PASS
          - docker pull registry.gitlab.com/$ORG:$APP
          - docker run -e ORG=$ORG -e APP=$APP -e USER=$USER
                       -e PASS=$PASS -e FA_STRICT="true"
                       registry.gitlab.com/$ORG:$APP

#. Now your pipeline will break
   if any vulnerability is found to be open.
   In order to not break the build,
   but still run the tests,
   set the ``FA_STRICT`` variable above to ``"false"``.