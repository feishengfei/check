
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp                            | ip            | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:-------------------------------|:--------------|:-----------------|
|  0 | [2](config/2.json)   | ci.outline-vpn.cloud | United States | US   | SHARKTECH                      | 67.21.72.34   | Yes (Region: US) |
|  1 | [5](config/5.json)   | 67.21.64.84          | United States | US   | SHARKTECH                      | 67.21.72.34   | Yes (Region: US) |
|  2 | [7](config/7.json)   | 156.245.8.145        | Netherlands   | NL   | YISP B.V.                      | 154.84.1.134  | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 9.wyhkaa0.gq         | Poland        | PL   | OVH SAS                        | 54.36.174.181 | Yes (Region: FR) |
|  4 | [12](config/12.json) | 156.225.67.171       | Netherlands   | NL   | YISP B.V.                      | 154.84.1.121  | Yes (Region: NL) |
|  5 | [22](config/22.json) | 172.64.153.211       | Sweden        | SE   | Stark Industries Solutions Ltd | 94.131.115.68 | Yes (Region: SE) |

## Valid
```
vmess://eyJhZGQiOiAiY2kub3V0bGluZS12cG4uY2xvdWQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAicG9ydCI6IDQzMTIzLCAiaWQiOiAiMjU2NmQwMGYtMjE4Yy00OGY3LTlhMzYtMTNkM2Q2ZjFhNzI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwOTEzYjFhYy0xZjZjLTQzNmItOTliNC1hNWQ2ZTM0M2QwMjUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTE4NzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjcuMjEuNjQuODQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMxMjMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0NSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMyMTU5ODc3Lnh5eiIsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5Mjk2MjQzMTA5OSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDciLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjkud3loa2FhMC5ncSIsICJwb3J0IjogIjIwOTUiLCAiaWQiOiAiZDgzOGQ5OWEtNjgwNi00YmU0LWMxMjYtN2ZjYTYxM2NmNmE5IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI5Lnd5aGthYTAuZ3EiLCAicGF0aCI6ICIvVEc6QGhrYWEwIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNzEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAxMiIsICJwb3J0IjogMzU5NzcsICJpZCI6ICJiZDI0OWUzNy03MzU5LTQxZWUtODRhNy0wOWU0OWUwZWM1YzQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIyIiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI2ZTc1MTcxMi05NTY5LTUxODctODZlYS04ZjU4NWFkOTkxMDUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInBhdGgiOiAiL2FwaTAxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

