import boto3
import sys

def scan_ecr_repository(repo_name):
    client = boto3.client('ecr')
    response = client.describe_images(repositoryName=repo_name)
    images = response['imageDetails']
    for image in images:
        print(f"Image Tag: {image.get('imageTags', ['<untagged>'])[0]}")
        print(f"Image Digest: {image['imageDigest']}")
        print(f"Image Pushed At: {image['imagePushedAt']}")
        print("----")

if __name__ == '__main__':
    repo_name = sys.argv[1]
    scan_ecr_repository(repo_name)

