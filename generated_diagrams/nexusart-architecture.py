#!/usr/bin/env python3
"""
NexusArt AWS Architecture Diagram Generator
Based on design.md specifications
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway, CloudFront
from diagrams.aws.storage import S3
from diagrams.aws.database import DynamoDB, Neptune
from diagrams.aws.ml import Bedrock, Sagemaker
from diagrams.aws.media import ElementalMediaconvert
from diagrams.aws.ml import Transcribe, Translate, Rekognition
from diagrams.aws.security import Cognito
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import Eventbridge
from diagrams.aws.general import Client

# Graph attributes for better visualization
graph_attr = {
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho"
}

with Diagram("NexusArt - Collaborative Creative Ecosystem", 
             filename="generated_diagrams/nexusart_architecture",
             show=False,
             direction="TB",
             graph_attr=graph_attr):
    
    # Client Layer
    with Cluster("Client Layer"):
        web_client = Client("React Web App")
        mobile_client = Client("React Native Mobile")
    
    # API Gateway & Auth
    with Cluster("API Gateway Layer"):
        api_gateway = APIGateway("API Gateway\nREST + WebSocket")
        cognito = Cognito("Amazon Cognito\nAuthentication")
    
    # Lambda Compute Layer
    with Cluster("Compute Layer (Serverless)"):
        lambda_embedding = Lambda("embedding-generator")
        lambda_matcher = Lambda("semantic-matcher")
        lambda_metadata = Lambda("metadata-processor")
        lambda_creative = Lambda("creative-assistant")
        lambda_predictor = Lambda("engagement-predictor")
        lambda_distributor = Lambda("distribution-orchestrator")
    
    # Module A: Semantic Matchmaking
    with Cluster("Module A: Semantic Matchmaking"):
        bedrock_titan = Bedrock("Bedrock Titan\nEmbeddings")
        dynamodb_profiles = DynamoDB("UserProfiles")
        dynamodb_embeddings = DynamoDB("VectorEmbeddings")
        neptune = Neptune("Neptune\nGraph DB")
    
    # Module B: Living Workspace
    with Cluster("Module B: Living Workspace"):
        s3_projects = S3("S3 Projects\n(Versioned)")
        dynamodb_projects = DynamoDB("Projects")
        dynamodb_assets = DynamoDB("Assets")
        dynamodb_ledger = DynamoDB("ContributionLedger")
    
    # Module C: AI/ML Services
    with Cluster("Module C: AI Creative Assistant"):
        bedrock_claude = Bedrock("Bedrock Claude 3\nCreative Assistant")
        sagemaker = Sagemaker("SageMaker\nEngagement Predictor")
        rekognition = Rekognition("Rekognition\nContent Moderation")
    
    # Module D: Distribution
    with Cluster("Module D: Intelligent Distribution"):
        mediaconvert = ElementalMediaconvert("MediaConvert\nTranscoding")
        transcribe = Transcribe("Transcribe\nSpeech-to-Text")
        translate = Translate("Translate\nMulti-lingual")
        s3_distribution = S3("S3 Distribution")
        cloudfront = CloudFront("CloudFront CDN")
    
    # Monitoring
    with Cluster("Monitoring & Events"):
        cloudwatch = Cloudwatch("CloudWatch\nLogs & Metrics")
        eventbridge = Eventbridge("EventBridge\nEvent Bus")
    
    # Client to API Gateway
    web_client >> Edge(label="HTTPS") >> api_gateway
    mobile_client >> Edge(label="HTTPS") >> api_gateway
    
    # API Gateway to Auth
    api_gateway >> cognito
    
    # API Gateway to Lambda Functions
    api_gateway >> lambda_embedding
    api_gateway >> lambda_matcher
    api_gateway >> lambda_creative
    api_gateway >> lambda_predictor
    api_gateway >> lambda_distributor
    
    # Module A: Semantic Matchmaking Flow
    lambda_embedding >> bedrock_titan
    lambda_embedding >> dynamodb_embeddings
    lambda_embedding >> neptune
    lambda_matcher >> dynamodb_profiles
    lambda_matcher >> dynamodb_embeddings
    lambda_matcher >> neptune
    
    # Module B: Living Workspace Flow
    api_gateway >> lambda_metadata
    lambda_metadata >> s3_projects
    lambda_metadata >> dynamodb_projects
    lambda_metadata >> dynamodb_assets
    lambda_metadata >> dynamodb_ledger
    s3_projects >> Edge(label="S3 Event") >> lambda_metadata
    
    # Module C: AI Creative Assistant Flow
    lambda_creative >> bedrock_claude
    lambda_predictor >> sagemaker
    lambda_metadata >> rekognition
    
    # Module D: Distribution Flow
    lambda_distributor >> mediaconvert
    lambda_distributor >> transcribe
    lambda_distributor >> translate
    mediaconvert >> s3_distribution
    transcribe >> s3_distribution
    translate >> s3_distribution
    s3_distribution >> cloudfront
    
    # Event-driven architecture
    s3_projects >> eventbridge
    eventbridge >> lambda_embedding
    eventbridge >> lambda_metadata
    
    # Monitoring
    lambda_embedding >> cloudwatch
    lambda_matcher >> cloudwatch
    lambda_metadata >> cloudwatch
    lambda_creative >> cloudwatch
    lambda_predictor >> cloudwatch
    lambda_distributor >> cloudwatch
    api_gateway >> cloudwatch

print("✓ NexusArt architecture diagram generated successfully!")
print("✓ Output: generated_diagrams/nexusart_architecture.png")
