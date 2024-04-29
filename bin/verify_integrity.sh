#!/usr/bin/env bash



if [ $# -ne 3 ]; then
    echo "Pass valid arguments"
    exit 1;
fi

device_id="$1"
device_data="$2"
message_signature="$3"


if [ -f "$device_id/cert" ]; then
    cert_content=$(realpath "$device_id/cert")


    python3 authenticate_message.py "$device_data" "$message_signature" "$cert_content"

    if [ $? -eq 0 ]; then
        exit 0
    else
        exit 1
    fi
fi

exit 1