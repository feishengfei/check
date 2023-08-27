
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                 | cn             | cc   | isp                               | ip                                  | chatgpt          |
|---:|:---------------------|:-------------------------------------|:---------------|:-----|:----------------------------------|:------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.178                       | Netherlands    | NL   | YISP B.V.                         | 2a02:2a38:1:2796:7b3e:ad16:6b3:c6b5 | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 120.226.50.91                        | United Kingdom | GB   | OVH SAS                           | 51.89.40.141                        | Yes (Region: GB) |
|  2 | [5](config/5.json)   | gamespeed-gateway-1.numastergame.com | Taiwan         | TW   | Data Communication Business Group | 61.219.15.82                        | Yes (Region: TW) |
|  3 | [8](config/8.json)   | stock.hostmonit.com                  | Poland         | PL   | OVH SAS                           | 54.36.174.181                       | Yes (Region: FR) |
|  4 | [19](config/19.json) | 156.245.8.144                        | Netherlands    | NL   | YISP B.V.                         | 154.84.1.134                        | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3OCIsICJwb3J0IjogIjM3OTUyIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZlNTZcdTUzNTdcdTc3MDFcdTc5ZmJcdTUyYTggNCIsICJhZGQiOiAiMTIwLjIyNi41MC45MSIsICJwb3J0IjogIjQ3MDA5IiwgImlkIjogIjgzYTQyNGQ4LTRiY2ItNGNlZS1iMDE2LTJjOGYxZGI0YTkyMSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwOTEzYjFhYy0xZjZjLTQzNmItOTliNC1hNWQ2ZTM0M2QwMjUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTE4NzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAic3RvY2suaG9zdG1vbml0LmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJ1czIuaWN1MnJpcC5ldS5vcmciLCAiaWQiOiAiY2Q3ZjZhODktZTg2YS00N2FlLTg3ZDMtMDI3N2QyMDUyODZmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9uaXNoaWthdGEiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0NCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjMyMTU5ODc3Lnh5eiIsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTQyNzMxMjYzMDE0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZiAgMTkiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

