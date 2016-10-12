# check-ecs_optimized_ami_id

  ECS Optimized AMI ID を[Launching an Amazon ECS Container Instance](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/launch_container_instance.html) から取得(スクレイピング)して、S3に置いてあるJSONファイルと比較(初回は存在しないので比較しない)し、差異があれば更新があったと見なしてS3にJSONファイルをPUTするためのAWS Lambda Functionコード。

## Install

 ```sh
git clone git@github.com:maehachi08/aws-lambda.git
cd aws-lambda/check-ecs_optimized_ami_id

# virtualenvで仮想実行環境を準備
easy_install virtualenv
virtualenv ./virtual-env
source virtual-env/bin/activate

# virtualenv環境でコード実行に必要なパッケージをインストール
pip install beautifulsoup4
pip install chardet
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

