#!/bin/bash

set -e

IBlue='\033[0;94m'
RED='\033[0;31m'
Green='\033[0;32m'
NC='\033[0m' # No Color

curl -I http://localhost:8080/png/ 2>/dev/null | grep -q 'HTTP/1.1 200 OK' || { printf "[${RED}ERROR${NC}] PlantUML server not running, try running with docker: ${IBlue} docker run -p 8080:8080 plantuml/plantuml-server:jetty ${NC}\n"; exit 1; }

target=${1:?needs target dir argument}
mkdir -p $target
find ./Drawings -type f -name '*.puml' | while read f
do
    d=$(dirname $f)
    printf "[${Green}INFO${NC}] $f - regenerating\n"
    mkdir -p $target/$d
    destfile=${f%%.puml}.png
    cat "${f}" |  curl --silent --show-error --fail -H "Content-Type: text/plain" --data-binary @- http://localhost:8080/png/ --output - > "${target}/${destfile}"
done
