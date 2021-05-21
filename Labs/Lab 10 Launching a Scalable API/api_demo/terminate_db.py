import boto3

def delete_books_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('books')
    table.delete()

if __name__ == "__main__":
    delete_books_table()
    print("DynamoDB 'books' table has been terminated")
