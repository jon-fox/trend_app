import requests
import boto3
from src.utils.logger import logger
from openai import OpenAI


try:
    ssm = boto3.client('ssm', region_name='us-east-1')
    OPENAI_API_KEY = ssm.get_parameter(Name="/openai/api_key", WithDecryption=True)['Parameter']['Value']
except Exception as e:
    logger.error(f"Error getting OpenAI API Key: {e}")
    raise e

openai_client = OpenAI(api_key=OPENAI_API_KEY)

