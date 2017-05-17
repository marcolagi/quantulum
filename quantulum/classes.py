#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""quantulum classes."""


###############################################################################
class Quantity(object):
    """Class for a quantity (e.g. "4.2 gallons")."""

    def __init__(self, value=None, unit=None, surface=None, span=None,
                 uncertainty=None):
        """Initialization method."""
        self.value = value
        self.unit = unit
        self.surface = surface
        self.span = span
        self.uncertainty = uncertainty

    def __repr__(self):
        """Representation method."""
        msg = 'Quantity(%g, "%s")'
        msg = msg % (self.value, self.unit.name)
        return msg

    def __eq__(self, other):
        """Equality method."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Non equality method."""
        return not self.__eq__(other)


###############################################################################
class Unit(object):
    """Class for a unit (e.g. "gallon")."""

    def __init__(self, name=None, surfaces=None, entity=None, uri=None,
                 symbols=None, dimensions=None):
        """Initialization method."""
        self.name = name
        self.surfaces = surfaces
        self.entity = entity
        self.uri = uri
        self.symbols = symbols
        self.dimensions = dimensions

    def __repr__(self):
        """Representation method."""
        msg = 'Unit(name="%s", entity=Entity("%s"), uri=%s)'
        msg = msg % (self.name, self.entity.name, self.uri)
        return msg

    def __eq__(self, other):
        """Equality method."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Non equality method."""
        return not self.__eq__(other)


###############################################################################
class Entity(object):
    """Class for an entity (e.g. "volume")."""

    def __init__(self, name=None, dimensions=None, uri=None):
        """Initialization method."""
        self.name = name
        self.dimensions = dimensions
        self.uri = uri

    def __repr__(self):
        """Representation method."""
        msg = 'Entity(name="%s", uri=%s)'
        msg = msg % (self.name, self.uri)
        return msg

    def __eq__(self, other):
        """Equality method."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Non equality method."""
        return not self.__eq__(other)
