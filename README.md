
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr           | cn          | cc   | isp                 | ip            | chatgpt          |
|---:|:-------------------|:---------------|:------------|:-----|:--------------------|:--------------|:-----------------|
|  0 | [2](config/2.json) | 198.2.215.119  | China       | CN   | PEG-SV              | 142.4.107.246 | Yes (Region: US) |
|  1 | [3](config/3.json) | 49.13.115.8    | Germany     | DE   | Hetzner Online GmbH | 49.13.115.8   | Yes (Region: DE) |
|  2 | [4](config/4.json) | 156.249.18.4   | Netherlands | NL   | YISP B.V.           | 154.84.1.148  | Yes (Region: NL) |
|  3 | [5](config/5.json) | 156.225.67.104 | Netherlands | NL   | YISP B.V.           | 154.84.1.44   | Yes (Region: NL) |
|  4 | [8](config/8.json) | 45.199.138.186 | Netherlands | NL   | YISP B.V.           | 154.84.1.122  | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAyIiwgImFkZCI6ICIxOTguMi4yMTUuMTE5IiwgInBvcnQiOiA0NDMsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNzI3OTUwMjUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5Nzk4MDEwMTI0OSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTYgIDMiLCAiYWRkIjogIjQ5LjEzLjExNS44IiwgInBvcnQiOiA0NjgxOCwgImlkIjogIjQyNzc2ZWQ2LWFhYzYtNGY5NC1kYWE1LWM2YmQxOThkMDliMiIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAicHZlLWFzaWF0ZWNoLTEubWFuYWdlbWVudC5hcnZhbmNkbi5pciIsICJwYXRoIjogIi92cG52MnJheXNwZWVkIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU2LjI0OS4xOC40IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjg0ZDFkZTExLWNlMTItNGExNS04MzEyLTEzMzgzNTZkNGFjNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41NzQyNDM0OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3NzE5NTA2Mjc1IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA4IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NzM3Njc4Mjg3OSIsICJ0bHMiOiAidGxzIn0=
```

