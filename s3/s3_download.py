import boto
from boto.s3.key import Key
import sys

bucket_name = '<your bucket name>'

s3 = boto.connect_s3()
bucket = s3.get_bucket(bucket_name)

keyname = sys.argv[1]
destfile = sys.argv[2]

k = Key(bucket)
k.key = keyname #'archive/testfile.txt'
k.get_contents_to_filename(destfile)  #to download

# python s3_download.py sourcefiles/sample_file.tsv data/sample_file.tsv
