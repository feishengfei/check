
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp                            | ip             | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:-------------------------------|:---------------|:-----------------|
|  0 | [8](config/8.json)   | 109.123.229.43       | Poland        | PL   | OVH SAS                        | 54.36.174.181  | Yes (Region: FR) |
|  1 | [9](config/9.json)   | 162.159.58.231       | France        | FR   | SYNLINQ                        | 103.252.90.249 | Yes (Region: FR) |
|  2 | [13](config/13.json) | 45.199.138.180       | Netherlands   | NL   | YISP B.V.                      | 154.84.1.229   | Yes (Region: NL) |
|  3 | [16](config/16.json) | 172.64.153.211       | Sweden        | SE   | Stark Industries Solutions Ltd | 94.131.115.68  | Yes (Region: SE) |
|  4 | [21](config/21.json) | ci.outline-vpn.cloud | United States | US   | SHARKTECH                      | 67.21.72.34    | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTYzNzdcdTUxNGIgIDgiLCAiYWRkIjogIjEwOS4xMjMuMjI5LjQzIiwgInBvcnQiOiAiNTU0NzMiLCAidHlwZSI6ICJub25lIiwgImlkIjogImZkODAyM2VhLThhOTEtMzM1MS1hYWNlLTkwNWYzYjRhM2Q2ZSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogImRvd25sb2FkLnhuLS1tZXMzNThhY2dtOTlsLmNvbSIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTYyLjE1OS41OC4yMzEiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xODAiLCAiYWlkIjogNjQsICJob3N0IjogIjQ1LjE5OS4xMzguMTgwIiwgImlkIjogImQzMTMzNDg0LWYyYmYtNGIwYy04ZDM4LWY4ZTY0NWI2NTY4NyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1NDc4NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgMTMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI2ZTc1MTcxMi05NTY5LTUxODctODZlYS04ZjU4NWFkOTkxMDUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInBhdGgiOiAiL2FwaTAxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiY2kub3V0bGluZS12cG4uY2xvdWQiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQzMTIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIxIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
```

