import json
import boto3
import uuid

rekognition = boto3.client("rekognition")
polly = boto3.client("polly")
s3 = boto3.client("s3")

AUDIO_BUCKET = "pallavi-image-audio-bucket"

def lambda_handler(event, context):

    print("Event:", json.dumps(event))

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    image_key = event['Records'][0]['s3']['object']['key']

    print("Source bucket:", source_bucket)
    print("Image key:", image_key)

    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': source_bucket,
                'Name': image_key
            }
        },
        MaxLabels=10,
        MinConfidence=70
    )

    labels = []

    for label in response['Labels']:
        labels.append(label['Name'])

    print("Labels:", labels)

    if len(labels) == 0:
        labels.append("Unknown object")

    text = "This image contains " + ", ".join(labels)

    print("Text:", text)

    polly_response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna"
    )

    audio_data = polly_response["AudioStream"].read()

    file_name = str(uuid.uuid4()) + ".mp3"

    print("Uploading file:", file_name)

    s3.put_object(
        Bucket=AUDIO_BUCKET,
        Key=file_name,
        Body=audio_data,
        ContentType="audio/mpeg"
    )

    print("Upload successful")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "labels": labels,
            "audio_file": file_name,
            "message": "Audio generated successfully"
        })
    }