
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp        | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 192.74.228.161 | United States | US   | PEGTECHINC | 142.0.129.201  | Yes (Region: US) |
|  1 | [3](config/3.json)   | 156.225.67.76  | Netherlands   | NL   | YISP B.V.  | 46.182.107.216 | Yes (Region: US) |
|  2 | [6](config/6.json)   | 156.249.18.16  | Netherlands   | NL   | YISP B.V.  | 154.84.1.193   | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 156.225.67.73  | Netherlands   | NL   | YISP B.V.  | 154.84.1.19    | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 51.195.125.16  | United States | US   | CNSERVERS  | 23.225.9.234   | Yes (Region: US) |
|  5 | [17](config/17.json) | 107.167.7.12   | United States | US   | SHARKTECH  | 107.167.18.50  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTkyLjc0LjIyOC4xNjEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDI4NTcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny43NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNlMDE2YzRkLTk4NmUtNDJkZi04MzhjLTYwNDZmM2Q4OWVjZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NDg5OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTU2LjI0OS4xOC4xNiIsICJwb3J0IjogIjQ3MDUwIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDciLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1MzEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNTEuMTk1LjEyNS4xNiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1NDkwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4MmYxXHU1NmZkXHU3OTNlXHU0ZjFhXHU0ZmRkXHU5NjY5XHU1Yjg5XHU1MTY4XHU5MGU4IDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTA3LjE2Ny43LjEyIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJiZGVlMjAyYy04ZmFlLTQ0MWYtYTU4OC03YmM0ZDM4ODcwMTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0MTY1NCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlx1NWUwMlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxNyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
```

