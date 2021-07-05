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

class RabRelNotification(object):
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
        'associate_id': 'list[AssociateId]',
        'ecgi': 'Ecgi',
        'erab_release_info': 'RabRelNotificationErabReleaseInfo',
        'notification_type': 'str',
        'time_stamp': 'TimeStamp'
    }

    attribute_map = {
        'associate_id': 'associateId',
        'ecgi': 'ecgi',
        'erab_release_info': 'erabReleaseInfo',
        'notification_type': 'notificationType',
        'time_stamp': 'timeStamp'
    }

    def __init__(self, associate_id=None, ecgi=None, erab_release_info=None, notification_type=None, time_stamp=None):  # noqa: E501
        """RabRelNotification - a model defined in Swagger"""  # noqa: E501
        self._associate_id = None
        self._ecgi = None
        self._erab_release_info = None
        self._notification_type = None
        self._time_stamp = None
        self.discriminator = None
        if associate_id is not None:
            self.associate_id = associate_id
        self.ecgi = ecgi
        self.erab_release_info = erab_release_info
        self.notification_type = notification_type
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def associate_id(self):
        """Gets the associate_id of this RabRelNotification.  # noqa: E501

        0 to N identifiers to bind the event for a specific UE or flow as defined below.  # noqa: E501

        :return: The associate_id of this RabRelNotification.  # noqa: E501
        :rtype: list[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id):
        """Sets the associate_id of this RabRelNotification.

        0 to N identifiers to bind the event for a specific UE or flow as defined below.  # noqa: E501

        :param associate_id: The associate_id of this RabRelNotification.  # noqa: E501
        :type: list[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self):
        """Gets the ecgi of this RabRelNotification.  # noqa: E501


        :return: The ecgi of this RabRelNotification.  # noqa: E501
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi):
        """Sets the ecgi of this RabRelNotification.


        :param ecgi: The ecgi of this RabRelNotification.  # noqa: E501
        :type: Ecgi
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi

    @property
    def erab_release_info(self):
        """Gets the erab_release_info of this RabRelNotification.  # noqa: E501


        :return: The erab_release_info of this RabRelNotification.  # noqa: E501
        :rtype: RabRelNotificationErabReleaseInfo
        """
        return self._erab_release_info

    @erab_release_info.setter
    def erab_release_info(self, erab_release_info):
        """Sets the erab_release_info of this RabRelNotification.


        :param erab_release_info: The erab_release_info of this RabRelNotification.  # noqa: E501
        :type: RabRelNotificationErabReleaseInfo
        """
        if erab_release_info is None:
            raise ValueError("Invalid value for `erab_release_info`, must not be `None`")  # noqa: E501

        self._erab_release_info = erab_release_info

    @property
    def notification_type(self):
        """Gets the notification_type of this RabRelNotification.  # noqa: E501

        Shall be set to \"RabRelNotification\".  # noqa: E501

        :return: The notification_type of this RabRelNotification.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this RabRelNotification.

        Shall be set to \"RabRelNotification\".  # noqa: E501

        :param notification_type: The notification_type of this RabRelNotification.  # noqa: E501
        :type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def time_stamp(self):
        """Gets the time_stamp of this RabRelNotification.  # noqa: E501


        :return: The time_stamp of this RabRelNotification.  # noqa: E501
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this RabRelNotification.


        :param time_stamp: The time_stamp of this RabRelNotification.  # noqa: E501
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
        if issubclass(RabRelNotification, dict):
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
        if not isinstance(other, RabRelNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
