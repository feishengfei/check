
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp                              | ip                                   | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:---------------------------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 156.245.8.84         | Netherlands   | NL   | YISP B.V.                        | 154.84.1.161                         | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 45.199.138.154       | Netherlands   | NL   | YISP B.V.                        | 154.84.1.232                         | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 45.199.138.136       | Netherlands   | NL   | YISP B.V.                        | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  3 | [6](config/6.json)   | cfcdn2.sanfencdn.net | United States | US   | Eons Data Communications Limited | 38.207.156.106                       | Yes (Region: US) |
|  4 | [7](config/7.json)   | 142.4.109.225        | United States | US   | PEGTECHINC                       | 142.4.99.65                          | Yes (Region: US) |
|  5 | [8](config/8.json)   | vm.uk.serverfast.pw  | Netherlands   | NL   | YISP B.V.                        | 154.84.1.197                         | Yes (Region: NL) |
|  6 | [13](config/13.json) | 45.199.138.90        | Netherlands   | NL   | YISP B.V.                        | 154.84.1.159                         | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDIiLCAiYWRkIjogIjE1Ni4yNDUuOC44NCIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvdnBuamFudGl0IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNTQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIxMzBjOWYyZS00MmIxLTRlYmYtYjM0NS1lMjY0NTZhMDYxZjkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDAyOTgsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEzNiIsICJwb3J0IjogIjQ4MzQ0IiwgImlkIjogIjc0M2JkYzg3LTFkZWEtNDFiZi1hYTBiLTUxZGZiYmZlYzhhYSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDYiLCAiYWRkIjogImNmY2RuMi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAyMDUyLCAiaWQiOiAiOTFiOWRhNDktY2I1My00ZTgyLTk3MzItODczNjkzNDcwNDQwIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ1czYuc2FuZmVuY2RuMi5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA3IiwgImFkZCI6ICIxNDIuNC4xMDkuMjI1IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImI2NWRhNGFmLWExMmEtNGE1OS05MzE2LTQ1NDllMTJiYTYyYyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy43MzMzMjQ2My54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjg5NTg4NDk3NzY1IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRJbnRlcmxhbmQgOCIsICJhZGQiOiAidm0udWsuc2VydmVyZmFzdC5wdyIsICJwb3J0IjogIjgwIiwgImlkIjogIjExNWJmYjM5LWMxNmMtNDQ3NC05ZDA2LTQ1MDBlZmVmNmQ3MiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidm0udWsuc2VydmVyZmFzdC5wdyIsICJwYXRoIjogIi92MnJheS12bWVzcy9udGxzIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMyIsICJhZGQiOiAiNDUuMTk5LjEzOC45MCIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogIjA3OGViMjRkLThkMWQtNGZiZC1iOTE0LWVlNThhODk3YTM1ZSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi9pc2FpZnFhYWdwaSIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

