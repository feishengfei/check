
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                                                            | ip                       | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:---------------------------------------------------------------|:-------------------------|:-----------------|
|  0 | [2](config/2.json)   | 50.118.145.164  | United States | US   | Evoxt Enterprise                                               | 2400:8d60:2::1:5143:b3e2 | Yes (Region: US) |
|  1 | [4](config/4.json)   | 223.165.6.246   | United States | US   | Evoxt Enterprise                                               | 2400:8d60:2::1:4646:6e5f | Yes (Region: US) |
|  2 | [11](config/11.json) | 108.165.113.99  | United States | US   | US-CLOUDNIUM-01                                                | 108.165.113.99           | Yes (Region: US) |
|  3 | [21](config/21.json) | 217.160.45.31   | Germany       | DE   | IONOS SE                                                       | 217.160.45.31            | Yes (Region: DE) |
|  4 | [25](config/25.json) | 199.188.111.232 | United States | US   | PEG-SV                                                         | 199.188.111.225          | Yes (Region: US) |
|  5 | [38](config/38.json) | 172.252.193.229 | United States | US   | Evoxt Enterprise                                               | 2400:8d60:2::1:ce97:8e1  | Yes (Region: US) |
|  6 | [63](config/63.json) | 183.232.238.77  | Hong Kong     | HK   | Zhipinshang Hongkong Electron Communication Technology Limited | 104.251.224.35           | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNTAuMTE4LjE0NS4xNjQiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogImFhNjE3NjczLTU2MzktNDY0NC1mNmRhLTEyYWRlNmU2MjQ0YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0ODE5NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMjIzLjE2NS42LjI0NiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMTFhYzUwYzAtZjc5Zi00NWFiLThkNmMtOWZjYjM1NzYyNDZhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM4ODY2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNzBcdTVlYTZcdTVjM2NcdTg5N2ZcdTRlOWEgIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTA4LjE2NS4xMTMuOTkiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogImVmMjJmYWQzLTY1MmEtNDhmYy1lODBhLTQ2ZmFhM2E2YTc4NyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAxMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIiIsICJwb3J0IjogODg4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZmI3XHU1NmZkT25lQW5kT25lXHU1MTZjXHU1M2Y4IDIxIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDI1IiwgImFkZCI6ICIxOTkuMTg4LjExMS4yMzIiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjUxMzYwODE4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE3MDA5MTY3NDkwMTgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTcyLjI1Mi4xOTMuMjI5IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIyMTljYWEyYS1lMGM0LTQ3MTAtYjIzNy1kYjUxYjZiMTlmN2QiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMjcxNTQsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMzgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRlMWNcdTgzOWVcdTVlMDJcdTc5ZmJcdTUyYTggNjMiLCAiYWRkIjogIjE4My4yMzIuMjM4Ljc3IiwgInBvcnQiOiAiMzUwNCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiYWI1MzcxOTUtYjc0Yy0zZGY1LWEzYTEtZDUwNDM0NWU4MGJiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
```

