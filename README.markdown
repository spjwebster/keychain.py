keychain.py
===========

A python module for accessing Mac OS X keychain data from Python. This is a fork of [Stuart Colville's](http://muffinresearch.co.uk) original [Keychain.py](https://launchpad.net/keychain.py/) project, with additional support for querying keys for specific service names rather than just account names.


Installation
------------

If you've already installed [setuptools](http://pypi.python.org/pypi/setuptools) you can download and install the keychain module with the following command:

    easy_install http://github.com/spjwebster/keychain.py/tarball/master

If not, [download the tarball](http://github.com/spjwebster/keychain.py/tarball/master), extract it and then:

    cd path/to/extracted/directory
    python setup.py install


Unit tests
----------

Once you've installed the keychain module, you can run the unit tests to make sure that everything is working:

    python tests.py


License
-------

Copyright (c) 2008, Stuart J Colville and Steve Webster
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Muffin Research Labs nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHORS 'AS IS' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.