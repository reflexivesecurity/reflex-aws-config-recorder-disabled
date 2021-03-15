# config-recorder-disabled

Alerts if a Config recorder is deleted or disabled.

## Usage

To use this rule either add it to your `reflex.yaml` configuration file:

```
rules:
  - config-recorder-disabled:
      version: latest
```

or add it directly to your Terraform:

```
...

module "config-recorder-disabled-cwe" {
  source            = "git::https://github.com/reflexivesecurity/config-recorder-disabled.git//terraform/cwe?ref=latest"
}

module "config-recorder-disabled" {
  source            = "git::https://github.com/reflexivesecurity/config-recorder-disabled.git?ref=latest"
  sns_topic_arn     = module.central-sns-topic.arn
  reflex_kms_key_id = module.reflex-kms-key.key_id
}

...
```

Note: The `sns_topic_arn` and `reflex_kms_key_id` example values shown here assume you generated resources with `reflex build`. If you are using the Terraform on its own you need to provide your own valid values.

## Contributing
If you are interested in contributing, please review [our contribution guide](https://docs.reflexivesecurity.com/about/contributing.html).

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view
the [LICENSE](https://github.com/reflexivesecurity/config-recorder-disabled/blob/master/LICENSE)
