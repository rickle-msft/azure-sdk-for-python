# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class SkuName(Enum):

    f0 = "F0"
    s0 = "S0"
    s1 = "S1"
    s2 = "S2"
    s3 = "S3"
    s4 = "S4"


class SkuTier(Enum):

    free = "Free"
    standard = "Standard"
    premium = "Premium"


class Kind(Enum):

    computer_vision = "ComputerVision"
    emotion = "Emotion"
    face = "Face"
    luis = "LUIS"
    recommendations = "Recommendations"
    speech = "Speech"
    text_analytics = "TextAnalytics"
    web_lm = "WebLM"


class ProvisioningState(Enum):

    creating = "Creating"
    resolving_dns = "ResolvingDNS"
    succeeded = "Succeeded"
    failed = "Failed"


class KeyName(Enum):

    key1 = "Key1"
    key2 = "Key2"
