# coding: utf-8

"""
    ETSI GS MEC 012 - Radio Network Information API

    The ETSI MEC ISG MEC012 Radio Network Information API described using OpenAPI.  # noqa: E501

    OpenAPI spec version: 2.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Ecgi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cell_id': 'CellId',
        'plmn': 'Plmn'
    }

    attribute_map = {
        'cell_id': 'cellId',
        'plmn': 'plmn'
    }

    def __init__(self, cell_id=None, plmn=None):  # noqa: E501
        """Ecgi - a model defined in Swagger"""  # noqa: E501
        self._cell_id = None
        self._plmn = None
        self.discriminator = None
        self.cell_id = cell_id
        self.plmn = plmn

    @property
    def cell_id(self):
        """Gets the cell_id of this Ecgi.  # noqa: E501


        :return: The cell_id of this Ecgi.  # noqa: E501
        :rtype: CellId
        """
        return self._cell_id

    @cell_id.setter
    def cell_id(self, cell_id):
        """Sets the cell_id of this Ecgi.


        :param cell_id: The cell_id of this Ecgi.  # noqa: E501
        :type: CellId
        """
        if cell_id is None:
            raise ValueError("Invalid value for `cell_id`, must not be `None`")  # noqa: E501

        self._cell_id = cell_id

    @property
    def plmn(self):
        """Gets the plmn of this Ecgi.  # noqa: E501


        :return: The plmn of this Ecgi.  # noqa: E501
        :rtype: Plmn
        """
        return self._plmn

    @plmn.setter
    def plmn(self, plmn):
        """Sets the plmn of this Ecgi.


        :param plmn: The plmn of this Ecgi.  # noqa: E501
        :type: Plmn
        """
        if plmn is None:
            raise ValueError("Invalid value for `plmn`, must not be `None`")  # noqa: E501

        self._plmn = plmn

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Ecgi, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Ecgi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
