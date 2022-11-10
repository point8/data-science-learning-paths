from contextlib import contextmanager
import findspark
findspark.init()
import pyspark


@contextmanager
def use_spark_context(appName):
    conf = pyspark.SparkConf().setAppName(appName) 
    spark_context = pyspark.SparkContext(conf=conf)

    try:
        yield spark_context
    finally:
        spark_context.stop()


@contextmanager
def use_spark_session(appName):
    spark_session = pyspark.sql.SparkSession.builder.appName(appName).getOrCreate()
    try:
        print("starting ", appName)
        yield spark_session
    finally:
        spark_session.stop()
        print("stopping ", appName)

        
