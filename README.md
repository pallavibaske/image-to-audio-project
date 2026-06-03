# Image to Audio Generator using AWS

## Project Overview

This project automatically converts uploaded images into audio descriptions.

### Workflow

1. Upload image to Amazon S3
2. S3 triggers AWS Lambda
3. Lambda sends image to Amazon Rekognition
4. Rekognition detects labels
5. Amazon Polly converts labels into speech
6. MP3 is stored in S3

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon Rekognition
- Amazon Polly