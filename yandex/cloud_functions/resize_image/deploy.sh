#!/bin/bash
source ./src/.env

function create_cloud_function {
    yc serverless function create \
      --name="$YANDEX_FUNCTION_RESIZE_IMAGE_NAME" \
      --cloud-id="$YANDEX_FUNCTION_RESIZE_IMAGE_CLOUD_ID" \
      --folder-id="$YANDEX_FUNCTION_RESIZE_IMAGE_FOLDER_ID"
}

function create_cloud_function_version {
  yc serverless function version create \
    --function-name="$YANDEX_FUNCTION_RESIZE_IMAGE_NAME" \
    --service-account-id="$YANDEX_FUNCTION_RESIZE_IMAGE_SERVICE_ACCOUNT_ID" \
    --cloud-id="$YANDEX_FUNCTION_RESIZE_IMAGE_CLOUD_ID" \
    --folder-id="$YANDEX_FUNCTION_RESIZE_IMAGE_FOLDER_ID" \
    --runtime python39 \
    --entrypoint main.handler \
    --memory 128m \
    --execution-timeout 30s \
    --source-path ./build.zip \
    --environment \
YANDEX_CLOUD_FUNCTIONS_AWS_ACCESS_KEY_ID="$YANDEX_CLOUD_FUNCTIONS_AWS_ACCESS_KEY_ID",\
YANDEX_CLOUD_FUNCTIONS_AWS_ACCESS_KEY_SECRET="$YANDEX_CLOUD_FUNCTIONS_AWS_ACCESS_KEY_SECRET",\
YANDEX_CLOUD_FUNCTIONS_AWS_DEFAULT_REGION="$YANDEX_CLOUD_FUNCTIONS_AWS_DEFAULT_REGION",\
YANDEX_FUNCTION_RESIZE_IMAGE_IAM_TOKEN="$YANDEX_FUNCTION_RESIZE_IMAGE_IAM_TOKEN",\
YANDEX_FUNCTION_RESIZE_IMAGE_FOLDER_ID="$YANDEX_FUNCTION_RESIZE_IMAGE_FOLDER_ID",\
YANDEX_FUNCTION_RESIZE_IMAGE_NAME="$YANDEX_FUNCTION_RESIZE_IMAGE_NAME",\
YANDEX_FUNCTION_RESIZE_IMAGE_BUCKET_NAME="$YANDEX_FUNCTION_RESIZE_IMAGE_BUCKET_NAME",\
YANDEX_FUNCTION_RESIZE_IMAGE_OBJECT_STORAGE_MEDIA_PREFIX="$YANDEX_FUNCTION_RESIZE_IMAGE_OBJECT_STORAGE_MEDIA_PREFIX",\
RESIZE_IMAGE_VALID_SIZES="$RESIZE_IMAGE_VALID_SIZES"

  yc serverless function allow-unauthenticated-invoke \
    --name="$YANDEX_FUNCTION_RESIZE_IMAGE_NAME" \
    --cloud-id="$YANDEX_FUNCTION_RESIZE_IMAGE_CLOUD_ID" \
    --folder-id="$YANDEX_FUNCTION_RESIZE_IMAGE_FOLDER_ID"
}

function deploy {
  make check
  make compile-requirements
  python3 src/build.py
  create_cloud_function || echo "Function '$YANDEX_FUNCTION_RESIZE_IMAGE_NAME' is already created."
  create_cloud_function_version
}

echo "Deploying '$YANDEX_FUNCTION_RESIZE_IMAGE_NAME' function"
deploy
