from aws_cdk import (
    core as cdk,
    # aws_sqs as sqs,
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from . import widget_service


class ChattyAwsStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # init the widget service
        widget_service.WidgetService(self, "Widgets")

        # example resource
        # queue = sqs.Queue(
        #     self, "ChattyAwsQueue",
        #     visibility_timeout=cdk.Duration.seconds(300),
        # )
