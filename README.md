# scadabr-docker
This script installs ScadaBR v1.2 with all the required components (Apache Tomcat 9, JDK 8, Python 3.10, and pyModbusTCP 0.2.2). Upon container creation, it starts the Tomcat server with ScadaBR.war and also initiates a ModbusTCP server listening on port 502/tcp.

To build and run:
```
docker compose build && docker compose up -d
```

Then, open a browser and type URL in order to access ScadaBR service: `http://localhost:8080/ScadaBR`

### :page_facing_up: License

Copyright (c) 2024 [CARLOS M. D. VIEGAS](https://github.com/cmdviegas).
