import boto3
import os

BUCKET_NAME = ''
s3 = boto3.resource('s3')
my_bucket = s3.Bucket(BUCKET_NAME)

def fix(date):
    n = 0
    for my_bucket_object in my_bucket.objects.filter(Prefix=date):
        if my_bucket_object.key.endswith('mp3'):
            try:
                anomes = date[0:6]
                dia = date[6:8]
                
                print(f"# {my_bucket_object.key}")
                
                current_path = "%s/%s" % (my_bucket_object.bucket_name, my_bucket_object.key)
                newpath = "%s/%s/%s" % (anomes, dia, my_bucket_object.key)

                s3.Object(my_bucket_object.bucket_name, newpath).copy_from(CopySource=current_path)
                s3.ObjectSummary(bucket_name=my_bucket_object.bucket_name, key=newpath).load()
                s3.Object(my_bucket_object.bucket_name, my_bucket_object.key).delete()
                n = n + 1
            except Exception as ex:
                print(f'Exception: {ex}')
                pass
    print(f"Total files: {n}")

# 20201126_etc_etc.mp3 will be moved to 202011/26/20201126_etc_etc.mp3
fix('20201126')
