import boto3
import sys
from flask import jsonify

BUCKET = "liwwa-hr-test"
#Helper class for using the as features


#function to upload the files
def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    try:
        s3_client = boto3.client('s3')
        object_name = file_name
        response = s3_client.upload_file(file_name, bucket, object_name)
        return jsonify({'sucess': "File updated successfully"})
    except Exception as e:
        print(f"Error in uploading file => {e} ",file=sys.stdout)
        return jsonify({"error":"Somethign went wrong uploading the file"})


#function to download a given file
#params file_name and bucket name to download
def download_file(file_name, bucket):
    s3 = boto3.resource('s3')
    output = f"{file_name}"
    x = s3.Bucket(bucket).download_file(file_name, output)
    print (f"x => {x} ", file=sys.stdout)
    return output

#This function to list all of the files in the bucket and display them
#params bycket_name
def list_files(bucket):
    contents = []
    s3 = boto3.client('s3')
    s3_files = s3.list_objects(Bucket=bucket)['Contents']
    for item in s3_files:
        contents.append(item)
    return contents
