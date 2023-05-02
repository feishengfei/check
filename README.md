
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn            | cc   | isp                 | ip                    | chatgpt          |
|---:|:---------------------|:-------------------|:--------------|:-----|:--------------------|:----------------------|:-----------------|
|  0 | [3](config/3.json)   | 169.197.141.187    | United States | US   | AS-GLOBALTELEHOST   | 169.197.141.187       | Yes (Region: US) |
|  1 | [8](config/8.json)   | i.vpchi.tk         | United States | US   | AS-GLOBALTELEHOST   | 169.197.141.187       | Yes (Region: US) |
|  2 | [11](config/11.json) | 156.245.8.95       | Netherlands   | NL   | YISP B.V.           | 154.84.1.178          | Yes (Region: NL) |
|  3 | [13](config/13.json) | new6.huvicloud.com | United States | US   | PONYNET             | 199.195.251.9         | Yes (Region: US) |
|  4 | [22](config/22.json) | 172.67.38.105      | Finland       | FI   | Hetzner Online GmbH | 2a01:4f9:c010:baec::1 | Yes (Region: DE) |
|  5 | [25](config/25.json) | 156.225.67.126     | Netherlands   | NL   | YISP B.V.           | 154.84.1.158          | Yes (Region: NL) |
|  6 | [27](config/27.json) | 156.249.18.16      | Netherlands   | NL   | YISP B.V.           | 154.84.1.193          | Yes (Region: NL) |

## Valid
```
ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0@169.197.141.187:8882#github.com/freefq%20-%20%E5%8C%97%E7%BE%8E%E5%9C%B0%E5%8C%BA%20%203
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImkudnBjaGkudGsiLCAicG9ydCI6IDIwODIsICJpZCI6ICIxY2JjYmVmZi1kZTA3LTRmNDMtOGNhOS00Y2IzYTJhNTA4YWIiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImkudnBjaGkudGsiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDExIiwgImFkZCI6ICIxNTYuMjQ1LjguOTUiLCAicG9ydCI6ICI1MTk0OCIsICJpZCI6ICI5MzUwM2RkNS0yNDVhLTRlYjEtYWUyYS01N2FiOWYyYjNjMjkiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAibmV3Ni5odXZpY2xvdWQuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJhMTFjYTc2MC05ZWY5LTRhNjMtOTVjOS00YzVjMzJkNTYyNTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2h1dmkiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjY3LjM4LjEwNSIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJoLmgzaW8uY28iLCAiaWQiOiAiZmNiZDVjMDctZmJhNS00ZmY5LWMxOWMtMDJlMDIzMjIwNjI4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogImhvM2lubyIsICJwb3J0IjogIjIwOTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJoLmgzaW8uY28iLCAidGxzIjogInRscyIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDI1IiwgImFkZCI6ICIxNTYuMjI1LjY3LjEyNiIsICJwb3J0IjogIjUyODAzIiwgImlkIjogIjNhM2M4YTljLTMzNGUtNDM2MC1hZGI4LWE4MGE1N2RkY2JiZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4xNiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzMTIyMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlXHU4YzZhXHU3NjdiXHU3NzAxXHU3ZWE2XHU3ZmYwXHU1MTg1XHU2NWFmXHU1ODIxQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDI3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

