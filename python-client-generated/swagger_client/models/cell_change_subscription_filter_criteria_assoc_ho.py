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

class CellChangeSubscriptionFilterCriteriaAssocHo(object):
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
        'associate_id': 'list[AssociateId]',
        'ecgi': 'list[Ecgi]',
        'ho_status': 'list[Enum]'
    }

    attribute_map = {
        'app_instance_id': 'appInstanceId',
        'associate_id': 'associateId',
        'ecgi': 'ecgi',
        'ho_status': 'hoStatus'
    }

    def __init__(self, app_instance_id=None, associate_id=None, ecgi=None, ho_status=None):  # noqa: E501
        """CellChangeSubscriptionFilterCriteriaAssocHo - a model defined in Swagger"""  # noqa: E501
        self._app_instance_id = None
        self._associate_id = None
        self._ecgi = None
        self._ho_status = None
        self.discriminator = None
        if app_instance_id is not None:
            self.app_instance_id = app_instance_id
        if associate_id is not None:
            self.associate_id = associate_id
        if ecgi is not None:
            self.ecgi = ecgi
        if ho_status is not None:
            self.ho_status = ho_status

    @property
    def app_instance_id(self):
        """Gets the app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501

        Unique identifier for the MEC application instance.  # noqa: E501

        :return: The app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id):
        """Sets the app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :type: str
        """

        self._app_instance_id = app_instance_id

    @property
    def associate_id(self):
        """Gets the associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :rtype: list[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id):
        """Sets the associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :type: list[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self):
        """Gets the ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :return: The ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :rtype: list[Ecgi]
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi):
        """Sets the ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :param ecgi: The ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :type: list[Ecgi]
        """

        self._ecgi = ecgi

    @property
    def ho_status(self):
        """Gets the ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501

        In case hoStatus is not included in the subscription request, the default value 3 = COMPLETED shall be used and included in the response: <p>1 = IN_PREPARATION. <p>2 = IN_EXECUTION. <p>3 = COMPLETED. <p>4 = REJECTED. <p>5 = CANCELLED.  # noqa: E501

        :return: The ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :rtype: list[Enum]
        """
        return self._ho_status

    @ho_status.setter
    def ho_status(self, ho_status):
        """Sets the ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.

        In case hoStatus is not included in the subscription request, the default value 3 = COMPLETED shall be used and included in the response: <p>1 = IN_PREPARATION. <p>2 = IN_EXECUTION. <p>3 = COMPLETED. <p>4 = REJECTED. <p>5 = CANCELLED.  # noqa: E501

        :param ho_status: The ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :type: list[Enum]
        """

        self._ho_status = ho_status

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
        if issubclass(CellChangeSubscriptionFilterCriteriaAssocHo, dict):
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
        if not isinstance(other, CellChangeSubscriptionFilterCriteriaAssocHo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
