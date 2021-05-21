import boto3

def create_books_table():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='books',
        KeySchema=[
            {
                'AttributeName': 'isbn',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'isbn',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    # Wait until AWS confirms that table exists before moving on
    table.meta.client.get_waiter('table_exists').wait(TableName='books')

    # Put some data into the table
    table.put_item(
        Item={
             'isbn': '043591010',
             'title': "Opening Spaces: An Anthology of Contemporary African Women's Writing",
             'author': 'Yvonne Vera',
             'year': '1999'
        }
    )

    table.put_item(
        Item={
             'isbn': '0394721179',
             'title': "African Folktales: Traditional Stories of the Black World",
             'author': 'Roger D. Abrahams',
             'year': '1983'
        }
    )

if __name__ == "__main__":
    create_books_table()
    print("DynamoDB 'books' table has been created and populated")
