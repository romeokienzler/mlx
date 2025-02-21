# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.27-pipeline-namespace
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiMetadata(object):
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
        'annotations': 'dict(str, str)',
        'labels': 'dict(str, str)',
        'tags': 'list[str]'
    }

    attribute_map = {
        'annotations': 'annotations',
        'labels': 'labels',
        'tags': 'tags'
    }

    def __init__(self, annotations=None, labels=None, tags=None):  # noqa: E501
        """ApiMetadata - a model defined in Swagger"""  # noqa: E501

        self._annotations = None
        self._labels = None
        self._tags = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if labels is not None:
            self.labels = labels
        if tags is not None:
            self.tags = tags

    @property
    def annotations(self):
        """Gets the annotations of this ApiMetadata.  # noqa: E501


        :return: The annotations of this ApiMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ApiMetadata.


        :param annotations: The annotations of this ApiMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def labels(self):
        """Gets the labels of this ApiMetadata.  # noqa: E501


        :return: The labels of this ApiMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ApiMetadata.


        :param labels: The labels of this ApiMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def tags(self):
        """Gets the tags of this ApiMetadata.  # noqa: E501


        :return: The tags of this ApiMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ApiMetadata.


        :param tags: The tags of this ApiMetadata.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(ApiMetadata, dict):
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
        if not isinstance(other, ApiMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
