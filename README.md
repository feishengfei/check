
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp          | ip            | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-------------|:--------------|:-----------------|
|  0 | [2](config/2.json)   | 156.225.67.170 | Netherlands   | NL   | YISP B.V.    | 154.84.1.121  | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.249.18.10  | Netherlands   | NL   | YISP B.V.    | 154.84.1.40   | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 45.153.203.66  | United States | US   | DEDIPATH-LLC | 2.56.121.242  | Yes (Region: US) |
|  3 | [8](config/8.json)   | 156.245.8.143  |               |      |              | 54.36.174.181 | Yes (Region: FR) |
|  4 | [18](config/18.json) | 172.64.153.211 |               |      |              | 94.131.115.68 | Yes (Region: SE) |
|  5 | [29](config/29.json) | 6.wyhkaa0.gq   |               |      |              | 38.95.233.155 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNzAiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJiZDI0OWUzNy03MzU5LTQxZWUtODRhNy0wOWU0OWUwZWM1YzQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjM1OTc3IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4xMCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Nzk2NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlXHU4YzZhXHU3NjdiXHU3NzAxXHU3ZWE2XHU3ZmYwXHU1MTg1XHU2NWFmXHU1ODIxQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTUzLjIwMy42NiIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMwOTA1MDg5Lnh5eiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MzMwNDA5MTAzNyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0MyIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjkyODczODg5Lnh5eiIsICJpZCI6ICI2MTkzMTE2ZC05NmY5LTRkN2EtOWJlNS01YmIwNmE2OWFmMGIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MzIxOTQ4Mzg4NSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4yMTEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAic2NoZXJlc3dlZC5zb2Z0d2FyZW5ld3Muc3RvcmUiLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkwMSIsICJwb3J0IjogIjQ0MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTgiLCAic2N5IjogImF1dG8iLCAic25pIjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI5IiwgImFkZCI6ICI2Lnd5aGthYTAuZ3EiLCAicG9ydCI6IDIwOTUsICJpZCI6ICI2YmJjOTU1NC0wN2JjLTQ3YzYtYTA4OC04N2FhNzlmZDVjYTEiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogIjYud3loa2FhMC5ncSIsICJwYXRoIjogIi9URzpAaGthYTAiLCAidGxzIjogIiJ9
```

