
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn            | cc   | isp                 | ip                          | chatgpt          |
|---:|:---------------------|:-----------------------|:--------------|:-----|:--------------------|:----------------------------|:-----------------|
|  0 | [3](config/3.json)   | 156.245.8.156          | Netherlands   | NL   | YISP B.V.           | 154.84.1.138                | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 154.84.1.47            | Netherlands   | NL   | YISP B.V.           | 154.84.1.121                | Yes (Region: NL) |
|  2 | [8](config/8.json)   | 156.245.8.187          | United States | US   | AS-GLOBALTELEHOST   | 169.197.141.187             | Yes (Region: US) |
|  3 | [9](config/9.json)   | 156.225.67.107         | Netherlands   | NL   | YISP B.V.           | 154.84.1.44                 | Yes (Region: NL) |
|  4 | [12](config/12.json) | join-bede.vmessorg.fun | Germany       | DE   | Hetzner Online GmbH | 2a01:4f8:192:348a::2        | Yes (Region: DE) |
|  5 | [16](config/16.json) | new6.huvicloud.com     | United States | US   | PONYNET             | 199.195.251.9               | Yes (Region: US) |
|  6 | [24](config/24.json) | st.suchenawa.com       |               |      |                     | 2a09:bac1:7680:99d8::1c:213 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE1NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjExMTE3ZDRjLTNiNmEtNGU3Ni04YmNjLTJiNDFiM2U5Y2E5MyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzU1MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU0Ljg0LjEuNDciLCAicG9ydCI6ICI0OTkyMCIsICJpZCI6ICJiZDI0OWUzNy03MzU5LTQxZWUtODRhNy0wOWU0OWUwZWM1YzQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE4NyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTMwOSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDkiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA3IiwgInBvcnQiOiAiNDUwMjAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiam9pbi1iZWRlLnZtZXNzb3JnLmZ1biIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjkxMTA1YzktMjA2MS00MGU2LTkyMTktZDA0ZDViNDg2OWQzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI4MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OWE2Y1x1Njc2NVx1ODk3Zlx1NGU5YVRtbmV0XHU1OTI3XHU5YTZjXHU3NTM1XHU4YmFmIDEyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAibmV3Ni5odXZpY2xvdWQuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJhMTFjYTc2MC05ZWY5LTRhNjMtOTVjOS00YzVjMzJkNTYyNTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2h1dmkiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAxNiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI0IiwgImFkZCI6ICJzdC5zdWNoZW5hd2EuY29tIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjY3MGM3NDVjLTg2OTktNDc0MS05NWIxLTJmZWZmYzBlNmUwYiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAic3Quc3VjaGVuYXdhLmNvbSIsICJwYXRoIjogIi9zdWNoZW4iLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

