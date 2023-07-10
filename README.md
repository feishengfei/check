
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp          | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 45.92.160.20   | United States | US   | DEDIPATH-LLC | 193.202.44.194 | Yes (Region: US) |
|  1 | [4](config/4.json)   | 156.225.67.71  | Netherlands   | NL   | YISP B.V.    | 154.84.1.19    | Yes (Region: NL) |
|  2 | [8](config/8.json)   | 203.23.104.190 | United States | US   | CNSERVERS    | 23.225.9.234   | Yes (Region: US) |
|  3 | [11](config/11.json) | 192.74.228.189 | United States | US   | PEGTECHINC   | 142.0.129.201  | Yes (Region: US) |
|  4 | [12](config/12.json) | 192.74.228.171 | United States | US   | PEGTECHINC   | 142.0.129.201  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuOTIuMTYwLjIwIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NmIyN1x1NzZkZiAgMyIsICJwb3J0IjogNDc4MzksICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzEiLCAicG9ydCI6ICI0ODEyMyIsICJpZCI6ICIyMTE1NWVmZC04ZTI5LTQzZDItOTViYy1mZTMxOTBlY2IxYzYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2MgOCIsICJhZGQiOiAiMjAzLjIzLjEwNC4xOTAiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiRUY2RUU2OTQtM0IwNy00RDBBLTk5NTUtMDQzRkQyMzVGNkQzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJEdXNzZWxkb3JmLmtvdGljay5zaXRlIiwgInBhdGgiOiAiL3NwZWVkdGVzdCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTkyLjc0LjIyOC4xODkiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAicG9ydCI6IDQyODU3LCAiaWQiOiAiMDUxYjg0NGYtZWZlMy00ODQ3LTkyYWEtNjZiNWRlMGI2ZDRlIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxMiIsICJhZGQiOiAiMTkyLjc0LjIyOC4xNzEiLCAicG9ydCI6ICI0Mjg1NyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMDUxYjg0NGYtZWZlMy00ODQ3LTkyYWEtNjZiNWRlMGI2ZDRlIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL3BvaXNvbiIsICJob3N0IjogInMxLjJiMi50b3AiLCAidGxzIjogIiJ9
```

