#!/bin/bash

tag="$1"
docker build -t remy1991/image_similarity_app:$tag
docker push remy1991/image_similarity_app:$tag