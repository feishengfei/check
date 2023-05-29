
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp              | ip                                  | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:-----------------|:------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.10.117                | United States | US   | SHARKTECH        | 64.32.10.114                        | Yes (Region: US) |
|  1 | [3](config/3.json)   | 45.131.248.228              | United States | US   | DEDIPATH-LLC     | 2402:d0c0:0:b230::1                 | Yes (Region: US) |
|  2 | [4](config/4.json)   | 173.82.59.238               | United States | US   | MULTA-ASN1       | 2607:f130:109:0:d6ae:52ff:febd:48da | Yes (Region: US) |
|  3 | [5](config/5.json)   | 67.21.84.214                | United States | US   | SHARKTECH        | 67.21.85.2                          | Yes (Region: US) |
|  4 | [6](config/6.json)   | 108.166.203.183             | United States | US   | MULTA-ASN1       | 173.82.156.42                       | Yes (Region: US) |
|  5 | [8](config/8.json)   | mg.txy.a.node1.jijio.stream | Netherlands   | NL   | YISP B.V.        | 154.84.1.145                        | Yes (Region: NL) |
|  6 | [12](config/12.json) | cf.noaries.de               | United States | US   | DEDIPATH-LLC     | 2602:fe90:1a:1::81b7:b0dc           | Yes (Region: US) |
|  7 | [15](config/15.json) | cdn.noice.id                | Singapore     | SG   | DIGITALOCEAN-ASN | 143.198.94.243                      | Yes (Region: SG) |
|  8 | [16](config/16.json) | 162.159.35.77               | France        | FR   | FEELB SARL       | 45.145.166.232                      | Yes (Region: FR) |
|  9 | [18](config/18.json) | 8.v2-ray.cyou               | Japan         | JP   | AMAZON-02        | 18.179.36.139                       | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMTAuMTE3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYzUyOGQ4ZDgtOTRkNi00OGE5LThkZDMtNTI4OTI1NThhNmFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQxMTY5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDMiLCAiYWRkIjogIjQ1LjEzMS4yNDguMjI4IiwgInBvcnQiOiAiNTkxMDIiLCAiaWQiOiAiYWMwMjczNjItYzk4OC00NjcwLWY3OGYtMDIxYjViZTZmNGUzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI0NS4xMzEuMjQ4LjIyOCIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTczLjgyLjU5LjIzOCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjE2OWZiNjRkLTIwOGQtNGUwNi1iZmMxLTZmOTY1NTRjYTNlZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1NjUzNiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYjlhMzA1YTktMWZmMi00ZWMxLWIzMzgtOTMzNTU1ODMzYmFhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3MDg4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMjY4YTQ5MWItNzY0Yy00NGQxLTgxYTQtMzBkZTE2MTMwODY3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0OTQ1LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAibWcudHh5LmEubm9kZTEuamlqaW8uc3RyZWFtIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJhZGM1NzBmMS1kNTkxLTRhNWEtOTNmMC0wMDEzYmJhM2YxMTYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3dlc2FkIiwgInBvcnQiOiAzODk5OSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjICA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAyMDgyLCAiaWQiOiAiNjdjNWNlNDUtN2I0OC00NzNlLWJmMjUtZTRjODMwYjBlZDI0IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJkZWRpcGF0aDIuaWlpby53aWtpIiwgInBhdGgiOiAiL2FyaWVzP2VkPTIwNDgiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICIxNjIuMTU5LjM1Ljc3IiwgInBvcnQiOiA0NDMsICJpZCI6ICJjOTFjN2NiNS02MDljLTRmYWUtODE4ZS05MTk0YzNkNDY5NjkiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImFmcmhtczEyLmJlc3QtdGl6aS50b3AiLCAicGF0aCI6ICIvbGlua3dzIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTgiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

