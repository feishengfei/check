
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                     | cn            | cc   | isp           | ip                                  | chatgpt          |
|---:|:-------------------|:-------------------------|:--------------|:-----|:--------------|:------------------------------------|:-----------------|
|  0 | [4](config/4.json) | 100.42.70.145            | United States | US   | MULTA-ASN1    | 2607:f130:109:0:d6ae:52ff:febc:e193 | Yes (Region: US) |
|  1 | [5](config/5.json) | 156.249.18.38            | Netherlands   | NL   | YISP B.V.     | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: US) |
|  2 | [6](config/6.json) | 156.225.67.230           | Netherlands   | NL   | YISP B.V.     | 154.84.1.219                        | Yes (Region: NL) |
|  3 | [8](config/8.json) | cf-lt.sharecentre.online | Netherlands   | NL   | CLOUDFLARENET | 2a09:bac1:5560::20a:2a              | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTAwLjQyLjcwLjE0NSIsICJhaWQiOiAiNjQiLCAiZW5jcnlwdGlvbiI6ICJhdXRvIiwgImhvc3QiOiAiIiwgImlkIjogIjZhYWEyZjlmLTdjOTEtNGI1MS1hYTc3LTA1YTgzYTVkNmE0ZCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjQxMjQ1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiBmYWxzZSwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidXJsX2dyb3VwIjogInYycmF5IiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiMTU2LjI0OS4xOC4zOCIsICJwb3J0IjogIjQ4MjIyIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1cy5jYXNoZGF3aW9keGthd2phaW9jamRhd2Rhd2RhZHdyYXdnZnNlZ3NlZGVkd2FkYXdmZ3JkcmN2c3NzbC50b3AiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjMwIiwgInBvcnQiOiAiNTk4MDEiLCAiaWQiOiAiNTE1YmNiNGQtMGJhMS00Y2FlLTg3Y2YtYTA0NzAwN2VlYzU0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRlZFx1ZDgzY1x1ZGRmMEhLXHU5OTk5XHU2ZTJmKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjVmNzUxYzZlLTUwYjEtNDc5Ny1iYThlLTZmZmUzMjRhMGJjZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZHAzLnNjcHJveHkudG9wIiwgInBhdGgiOiAiL3NoaXJrZXIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

