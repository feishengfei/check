
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn              | cc   | isp                            | ip                                     | chatgpt          |
|---:|:---------------------|:---------------|:----------------|:-----|:-------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 52.142.146.57  | United Kingdom  | GB   | MICROSOFT-CORP-MSN-AS-BLOCK    | 52.142.146.57                          | Yes (Region: GB) |
|  1 | [7](config/7.json)   | 198.2.200.37   | United States   | US   | PEG-SV                         | 142.4.98.185                           | Yes (Region: US) |
|  2 | [24](config/24.json) | 45.87.153.246  | The Netherlands | NL   | Stark Industries Solutions Ltd | 45.87.153.246                          | Yes (Region: NL) |
|  3 | [30](config/30.json) | 45.159.249.231 | Finland         | FI   | Stark Industries Solutions Ltd | 45.159.249.231                         | Yes (Region: FI) |
|  4 | [36](config/36.json) | 64.176.37.216  | Japan           | JP   | AS-CHOOPA                      | 2401:c080:3800:3d2f:5400:4ff:feaa:a93e | Yes (Region: JP) |
|  5 | [37](config/37.json) | 188.114.97.18  | Canada          | CA   | AS-GLOBALTELEHOST              | 158.51.121.134                         | Yes (Region: CA) |
|  6 | [44](config/44.json) | 38.75.136.49   | United States   | US   | AS-GLOBALTELEHOST              | 38.75.136.49                           | Yes (Region: US) |
|  7 | [51](config/51.json) | 103.159.206.35 | Taiwan          | TW   | EMGINECONCEPT-01               | 103.159.206.35                         | Yes (Region: TW) |
|  8 | [55](config/55.json) | 45.8.147.80    | Sweden          | SE   | Stark Industries Solutions Ltd | 45.8.147.80                            | Yes (Region: SE) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6cGdQQmlZWEVoT3dnd3BDVGFvVHVp@52.142.146.57:50395#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%202
vmess://eyJhZGQiOiAiMTk4LjIuMjAwLjM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjE3MDgyNDAueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNzAyMjE1MjIzMzIwIiwgInBvcnQiOiAzMDAwMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgNyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2024
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2030
vmess://eyJhZGQiOiAiNjQuMTc2LjM3LjIxNiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMzYiLCAicG9ydCI6IDQ1OTMwLCAiaWQiOiAiYjI5MzBiMGQtMDJiNC00NWRjLTgwMjUtYTNjMTk4NzlkNGFiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICI2NC4xNzYuMzcuMjE2IiwgInBhdGgiOiAiL3ZtZXNzIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTg4LjExNC45Ny4xOCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJvZGVsaWEuYXV0b3MiLCAiaWQiOiAiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogImxpbmt2d3MiLCAicG9ydCI6ICI0NDMiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVkZjRcdTg5N2ZcdTU3MjNcdTRmZGRcdTdmNTdDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDM3IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJvZGVsaWEuYXV0b3MiLCAidGxzIjogInRscyIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@38.75.136.49:7306#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2044
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDUxIiwgImFkZCI6ICIxMDMuMTU5LjIwNi4zNSIsICJwb3J0IjogIjMxOTQ1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiZTJlNTExYjAtN2RlZi00ZTFiLWQyMzgtNmNiNTM5MWIyZTNmIiwgInNuaSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRNUNFaWViU3VTbDJxRmtmRTR6dEcy@45.8.147.80:5741#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2055
```

