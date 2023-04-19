
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                 | ip                                  | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:--------------------|:------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 3.mamadcucu.com          | Finland       | FI   | Hetzner Online GmbH | 2a01:4f9:c011:752c::1               | Yes (Region: FI) |
|  1 | [4](config/4.json)   | germany1.unlimiteddev.co | Germany       | DE   | Hetzner Online GmbH | 116.202.230.160                     | Yes (Region: DE) |
|  2 | [5](config/5.json)   | 46.182.107.15            | Netherlands   | NL   | YISP B.V.           | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 170.187.206.48           | Germany       | DE   | Hetzner Online GmbH | 116.202.230.160                     | Yes (Region: DE) |
|  4 | [12](config/12.json) | 25.v2-ray.cyou           | United States | US   | AMAZON-02           | 3.138.119.192                       | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMy5tYW1hZGN1Y3UuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIjMubWFtYWRjdWN1LmNvbSIsICJpZCI6ICI5MjkzNDRlMS00NzNjLTRmZWItYjg2Yi1mZGUzZWUxY2NkMTYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0Fyc2FsYW5UYXVCb3QiLCAicG9ydCI6ICIyMDg2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAyIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDQiLCAiYWRkIjogImdlcm1hbnkxLnVubGltaXRlZGRldi5jbyIsICJwb3J0IjogIjgwIiwgImlkIjogIjk3ZWE3OWE2LTYxNWMtNGFkNy04MDgzLTRmM2I0OWNiZThhMiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZ2VybWFueTEudW5saW1pdGVkZGV2LmNvIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNDYuMTgyLjEwNy4xNSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MTMzMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4Mzc3XHU1MTcwICA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTcwLjE4Ny4yMDYuNDgiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvY2hhdCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjI1LnYyLXJheS5jeW91IiwgInBvcnQiOiAiMjM2MjUiLCAiaWQiOiAiMGRkMTlkMjAtZWM4Ni0zNjgwLWIyNTYtODcyMzdiYWZhODllIiwgImFpZCI6ICIyIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIyNS52Mi1yYXkuY3lvdSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

