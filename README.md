
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp                 | ip                                 | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:--------------------|:-----------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 23.225.28.186    | United States | US   | CNSERVERS           | 23.225.9.234                       | Yes (Region: US) |
|  1 | [2](config/2.json)   | 67.21.64.38      | United States | US   | SHARKTECH           | 2610:150:c011:6:ec4:7aff:fe4a:b00a | Yes (Region: US) |
|  2 | [3](config/3.json)   | 67.21.90.30      | United States | US   | SHARKTECH           | 107.167.22.10                      | Yes (Region: US) |
|  3 | [4](config/4.json)   | 107.148.242.216  | United States | US   | PEGTECHINC          | 107.148.242.241                    | Yes (Region: US) |
|  4 | [5](config/5.json)   | 45.58.186.81     | United States | US   | SHARKTECH           | 64.32.2.26                         | Yes (Region: US) |
|  5 | [6](config/6.json)   | 64.32.20.95      | United States | US   | SHARKTECH           | 64.32.0.58                         | Yes (Region: US) |
|  6 | [7](config/7.json)   | 154.85.0.242     | Netherlands   | NL   | YISP B.V.           | 154.84.1.145                       | Yes (Region: NL) |
|  7 | [8](config/8.json)   | 92.223.30.8      | United States | US   | AS-GLOBALTELEHOST   | 169.197.141.187                    | Yes (Region: US) |
|  8 | [11](config/11.json) | 156.245.8.93     | Netherlands   | NL   | YISP B.V.           | 154.84.1.178                       | Yes (Region: NL) |
|  9 | [12](config/12.json) | 107.167.16.85    | United States | US   | SHARKTECH           | 170.178.189.50                     | Yes (Region: US) |
| 10 | [19](config/19.json) | hd.mamadcucu.com | Germany       | DE   | Hetzner Online GmbH | 2a01:4f8:c010:7f47::1              | Yes (Region: DE) |
| 11 | [25](config/25.json) | hd.mamadcucu.com | Germany       | DE   | Hetzner Online GmbH | 2a01:4f8:c010:7495::1              | Yes (Region: DE) |

## Valid
```
vmess://eyJhZGQiOiAiMjMuMjI1LjI4LjE4NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjIyNzhlZmU0LWFkMGMtNDdjZS05NDgwLTA2ODYwODM2OGQ3NiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MDAzNCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2Q29wZXJhdGlvbiBDb2xvY3Rpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiNjcuMjEuNjQuMzgiLCAicG9ydCI6ICI0ODA3NCIsICJpZCI6ICJiNzRmNGFmYS0xYTU3LTRhZmYtYjdlNS04YWQ1ZWEzMzU2NmYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjcuMjEuOTAuMzAiLCAicG9ydCI6ICI0MjIxNiIsICJpZCI6ICIyOGRkNmMyNi0wNWE1LTRiYmEtOGE1ZC0wNTJiNzBhYzEzYjIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTA3LjE0OC4yNDIuMjE2IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiZGNjYTEyOTQtNzA5Ny00NGI3LWJkNDktNWY1MWM3M2Y1MzJmIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU0MDgyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiNDUuNTguMTg2LjgxIiwgInBvcnQiOiAiNTExNDAiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiNjQuMzIuMjAuOTUiLCAicG9ydCI6ICI0MzMzOSIsICJpZCI6ICJjMWJhZDlhNi0xNDgyLTQ5NDEtYTBjNC1lODVmM2NiYmNiNWEiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTU0Ljg1LjAuMjQyIiwgInBvcnQiOiAiNDg4MjMiLCAiaWQiOiAiNmU3OWVlYTQtNWY3Mi00NjgzLWFkMGUtNTMzOWYwMTM0MjFiIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiOTIuMjIzLjMwLjgiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjMzZDA0YWQ2LWM3ZGEtM2JhMS04OTQxLTM4NDU5NzgyMDlhOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAyMDg3LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVmYjdcdTU2ZmQgIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDExIiwgImFkZCI6ICIxNTYuMjQ1LjguOTMiLCAicG9ydCI6ICI0ODgyMiIsICJpZCI6ICI5MzUwM2RkNS0yNDVhLTRlYjEtYWUyYS01N2FiOWYyYjNjMjkiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTIiLCAiYWRkIjogIjEwNy4xNjcuMTYuODUiLCAicG9ydCI6ICI0NTY4OSIsICJpZCI6ICI3NjQwYTFlNy05NzAxLTQyOGUtYTRiMi0xOWIzZTdkZDZmOWYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiaGQubWFtYWRjdWN1LmNvbSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE5IiwgInBvcnQiOiAyMDk1LCAiaWQiOiAiMTkzNTBkNjQtNjg2OC00YTY0LWU1MDEtOWMwZGY5MDNkNzg4IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogImgzLm1hbWFkY3VjdS5jb20iLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiaGQubWFtYWRjdWN1LmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJoNC5tYW1hZGN1Y3UuY29tIiwgImlkIjogIjhlZDlhZWMyLWUwMmUtNGEyNy1mZTAyLWMzZTIwNDUyZTRjNyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAyMDUyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI1IiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIn0=
```

