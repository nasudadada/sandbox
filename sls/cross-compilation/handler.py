import json
import numpy as np


def hello(event, context):
    """ NumPyのバージョンを出力し、Lambdaレスポンスとして返す
    """
    numpy_version = np.__version__
    print(f"NumPy version: {numpy_version}")
    return {
        'statusCode': 200,
        'body': json.dumps(f"NumPy version: {numpy_version}")
    }

