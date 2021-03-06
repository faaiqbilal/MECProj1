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

class S1BearerSubscriptionS1BearerSubscriptionCriteria(object):
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
        'erab_id': 'list[int]'
    }

    attribute_map = {
        'associate_id': 'associateId',
        'ecgi': 'ecgi',
        'erab_id': 'erabId'
    }

    def __init__(self, associate_id=None, ecgi=None, erab_id=None):  # noqa: E501
        """S1BearerSubscriptionS1BearerSubscriptionCriteria - a model defined in Swagger"""  # noqa: E501
        self._associate_id = None
        self._ecgi = None
        self._erab_id = None
        self.discriminator = None
        if associate_id is not None:
            self.associate_id = associate_id
        if ecgi is not None:
            self.ecgi = ecgi
        if erab_id is not None:
            self.erab_id = erab_id

    @property
    def associate_id(self):
        """Gets the associate_id of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501

        0 to N identifiers to associate the events for a specific UE or a flow.  # noqa: E501

        :return: The associate_id of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501
        :rtype: list[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id):
        """Sets the associate_id of this S1BearerSubscriptionS1BearerSubscriptionCriteria.

        0 to N identifiers to associate the events for a specific UE or a flow.  # noqa: E501

        :param associate_id: The associate_id of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501
        :type: list[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self):
        """Gets the ecgi of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :return: The ecgi of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501
        :rtype: list[Ecgi]
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi):
        """Sets the ecgi of this S1BearerSubscriptionS1BearerSubscriptionCriteria.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :param ecgi: The ecgi of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501
        :type: list[Ecgi]
        """

        self._ecgi = ecgi

    @property
    def erab_id(self):
        """Gets the erab_id of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501

        The attribute that uniquely identifies a S1 bearer for a specific UE, as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The erab_id of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501
        :rtype: list[int]
        """
        return self._erab_id

    @erab_id.setter
    def erab_id(self, erab_id):
        """Sets the erab_id of this S1BearerSubscriptionS1BearerSubscriptionCriteria.

        The attribute that uniquely identifies a S1 bearer for a specific UE, as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param erab_id: The erab_id of this S1BearerSubscriptionS1BearerSubscriptionCriteria.  # noqa: E501
        :type: list[int]
        """

        self._erab_id = erab_id

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
        if issubclass(S1BearerSubscriptionS1BearerSubscriptionCriteria, dict):
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
        if not isinstance(other, S1BearerSubscriptionS1BearerSubscriptionCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
