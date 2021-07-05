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

class SubscriptionLinkList(object):
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
        'links': 'SubscriptionLinkListLinks'
    }

    attribute_map = {
        'links': '_links'
    }

    def __init__(self, links=None):  # noqa: E501
        """SubscriptionLinkList - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self.discriminator = None
        self.links = links

    @property
    def links(self):
        """Gets the links of this SubscriptionLinkList.  # noqa: E501


        :return: The links of this SubscriptionLinkList.  # noqa: E501
        :rtype: SubscriptionLinkListLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SubscriptionLinkList.


        :param links: The links of this SubscriptionLinkList.  # noqa: E501
        :type: SubscriptionLinkListLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

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
        if issubclass(SubscriptionLinkList, dict):
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
        if not isinstance(other, SubscriptionLinkList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
