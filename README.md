
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp       | ip                                  | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:----------|:------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 156.249.18.38       | Netherlands   | NL   | YISP B.V. | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: US) |
|  1 | [5](config/5.json)   | 156.225.67.230      | Netherlands   | NL   | YISP B.V. | 154.84.1.219                        | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 45.199.138.155      | Netherlands   | NL   | YISP B.V. | 154.84.1.232                        | Yes (Region: NL) |
|  3 | [10](config/10.json) | a25.2e5bf271.win    | South Korea   | KR   | AMAZON-02 | 13.124.177.143                      | Yes (Region: KR) |
|  4 | [13](config/13.json) | 64.32.20.104        | United States | US   | SHARKTECH | 64.32.0.58                          | Yes (Region: US) |
|  5 | [18](config/18.json) | de01.vipnode.online | Germany       | DE   | AMAZON-02 | 3.76.210.224                        | Yes (Region: DE) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU2LjI0OS4xOC4zOCIsICJwb3J0IjogIjQ4MjIyIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1cy5jYXNoZGF3aW9keGthd2phaW9jamRhd2Rhd2RhZHdyYXdnZnNlZ3NlZGVkd2FkYXdmZ3JkcmN2c3NzbC50b3AiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjMwIiwgInBvcnQiOiAiNTk4MDEiLCAiaWQiOiAiNTE1YmNiNGQtMGJhMS00Y2FlLTg3Y2YtYTA0NzAwN2VlYzU0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRlZFx1ZDgzY1x1ZGRmMEhLXHU5OTk5XHU2ZTJmKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNTUiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIxMzBjOWYyZS00MmIxLTRlYmYtYjM0NS1lMjY0NTZhMDYxZjkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQ5MjAwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgNiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiYTI1LjJlNWJmMjcxLndpbiIsICJhaWQiOiAwLCAiaG9zdCI6ICJhMjUuMmU1YmYyNzEud2luIiwgImlkIjogIjM4Yjg5NjM5LTg2YmItNGViNS1iNzY2LTE4MTY0NDhjNDcyZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5N2U5XHU1NmZkXHU5OTk2XHU1YzE0QW1hem9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDEwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuMjAuMTA0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYzFiYWQ5YTYtMTQ4Mi00OTQxLWEwYzQtZTg1ZjNjYmJjYjVhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQwMDM5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRBbWF6b24gRUMyXHU2NzBkXHU1MmExXHU1NjY4IDE4IiwgImFkZCI6ICJkZTAxLnZpcG5vZGUub25saW5lIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMmExOWQ0ODYtYzZiOS00MTdmLWE4YTEtYTVmODQxZTg3ODc5IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
```

