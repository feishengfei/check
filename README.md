
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                          | cn            | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:------------------------------|:--------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 67.21.77.73                   | United States | US   | SHARKTECH         | 107.167.18.42  | Yes (Region: US) |
|  1 | [8](config/8.json)   | 46.17.43.192                  | Germany       | DE   | AS-GLOBALTELEHOST | 193.108.118.34 | Yes (Region: DE) |
|  2 | [25](config/25.json) | goodbyefilteringchannel.space |               |      |                   | 104.28.222.46  | Yes (Region: SG) |
|  3 | [30](config/30.json) | goodbyefilteringchannel.space |               |      |                   | 104.28.222.47  | Yes (Region: SG) |
|  4 | [31](config/31.json) | goodbyefilteringchannel.space |               |      |                   | 104.28.254.47  | Yes (Region: SG) |
|  5 | [34](config/34.json) | 8.v2-ray.cyou                 | Japan         | JP   | AMAZON-02         | 18.179.36.139  | Yes (Region: JP) |
|  6 | [36](config/36.json) | 104.25.243.70                 | Canada        | CA   |                   | 45.61.128.240  | Yes (Region: CA) |

## Valid
```
vmess://eyJhZGQiOiAiNjcuMjEuNzcuNzMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmYWJiMzBlOC0zYTJjLTQxNDktOTY1MS0yNzU4Zjc3MTI0ODEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDcxNDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@46.17.43.192:12345#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%E9%9E%91%E9%9D%BC%E6%96%AF%E5%9D%A6%E5%96%80%E5%B1%B1justhost%208
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI1IiwgImFkZCI6ICJnb29kYnllZmlsdGVyaW5nY2hhbm5lbC5zcGFjZSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNDI1OGVmZTYtZTU0Mi00NjhhLWZjNGYtOGNkMWZkN2JiM2JjIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJnb29kYnllZmlsdGVyaW5nY2hhbm5lbC5zcGFjZSIsICJwYXRoIjogIi9wb3J0cy8xOTc0NSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDMwIiwgImFkZCI6ICJnb29kYnllZmlsdGVyaW5nY2hhbm5lbC5zcGFjZSIsICJwb3J0IjogNDQzLCAiaWQiOiAiMGYyYjk4YTYtZWNjZi00NmE1LWY0N2UtZDNjNGY5Yzk1OTk5IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJnb29kYnllZmlsdGVyaW5nY2hhbm5lbC5zcGFjZSIsICJwYXRoIjogIi9wb3J0cy8yMDkyNiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDMxIiwgImFkZCI6ICJnb29kYnllZmlsdGVyaW5nY2hhbm5lbC5zcGFjZSIsICJwb3J0IjogNDQzLCAiaWQiOiAiOGM3ZjM1YmMtZGI1NC00NTg1LWE2YTMtMjM1NmUxY2NmZjU3IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJnb29kYnllZmlsdGVyaW5nY2hhbm5lbC5zcGFjZSIsICJwYXRoIjogIi9wb3J0cy81NjQxNiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMzQiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDM2IiwgImFkZCI6ICIxMDQuMjUuMjQzLjcwIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiNjg4NGQ3MjgtN2ZiMC00MTcyLWMzMTktZThjYWVhZGNkMDFmIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1cy5oZXJvZnJlZTY2LnRrIiwgInBhdGgiOiAiL3RnQGhlcmhlcm82IiwgInRscyI6ICIiLCAic25pIjogIiJ9
```

