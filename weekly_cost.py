import boto3
from datetime import datetime, timedelta

def get_weekly_cost():
    client = boto3.client('ce')
    now = datetime.now()
    start = (now - timedelta(days=7)).strftime('%Y-%m-%d')
    end = now.strftime('%Y-%m-%d')

    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End': end
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    print("Weekly AWS Cost:")
    for result in response['ResultsByTime']:
        print(f"Date: {result['TimePeriod']['Start']}, Cost: {result['Total']['UnblendedCost']['Amount']} {result['Total']['UnblendedCost']['Unit']}")

get_weekly_cost()

