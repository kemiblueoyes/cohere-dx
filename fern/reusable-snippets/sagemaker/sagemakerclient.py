import cohere

co = cohere.SagemakerClient(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)