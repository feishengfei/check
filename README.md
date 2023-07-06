
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr               | cn             | cc   | isp                               | ip            | chatgpt          |
|---:|:-------------------|:-------------------|:---------------|:-----|:----------------------------------|:--------------|:-----------------|
|  0 | [2](config/2.json) | 107.167.16.217     | United States  | US   | SHARKTECH                         | 67.21.87.226  | Yes (Region: US) |
|  1 | [3](config/3.json) | 156.225.67.233     | Netherlands    | NL   | YISP B.V.                         | 154.84.1.178  | Yes (Region: NL) |
|  2 | [4](config/4.json) | eeee.ednovas.cloud | Taiwan         | TW   | Data Communication Business Group | 114.43.139.16 | Yes (Region: TW) |
|  3 | [6](config/6.json) | 83.142.225.32      | United Kingdom | GB   | Iomart Cloud Services Limited     | 83.142.225.28 | Yes (Region: GB) |
|  4 | [8](config/8.json) | 104.17.3.81        | United States  | US   | CNSERVERS                         | 23.225.9.234  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTA3LjE2Ny4xNi4yMTciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAicG9ydCI6IDMzNTg5LCAiaWQiOiAiOGM2NzliODEtODRmYy00M2NlLTk1NTMtZGRjYTU3NWE2OTQ5IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yMzMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5MzUwM2RkNS0yNDVhLTRlYjEtYWUyYS01N2FiOWYyYjNjMjkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDgxMjMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggNCIsICJhZGQiOiAiZWVlZS5lZG5vdmFzLmNsb3VkIiwgInBvcnQiOiAiMjE5MzUiLCAiaWQiOiAiODA2ZDlmZmEtNWYzNC00MWRmLThlZjUtNTMwZDc1OGFiMmRiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiODMuMTQyLjIyNS4zMiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjUyNjdjYTcxLTk3ZTYtNDRjOC04ZmI1LTlmZTRhZmUwOTU0ZSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTkyMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4MmYxXHU1NmZkICA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjEwNC4xNy4zLjgxIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjEzMjYzM2E5LWI1M2UtNDM1Mi04MmE2LTkzZWFlMTE0NDgyZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZHluYW1pYy1zZzFiLm9iZnMueHl6IiwgInBhdGgiOiAiL3dvcnJ5ZnJlZSIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIifQ==
```

