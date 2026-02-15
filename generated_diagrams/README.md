# NexusArt Architecture Diagrams

This folder contains the AWS architecture diagrams for the NexusArt platform.

## Prerequisites

### Windows Installation

1. **Install Graphviz**:
   ```powershell
   # Using Chocolatey
   choco install graphviz
   
   # OR download installer from:
   # https://graphviz.org/download/
   ```

2. **Install Python** (optional, for Python-based diagram generation):
   ```powershell
   # Download from https://www.python.org/downloads/
   # OR using Chocolatey
   choco install python
   ```

3. **Install Python dependencies** (if using Python approach):
   ```bash
   pip install -r requirements.txt
   ```

### Mac Installation

```bash
brew install graphviz
brew install python3
pip3 install -r requirements.txt
```

### Linux Installation

```bash
sudo apt-get install graphviz
sudo apt-get install python3-pip
pip3 install -r requirements.txt
```

## Generating the Diagram

### Method 1: Using DOT file (Recommended - No Python needed)

```bash
# Generate PNG
dot -Tpng nexusart-architecture.dot -o nexusart-architecture.png

# Generate SVG (scalable)
dot -Tsvg nexusart-architecture.dot -o nexusart-architecture.svg

# Generate PDF
dot -Tpdf nexusart-architecture.dot -o nexusart-architecture.pdf
```

### Method 2: Using Python script (Requires Python + diagrams library)

```bash
python nexusart-architecture.py
```

## Architecture Overview

The diagram visualizes the complete NexusArt serverless architecture with four main modules:

### Module A: Semantic Matchmaking Engine
- Amazon Bedrock Titan for embeddings
- DynamoDB for user profiles and vector storage
- Amazon Neptune for relationship graphs

### Module B: Living Workspace
- S3 versioned storage for media assets
- DynamoDB for project metadata and contribution tracking
- Git-style version control

### Module C: AI Creative Assistant & Predictive Intelligence
- Amazon Bedrock Claude 3 for creative suggestions
- Amazon SageMaker for engagement prediction
- Amazon Rekognition for content moderation

### Module D: Intelligent Distribution
- AWS Elemental MediaConvert for transcoding
- Amazon Transcribe for captions
- Amazon Translate for multi-lingual support
- CloudFront CDN for global delivery

## Output Files

After generation, you'll find:
- `nexusart-architecture.png` - High-resolution architecture diagram
- `nexusart-architecture.svg` - Scalable vector version
- `nexusart-architecture.pdf` - Print-ready PDF version

## Troubleshooting

**Error: "dot: command not found"**
- Graphviz is not installed or not in PATH
- Restart terminal after installation

**Error: "Python was not found"**
- Install Python from python.org or use Method 1 (DOT file only)

**Error: "No module named 'diagrams'"**
- Run: `pip install diagrams graphviz`
