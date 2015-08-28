import boto
from boto.s3.key import Key
import sys

bucket_name = '<your bucket name>'

s3 = boto.connect_s3()

sourcefile = sys.argv[1]
keyname = sys.argv[2]

bucket = s3.get_bucket(bucket_name)
k_up = Key(bucket)
k_up.key = keyname
k_up.set_contents_from_filename(sourcefile)

# Example to run...
# python s3_upload.py data/sample_file.tsv sourcefiles/sample_file.tsv
