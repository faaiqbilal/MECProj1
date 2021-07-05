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

class ResultsPerSsbIndexList(object):
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
        'results_per_ssb_index': 'list[ResultsPerSsbIndexListResultsPerSsbIndex]'
    }

    attribute_map = {
        'results_per_ssb_index': 'resultsPerSsbIndex'
    }

    def __init__(self, results_per_ssb_index=None):  # noqa: E501
        """ResultsPerSsbIndexList - a model defined in Swagger"""  # noqa: E501
        self._results_per_ssb_index = None
        self.discriminator = None
        if results_per_ssb_index is not None:
            self.results_per_ssb_index = results_per_ssb_index

    @property
    def results_per_ssb_index(self):
        """Gets the results_per_ssb_index of this ResultsPerSsbIndexList.  # noqa: E501


        :return: The results_per_ssb_index of this ResultsPerSsbIndexList.  # noqa: E501
        :rtype: list[ResultsPerSsbIndexListResultsPerSsbIndex]
        """
        return self._results_per_ssb_index

    @results_per_ssb_index.setter
    def results_per_ssb_index(self, results_per_ssb_index):
        """Sets the results_per_ssb_index of this ResultsPerSsbIndexList.


        :param results_per_ssb_index: The results_per_ssb_index of this ResultsPerSsbIndexList.  # noqa: E501
        :type: list[ResultsPerSsbIndexListResultsPerSsbIndex]
        """

        self._results_per_ssb_index = results_per_ssb_index

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
        if issubclass(ResultsPerSsbIndexList, dict):
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
        if not isinstance(other, ResultsPerSsbIndexList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
