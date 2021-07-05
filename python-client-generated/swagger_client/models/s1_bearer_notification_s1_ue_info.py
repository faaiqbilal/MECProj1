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

class S1BearerNotificationS1UeInfo(object):
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
        'ecgi': 'list[Ecgi]',
        's1_bearer_info': 'list[S1BearerInfoS1BearerInfoDetailed]',
        'temp_ue_id': 'CellChangeNotificationTempUeId'
    }

    attribute_map = {
        'associate_id': 'associateId',
        'ecgi': 'ecgi',
        's1_bearer_info': 's1BearerInfo',
        'temp_ue_id': 'tempUeId'
    }

    def __init__(self, associate_id=None, ecgi=None, s1_bearer_info=None, temp_ue_id=None):  # noqa: E501
        """S1BearerNotificationS1UeInfo - a model defined in Swagger"""  # noqa: E501
        self._associate_id = None
        self._ecgi = None
        self._s1_bearer_info = None
        self._temp_ue_id = None
        self.discriminator = None
        if associate_id is not None:
            self.associate_id = associate_id
        self.ecgi = ecgi
        self.s1_bearer_info = s1_bearer_info
        if temp_ue_id is not None:
            self.temp_ue_id = temp_ue_id

    @property
    def associate_id(self):
        """Gets the associate_id of this S1BearerNotificationS1UeInfo.  # noqa: E501

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this S1BearerNotificationS1UeInfo.  # noqa: E501
        :rtype: list[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id):
        """Sets the associate_id of this S1BearerNotificationS1UeInfo.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this S1BearerNotificationS1UeInfo.  # noqa: E501
        :type: list[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self):
        """Gets the ecgi of this S1BearerNotificationS1UeInfo.  # noqa: E501

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :return: The ecgi of this S1BearerNotificationS1UeInfo.  # noqa: E501
        :rtype: list[Ecgi]
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi):
        """Sets the ecgi of this S1BearerNotificationS1UeInfo.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :param ecgi: The ecgi of this S1BearerNotificationS1UeInfo.  # noqa: E501
        :type: list[Ecgi]
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi

    @property
    def s1_bearer_info(self):
        """Gets the s1_bearer_info of this S1BearerNotificationS1UeInfo.  # noqa: E501

        S1 bearer information as defined below.  # noqa: E501

        :return: The s1_bearer_info of this S1BearerNotificationS1UeInfo.  # noqa: E501
        :rtype: list[S1BearerInfoS1BearerInfoDetailed]
        """
        return self._s1_bearer_info

    @s1_bearer_info.setter
    def s1_bearer_info(self, s1_bearer_info):
        """Sets the s1_bearer_info of this S1BearerNotificationS1UeInfo.

        S1 bearer information as defined below.  # noqa: E501

        :param s1_bearer_info: The s1_bearer_info of this S1BearerNotificationS1UeInfo.  # noqa: E501
        :type: list[S1BearerInfoS1BearerInfoDetailed]
        """
        if s1_bearer_info is None:
            raise ValueError("Invalid value for `s1_bearer_info`, must not be `None`")  # noqa: E501

        self._s1_bearer_info = s1_bearer_info

    @property
    def temp_ue_id(self):
        """Gets the temp_ue_id of this S1BearerNotificationS1UeInfo.  # noqa: E501


        :return: The temp_ue_id of this S1BearerNotificationS1UeInfo.  # noqa: E501
        :rtype: CellChangeNotificationTempUeId
        """
        return self._temp_ue_id

    @temp_ue_id.setter
    def temp_ue_id(self, temp_ue_id):
        """Sets the temp_ue_id of this S1BearerNotificationS1UeInfo.


        :param temp_ue_id: The temp_ue_id of this S1BearerNotificationS1UeInfo.  # noqa: E501
        :type: CellChangeNotificationTempUeId
        """

        self._temp_ue_id = temp_ue_id

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
        if issubclass(S1BearerNotificationS1UeInfo, dict):
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
        if not isinstance(other, S1BearerNotificationS1UeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
