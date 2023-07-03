
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                             | cn            | cc   | isp           | ip                                    | chatgpt          |
|---:|:---------------------|:---------------------------------|:--------------|:-----|:--------------|:--------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 23.234.198.83                    | United States | US   | MULTA-ASN1    | 2607:f130:109:0:225:90ff:fe79:7d34    | Yes (Region: US) |
|  1 | [4](config/4.json)   | 64.32.4.41                       | United States | US   | SHARKTECH     | 107.167.13.162                        | Yes (Region: US) |
|  2 | [5](config/5.json)   | hk80-2.6d83777c049c.sanfen004.me | Singapore     | SG   | AMAZON-02     | 54.255.147.188                        | Yes (Region: SG) |
|  3 | [8](config/8.json)   | cfcdn.sanfencdn.net              | United States | US   | CNSERVERS     | 23.225.9.234                          | Yes (Region: US) |
|  4 | [10](config/10.json) | 129.146.247.135                  | United States | US   | CLOUDFLARENET | 2a09:bac1:76c0:e18::26a:2f            | Yes (Region: US) |
|  5 | [14](config/14.json) | cdn.yuntujisu.ml                 | United States | US   | PONYNET       | 2605:6400:20:1fa6:c288:57d0:989e:4654 | Yes (Region: US) |
|  6 | [15](config/15.json) | 154.84.1.113                     |               |      |               | 154.84.1.40                           | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImE5YWJmM2U3LTg3ZjQtNDczZC04ZDAzLTJmMjZjYTRiMzU4MyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNDg4OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuNC40MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzE2NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1YjBcdTUyYTBcdTU3NjFcdTRlOWFcdTlhNmNcdTkwMGEoQW1hem9uKVx1NTE2Y1x1NTNmOFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA1IiwgImFkZCI6ICJoazgwLTIuNmQ4Mzc3N2MwNDljLnNhbmZlbjAwNC5tZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjBhNWYzYmZlLWY4YmEtNGYxNy1iMjJmLTYzY2IyMjU1ZGQ3NCIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LmJhaWR1LmNvbSIsICJwYXRoIjogIi96aC1jbi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmY2RuLnNhbmZlbmNkbi5uZXQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiZjExNGU2ZDktMGNkYS00ZmU4LWI3NjktM2JjZWIzYmNhNDUzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1czQuc2FuZmVuY2RuMS5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAidXMxLnNhbmZlbmNkbjEuY29tIn0=
vmess://eyJhZGQiOiAiMTI5LjE0Ni4yNDcuMTM1IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJjMjRiNjE3MC1iYTU0LTRiMmItOTJhNy1jMDQ3NDBiZmM3YmYiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjMyNTYwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAxMCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICJjZG4ueXVudHVqaXN1Lm1sIiwgInBvcnQiOiAiMjA5NSIsICJpZCI6ICJkNTliMjRiMS1iNDc1LTRkNDQtYmU0Ni1hMTg1NjNhODc3MTEiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm5hbm91cy55dGpzMTE0NTE0Lm1sIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTUiLCAiYWRkIjogIjE1NC44NC4xLjExMyIsICJwb3J0IjogIjQ3ODUyIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

