
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn          | cc   | isp                 | ip                    | chatgpt          |
|---:|:---------------------|:-------------------------|:------------|:-----|:--------------------|:----------------------|:-----------------|
|  0 | [4](config/4.json)   | 156.245.8.105            | Netherlands | NL   | YISP B.V.           | 154.84.1.128          | Yes (Region: NL) |
|  1 | [7](config/7.json)   | 156.225.67.250           | Netherlands | NL   | YISP B.V.           | 154.84.1.36           | Yes (Region: NL) |
|  2 | [15](config/15.json) | 3.mamadcucu.com          | Finland     | FI   | Hetzner Online GmbH | 2a01:4f9:c011:752c::1 | Yes (Region: FI) |
|  3 | [17](config/17.json) | join-bede.vmessorg.fun   | Germany     | DE   | Hetzner Online GmbH | 2a01:4f8:192:348a::2  | Yes (Region: DE) |
|  4 | [19](config/19.json) | 4.mamadcucu.com          | Finland     | FI   | Hetzner Online GmbH | 2a01:4f9:c011:605c::1 | Yes (Region: FI) |
|  5 | [29](config/29.json) | germany1.unlimiteddev.co | Germany     | DE   | Hetzner Online GmbH | 116.202.230.160       | Yes (Region: DE) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjEwNSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImZlNWY2OWU3LWUxODMtNDM5Yi05NTBiLTk2NjFlZjA2NTFmMiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzMDc3OSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yNTAiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIzZmQ2MzdhZC00NmZlLTRmODUtYTZlOC04NmIwMGJjYTExMjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMy5tYW1hZGN1Y3UuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIjMubWFtYWRjdWN1LmNvbSIsICJpZCI6ICI5MjkzNDRlMS00NzNjLTRmZWItYjg2Yi1mZGUzZWUxY2NkMTYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0Fyc2FsYW5UYXVCb3QiLCAicG9ydCI6ICIyMDg2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxNSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiam9pbi1iZWRlLnZtZXNzb3JnLmZ1biIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiNTk0NzgwZWEtMWQyMC00NTk4LTllYzEtZGRjMjIyMDA4ODhkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI4MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OWE2Y1x1Njc2NVx1ODk3Zlx1NGU5YVRtbmV0XHU1OTI3XHU5YTZjXHU3NTM1XHU4YmFmIDE3IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiNC5tYW1hZGN1Y3UuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIjQubWFtYWRjdWN1LmNvbSIsICJpZCI6ICI1MWJhNWE5YS00YjdjLTRjNjItYjRhZS0wZTUzZWM4ZDMwMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0Fyc2FsYW5UYXVCb3QiLCAicG9ydCI6ICI4ODgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxOSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI5IiwgImFkZCI6ICJnZXJtYW55MS51bmxpbWl0ZWRkZXYuY28iLCAicG9ydCI6ICI4MCIsICJpZCI6ICI5N2VhNzlhNi02MTVjLTRhZDctODA4My00ZjNiNDljYmU4YTIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImdlcm1hbnkxLnVubGltaXRlZGRldi5jbyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

