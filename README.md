# AWS Serverless Image-to-Audio Converter

This project implements a serverless architecture on AWS to convert text extracted from images into audio files automatically.

## 🎯 Project Overview
This tool automates the process of image analysis and speech conversion. When an image is uploaded to S3, the system triggers a pipeline that reads the text (labels) and converts it into a speech-enabled MP3 file.

## 🛠️ Tech Stack & AWS Services
* **Amazon S3:** Used for image storage and hosting the output audio files.
* **AWS Lambda:** Executes the serverless Python code to bridge services.
* **Amazon Rekognition:** Performs image analysis to detect labels/text.
* **Amazon Polly:** Converts extracted text into human-like speech.

## 🏗️ Workflow
1. **Upload:** User uploads an image to the source S3 bucket.
2. **Trigger:** The S3 event triggers the AWS Lambda function.
3. **Analysis:** Lambda sends the image to Amazon Rekognition for label detection.
4. **Conversion:** The detected text/labels are passed to Amazon Polly to generate speech.
5. **Storage:** The final MP3 file is saved into the destination S3 bucket.

## 🚀 Key Learnings
* Understanding **Event-Driven Architecture** in AWS.
* Experience in integrating **Serverless services** (Lambda, S3, Rekognition, Polly).
* Writing and deploying Python code in an AWS Lambda environment.

## 📬 Contact
Connect with me on [LinkedIn](https://www.linkedin.com/in/pallavi_baske)
