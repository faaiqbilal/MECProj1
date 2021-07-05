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

class S1BearerInfoS1BearerInfoDetailed(object):
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
        'enb_info': 'S1BearerInfoEnbInfo',
        'erab_id': 'int',
        's_gw_info': 'S1BearerInfoSGwInfo'
    }

    attribute_map = {
        'enb_info': 'enbInfo',
        'erab_id': 'erabId',
        's_gw_info': 'sGwInfo'
    }

    def __init__(self, enb_info=None, erab_id=None, s_gw_info=None):  # noqa: E501
        """S1BearerInfoS1BearerInfoDetailed - a model defined in Swagger"""  # noqa: E501
        self._enb_info = None
        self._erab_id = None
        self._s_gw_info = None
        self.discriminator = None
        if enb_info is not None:
            self.enb_info = enb_info
        if erab_id is not None:
            self.erab_id = erab_id
        if s_gw_info is not None:
            self.s_gw_info = s_gw_info

    @property
    def enb_info(self):
        """Gets the enb_info of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501


        :return: The enb_info of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :rtype: S1BearerInfoEnbInfo
        """
        return self._enb_info

    @enb_info.setter
    def enb_info(self, enb_info):
        """Sets the enb_info of this S1BearerInfoS1BearerInfoDetailed.


        :param enb_info: The enb_info of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :type: S1BearerInfoEnbInfo
        """

        self._enb_info = enb_info

    @property
    def erab_id(self):
        """Gets the erab_id of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501

        The attribute that uniquely identifies a S1 bearer for a specific UE, as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The erab_id of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :rtype: int
        """
        return self._erab_id

    @erab_id.setter
    def erab_id(self, erab_id):
        """Sets the erab_id of this S1BearerInfoS1BearerInfoDetailed.

        The attribute that uniquely identifies a S1 bearer for a specific UE, as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param erab_id: The erab_id of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :type: int
        """

        self._erab_id = erab_id

    @property
    def s_gw_info(self):
        """Gets the s_gw_info of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501


        :return: The s_gw_info of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :rtype: S1BearerInfoSGwInfo
        """
        return self._s_gw_info

    @s_gw_info.setter
    def s_gw_info(self, s_gw_info):
        """Sets the s_gw_info of this S1BearerInfoS1BearerInfoDetailed.


        :param s_gw_info: The s_gw_info of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :type: S1BearerInfoSGwInfo
        """

        self._s_gw_info = s_gw_info

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
        if issubclass(S1BearerInfoS1BearerInfoDetailed, dict):
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
        if not isinstance(other, S1BearerInfoS1BearerInfoDetailed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other