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


def analyze_market_trend(prompt):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a market trend analyst providing concise insights."},
                {"role": "user", "content": f"{prompt}"}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error calling OpenAI API: {e}")
        return f"Error analyzing market trend: {str(e)}"
    