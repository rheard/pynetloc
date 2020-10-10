import clr

from clr import System
from expanded_clr.utils import get_wrapper_class, python_name_to_csharp_name


clr.AddReference('System.Device')


class GeoCoordinateWatcher(get_wrapper_class(System.Device.Location.GeoCoordinateWatcher)):
    """We want to provide default arguments for some of the methods..."""

    def start(self, suppress_permission_prompt=True):
        return self.__getattr__('start')(suppress_permission_prompt)

    def try_start(self, suppress_permission_prompt=True, timeout=30):
        return self.__getattr__('try_start')(suppress_permission_prompt, timeout)

    @property
    def location(self):
        return self.position.location


def __getattr__(name):
    """This module is also an entry point for items found in System.Device.Location"""
    name = python_name_to_csharp_name(name)
    return get_wrapper_class(getattr(System.Device.Location, name))
