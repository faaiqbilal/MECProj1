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

class MeasRepUeNotificationNrBNCs(object):
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
        'nr_bn_cell_info': 'list[MeasRepUeNotificationNrBNCsNrBNCellInfo]',
        'nr_bn_cell_rsrp': 'int',
        'nr_bn_cell_rsrq': 'int',
        'nr_bn_cell_rssi': 'int'
    }

    attribute_map = {
        'nr_bn_cell_info': 'nrBNCellInfo',
        'nr_bn_cell_rsrp': 'nrBNCellRsrp',
        'nr_bn_cell_rsrq': 'nrBNCellRsrq',
        'nr_bn_cell_rssi': 'nrBNCellRssi'
    }

    def __init__(self, nr_bn_cell_info=None, nr_bn_cell_rsrp=None, nr_bn_cell_rsrq=None, nr_bn_cell_rssi=None):  # noqa: E501
        """MeasRepUeNotificationNrBNCs - a model defined in Swagger"""  # noqa: E501
        self._nr_bn_cell_info = None
        self._nr_bn_cell_rsrp = None
        self._nr_bn_cell_rsrq = None
        self._nr_bn_cell_rssi = None
        self.discriminator = None
        self.nr_bn_cell_info = nr_bn_cell_info
        if nr_bn_cell_rsrp is not None:
            self.nr_bn_cell_rsrp = nr_bn_cell_rsrp
        if nr_bn_cell_rsrq is not None:
            self.nr_bn_cell_rsrq = nr_bn_cell_rsrq
        if nr_bn_cell_rssi is not None:
            self.nr_bn_cell_rssi = nr_bn_cell_rssi

    @property
    def nr_bn_cell_info(self):
        """Gets the nr_bn_cell_info of this MeasRepUeNotificationNrBNCs.  # noqa: E501

        Best neighbours of the secondary serving cell(s) info  # noqa: E501

        :return: The nr_bn_cell_info of this MeasRepUeNotificationNrBNCs.  # noqa: E501
        :rtype: list[MeasRepUeNotificationNrBNCsNrBNCellInfo]
        """
        return self._nr_bn_cell_info

    @nr_bn_cell_info.setter
    def nr_bn_cell_info(self, nr_bn_cell_info):
        """Sets the nr_bn_cell_info of this MeasRepUeNotificationNrBNCs.

        Best neighbours of the secondary serving cell(s) info  # noqa: E501

        :param nr_bn_cell_info: The nr_bn_cell_info of this MeasRepUeNotificationNrBNCs.  # noqa: E501
        :type: list[MeasRepUeNotificationNrBNCsNrBNCellInfo]
        """
        if nr_bn_cell_info is None:
            raise ValueError("Invalid value for `nr_bn_cell_info`, must not be `None`")  # noqa: E501

        self._nr_bn_cell_info = nr_bn_cell_info

    @property
    def nr_bn_cell_rsrp(self):
        """Gets the nr_bn_cell_rsrp of this MeasRepUeNotificationNrBNCs.  # noqa: E501

        Reference Signal Received Power measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_bn_cell_rsrp of this MeasRepUeNotificationNrBNCs.  # noqa: E501
        :rtype: int
        """
        return self._nr_bn_cell_rsrp

    @nr_bn_cell_rsrp.setter
    def nr_bn_cell_rsrp(self, nr_bn_cell_rsrp):
        """Sets the nr_bn_cell_rsrp of this MeasRepUeNotificationNrBNCs.

        Reference Signal Received Power measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_bn_cell_rsrp: The nr_bn_cell_rsrp of this MeasRepUeNotificationNrBNCs.  # noqa: E501
        :type: int
        """

        self._nr_bn_cell_rsrp = nr_bn_cell_rsrp

    @property
    def nr_bn_cell_rsrq(self):
        """Gets the nr_bn_cell_rsrq of this MeasRepUeNotificationNrBNCs.  # noqa: E501

        Reference Signal Received Quality measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_bn_cell_rsrq of this MeasRepUeNotificationNrBNCs.  # noqa: E501
        :rtype: int
        """
        return self._nr_bn_cell_rsrq

    @nr_bn_cell_rsrq.setter
    def nr_bn_cell_rsrq(self, nr_bn_cell_rsrq):
        """Sets the nr_bn_cell_rsrq of this MeasRepUeNotificationNrBNCs.

        Reference Signal Received Quality measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_bn_cell_rsrq: The nr_bn_cell_rsrq of this MeasRepUeNotificationNrBNCs.  # noqa: E501
        :type: int
        """

        self._nr_bn_cell_rsrq = nr_bn_cell_rsrq

    @property
    def nr_bn_cell_rssi(self):
        """Gets the nr_bn_cell_rssi of this MeasRepUeNotificationNrBNCs.  # noqa: E501

        Reference signal SINR measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_bn_cell_rssi of this MeasRepUeNotificationNrBNCs.  # noqa: E501
        :rtype: int
        """
        return self._nr_bn_cell_rssi

    @nr_bn_cell_rssi.setter
    def nr_bn_cell_rssi(self, nr_bn_cell_rssi):
        """Sets the nr_bn_cell_rssi of this MeasRepUeNotificationNrBNCs.

        Reference signal SINR measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_bn_cell_rssi: The nr_bn_cell_rssi of this MeasRepUeNotificationNrBNCs.  # noqa: E501
        :type: int
        """

        self._nr_bn_cell_rssi = nr_bn_cell_rssi

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
        if issubclass(MeasRepUeNotificationNrBNCs, dict):
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
        if not isinstance(other, MeasRepUeNotificationNrBNCs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other