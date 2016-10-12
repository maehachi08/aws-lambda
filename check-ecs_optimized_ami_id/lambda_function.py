# coding:utf-8
#  Name:
#    get-ecs-ami.py
#
#  Description:
#    ECS Optimized AMIのAMI IDをAWSドキュメント内から取得する
#
#    refs https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
#
import boto3
import urllib2
import chardet
import json
from bs4 import BeautifulSoup

def s3_obj():
  AWS_S3_BUCKET_NAME = 'build-custom-ami-ecs-optimized'
  OBJECT_KEY_NAME = 'ecs-ami-id.json'
  s3 = boto3.resource('s3')
  bucket = s3.Bucket(AWS_S3_BUCKET_NAME)
  obj = bucket.Object(OBJECT_KEY_NAME)
  return obj

def put_s3( body='' ):
  obj = s3_obj()

  # put json content to s3
  response = obj.put(
    Body=body.encode('utf-8'),
    ContentEncoding='utf-8',
    ContentType='text/plane'
  )

def lambda_handler(event, context):
  # set url of aws optimized ami-id
  url = 'http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs-optimized_AMI.html'

  try:
    # open
    response = urllib2.urlopen(url)
  except urllib2.HTTPError, e:
    raise Exception('HTTPError = ' + str(e.code))
  except urllib2.URLError, e:
    raise Exception('URLError = ' + str(e.reason))
  except httplib.HTTPException, e:
    raise Exception('HTTPException')
  except Exception:
    import traceback
    raise Exception('generic exception: ' + traceback.format_exc())
  else:
    if response.code != 200:
      raise Exception('HTTPResponse is not 200: ' + str(response.code) )

  # read
  html = response.read().decode("utf-8", "replace")

  # scraping
  soup = BeautifulSoup(html)
  table = soup.findAll( "div", { "class" : "informaltable-contents" } )[0]
  t_body = table.findAll( "table" )[0].findAll( "tbody" )[0]

  # initialize dictionary
  dict = {}

  # <code class="literal"></code> を抽出
  #   1つ目がリージョン、2つ目がAMI IDの組みなので、
  #   ディクショナリ型変数に格納する
  for t_code in t_body.findAll( "tr" ):
    k, v = BeautifulSoup( str( t_code ) ).findAll( "code", { "class" : "literal" } )
    # k,vはunicode型インスタンスなのでstrで文字列へ変換する
    dict[str( k.text )] = str( v.text )

  # dictをJSONに変換
  web_body = json.dumps(dict, ensure_ascii=False)

  # get json content from s3
  obj = s3_obj()

  try:
    response = obj.get()
  except:
    put_s3( web_body )
  else:
    body = response['Body'].read()
    s3_body = body.decode('utf-8')

    # string comparison
    if web_body == s3_body:
      print( 'ECS Optimzed AMI is not change...' )
    else:
      print( 'ECS Optimzed AMI is change...' )
      put_s3( web_body )

