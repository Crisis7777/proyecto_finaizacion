import boto3
from credentials.keys import ACCESS_KEY, SECRET_KEY

bucket_name = "files-cym"
def connection_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
        s3_resource = session_aws.resource('s3')
        print("Connecting to S3")
        return s3_resource
    except Exception as err:
        print("Error", err)
        return None

def save_file(photo):
    try:
        photo_path_local = "/tmp/photo"
        photo.save(photo_path_local)
        print("Photo saved")
        return photo_path_local
    except Exception as err:
        print("Error", err)
        return None

def upload_file(s3_resource, photo, photo_path_local, id):
    try:
        photo_name = photo.filename
        photo_extension = photo_name.split(".")[len(photo_name.split("."))-1]
        photo_path_dest = "images/" + id + "." + photo_extension
        bucket_connection = s3_resource.meta.client.upload_file(photo_path_local, bucket_name, photo_path_dest)
        print("File uploaded")
        return True
    except Exception as err:
        print("Error", err)
        return False

def consult_file(s3_resource, id):
    bucket_repo = s3_resource.Bucket(bucket_name)
    bucket_objects = bucket_repo.objects.all()
    for obj in bucket_objects:
        path_file_s3 = obj.key
        path_file_list = path_file_s3.split("/")
        name_photo_process = path_file_list[len(path_file_list)-1].split(".")[0]
        if name_photo_process == id:
            return path_file_s3
    return None
        
        