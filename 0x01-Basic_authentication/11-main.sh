#!/bin/bash

curl localhost:5000/api/v1/status
curl localhost:5000/api/v1/users
curl localhost:5000/api/v1/users -H 'Authorization: Test'
curl localhost:5000/api/v1/users -H 'Authorization: Basic test'
curl localhost:5000/api/v1/users -H 'Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh'