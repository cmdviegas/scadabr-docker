# scadabr-docker
This script installs ScadaBR v1.2 with all requirements (Apache Tomcat 9 + JDK 8 + Python 3.10 + pyModbusTCP 0.2.1)

To build and run this:
```
docker compose build && docker compose up -d
```

Then, open a browser and type URL in order to access ScadaBR service: `http://localhost:8080/ScadaBR`
