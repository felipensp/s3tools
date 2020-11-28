import boto3
import os
from io import BytesIO
from s3_to_transcribe import handle

BUCKET_NAME = ''
s3 = boto3.client('s3')
my_bucket = boto3.resource('s3').Bucket(BUCKET_NAME)

def list(prefix, dump=True):
    n = 0
    for my_bucket_object in my_bucket.objects.filter(Prefix=prefix):
        try:            
            print(f"# '{my_bucket_object.key}'")   
            if dump:
                f = BytesIO()
                s3.download_fileobj(my_bucket_object.bucket_name, my_bucket_object.key, f)            
                f.seek(0)
                print(f.getvalue())
            n = n + 1
        except Exception as ex:
            print(f'Exception: {ex}')
            pass
    print(f"Total files: {n}")
    
if __name__ == "__main__":
    list('', dump=False)
