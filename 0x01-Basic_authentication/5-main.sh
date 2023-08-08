#!/bin/bash

curl localhost:5000/api/v1/status
curl localhost:5000/api/v1/status/
curl localhost:5000/api/v1/users
curl localhost:5000/api/v1/users -H 'Authorization: Test'