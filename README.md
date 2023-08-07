
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn          | cc   | isp              | ip                     | chatgpt          |
|---:|:---------------------|:-----------------|:------------|:-----|:-----------------|:-----------------------|:-----------------|
|  0 | [6](config/6.json)   | 156.249.18.129   | Netherlands | NL   | YISP B.V.        | 154.84.1.138           | Yes (Region: NL) |
|  1 | [8](config/8.json)   | dongtaiwang3.com | Netherlands | NL   | CLOUDFLARENET    | 2a09:bac1:5560::20a:2a | Yes (Region: NL) |
|  2 | [11](config/11.json) | 156.245.8.183    | Netherlands | NL   | YISP B.V.        | 154.84.1.161           | Yes (Region: NL) |
|  3 | [14](config/14.json) | 45.199.138.155   | Netherlands | NL   | YISP B.V.        | 154.84.1.232           | Yes (Region: NL) |
|  4 | [22](config/22.json) | Gmail.tikal.tk   | Germany     | DE   | DIGITALOCEAN-ASN | 209.38.222.89          | Yes (Region: DE) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4xMjkiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xMTY0OTc2OS54eXoiLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTEzMTgzMTg0MjAiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlXHU4YzZhXHU3NjdiXHU3NzAxXHU3ZWE2XHU3ZmYwXHU1MTg1XHU2NWFmXHU1ODIxQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDYiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogImRvbmd0YWl3YW5nMy5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNmRlZGRiN2YtZTU1Ny00MmRiLWJmYTAtY2Y0MGIzNmIyN2UyIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJkLmZyZWVoMS54eXoiLCAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwgInRscyI6ICJ0bHMiLCAic25pIjogImQuZnJlZWgxLnh5eiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE4MyIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjIwMTYzMzIyLnh5eiIsICJpZCI6ICJkNzczNTA1OC0xZGFjLTQ2MTgtOTlmZi0wYWEwNDQxZWMyZDciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MTMxODMxODQyMCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDExIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNCIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNTUiLCAicG9ydCI6ICI1NDAwMCIsICJpZCI6ICIxMzBjOWYyZS00MmIxLTRlYmYtYjM0NS1lMjY0NTZhMDYxZjkiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDIyIiwgImFkZCI6ICJHbWFpbC50aWthbC50ayIsICJwb3J0IjogIjgwIiwgImlkIjogIjA3NjYwODhjLWUxZDAtNGYwOC1jYWM5LTljNGM2MGY3M2E0NSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiczMwLmdvb2R0b3AudGVjaCIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

