
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn              | cc   | isp       | ip            | chatgpt          |
|---:|:---------------------|:---------------|:----------------|:-----|:----------|:--------------|:-----------------|
|  0 | [3](config/3.json)   | 45.199.138.231 | The Netherlands | NL   | YISP B.V. | 154.84.1.145  | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 142.4.110.10   | China           | CN   | PEG-SV    | 142.4.110.1   | Yes (Region: US) |
|  2 | [6](config/6.json)   | 45.199.138.185 | The Netherlands | NL   | YISP B.V. | 154.84.1.159  | Yes (Region: NL) |
|  3 | [18](config/18.json) | 54.36.174.181  | Poland          | PL   | OVH SAS   | 54.36.174.181 | Yes (Region: FR) |
|  4 | [20](config/20.json) | 45.58.145.200  | The Netherlands | NL   | SHARKTECH | 45.58.145.194 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjIzMSIsICJwb3J0IjogIjQwMDAwIiwgImlkIjogIjZlNzllZWE0LTVmNzItNDY4My1hZDBlLTUzMzlmMDEzNDIxYiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xOTc0MDcxNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyMzkyMjU1MzU1IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA1IiwgImFkZCI6ICIxNDIuNC4xMTAuMTAiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICIwOGZjNDk0My00YzdhLTRhNjktOTI2NS1mYjk2MWVhZWE5MTciLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMjUyMDgwMTAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjIxNTIyMzMyMCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4NSIsICJwb3J0IjogIjMxMDAwIiwgImlkIjogIjA3OGViMjRkLThkMWQtNGZiZC1iOTE0LWVlNThhODk3YTM1ZSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xNTY5NzA2NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyMzAxMDk4NTU3IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@54.36.174.181:7306#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2018
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjAiLCAiYWRkIjogIjQ1LjU4LjE0NS4yMDAiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICI1NTU0NWY5ZS1hNTYxLTQ1NGEtOGRjMC04YmMxMTBlNmIxYzkiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTE2NTIxMDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjMwMTA5ODU1NyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

