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

class MeasRepUeSubscription(object):
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
        'links': 'CaReconfSubscriptionLinks',
        'callback_reference': 'str',
        'expiry_deadline': 'TimeStamp',
        'filter_criteria_assoc_tri': 'MeasRepUeSubscriptionFilterCriteriaAssocTri',
        'subscription_type': 'str'
    }

    attribute_map = {
        'links': '_links',
        'callback_reference': 'callbackReference',
        'expiry_deadline': 'expiryDeadline',
        'filter_criteria_assoc_tri': 'filterCriteriaAssocTri',
        'subscription_type': 'subscriptionType'
    }

    def __init__(self, links=None, callback_reference=None, expiry_deadline=None, filter_criteria_assoc_tri=None, subscription_type=None):  # noqa: E501
        """MeasRepUeSubscription - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._callback_reference = None
        self._expiry_deadline = None
        self._filter_criteria_assoc_tri = None
        self._subscription_type = None
        self.discriminator = None
        if links is not None:
            self.links = links
        self.callback_reference = callback_reference
        if expiry_deadline is not None:
            self.expiry_deadline = expiry_deadline
        self.filter_criteria_assoc_tri = filter_criteria_assoc_tri
        self.subscription_type = subscription_type

    @property
    def links(self):
        """Gets the links of this MeasRepUeSubscription.  # noqa: E501


        :return: The links of this MeasRepUeSubscription.  # noqa: E501
        :rtype: CaReconfSubscriptionLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MeasRepUeSubscription.


        :param links: The links of this MeasRepUeSubscription.  # noqa: E501
        :type: CaReconfSubscriptionLinks
        """

        self._links = links

    @property
    def callback_reference(self):
        """Gets the callback_reference of this MeasRepUeSubscription.  # noqa: E501

        URI selected by the service consumer to receive notifications on the subscribed RNIS information. This shall be included both in the request and in response.  # noqa: E501

        :return: The callback_reference of this MeasRepUeSubscription.  # noqa: E501
        :rtype: str
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference):
        """Sets the callback_reference of this MeasRepUeSubscription.

        URI selected by the service consumer to receive notifications on the subscribed RNIS information. This shall be included both in the request and in response.  # noqa: E501

        :param callback_reference: The callback_reference of this MeasRepUeSubscription.  # noqa: E501
        :type: str
        """
        if callback_reference is None:
            raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

        self._callback_reference = callback_reference

    @property
    def expiry_deadline(self):
        """Gets the expiry_deadline of this MeasRepUeSubscription.  # noqa: E501


        :return: The expiry_deadline of this MeasRepUeSubscription.  # noqa: E501
        :rtype: TimeStamp
        """
        return self._expiry_deadline

    @expiry_deadline.setter
    def expiry_deadline(self, expiry_deadline):
        """Sets the expiry_deadline of this MeasRepUeSubscription.


        :param expiry_deadline: The expiry_deadline of this MeasRepUeSubscription.  # noqa: E501
        :type: TimeStamp
        """

        self._expiry_deadline = expiry_deadline

    @property
    def filter_criteria_assoc_tri(self):
        """Gets the filter_criteria_assoc_tri of this MeasRepUeSubscription.  # noqa: E501


        :return: The filter_criteria_assoc_tri of this MeasRepUeSubscription.  # noqa: E501
        :rtype: MeasRepUeSubscriptionFilterCriteriaAssocTri
        """
        return self._filter_criteria_assoc_tri

    @filter_criteria_assoc_tri.setter
    def filter_criteria_assoc_tri(self, filter_criteria_assoc_tri):
        """Sets the filter_criteria_assoc_tri of this MeasRepUeSubscription.


        :param filter_criteria_assoc_tri: The filter_criteria_assoc_tri of this MeasRepUeSubscription.  # noqa: E501
        :type: MeasRepUeSubscriptionFilterCriteriaAssocTri
        """
        if filter_criteria_assoc_tri is None:
            raise ValueError("Invalid value for `filter_criteria_assoc_tri`, must not be `None`")  # noqa: E501

        self._filter_criteria_assoc_tri = filter_criteria_assoc_tri

    @property
    def subscription_type(self):
        """Gets the subscription_type of this MeasRepUeSubscription.  # noqa: E501

        Shall be set to \"MeasRepUeSubscription\".  # noqa: E501

        :return: The subscription_type of this MeasRepUeSubscription.  # noqa: E501
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        """Sets the subscription_type of this MeasRepUeSubscription.

        Shall be set to \"MeasRepUeSubscription\".  # noqa: E501

        :param subscription_type: The subscription_type of this MeasRepUeSubscription.  # noqa: E501
        :type: str
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type

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
        if issubclass(MeasRepUeSubscription, dict):
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
        if not isinstance(other, MeasRepUeSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
