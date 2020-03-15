Welcome to async_lichess_sdk's documentation!
=============================================
This package is meant to be an unofficial Python API Client for lichees.org.
For information about the API please refer to https://lichess.org/api
Every API endpoint uses async Python methods (asyncio).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Requirements
============
* `aiohttp <https://github.com/aio-libs/aiohttp>`_
* `python-chess <https://github.com/niklasf/python-chess>`_

Installation
============
You can just install me from a test PyPi

.. code-block:: bash

    pip install --index-url https://test.pypi.org/simple/ async_lichess_sdk

or official PyPi

.. code-block:: bash

    pip install async_lichess_sdk

Available Modules / Endpoints
=============================

APIClient
+++++++++
.. automodule:: lichess_client.clients.client
    :members:

Account
+++++++++
.. automodule:: lichess_client.endpoints.account
    :members:

Boards
+++++++++
.. automodule:: lichess_client.endpoints.boards
    :members:

Bots
+++++++++
.. automodule:: lichess_client.endpoints.bots
    :members:

Broadcast
+++++++++
.. automodule:: lichess_client.endpoints.broadcast
    :members:

Challenges
++++++++++
.. automodule:: lichess_client.endpoints.challenges
    :members:

Games
++++++++++
.. automodule:: lichess_client.endpoints.games
    :members:

Messaging
++++++++++
.. automodule:: lichess_client.endpoints.messaging
    :members:

Relations
++++++++++
.. automodule:: lichess_client.endpoints.relations
    :members:

Simulations
+++++++++++
.. automodule:: lichess_client.endpoints.simulations
    :members:

Studies
++++++++++
.. automodule:: lichess_client.endpoints.studies
    :members:

Teams
++++++++++
.. automodule:: lichess_client.endpoints.teams
    :members:

Tournaments
++++++++++
.. automodule:: lichess_client.endpoints.tournaments
    :members:

Users
++++++++++
.. automodule:: lichess_client.endpoints.users
    :members:

Helpers
========
.. automodule:: lichess_client.helpers.response_helpers
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
