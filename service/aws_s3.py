import boto3


class S3Service:
    def __init__(self, bucket_name):
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(bucket_name)
        self.bucket_name = bucket_name

    def create_bucket(self):
        try:
            response = self.bucket.create_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} created")
            return response
        except Exception as e:
            print(e)
            return False

    def get_bucket(self):
        objs = []
        try:
            all_objects = self.bucket.objects.all()
            for obj in all_objects:
                objs.append(obj.key)
            return objs
        except Exception as e:
            print(e)
            return False

    def delete_bucket(self):
        try:
            self.bucket.delete()
            print(f"Bucket {self.bucket_name} deleted")
        except Exception as e:
            print(e)

    def format_bucket(self):
        try:
            for obj in self.bucket.objects.all():
                self.bucket.Object(obj.key).delete()
            for obj in self.bucket.object_versions.all():
                self.bucket.object_versions(obj.key).delete()
            print(f"Bucket {self.bucket_name} deleted")
        except Exception as e:
            print(e)
            return False
