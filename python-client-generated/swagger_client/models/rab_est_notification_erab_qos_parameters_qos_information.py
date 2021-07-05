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

class RabEstNotificationErabQosParametersQosInformation(object):
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
        'erab_gbr_dl': 'int',
        'erab_gbr_ul': 'int',
        'erab_mbr_dl': 'int',
        'erab_mbr_ul': 'int'
    }

    attribute_map = {
        'erab_gbr_dl': 'erabGbrDl',
        'erab_gbr_ul': 'erabGbrUl',
        'erab_mbr_dl': 'erabMbrDl',
        'erab_mbr_ul': 'erabMbrUl'
    }

    def __init__(self, erab_gbr_dl=None, erab_gbr_ul=None, erab_mbr_dl=None, erab_mbr_ul=None):  # noqa: E501
        """RabEstNotificationErabQosParametersQosInformation - a model defined in Swagger"""  # noqa: E501
        self._erab_gbr_dl = None
        self._erab_gbr_ul = None
        self._erab_mbr_dl = None
        self._erab_mbr_ul = None
        self.discriminator = None
        self.erab_gbr_dl = erab_gbr_dl
        self.erab_gbr_ul = erab_gbr_ul
        self.erab_mbr_dl = erab_mbr_dl
        self.erab_mbr_ul = erab_mbr_ul

    @property
    def erab_gbr_dl(self):
        """Gets the erab_gbr_dl of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501

        This attribute indicates the guaranteed downlink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :return: The erab_gbr_dl of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501
        :rtype: int
        """
        return self._erab_gbr_dl

    @erab_gbr_dl.setter
    def erab_gbr_dl(self, erab_gbr_dl):
        """Sets the erab_gbr_dl of this RabEstNotificationErabQosParametersQosInformation.

        This attribute indicates the guaranteed downlink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :param erab_gbr_dl: The erab_gbr_dl of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501
        :type: int
        """
        if erab_gbr_dl is None:
            raise ValueError("Invalid value for `erab_gbr_dl`, must not be `None`")  # noqa: E501

        self._erab_gbr_dl = erab_gbr_dl

    @property
    def erab_gbr_ul(self):
        """Gets the erab_gbr_ul of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501

        This attribute indicates the guaranteed uplink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :return: The erab_gbr_ul of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501
        :rtype: int
        """
        return self._erab_gbr_ul

    @erab_gbr_ul.setter
    def erab_gbr_ul(self, erab_gbr_ul):
        """Sets the erab_gbr_ul of this RabEstNotificationErabQosParametersQosInformation.

        This attribute indicates the guaranteed uplink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :param erab_gbr_ul: The erab_gbr_ul of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501
        :type: int
        """
        if erab_gbr_ul is None:
            raise ValueError("Invalid value for `erab_gbr_ul`, must not be `None`")  # noqa: E501

        self._erab_gbr_ul = erab_gbr_ul

    @property
    def erab_mbr_dl(self):
        """Gets the erab_mbr_dl of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501

        This attribute indicates the maximum downlink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :return: The erab_mbr_dl of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501
        :rtype: int
        """
        return self._erab_mbr_dl

    @erab_mbr_dl.setter
    def erab_mbr_dl(self, erab_mbr_dl):
        """Sets the erab_mbr_dl of this RabEstNotificationErabQosParametersQosInformation.

        This attribute indicates the maximum downlink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :param erab_mbr_dl: The erab_mbr_dl of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501
        :type: int
        """
        if erab_mbr_dl is None:
            raise ValueError("Invalid value for `erab_mbr_dl`, must not be `None`")  # noqa: E501

        self._erab_mbr_dl = erab_mbr_dl

    @property
    def erab_mbr_ul(self):
        """Gets the erab_mbr_ul of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501

        This attribute indicates the maximum uplink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :return: The erab_mbr_ul of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501
        :rtype: int
        """
        return self._erab_mbr_ul

    @erab_mbr_ul.setter
    def erab_mbr_ul(self, erab_mbr_ul):
        """Sets the erab_mbr_ul of this RabEstNotificationErabQosParametersQosInformation.

        This attribute indicates the maximum uplink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :param erab_mbr_ul: The erab_mbr_ul of this RabEstNotificationErabQosParametersQosInformation.  # noqa: E501
        :type: int
        """
        if erab_mbr_ul is None:
            raise ValueError("Invalid value for `erab_mbr_ul`, must not be `None`")  # noqa: E501

        self._erab_mbr_ul = erab_mbr_ul

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
        if issubclass(RabEstNotificationErabQosParametersQosInformation, dict):
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
        if not isinstance(other, RabEstNotificationErabQosParametersQosInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
