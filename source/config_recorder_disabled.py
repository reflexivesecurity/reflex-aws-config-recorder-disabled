""" Module for ConfigRecorderDisabled """

import json

import boto3
from reflex_core import AWSRule, subscription_confirmation


class ConfigRecorderDisabled(AWSRule):
    """ Detects when a config recorder is either disabled or deleted. """

    client = boto3.client("config")

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.config_recorder_name = event["detail"]["requestParameters"][
            "configurationRecorderName"
        ]
        self.config_recorder_status = None

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        try:
            configuration_status = self.client.describe_configuration_recorder_status(
                ConfigurationRecorderName=[self.config_recorder_name]
            )
            if not configuration_status["ConfigurationRecordersStatus"][0]["recording"]:
                self.config_recorder_status = "disabled"
                return False
        except botocore.errorfactory.NoSuchConfigurationRecorderException:
            self.config_recorder_status = "deleted"
            return False
        return True

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        return f"The configuration recorder with name {self.config_recorder_name} was {self.config_recorder_status}."


def lambda_handler(event, _):
    """ Handles the incoming event """
    event_payload = json.loads(event["Records"][0]["body"])
    if subscription_confirmation.is_subscription_confirmation(event_payload):
        subscription_confirmation.confirm_subscription(event_payload)
        return
    rule = ConfigRecorderDisabled(event_payload)
    rule.run_compliance_rule()
