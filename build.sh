#!/bin/bash

tag=$1
namespace="remy1991"
docker build -t $namespace/image_similarity_app:$tag .
docker push $namespace/image_similarity_app:$tag