# PlantUML

Using a visual studio extension called "plantUML" which allows real time previews
https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml


## Rendering

1. Have docker desktop running on your local machine.
2. Install a local docker contain

    docker pull plantuml/plantuml-server

3. Start the docker container on port 8080

    docker run -d -p 8080:8080 plantuml/plantuml-server:jetty

4. Preview Diagram, Press Alt + D to start PlantUML preview (option + D on MacOS).