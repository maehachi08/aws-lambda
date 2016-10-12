#!/bin/bash

# set variable
PACKER_DIR='20161007_packer-customize-ami'
PACKER_JSON="/tmp/${PACKER_DIR}/packer-custom-ecs_optimized_ami.json"
META_URI="http://169.254.169.254/latest/meta-data/"
META_NW_URI="${META_URI}network/interfaces/macs/"
MAC_ADDR=`curl -s ${META_NW_URI}`

# set environment variable
export SUBNET_ID=`curl -s ${META_NW_URI}${MAC_ADDR}/subnet-id`
export VPC_ID=`curl -s ${META_NW_URI}${MAC_ADDR}/vpc-id`
export REGION=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone | sed -e 's/.$//g'`
export AMI_ID="ami-010ed160"

# get packer files
aws s3 cp s3://build-custom-ami-ecs-optimized/${PACKER_DIR}.tgz /tmp/

# decompress
tar xzvf /tmp/${PACKER_DIR}.tgz -C /tmp/

# packer build
cd /tmp/${PACKER_DIR}
/usr/local/bin/packer build ${PACKER_JSON}

echo "$0 is end"
exit 0

