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

class ResultsPerCsiRsIndexListResultsPerCsiRsIndex(object):
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
        'csi_rs_index': 'int',
        'csi_rs_results': 'MeasQuantityResultsNr'
    }

    attribute_map = {
        'csi_rs_index': 'csiRsIndex',
        'csi_rs_results': 'csiRsResults'
    }

    def __init__(self, csi_rs_index=None, csi_rs_results=None):  # noqa: E501
        """ResultsPerCsiRsIndexListResultsPerCsiRsIndex - a model defined in Swagger"""  # noqa: E501
        self._csi_rs_index = None
        self._csi_rs_results = None
        self.discriminator = None
        if csi_rs_index is not None:
            self.csi_rs_index = csi_rs_index
        if csi_rs_results is not None:
            self.csi_rs_results = csi_rs_results

    @property
    def csi_rs_index(self):
        """Gets the csi_rs_index of this ResultsPerCsiRsIndexListResultsPerCsiRsIndex.  # noqa: E501


        :return: The csi_rs_index of this ResultsPerCsiRsIndexListResultsPerCsiRsIndex.  # noqa: E501
        :rtype: int
        """
        return self._csi_rs_index

    @csi_rs_index.setter
    def csi_rs_index(self, csi_rs_index):
        """Sets the csi_rs_index of this ResultsPerCsiRsIndexListResultsPerCsiRsIndex.


        :param csi_rs_index: The csi_rs_index of this ResultsPerCsiRsIndexListResultsPerCsiRsIndex.  # noqa: E501
        :type: int
        """

        self._csi_rs_index = csi_rs_index

    @property
    def csi_rs_results(self):
        """Gets the csi_rs_results of this ResultsPerCsiRsIndexListResultsPerCsiRsIndex.  # noqa: E501


        :return: The csi_rs_results of this ResultsPerCsiRsIndexListResultsPerCsiRsIndex.  # noqa: E501
        :rtype: MeasQuantityResultsNr
        """
        return self._csi_rs_results

    @csi_rs_results.setter
    def csi_rs_results(self, csi_rs_results):
        """Sets the csi_rs_results of this ResultsPerCsiRsIndexListResultsPerCsiRsIndex.


        :param csi_rs_results: The csi_rs_results of this ResultsPerCsiRsIndexListResultsPerCsiRsIndex.  # noqa: E501
        :type: MeasQuantityResultsNr
        """

        self._csi_rs_results = csi_rs_results

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
        if issubclass(ResultsPerCsiRsIndexListResultsPerCsiRsIndex, dict):
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
        if not isinstance(other, ResultsPerCsiRsIndexListResultsPerCsiRsIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other