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

class MeasRepUeNotificationNewRadioMeasNeiInfo(object):
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
        'nr_n_cell_info': 'list[MeasRepUeNotificationNrNCellInfo]',
        'nr_n_cell_rsrp': 'int',
        'nr_n_cell_rsrq': 'int',
        'nr_n_cell_rssi': 'int',
        'rs_index_results': 'RsIndexResults'
    }

    attribute_map = {
        'nr_n_cell_info': 'nrNCellInfo',
        'nr_n_cell_rsrp': 'nrNCellRsrp',
        'nr_n_cell_rsrq': 'nrNCellRsrq',
        'nr_n_cell_rssi': 'nrNCellRssi',
        'rs_index_results': 'rsIndexResults'
    }

    def __init__(self, nr_n_cell_info=None, nr_n_cell_rsrp=None, nr_n_cell_rsrq=None, nr_n_cell_rssi=None, rs_index_results=None):  # noqa: E501
        """MeasRepUeNotificationNewRadioMeasNeiInfo - a model defined in Swagger"""  # noqa: E501
        self._nr_n_cell_info = None
        self._nr_n_cell_rsrp = None
        self._nr_n_cell_rsrq = None
        self._nr_n_cell_rssi = None
        self._rs_index_results = None
        self.discriminator = None
        if nr_n_cell_info is not None:
            self.nr_n_cell_info = nr_n_cell_info
        if nr_n_cell_rsrp is not None:
            self.nr_n_cell_rsrp = nr_n_cell_rsrp
        if nr_n_cell_rsrq is not None:
            self.nr_n_cell_rsrq = nr_n_cell_rsrq
        if nr_n_cell_rssi is not None:
            self.nr_n_cell_rssi = nr_n_cell_rssi
        if rs_index_results is not None:
            self.rs_index_results = rs_index_results

    @property
    def nr_n_cell_info(self):
        """Gets the nr_n_cell_info of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501

        5G NR neighbour cell info.  # noqa: E501

        :return: The nr_n_cell_info of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :rtype: list[MeasRepUeNotificationNrNCellInfo]
        """
        return self._nr_n_cell_info

    @nr_n_cell_info.setter
    def nr_n_cell_info(self, nr_n_cell_info):
        """Sets the nr_n_cell_info of this MeasRepUeNotificationNewRadioMeasNeiInfo.

        5G NR neighbour cell info.  # noqa: E501

        :param nr_n_cell_info: The nr_n_cell_info of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :type: list[MeasRepUeNotificationNrNCellInfo]
        """

        self._nr_n_cell_info = nr_n_cell_info

    @property
    def nr_n_cell_rsrp(self):
        """Gets the nr_n_cell_rsrp of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501

        Reference Signal Received Power measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_n_cell_rsrp of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :rtype: int
        """
        return self._nr_n_cell_rsrp

    @nr_n_cell_rsrp.setter
    def nr_n_cell_rsrp(self, nr_n_cell_rsrp):
        """Sets the nr_n_cell_rsrp of this MeasRepUeNotificationNewRadioMeasNeiInfo.

        Reference Signal Received Power measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_n_cell_rsrp: The nr_n_cell_rsrp of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :type: int
        """

        self._nr_n_cell_rsrp = nr_n_cell_rsrp

    @property
    def nr_n_cell_rsrq(self):
        """Gets the nr_n_cell_rsrq of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501

        Reference Signal Received Quality measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_n_cell_rsrq of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :rtype: int
        """
        return self._nr_n_cell_rsrq

    @nr_n_cell_rsrq.setter
    def nr_n_cell_rsrq(self, nr_n_cell_rsrq):
        """Sets the nr_n_cell_rsrq of this MeasRepUeNotificationNewRadioMeasNeiInfo.

        Reference Signal Received Quality measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_n_cell_rsrq: The nr_n_cell_rsrq of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :type: int
        """

        self._nr_n_cell_rsrq = nr_n_cell_rsrq

    @property
    def nr_n_cell_rssi(self):
        """Gets the nr_n_cell_rssi of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501

        Reference signal SINR measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_n_cell_rssi of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :rtype: int
        """
        return self._nr_n_cell_rssi

    @nr_n_cell_rssi.setter
    def nr_n_cell_rssi(self, nr_n_cell_rssi):
        """Sets the nr_n_cell_rssi of this MeasRepUeNotificationNewRadioMeasNeiInfo.

        Reference signal SINR measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_n_cell_rssi: The nr_n_cell_rssi of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :type: int
        """

        self._nr_n_cell_rssi = nr_n_cell_rssi

    @property
    def rs_index_results(self):
        """Gets the rs_index_results of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501


        :return: The rs_index_results of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :rtype: RsIndexResults
        """
        return self._rs_index_results

    @rs_index_results.setter
    def rs_index_results(self, rs_index_results):
        """Sets the rs_index_results of this MeasRepUeNotificationNewRadioMeasNeiInfo.


        :param rs_index_results: The rs_index_results of this MeasRepUeNotificationNewRadioMeasNeiInfo.  # noqa: E501
        :type: RsIndexResults
        """

        self._rs_index_results = rs_index_results

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
        if issubclass(MeasRepUeNotificationNewRadioMeasNeiInfo, dict):
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
        if not isinstance(other, MeasRepUeNotificationNewRadioMeasNeiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
