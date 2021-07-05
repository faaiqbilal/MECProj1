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

class ResultsPerSsbIndexListResultsPerSsbIndex(object):
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
        'ssb_index': 'int',
        'ssb_results': 'MeasQuantityResultsNr'
    }

    attribute_map = {
        'ssb_index': 'ssbIndex',
        'ssb_results': 'ssbResults'
    }

    def __init__(self, ssb_index=None, ssb_results=None):  # noqa: E501
        """ResultsPerSsbIndexListResultsPerSsbIndex - a model defined in Swagger"""  # noqa: E501
        self._ssb_index = None
        self._ssb_results = None
        self.discriminator = None
        if ssb_index is not None:
            self.ssb_index = ssb_index
        if ssb_results is not None:
            self.ssb_results = ssb_results

    @property
    def ssb_index(self):
        """Gets the ssb_index of this ResultsPerSsbIndexListResultsPerSsbIndex.  # noqa: E501


        :return: The ssb_index of this ResultsPerSsbIndexListResultsPerSsbIndex.  # noqa: E501
        :rtype: int
        """
        return self._ssb_index

    @ssb_index.setter
    def ssb_index(self, ssb_index):
        """Sets the ssb_index of this ResultsPerSsbIndexListResultsPerSsbIndex.


        :param ssb_index: The ssb_index of this ResultsPerSsbIndexListResultsPerSsbIndex.  # noqa: E501
        :type: int
        """

        self._ssb_index = ssb_index

    @property
    def ssb_results(self):
        """Gets the ssb_results of this ResultsPerSsbIndexListResultsPerSsbIndex.  # noqa: E501


        :return: The ssb_results of this ResultsPerSsbIndexListResultsPerSsbIndex.  # noqa: E501
        :rtype: MeasQuantityResultsNr
        """
        return self._ssb_results

    @ssb_results.setter
    def ssb_results(self, ssb_results):
        """Sets the ssb_results of this ResultsPerSsbIndexListResultsPerSsbIndex.


        :param ssb_results: The ssb_results of this ResultsPerSsbIndexListResultsPerSsbIndex.  # noqa: E501
        :type: MeasQuantityResultsNr
        """

        self._ssb_results = ssb_results

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
        if issubclass(ResultsPerSsbIndexListResultsPerSsbIndex, dict):
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
        if not isinstance(other, ResultsPerSsbIndexListResultsPerSsbIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other