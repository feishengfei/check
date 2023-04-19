
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                               | ip                    | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:----------------------------------|:----------------------|:-----------------|
|  0 | [8](config/8.json)   | 170.187.206.48           | Germany       | DE   | Hetzner Online GmbH               | 116.202.230.160       | Yes (Region: DE) |
|  1 | [11](config/11.json) | 3.mamadcucu.com          | Finland       | FI   | Hetzner Online GmbH               | 2a01:4f9:c011:752c::1 | Yes (Region: FI) |
|  2 | [16](config/16.json) | germany1.unlimiteddev.co | Germany       | DE   | Hetzner Online GmbH               | 116.202.230.160       | Yes (Region: DE) |
|  3 | [18](config/18.json) | hinet1261.gfwisbest.xyz  | Taiwan        | TW   | Data Communication Business Group | 1.171.219.239         | Yes (Region: TW) |
|  4 | [21](config/21.json) | 25.v2-ray.cyou           | United States | US   | AMAZON-02                         | 3.138.119.192         | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTcwLjE4Ny4yMDYuNDgiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvY2hhdCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMy5tYW1hZGN1Y3UuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIjMubWFtYWRjdWN1LmNvbSIsICJpZCI6ICI5MjkzNDRlMS00NzNjLTRmZWItYjg2Yi1mZGUzZWUxY2NkMTYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0Fyc2FsYW5UYXVCb3QiLCAicG9ydCI6ICIyMDg2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAxMSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICJnZXJtYW55MS51bmxpbWl0ZWRkZXYuY28iLCAicG9ydCI6ICI4MCIsICJpZCI6ICI5N2VhNzlhNi02MTVjLTRhZDctODA4My00ZjNiNDljYmU4YTIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImdlcm1hbnkxLnVubGltaXRlZGRldi5jbyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiaGluZXQxMjYxLmdmd2lzYmVzdC54eXoiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU2NWIwXHU1MzE3XHU1ZTAyXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDE4IiwgInBvcnQiOiAyMjQsICJpZCI6ICIyMjg1MTMzZS1iOWJhLTNmYjUtYTI0Ni05YzdkZGNjMmNkN2EiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMjEiLCAiYWRkIjogIjI1LnYyLXJheS5jeW91IiwgInBvcnQiOiAiMjM2MjUiLCAiaWQiOiAiMGRkMTlkMjAtZWM4Ni0zNjgwLWIyNTYtODcyMzdiYWZhODllIiwgImFpZCI6ICIyIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIyNS52Mi1yYXkuY3lvdSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

