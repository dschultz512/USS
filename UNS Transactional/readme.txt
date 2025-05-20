AsyncAPI schema used to describe the B2MML-BatchML interface
Interface is based on B2MML V0701

yaml files can be visualized using the VS code extension 'asyncapi-preview' or at studio.asyncapi.com

# Local Development 

install nodejs (nodejs.org)
Verify that nodejs is installed correctly
$ npm -v

install AsyncApi generator
$ npm install -g @asyncapi/generator

generate AsyncAPI (using V2 documentation)
$ ag -i --force-write asyncapi2.yaml @asyncapi/html-template@v0.28.4 -o docs -p favicon=./favicon.png


# Remote Deployment - Building Container

Preparations:

- Update publish date in asyncapi2.yaml

Prerequisites:

 - Docker >= v20

Command: 

- Set Terminal directory to AsyncAPI
- Run 'Docker' application

## Building the container
$ docker build . -t general-mills/rhize-mdh-documentation

## Run the container
$ docker run -p 80:80 general-mills/rhize-mdh-documentation:latest

## Pushing container
...

## Restart the Pod
...