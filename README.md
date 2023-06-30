
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                      | cn            | cc   | isp       | ip           | chatgpt          |
|---:|:-------------------|:--------------------------|:--------------|:-----|:----------|:-------------|:-----------------|
|  0 | [3](config/3.json) | 156.225.67.131            |               |      |           | 154.84.1.219 | Yes (Region: NL) |
|  1 | [4](config/4.json) | 170.178.194.20            |               |      |           | 173.82.56.82 | Yes (Region: CA) |
|  2 | [5](config/5.json) | 45.199.138.76             |               |      |           | 154.84.1.127 | Yes (Region: NL) |
|  3 | [6](config/6.json) | 45.199.138.33             |               |      |           | 154.84.1.128 | Yes (Region: NL) |
|  4 | [8](config/8.json) | tw99-hinet.mynodes001.one | United States | US   | CNSERVERS | 23.225.9.234 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMzEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI1MTViY2I0ZC0wYmExLTRjYWUtODdjZi1hMDQ3MDA3ZWVjNTQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDgxMjMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTcwLjE3OC4xOTQuMjAiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIzMDIzOTgxYi0wNDMxLTRiZmYtOGExMC0wZjk4NmJhODZjNzMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTMzODYsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4Ljc2IiwgInBvcnQiOiAiNDk1OTgiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjM3YzI5ZjQyLWI3YzctNDBjNy05ZGE5LTc0M2RjYzQ4OTViYyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4zMyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImZlNWY2OWU3LWUxODMtNDM5Yi05NTBiLTk2NjFlZjA2NTFmMiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTEyMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAidHc5OS1oaW5ldC5teW5vZGVzMDAxLm9uZSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNWYwNGRlODQtNmI3ZS0zNTY0LTgyYzItZDJhOTk4MDAyNjI5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxKEhpTmV0KVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

