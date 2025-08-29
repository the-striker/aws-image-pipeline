# 📷 Serverless Image Processing Pipeline (AWS)

A serverless pipeline that automatically resizes images when uploaded to S3 using **AWS Lambda, S3, IAM, CloudWatch, and Pillow**.

---

## 🚀 Architecture
[User Uploads Image] → [S3 Input Bucket] → (Trigger) → [Lambda + Pillow] → [S3 Output Bucket]

---

## 🛠️ Technologies
- **AWS Lambda** (Python 3.11)
- **Amazon S3** (input + output buckets)
- **IAM** (least-privilege roles)
- **CloudWatch Logs**
- **Pillow (Python Imaging Library)** via Lambda Layer

---

## 📂 Project Structure
image-processing-pipeline/
├── README.md
├── template.yaml # AWS SAM template
└── src/
└── app.py # Lambda function


---

## ⚡ Deployment (AWS SAM)

### 1. Install AWS SAM CLI
[bash]
brew install aws-sam-cli     # macOS
choco install aws-sam-cli    # Windows
sudo apt install aws-sam-cli # Linux

2. Build
   sam build
3. Deploy
   sam deploy --guided

Enter a stack name (e.g., image-pipeline-stack)

Choose region (e.g., ap-south-1)

Accept defaults for IAM creation

✅ Testing

Upload an image (cat.jpg) into the input bucket

After a few seconds, check the output bucket

The image will be resized to 200x200 pixels

Check CloudWatch Logs for execution details

📈 Future Improvements

Add watermarking

Store metadata in DynamoDB

Trigger SNS/Email when processing completes

Add API Gateway to upload images via REST endpoint

Author
Built by Umesh Godhwani |
