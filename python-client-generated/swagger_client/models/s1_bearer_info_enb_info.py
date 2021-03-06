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

class S1BearerInfoEnbInfo(object):
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
        'ip_address': 'str',
        'tunnel_id': 'str'
    }

    attribute_map = {
        'ip_address': 'ipAddress',
        'tunnel_id': 'tunnelId'
    }

    def __init__(self, ip_address=None, tunnel_id=None):  # noqa: E501
        """S1BearerInfoEnbInfo - a model defined in Swagger"""  # noqa: E501
        self._ip_address = None
        self._tunnel_id = None
        self.discriminator = None
        self.ip_address = ip_address
        self.tunnel_id = tunnel_id

    @property
    def ip_address(self):
        """Gets the ip_address of this S1BearerInfoEnbInfo.  # noqa: E501

        eNB transport layer address of this S1 bearer.  # noqa: E501

        :return: The ip_address of this S1BearerInfoEnbInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this S1BearerInfoEnbInfo.

        eNB transport layer address of this S1 bearer.  # noqa: E501

        :param ip_address: The ip_address of this S1BearerInfoEnbInfo.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def tunnel_id(self):
        """Gets the tunnel_id of this S1BearerInfoEnbInfo.  # noqa: E501

        eNB GTP-U TEID of this S1 bearer.  # noqa: E501

        :return: The tunnel_id of this S1BearerInfoEnbInfo.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_id

    @tunnel_id.setter
    def tunnel_id(self, tunnel_id):
        """Sets the tunnel_id of this S1BearerInfoEnbInfo.

        eNB GTP-U TEID of this S1 bearer.  # noqa: E501

        :param tunnel_id: The tunnel_id of this S1BearerInfoEnbInfo.  # noqa: E501
        :type: str
        """
        if tunnel_id is None:
            raise ValueError("Invalid value for `tunnel_id`, must not be `None`")  # noqa: E501

        self._tunnel_id = tunnel_id

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
        if issubclass(S1BearerInfoEnbInfo, dict):
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
        if not isinstance(other, S1BearerInfoEnbInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
