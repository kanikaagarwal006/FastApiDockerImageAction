# FastApiDockerImageAction
To create docker image using GitHub actions and push to docker hub
# to build docker image and tag
`docker build -t  localfastapiapp .`
to update tag for docker hub
`docker tag localfastapiapp DOCKERHUB_USERNAME/APPNAME`
like
`docker tag localfastapiapp kanikaagarwal006/demoapp`
user
`echo TOKEN | docker login -u USERNAME --stdin-passwd`