
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp       | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:----------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 142.4.99.72    | United States | US   | PEG-SV    | 142.4.99.65    | Yes (Region: US) |
|  1 | [5](config/5.json)   | 156.225.67.112 | Netherlands   | NL   | YISP B.V. | 154.84.1.140   | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 156.249.18.29  | Netherlands   | NL   | YISP B.V. | 154.84.1.158   | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 156.245.8.241  | Netherlands   | NL   | YISP B.V. | 154.84.1.44    | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 162.159.58.218 | Poland        | PL   | OVH SAS   | 54.36.174.181  | Yes (Region: FR) |
|  5 | [11](config/11.json) | 156.245.8.144  | Netherlands   | NL   | YISP B.V. | 154.84.1.134   | Yes (Region: NL) |
|  6 | [24](config/24.json) | 162.159.60.89  | Spain         | ES   | NIXVAL    | 213.162.210.42 | Yes (Region: ES) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAzIiwgImFkZCI6ICIxNDIuNC45OS43MiIsICJwb3J0IjogNDQzLCAiaWQiOiAiYjY1ZGE0YWYtYTEyYS00YTU5LTkzMTYtNDU0OWUxMmJhNjJjIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjczMzMyNDYzLnh5eiIsICJwYXRoIjogIi9wYXRoLzE0MDMxOTAwMDIxNiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTEyIiwgInBvcnQiOiA0NDMsICJpZCI6ICJiOGRmM2VmMS04ODdmLTRlZTQtODU1Zi00ZjgwNDE2YzI0NjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTI0NjAxNTgueHl6IiwgInBhdGgiOiAiL3BhdGgvMDMzMjA2MTkzMTE4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTU2LjI0OS4xOC4yOSIsICJwb3J0IjogNDQzLCAiaWQiOiAiM2EzYzhhOWMtMzM0ZS00MzYwLWFkYjgtYTgwYTU3ZGRjYmJmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjE2MDQ2NjI2Lnh5eiIsICJwYXRoIjogIi9wYXRoLzAzMzIwNjE5MzExOCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDciLCAiYWRkIjogIjE1Ni4yNDUuOC4yNDEiLCAicG9ydCI6IDQ0MywgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0NjYzMTAzMTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTYyLjE1OS41OC4yMTgiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDExIiwgImFkZCI6ICIxNTYuMjQ1LjguMTQ0IiwgInBvcnQiOiA0NDMsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMzIxNTk4NzcueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDY2MzEwMzExNCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI0IiwgImFkZCI6ICIxNjIuMTU5LjYwLjg5IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiN2E2MGMxNWUtY2JjZC00ODZkLWFlZTYtMDdhNDk0ZjQwM2UzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ4YnkuZGFvemhhbmcubGluayIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
```

