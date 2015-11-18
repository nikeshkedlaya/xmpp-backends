# -*- coding: utf-8 -*-
#
# This file is part of xmpp-backends (https://github.com/mathiasertl/xmpp-backends).
#
# xmpp-backends is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# xmpp-backends is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with xmpp-backends.  If
# not, see <http://www.gnu.org/licenses/>.

import inspect
import unittest

from xmpp_backends.base import XmppBackendBase
from xmpp_backends.ejabberd_xmlrpc import EjabberdXMLRPCBackend
from xmpp_backends.ejabberdctl import EjabberdctlBackend
from xmpp_backends.dummy import DummyBackend


class TestInterfaces(unittest.TestCase):
    def assertEqualInterface(self, subclass):
        for name, base_func in inspect.getmembers(XmppBackendBase, callable):
            if name.startswith('_'):
                continue

            self.assertEqual(
                inspect.getargspec(base_func),
                inspect.getargspec(getattr(subclass, name)),
                "%s.%s has a different signature" % (subclass.__name__, name)
            )

    def test_ejabberd_xmlrpc(self):
        self.assertEqualInterface(EjabberdXMLRPCBackend)

    def test_ejabberdctl(self):
        self.assertEqualInterface(EjabberdctlBackend)

    def test_dummy(self):
        self.assertEqualInterface(DummyBackend)