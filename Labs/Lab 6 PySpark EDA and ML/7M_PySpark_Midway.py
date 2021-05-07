from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Start Spark Session
spark = SparkSession.builder.getOrCreate()

# Read data
data = spark.read.csv('/project2/macs30123/AWS_book_reviews/*.csv',
                      header='true',
                      inferSchema='true')

# Recast columns to correct data type
data = (data.withColumn('star_rating', col('star_rating').cast('int'))
            .withColumn('total_votes', col('total_votes').cast('int'))
            .withColumn('helpful_votes', col('helpful_votes').cast('int'))
       )

# Summarize data by star_rating
stars_votes = (data.groupBy('star_rating')
                  .sum('total_votes', 'helpful_votes')
                  .sort('star_rating', ascending=False)
             )

# Drop rows with NaN values and then print out resulting data:
stars_votes_clean = stars_votes.dropna()
stars_votes_clean.show()
