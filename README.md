
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn            | cc   | isp                               | ip             | chatgpt          |
|---:|:---------------------|:-------------------|:--------------|:-----|:----------------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | eeee.ednovas.cloud | Taiwan        | TW   | Data Communication Business Group | 114.43.128.179 | Yes (Region: TW) |
|  1 | [4](config/4.json)   | 156.245.8.130      | Netherlands   | NL   | YISP B.V.                         | 154.84.1.121   | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 64.32.24.211       | United States | US   | SHARKTECH                         | 170.178.189.58 | Yes (Region: US) |
|  3 | [8](config/8.json)   | 104.18.134.125     | United States | US   | CNSERVERS                         | 23.225.9.234   | Yes (Region: US) |
|  4 | [9](config/9.json)   | 156.225.67.73      | Netherlands   | NL   | YISP B.V.                         | 154.84.1.19    | Yes (Region: NL) |
|  5 | [13](config/13.json) | 107.167.16.217     | United States | US   | SHARKTECH                         | 67.21.87.226   | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMyIsICJhZGQiOiAiZWVlZS5lZG5vdmFzLmNsb3VkIiwgInBvcnQiOiAiMjE5MzUiLCAiaWQiOiAiODA2ZDlmZmEtNWYzNC00MWRmLThlZjUtNTMwZDc1OGFiMmRiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjEzMCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImJkMjQ5ZTM3LTczNTktNDFlZS04NGE3LTA5ZTQ5ZTBlYzVjNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzMTkyMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjExIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ4NjU5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjE4LjEzNC4xMjUiLCAiYWlkIjogMCwgImhvc3QiOiAiZHouMjAwMjExMjQueHl6IiwgImlkIjogIjZkY2FkYjRmLTVmZGEtNGZhOS04OWRjLWNlNDU2NGVjMWZjNiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDkiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1MzEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTA3LjE2Ny4xNi4yMTciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDEzIiwgInBvcnQiOiAzMzU4OSwgImlkIjogIjhjNjc5YjgxLTg0ZmMtNDNjZS05NTUzLWRkY2E1NzVhNjk0OSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

