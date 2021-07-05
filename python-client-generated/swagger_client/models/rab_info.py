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

class RabInfo(object):
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
        'cell_user_info': 'list[RabInfoCellUserInfo]',
        'request_id': 'str',
        'time_stamp': 'TimeStamp'
    }

    attribute_map = {
        'app_instance_id': 'appInstanceId',
        'cell_user_info': 'cellUserInfo',
        'request_id': 'requestId',
        'time_stamp': 'timeStamp'
    }

    def __init__(self, app_instance_id=None, cell_user_info=None, request_id=None, time_stamp=None):  # noqa: E501
        """RabInfo - a model defined in Swagger"""  # noqa: E501
        self._app_instance_id = None
        self._cell_user_info = None
        self._request_id = None
        self._time_stamp = None
        self.discriminator = None
        self.app_instance_id = app_instance_id
        if cell_user_info is not None:
            self.cell_user_info = cell_user_info
        self.request_id = request_id
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def app_instance_id(self):
        """Gets the app_instance_id of this RabInfo.  # noqa: E501

        Unique identifier for the MEC application instance.  # noqa: E501

        :return: The app_instance_id of this RabInfo.  # noqa: E501
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id):
        """Sets the app_instance_id of this RabInfo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this RabInfo.  # noqa: E501
        :type: str
        """
        if app_instance_id is None:
            raise ValueError("Invalid value for `app_instance_id`, must not be `None`")  # noqa: E501

        self._app_instance_id = app_instance_id

    @property
    def cell_user_info(self):
        """Gets the cell_user_info of this RabInfo.  # noqa: E501

        The information on users per cell as defined below.  # noqa: E501

        :return: The cell_user_info of this RabInfo.  # noqa: E501
        :rtype: list[RabInfoCellUserInfo]
        """
        return self._cell_user_info

    @cell_user_info.setter
    def cell_user_info(self, cell_user_info):
        """Sets the cell_user_info of this RabInfo.

        The information on users per cell as defined below.  # noqa: E501

        :param cell_user_info: The cell_user_info of this RabInfo.  # noqa: E501
        :type: list[RabInfoCellUserInfo]
        """

        self._cell_user_info = cell_user_info

    @property
    def request_id(self):
        """Gets the request_id of this RabInfo.  # noqa: E501

        Unique identifier allocated by the service consumer for the RAB Information request.  # noqa: E501

        :return: The request_id of this RabInfo.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this RabInfo.

        Unique identifier allocated by the service consumer for the RAB Information request.  # noqa: E501

        :param request_id: The request_id of this RabInfo.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def time_stamp(self):
        """Gets the time_stamp of this RabInfo.  # noqa: E501


        :return: The time_stamp of this RabInfo.  # noqa: E501
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this RabInfo.


        :param time_stamp: The time_stamp of this RabInfo.  # noqa: E501
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
        if issubclass(RabInfo, dict):
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
        if not isinstance(other, RabInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other