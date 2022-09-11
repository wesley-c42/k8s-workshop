#!/usr/bin/env bash
docker build -t hello-workshop:v1 ./app/v1
docker build -t hello-workshop:v2 ./app/v2
docker build -t hello-workshop:v3 ./app/v3
