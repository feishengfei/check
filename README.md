
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                             | cn            | cc   | isp                               | ip              | chatgpt          |
|---:|:---------------------|:---------------------------------|:--------------|:-----|:----------------------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | hk80-2.6d83777c049b.sanfen004.me | Hong Kong     | HK   | AMAZON-02                         | 18.163.108.252  | Yes (Region: US) |
|  1 | [4](config/4.json)   | 194.15.196.106                   | Poland        | PL   | Artnet Sp. z o.o.                 | 194.15.196.106  | Yes (Region: PL) |
|  2 | [8](config/8.json)   | 23.227.60.146                    | United States | US   | Eons Data Communications Limited  | 65.75.220.16    | Yes (Region: US) |
|  3 | [9](config/9.json)   | 172.99.188.99                    | Netherlands   | NL   | AS-GLOBALTELEHOST                 | 172.99.188.99   | Yes (Region: NL) |
|  4 | [11](config/11.json) | 156.225.67.136                   | Netherlands   | NL   | YISP B.V.                         | 154.84.1.137    | Yes (Region: NL) |
|  5 | [17](config/17.json) | tw99-hinet.mynodes001.one        | Taiwan        | TW   | Data Communication Business Group | 122.118.124.141 | Yes (Region: TW) |
|  6 | [22](config/22.json) | new8.huvicloud.com               | United States | US   | PONYNET                           | 205.185.127.57  | Yes (Region: US) |
|  7 | [23](config/23.json) | cfcdn.sanfencdn.net              | United States | US   | Eons Data Communications Limited  | 65.75.220.16    | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiaGs4MC0yLjZkODM3NzdjMDQ5Yi5zYW5mZW4wMDQubWUiLCAiYWlkIjogMCwgImhvc3QiOiAid3d3LmJhaWR1LmNvbSIsICJpZCI6ICI3MjYyY2Y0NC1hNTg3LTQwMWEtOWNkMy1hODdlMmNlOGYwNGUiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3poLWNuLyIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZkFtYXpvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@194.15.196.106:8090#github.com/freefq%20-%20%E5%BE%B7%E5%9B%BD%20%204
vmess://eyJhZGQiOiAiMjMuMjI3LjYwLjE0NiIsICJhaWQiOiAwLCAiaG9zdCI6ICJLYW5zYXMua290aWNrLnNpdGUiLCAiaWQiOiAiNzZFNjY3OTktMTc2My00RUU5LUFCRDYtNTUyM0VFMEU0MTZEIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9zcGVlZHRlc3QiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MmEwXHU2MmZmXHU1OTI3ICA4IiwgInNjeSI6ICJhdXRvIiwgInRscyI6ICJ0bHMiLCAidiI6ICIyIn0=
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@172.99.188.99:4444#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%209
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3LjEzNiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI5NjRiZjQ5OS05ZWMwLTQzNzgtOTJiNi04N2Q4ZDg2MWIyZDAiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuODE2NzgwMzQueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4NDc1MDk2MTE3MyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICJ3d3cuODE2NzgwMzQueHl6In0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTgyZDdcdTY4MTdcdTUzYmZcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMTciLCAiYWRkIjogInR3OTktaGluZXQubXlub2RlczAwMS5vbmUiLCAicG9ydCI6ICI1NDMyIiwgImlkIjogImQ1ZWYxZGYzLTQwNjktM2IyNS05ZGMxLTE2YjJiZTliM2U2YiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAibmV3OC5odXZpY2xvdWQuY29tIiwgImFpZCI6IDAsICJob3N0IjogIm5ldzguaHV2aWNsb3VkLmNvbSIsICJpZCI6ICJhMTFjYTc2MC05ZWY5LTRhNjMtOTVjOS00YzVjMzJkNTYyNTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIyIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2ZjZG4uc2FuZmVuY2RuLm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICJ1czIuc2FuZmVuY2RuLm5ldCIsICJpZCI6ICJkZDgzMTRjYy0zNzU0LTQxNmQtOTQ1Ni0wOTkxZjJlNzQ3NTMiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3poLWNuIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMjMiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

