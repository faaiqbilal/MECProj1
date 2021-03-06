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

class RsIndexResults(object):
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
        'results_csi_rs_indexes': 'ResultsPerCsiRsIndexList',
        'results_ssb_indexes': 'ResultsPerSsbIndexList'
    }

    attribute_map = {
        'results_csi_rs_indexes': 'resultsCsiRsIndexes',
        'results_ssb_indexes': 'resultsSsbIndexes'
    }

    def __init__(self, results_csi_rs_indexes=None, results_ssb_indexes=None):  # noqa: E501
        """RsIndexResults - a model defined in Swagger"""  # noqa: E501
        self._results_csi_rs_indexes = None
        self._results_ssb_indexes = None
        self.discriminator = None
        self.results_csi_rs_indexes = results_csi_rs_indexes
        self.results_ssb_indexes = results_ssb_indexes

    @property
    def results_csi_rs_indexes(self):
        """Gets the results_csi_rs_indexes of this RsIndexResults.  # noqa: E501


        :return: The results_csi_rs_indexes of this RsIndexResults.  # noqa: E501
        :rtype: ResultsPerCsiRsIndexList
        """
        return self._results_csi_rs_indexes

    @results_csi_rs_indexes.setter
    def results_csi_rs_indexes(self, results_csi_rs_indexes):
        """Sets the results_csi_rs_indexes of this RsIndexResults.


        :param results_csi_rs_indexes: The results_csi_rs_indexes of this RsIndexResults.  # noqa: E501
        :type: ResultsPerCsiRsIndexList
        """
        if results_csi_rs_indexes is None:
            raise ValueError("Invalid value for `results_csi_rs_indexes`, must not be `None`")  # noqa: E501

        self._results_csi_rs_indexes = results_csi_rs_indexes

    @property
    def results_ssb_indexes(self):
        """Gets the results_ssb_indexes of this RsIndexResults.  # noqa: E501


        :return: The results_ssb_indexes of this RsIndexResults.  # noqa: E501
        :rtype: ResultsPerSsbIndexList
        """
        return self._results_ssb_indexes

    @results_ssb_indexes.setter
    def results_ssb_indexes(self, results_ssb_indexes):
        """Sets the results_ssb_indexes of this RsIndexResults.


        :param results_ssb_indexes: The results_ssb_indexes of this RsIndexResults.  # noqa: E501
        :type: ResultsPerSsbIndexList
        """
        if results_ssb_indexes is None:
            raise ValueError("Invalid value for `results_ssb_indexes`, must not be `None`")  # noqa: E501

        self._results_ssb_indexes = results_ssb_indexes

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
        if issubclass(RsIndexResults, dict):
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
        if not isinstance(other, RsIndexResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
