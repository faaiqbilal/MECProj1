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

class CaReconfNotificationCarrierAggregationMeasInfo(object):
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
        'cell_id_nei': 'CellId',
        'cell_id_srv': 'CellId',
        'rsrp_nei': 'int',
        'rsrp_srv': 'int',
        'rsrq_nei': 'int',
        'rsrq_srv': 'int'
    }

    attribute_map = {
        'cell_id_nei': 'cellIdNei',
        'cell_id_srv': 'cellIdSrv',
        'rsrp_nei': 'rsrpNei',
        'rsrp_srv': 'rsrpSrv',
        'rsrq_nei': 'rsrqNei',
        'rsrq_srv': 'rsrqSrv'
    }

    def __init__(self, cell_id_nei=None, cell_id_srv=None, rsrp_nei=None, rsrp_srv=None, rsrq_nei=None, rsrq_srv=None):  # noqa: E501
        """CaReconfNotificationCarrierAggregationMeasInfo - a model defined in Swagger"""  # noqa: E501
        self._cell_id_nei = None
        self._cell_id_srv = None
        self._rsrp_nei = None
        self._rsrp_srv = None
        self._rsrq_nei = None
        self._rsrq_srv = None
        self.discriminator = None
        if cell_id_nei is not None:
            self.cell_id_nei = cell_id_nei
        if cell_id_srv is not None:
            self.cell_id_srv = cell_id_srv
        if rsrp_nei is not None:
            self.rsrp_nei = rsrp_nei
        if rsrp_srv is not None:
            self.rsrp_srv = rsrp_srv
        if rsrq_nei is not None:
            self.rsrq_nei = rsrq_nei
        if rsrq_srv is not None:
            self.rsrq_srv = rsrq_srv

    @property
    def cell_id_nei(self):
        """Gets the cell_id_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501


        :return: The cell_id_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :rtype: CellId
        """
        return self._cell_id_nei

    @cell_id_nei.setter
    def cell_id_nei(self, cell_id_nei):
        """Sets the cell_id_nei of this CaReconfNotificationCarrierAggregationMeasInfo.


        :param cell_id_nei: The cell_id_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :type: CellId
        """

        self._cell_id_nei = cell_id_nei

    @property
    def cell_id_srv(self):
        """Gets the cell_id_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501


        :return: The cell_id_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :rtype: CellId
        """
        return self._cell_id_srv

    @cell_id_srv.setter
    def cell_id_srv(self, cell_id_srv):
        """Sets the cell_id_srv of this CaReconfNotificationCarrierAggregationMeasInfo.


        :param cell_id_srv: The cell_id_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :type: CellId
        """

        self._cell_id_srv = cell_id_srv

    @property
    def rsrp_nei(self):
        """Gets the rsrp_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501

        Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :return: The rsrp_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :rtype: int
        """
        return self._rsrp_nei

    @rsrp_nei.setter
    def rsrp_nei(self, rsrp_nei):
        """Sets the rsrp_nei of this CaReconfNotificationCarrierAggregationMeasInfo.

        Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :param rsrp_nei: The rsrp_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :type: int
        """

        self._rsrp_nei = rsrp_nei

    @property
    def rsrp_srv(self):
        """Gets the rsrp_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501

        Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :return: The rsrp_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :rtype: int
        """
        return self._rsrp_srv

    @rsrp_srv.setter
    def rsrp_srv(self, rsrp_srv):
        """Sets the rsrp_srv of this CaReconfNotificationCarrierAggregationMeasInfo.

        Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :param rsrp_srv: The rsrp_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :type: int
        """

        self._rsrp_srv = rsrp_srv

    @property
    def rsrq_nei(self):
        """Gets the rsrq_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501

        Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :return: The rsrq_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :rtype: int
        """
        return self._rsrq_nei

    @rsrq_nei.setter
    def rsrq_nei(self, rsrq_nei):
        """Sets the rsrq_nei of this CaReconfNotificationCarrierAggregationMeasInfo.

        Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :param rsrq_nei: The rsrq_nei of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :type: int
        """

        self._rsrq_nei = rsrq_nei

    @property
    def rsrq_srv(self):
        """Gets the rsrq_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501

        Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :return: The rsrq_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :rtype: int
        """
        return self._rsrq_srv

    @rsrq_srv.setter
    def rsrq_srv(self, rsrq_srv):
        """Sets the rsrq_srv of this CaReconfNotificationCarrierAggregationMeasInfo.

        Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :param rsrq_srv: The rsrq_srv of this CaReconfNotificationCarrierAggregationMeasInfo.  # noqa: E501
        :type: int
        """

        self._rsrq_srv = rsrq_srv

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
        if issubclass(CaReconfNotificationCarrierAggregationMeasInfo, dict):
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
        if not isinstance(other, CaReconfNotificationCarrierAggregationMeasInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other