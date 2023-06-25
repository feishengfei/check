
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                      | cn          | cc   | isp               | ip                                 | chatgpt          |
|---:|:---------------------|:--------------------------|:------------|:-----|:------------------|:-----------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 156.225.67.233            | Netherlands | NL   | YISP B.V.         | 154.84.1.178                       | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 156.245.8.225             | Netherlands | NL   | YISP B.V.         | 2a02:2a38:1:2796:ae1f:6bff:fef1:e2 | Yes (Region: NL) |
|  2 | [8](config/8.json)   | 23.227.38.99              | Germany     | DE   | AS-GLOBALTELEHOST | 193.108.118.34                     | Yes (Region: DE) |
|  3 | [10](config/10.json) | dl.v001sssv.pw            | France      | FR   | OVH SAS           | 51.77.213.73                       | Yes (Region: FR) |
|  4 | [23](config/23.json) | tw99-hinet.mynodes001.one |             |      |                   | 122.118.146.194                    | Yes (Region: TW) |
|  5 | [30](config/30.json) | 15.152.37.137             | Japan       | JP   | AMAZON-02         | 15.152.37.137                      | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yMzMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5MzUwM2RkNS0yNDVhLTRlYjEtYWUyYS01N2FiOWYyYjNjMjkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAiYWRkIjogIjE1Ni4yNDUuOC4yMjUiLCAicG9ydCI6ICI0ODEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMjMuMjI3LjM4Ljk5IiwgImFpZCI6IDAsICJob3N0IjogIjEuZnJlZWsxLnh5eiIsICJpZCI6ICI4NmQzNzUyNi01NzU4LTRjZWMtODYyZi1kZjQwNGIzMTMwODYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLzNHNldQREw3IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkoc2hvcGlmeSkgOCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiZGwudjAwMXNzc3YucHciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMCIsICJwb3J0IjogODAsICJpZCI6ICJhNGJiN2Y5My1jZWU2LTQzZDctYjJkZC1mYTljNzBiODgyMzMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiZGwudjAwMXNzc3YucHciLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEoSGlOZXQpXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIzIiwgImFkZCI6ICJ0dzk5LWhpbmV0Lm15bm9kZXMwMDEub25lIiwgInBvcnQiOiAiNDQ1IiwgImlkIjogIjVmMDRkZTg0LTZiN2UtMzU2NC04MmMyLWQyYTk5ODAwMjYyOSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmOVx1ZDgzY1x1ZGRmY1RXXHU1M2YwXHU2ZTdlKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTYwZTBcdTY2NmVIUCAzMCIsICJhZGQiOiAiMTUuMTUyLjM3LjEzNyIsICJwb3J0IjogIjI3NjQ3IiwgImlkIjogImIzNDgyNzc5LTgwYTYtNGI3Zi1jNTNkLTBkZjU4YTFmZTVjNyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRlZlx1ZDgzY1x1ZGRmNUpQXHU2NWU1XHU2NzJjKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
```

