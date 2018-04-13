"""
Implementation of getting started tutorial example http://boto3.readthedocs.io/en/latest/guide/dynamodb.html
Some tweaks, mostly around error handling if table already exists.
"""
import boto3
from boto3.dynamodb.conditions import Key, Attr
import botocore


dynamodb = boto3.Session(profile_name='dev').resource('dynamodb', endpoint_url='http://localhost:8000')
#.resource('dynamodb')

try:
    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='users')
except dynamodb.meta.client.exceptions.ResourceInUseException as e:
    print("Error creating table, continuing to attempt writes.  Error was %s" % e)
    table = dynamodb.Table('users')


table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)

# Print out some data about the table.
print(f"Row count {table.item_count}")

response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)

table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)

print("Deleting item janedoe")
table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
print(f"Row count {table.item_count}")

print("Run batch writes")
# This is set to overwrite if existing key
with table.batch_writer(overwrite_by_pkeys=['username', 'last_name']) as batch:
    batch.put_item(
        Item={
            'account_type': 'standard_user',
            'username': 'johndoe',
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 25,
            'address': {
                'road': '1 Jefferson Street',
                'city': 'Los Angeles',
                'state': 'CA',
                'zipcode': 90001
            }
        }
    )
    batch.put_item(
        Item={
            'account_type': 'super_user',
            'username': 'janedoering',
            'first_name': 'Jane',
            'last_name': 'Doering',
            'age': 40,
            'address': {
                'road': '2 Washington Avenue',
                'city': 'Seattle',
                'state': 'WA',
                'zipcode': 98109
            }
        }
    )
    batch.put_item(
        Item={
            'account_type': 'standard_user',
            'username': 'bobsmith',
            'first_name': 'Bob',
            'last_name':  'Smith',
            'age': 18,
            'address': {
                'road': '3 Madison Lane',
                'city': 'Louisville',
                'state': 'KY',
                'zipcode': 40213
            }
        }
    )
    batch.put_item(
        Item={
            'account_type': 'super_user',
            'username': 'alicedoe',
            'first_name': 'Alice',
            'last_name': 'Doe',
            'age': 27,
            'address': {
                'road': '1 Jefferson Street',
                'city': 'Los Angeles',
                'state': 'CA',
                'zipcode': 90001
            }
        }
    )
print(f"Row count {table.item_count}")

# Run a coulpe of queries with conditions
response = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)
items = response['Items']
print(items)

response = table.scan(
    FilterExpression=Attr('age').lt(27)
)
items = response['Items']
print(items)


print("Deleting table")
table.delete()
