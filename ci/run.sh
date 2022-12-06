#!/usr/bin/env bash

echo "****************************************"
echo "inside script"

 [ "$BRANCH_NAME" = "master" ] && [ "$GITHUB_EVENT" != "pull_request" ]

 echo "${{ github.event_name }}"