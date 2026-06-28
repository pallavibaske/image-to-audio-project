# AWS Serverless Image-to-Audio Converter

## 🎯 Project Overview

This project demonstrates a serverless AWS solution that automatically converts image content into speech. When an image is uploaded to an Amazon S3 bucket, an AWS Lambda function is triggered. The Lambda function uses Amazon Rekognition to analyze the image and Amazon Polly to generate an MP3 audio file.

---

## 🛠️ AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon Rekognition
- Amazon Polly
- IAM

---

## 🔄 Workflow

1. Upload an image to the S3 bucket.
2. S3 triggers the Lambda function.
3. Lambda sends the image to Amazon Rekognition.
4. Rekognition detects labels/text from the image.
5. Lambda sends the detected content to Amazon Polly.
6. Polly generates an MP3 audio file.
7. The MP3 file is stored in the output S3 bucket.

---

## ✨ Features

- Serverless Architecture
- Automatic S3 Event Trigger
- Image Analysis using Amazon Rekognition
- Text-to-Speech Conversion using Amazon Polly
- Automatic MP3 File Generation

---

## 📂 Repository Structure

```
image-to-audio-project/
├── lambda_function.py
├── README.md
├── LICENSE
├── Architecture/
└── Screenshots/
```

---

## 🚀 Future Enhancements

- OCR Text Extraction
- Multi-language Audio Support
- Web Dashboard
- Email Notifications

---

## 📚 Skills Demonstrated

- AWS Cloud
- Amazon S3
- AWS Lambda
- Amazon Rekognition
- Amazon Polly
- IAM
- Python
- Serverless Computing

---

## 👩‍💻 Author

**Pallavi Baske**

- LinkedIn: https://www.linkedin.com/in/pallavi-baske-6a0b80216
- GitHub: https://github.com/pallavibaske
