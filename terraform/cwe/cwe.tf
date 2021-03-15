module "cwe" {
  source           = "git::https://github.com/reflexivesecurity/reflex-engine.git//modules/cwe?ref=v2.1.3"
  name        = "ConfigRecorderDisabled"
  description = "Event rule to catch disable or delete configuration recorder."

  event_pattern = <<PATTERN
{
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "source": [
    "aws.config"
  ],
  "detail": {
    "eventSource": [
      "config.amazonaws.com"
    ],
    "eventName": [
      "DeleteConfigurationRecorder",
      "StopConfigurationRecorder"
    ]
  }
}
PATTERN
}