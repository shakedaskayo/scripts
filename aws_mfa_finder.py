import boto3

def find_users_without_mfa():
    client = boto3.client('iam')
    paginator = client.get_paginator('list_users')
    users_without_mfa = []

    for page in paginator.paginate():
        for user in page['Users']:
            mfa_devices = client.list_mfa_devices(UserName=user['UserName'])
            if len(mfa_devices['MFADevices']) == 0:
                users_without_mfa.append(user['UserName'])

    if users_without_mfa:
        print("Users without MFA:")
        for user in users_without_mfa:
            print(user)
    else:
        print("All users have MFA enabled.")

find_users_without_mfa()

