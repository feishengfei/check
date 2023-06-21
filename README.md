
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                      | cn          | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:--------------------------|:------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [8](config/8.json)   | tw99-hinet.mynodes001.one | Germany     | DE   | AS-GLOBALTELEHOST | 193.108.118.34 | Yes (Region: DE) |
|  1 | [15](config/15.json) | 156.249.18.159            | Netherlands | NL   | YISP B.V.         | 154.84.1.134   | Yes (Region: NL) |
|  2 | [16](config/16.json) | 156.245.8.128             | Netherlands | NL   | YISP B.V.         | 154.84.1.164   | Yes (Region: NL) |
|  3 | [21](config/21.json) | 156.225.67.76             | Netherlands | NL   | YISP B.V.         | 46.182.107.216 | Yes (Region: NL) |
|  4 | [22](config/22.json) | 156.225.67.131            | Netherlands | NL   | YISP B.V.         | 154.84.1.219   | Yes (Region: NL) |
|  5 | [26](config/26.json) | 156.245.8.142             | Netherlands | NL   | YISP B.V.         | 154.84.1.139   | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTgyZDdcdTY4MTdcdTUzYmZcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgOCIsICJhZGQiOiAidHc5OS1oaW5ldC5teW5vZGVzMDAxLm9uZSIsICJwb3J0IjogIjQ0NSIsICJpZCI6ICI1ZjA0ZGU4NC02YjdlLTM1NjQtODJjMi1kMmE5OTgwMDI2MjkiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjlcdWQ4M2NcdWRkZmNUV1x1NTNmMFx1NmU3ZSh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwMikiLCAicGF0aCI6ICIvYW50aTEzLnppbmdmYXN0LnZuIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTUiLCAiYWRkIjogIjE1Ni4yNDkuMTguMTU5IiwgInBvcnQiOiAiNDYwOTgiLCAiaWQiOiAiNjNiNGI4MjktN2YwMS00ZTI2LWIwMzctZjA0YjFmMDk4NzY1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE2IiwgImFkZCI6ICIxNTYuMjQ1LjguMTI4IiwgInBvcnQiOiAiNTA5MDAiLCAiaWQiOiAiM2NhOTEyZGEtNmFjMi00MThmLWI5Y2YtNDViNmY2OTQ1NzliIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIxIiwgImFkZCI6ICIxNTYuMjI1LjY3Ljc2IiwgInBvcnQiOiAiNDA4MDAiLCAiaWQiOiAiM2UwMTZjNGQtOTg2ZS00MmRmLTgzOGMtNjA0NmYzZDg5ZWNmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIyIiwgImFkZCI6ICIxNTYuMjI1LjY3LjEzMSIsICJwb3J0IjogIjQ4ODIxIiwgImlkIjogIjUxNWJjYjRkLTBiYTEtNGNhZS04N2NmLWEwNDcwMDdlZWM1NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDI2IiwgImFkZCI6ICIxNTYuMjQ1LjguMTQyIiwgInBvcnQiOiAiNDg4MjEiLCAiaWQiOiAiNjE5MzExNmQtOTZmOS00ZDdhLTliZTUtNWJiMDZhNjlhZjBiIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

