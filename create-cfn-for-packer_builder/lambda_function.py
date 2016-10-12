# coding:utf-8
#  Name:
#    lambda_function.py
#
#  Description:
#    1. Get stack template from S3.
#    2. Create CloudFormation Stack specifying the AMI-ID.
#
import boto3
import json

def lambda_handler(event, context):
    cfn = boto3.resource( 'cloudformation',
        region_name = 'ap-northeast-1'
    )

    with open('template.json', 'r') as f:
        try:
            response = cfn.create_stack(
                StackName='CreatePackerBuilderEC2',
                TemplateBody=f.read(),
    
                # Specified AMI-ID is packer builder
                Parameters=[
                    {
                        'ParameterKey'    : 'ImageId',
                        'ParameterValue'  : 'ami-6d9d450c',
                        'UsePreviousValue': True,
                    },
                ],
            )
        except:
            print( 'create_stack error.' )

