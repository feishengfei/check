
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn             | cc   | isp               | ip              | chatgpt          |
|---:|:---------------------|:-------------------------|:---------------|:-----|:------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 183.238.202.173          | Hong Kong      | HK   | CNSERVERS         | 156.227.19.218  | Yes (Region: US) |
|  1 | [3](config/3.json)   | tg_mfbpn_d1.52vpn.eu.org | Japan          | JP   | CLOUDFLARENET     | 104.28.211.105  | Yes (Region: JP) |
|  2 | [4](config/4.json)   | 45.199.138.186           | Netherlands    | NL   | YISP B.V.         | 154.84.1.122    | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 156.225.67.104           | Netherlands    | NL   | YISP B.V.         | 154.84.1.44     | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 142.4.110.142            | China          | CN   | PEG-SV            | 142.4.110.137   | Yes (Region: US) |
|  5 | [9](config/9.json)   | 154.85.1.244             | Netherlands    | NL   | YISP B.V.         | 154.84.1.216    | Yes (Region: NL) |
|  6 | [11](config/11.json) | 146.190.96.141           | Singapore      | SG   | DIGITALOCEAN-ASN  | 146.190.96.141  | Yes (Region: SG) |
|  7 | [16](config/16.json) | laravel.com              | United Kingdom | GB   | AS-GLOBALTELEHOST | 172.99.190.223  | Yes (Region: US) |
|  8 | [18](config/18.json) | gzcm01.celerlink.one     | Singapore      | SG   | ORACLE-BMC-31898  | 158.178.226.110 | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMiIsICJhZGQiOiAiMTgzLjIzOC4yMDIuMTczIiwgInBvcnQiOiAiNTE5MDQiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTc5ZmJcdTUyYTggMyIsICJhZGQiOiAidGdfbWZicG5fZDEuNTJ2cG4uZXUub3JnIiwgInBvcnQiOiAiNDkwNDQiLCAiaWQiOiAiMDc5ODFmN2UtZDRjNi0zYmNjLTkzYTctZWMwMjI4MzI1MjM2IiwgImFpZCI6ICIyIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NzM3Njc4Mjg3OSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA2IiwgImFkZCI6ICIxNDIuNC4xMTAuMTQyIiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjY4ZDIzOGNlLTNjYTEtNDZkYy1iODMzLWEwOTE2YzgyOWFkMyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODI1MTY1OC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3Mzc2NzgyODc5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODExNTM2MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTQ2LjE5MC45Ni4xNDEiLCAiYWlkIjogMCwgImhvc3QiOiAibWVkaWEtZXhwMS5saWNkbi5jb20iLCAiaWQiOiAiY2RiY2EyNjYtMTBkOS00MDE4LWU5OWUtYzU2MTQ5N2Q2NTQyIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9pc3VydSIsICJwb3J0IjogNTU1OTksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMTEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAibGFyYXZlbC5jb20iLCAiYWlkIjogMCwgImhvc3QiOiAic3ViLnlpZmVuamljaGFuZy50b3AiLCAiaWQiOiAiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9vY3RhdmkuY2ZkOjQ0My9saW5rdndzIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTYiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozNTI1NTg4ZWUxNGVhOTI0@gzcm01.celerlink.one:41040#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%A7%BB%E5%8A%A8%2018
```

