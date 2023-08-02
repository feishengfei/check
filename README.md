
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                       | cn            | cc   | isp                               | ip                                   | chatgpt          |
|---:|:---------------------|:---------------------------|:--------------|:-----|:----------------------------------|:-------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 108.166.203.181            | United States | US   | MULTA-ASN1                        | 173.82.156.42                        | Yes (Region: US) |
|  1 | [6](config/6.json)   | 45.199.138.135             | Netherlands   | NL   | YISP B.V.                         | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: US) |
|  2 | [8](config/8.json)   | dongtaiwang2.com           | Hong Kong     | HK   | CNSERVERS                         | 172.247.175.42                       | Yes (Region: US) |
|  3 | [11](config/11.json) | 67.21.84.216               | United States | US   | SHARKTECH                         | 67.21.85.2                           | Yes (Region: US) |
|  4 | [13](config/13.json) | tw98-1g-hinet.mytls888.com | Taiwan        | TW   | Data Communication Business Group | 61.224.79.34                         | Yes (Region: TW) |

## Valid
```
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgxIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMjY4YTQ5MWItNzY0Yy00NGQxLTgxYTQtMzBkZTE2MTMwODY3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0OTQ1LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEzNSIsICJwb3J0IjogIjQ5MTI5IiwgImlkIjogIjc0M2JkYzg3LTFkZWEtNDFiZi1hYTBiLTUxZGZiYmZlYzhhYSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogImRvbmd0YWl3YW5nMi5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMjVhOWYzYjktMWU2ZC00MGJkLTk2OGItZTA4MThjMWIxOTZmIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIyLmZyZWVrMS54eXoiLCAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE2IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxMSIsICJwb3J0IjogNDcwODgsICJpZCI6ICJiOWEzMDVhOS0xZmYyLTRlYzEtYjMzOC05MzM1NTU4MzNiYWEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAidHc5OC0xZy1oaW5ldC5teXRsczg4OC5jb20iLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU1M2YwXHU0ZTJkXHU1ZTAyXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDEzIiwgInBvcnQiOiA1NTQsICJpZCI6ICIyMGU4YjU4MC0zYzExLTMwMTctYTg0MC1lYjYyNGI0ODMzMjQiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

