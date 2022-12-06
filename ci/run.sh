#!/usr/bin/env bash

echo "****************************************"
echo "inside script"

 [ "${{ github.ref_name }}" = "master" ] && [ "${{ github.event_name }}" != "pull_request" ]

 echo "${{ github.event_name }}"