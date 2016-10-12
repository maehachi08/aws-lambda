# create-cfn-for-packer_builder

  Packer Build環境を持つAMIからEC2インスタンスを起動し、S3からpacker buildに必要なファイルをダウンロード、buildを行うためのAWS Lambda Functionコード。

## Install

 ```sh
git clone git@github.com:maehachi08/aws-lambda.git
cd aws-lambda/create-cfn-for-packer_builder

# virtualenvで仮想実行環境を準備
easy_install virtualenv
virtualenv ./virtual-env
source virtual-env/bin/activate

# virtualenv環境でコード実行に必要なパッケージをインストール
pip install boto3

# Lamda Functionをローカル実行するためにpython-lambda-localをインストール
pip install python-lambda-local

# AWS Lamda Functionにアップロードするためにlambda-uploaderをインストール
pip install lambda-uploader
```

## local exec

 ```sh
python-lambda-local -f lambda_handler lambda_function.py event.json
```

## upload

 ```sh
lambda-uploader
```

