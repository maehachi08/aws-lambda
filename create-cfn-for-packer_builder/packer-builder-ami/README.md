# Packer Build環境を持つカスタムAMIの作成

 ```sh
# set variable
META_URI="http://169.254.169.254/latest/meta-data/"
META_NW_URI="${META_URI}network/interfaces/macs/"
MAC_ADDR=`curl -s ${META_NW_URI}`

# set environment variable
export SUBNET_ID=`curl -s ${META_NW_URI}${MAC_ADDR}/subnet-id`
export VPC_ID=`curl -s ${META_NW_URI}${MAC_ADDR}/vpc-id`
export REGION=`curl -s ${META_NW_URI}/placement/availability-zone | sed -e 's/.$//g'`
```
