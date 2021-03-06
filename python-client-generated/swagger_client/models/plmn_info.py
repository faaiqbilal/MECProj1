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

class PlmnInfo(object):
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
        'app_instance_id': 'str',
        'plmn': 'list[Plmn]',
        'time_stamp': 'TimeStamp'
    }

    attribute_map = {
        'app_instance_id': 'appInstanceId',
        'plmn': 'plmn',
        'time_stamp': 'timeStamp'
    }

    def __init__(self, app_instance_id=None, plmn=None, time_stamp=None):  # noqa: E501
        """PlmnInfo - a model defined in Swagger"""  # noqa: E501
        self._app_instance_id = None
        self._plmn = None
        self._time_stamp = None
        self.discriminator = None
        self.app_instance_id = app_instance_id
        self.plmn = plmn
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def app_instance_id(self):
        """Gets the app_instance_id of this PlmnInfo.  # noqa: E501

        Unique identifier for the MEC application instance.  # noqa: E501

        :return: The app_instance_id of this PlmnInfo.  # noqa: E501
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id):
        """Sets the app_instance_id of this PlmnInfo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this PlmnInfo.  # noqa: E501
        :type: str
        """
        if app_instance_id is None:
            raise ValueError("Invalid value for `app_instance_id`, must not be `None`")  # noqa: E501

        self._app_instance_id = app_instance_id

    @property
    def plmn(self):
        """Gets the plmn of this PlmnInfo.  # noqa: E501

        Public Land Mobile Network Identity.  # noqa: E501

        :return: The plmn of this PlmnInfo.  # noqa: E501
        :rtype: list[Plmn]
        """
        return self._plmn

    @plmn.setter
    def plmn(self, plmn):
        """Sets the plmn of this PlmnInfo.

        Public Land Mobile Network Identity.  # noqa: E501

        :param plmn: The plmn of this PlmnInfo.  # noqa: E501
        :type: list[Plmn]
        """
        if plmn is None:
            raise ValueError("Invalid value for `plmn`, must not be `None`")  # noqa: E501

        self._plmn = plmn

    @property
    def time_stamp(self):
        """Gets the time_stamp of this PlmnInfo.  # noqa: E501


        :return: The time_stamp of this PlmnInfo.  # noqa: E501
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this PlmnInfo.


        :param time_stamp: The time_stamp of this PlmnInfo.  # noqa: E501
        :type: TimeStamp
        """

        self._time_stamp = time_stamp

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
        if issubclass(PlmnInfo, dict):
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
        if not isinstance(other, PlmnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
