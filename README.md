
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                               | cn            | cc   | isp                              | ip                                    | chatgpt          |
|---:|:---------------------|:-----------------------------------|:--------------|:-----|:---------------------------------|:--------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 38.63.0.69                         | United States | US   | PEGTECHINC                       | 38.63.0.65                            | Yes (Region: US) |
|  1 | [4](config/4.json)   | cdn.yuntujisu.ml                   | United States | US   | PONYNET                          | 2605:6400:20:1fa6:c288:57d0:989e:4654 | Yes (Region: US) |
|  2 | [8](config/8.json)   | 156.249.18.9                       | Netherlands   | NL   | YISP B.V.                        | 154.84.1.145                          | Yes (Region: NL) |
|  3 | [9](config/9.json)   | 156.249.18.185                     | Netherlands   | NL   | YISP B.V.                        | 154.84.1.139                          | Yes (Region: NL) |
|  4 | [11](config/11.json) | cf.noaries.de                      | France        | FR   | CLOUDFLARENET                    | 2a09:bac1:27a0:48::13:284             | Yes (Region: FR) |
|  5 | [12](config/12.json) | 156.225.67.20                      | Netherlands   | NL   | YISP B.V.                        | 154.84.1.194                          | Yes (Region: NL) |
|  6 | [14](config/14.json) | 62e2186f.f0acf363.83df.34fb5e38.cc | Hong Kong     | HK   | Hong Kong Broadband Network Ltd. | 14.136.42.185                         | Yes (Region: US) |
|  7 | [15](config/15.json) | 8.v2-ray.cyou                      | Japan         | JP   | AMAZON-02                        | 18.179.36.139                         | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiMzguNjMuMC42OSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjE5NDU4MTYyLnh5eiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY4Mzk1NTY5Mzg0OCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiY2RuLnl1bnR1amlzdS5tbCIsICJhaWQiOiAwLCAiaG9zdCI6ICJuYW5vdXMueXRqczExNDUxNC5tbCIsICJpZCI6ICJkNTliMjRiMS1iNDc1LTRkNDQtYmU0Ni1hMTg1NjNhODc3MTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogMjA5NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiMTU2LjI0OS4xOC45IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40ODY0MzcwMC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjg0MzA2MjcyNDMwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAiMTU2LjI0OS4xOC4xODUiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNjE5MzExNmQtOTZmOS00ZDdhLTliZTUtNWJiMDZhNjlhZjBiIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjkyODczODg5Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2ODUwOTQ5MjM2MDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDExIiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiMjA1MiIsICJpZCI6ICI2N2M1Y2U0NS03YjQ4LTQ3M2UtYmYyNS1lNGM4MzBiMGVkMjQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNjdy1mci5paWlvLndpa2kiLCAicGF0aCI6ICIvYXJpZXM_ZWQ9MjA0OCIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEyIiwgImFkZCI6ICIxNTYuMjI1LjY3LjIwIiwgInBvcnQiOiAiNDQzIiwgImlkIjogImE3ZmE4ZjE0LTRmYjYtNDI4MC05MDA1LWQ2YmJlOTljNWRhOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy44NDU1MDE3OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjg1NTMwMDg5NjAwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://YWVzLTI1Ni1nY206MjNmMjRhNjUtNTdkZS00NjRiLTlmZjUtZTk5NGZiZDZmZTQ3@62e2186f.f0acf363.83df.34fb5e38.cc:30001#github.com/freefq%20-%20%E4%B8%8A%E6%B5%B7%E5%B8%82%E7%94%B5%E4%BF%A1%2014
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTUiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

