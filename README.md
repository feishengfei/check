
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn              | cc   | isp                                  | ip                             | chatgpt          |
|---:|:---------------------|:-------------------------|:----------------|:-----|:-------------------------------------|:-------------------------------|:-----------------|
|  0 | [2](config/2.json)   | series-a2.samanehha.co   | United Kingdom  | GB   | AMAZON-02                            | 18.132.198.231                 | Yes (Region: GB) |
|  1 | [4](config/4.json)   | 94.182.129.164           | The Netherlands | NL   | Aeza International Ltd               | 2a12:5940:187c::2              | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 158.69.0.27              | Canada          | CA   | OVH SAS                              | 2607:5300:201:3100::40e9       | Yes (Region: CA) |
|  3 | [7](config/7.json)   | v1.arvancode.eu.org      | United Kingdom  | GB   | AMAZON-02                            | 18.132.198.231                 | Yes (Region: GB) |
|  4 | [12](config/12.json) | 104.18.202.250           | United States   | US   | AS-GLOBALTELEHOST                    | 23.157.40.5                    | Yes (Region: DE) |
|  5 | [14](config/14.json) | cfcdn3.sanfencdn9.com    | Japan           | JP   | Eons Data Communications Limited     | 38.207.152.143                 | Yes (Region: US) |
|  6 | [16](config/16.json) | 104.21.73.14             | Canada          | CA   | Akamai Connected Cloud               | 2600:3c04::f03c:94ff:febd:7ea0 | Yes (Region: CA) |
|  7 | [22](config/22.json) | java.ct.arvancode.eu.org | United Kingdom  | GB   | AMAZON-02                            | 18.132.198.231                 | Yes (Region: GB) |
|  8 | [25](config/25.json) | data-us-v1.shwjfkw.cn    | United States   | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138                | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcHMzRndtRGpMcldhT1Zn@series-a2.samanehha.co:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%202
vmess://eyJhZGQiOiAiOTQuMTgyLjEyOS4xNjQiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImNiMjYzNzQ5LWQwMGMtNDkxOS1hNzljLWExNDRhNzFjZWNlYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiMjA2MzYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDQiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpLVmNkY3NKVDZmME9XTDVzRXlNMzhB@158.69.0.27:1080#github.com/freefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%E9%AD%81%E5%8C%97%E5%85%8B%E7%9C%81%E5%8D%9A%E9%98%BF%E5%8A%AA%E7%93%A6OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%206
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcHMzRndtRGpMcldhT1Zn@v1.arvancode.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%207
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICIxMDQuMTguMjAyLjI1MCIsICJwb3J0IjogIjIwODIiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvbmluYS5ib25kL2xpbmt2d3MiLCAiaG9zdCI6ICJlcmZhbm5ld2ZyZWVub2Rlcy52ZG1tc3d5em16aWdvbnZuams0NDMud29ya2Vycy5kZXYiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiY2ZjZG4zLnNhbmZlbmNkbjkuY29tIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTQiLCAicG9ydCI6IDIwNTIsICJpZCI6ICIxZWI1YzJhZi05MjExLTQ2MWQtODQzYi1kZTBkZTVkZTFkODAiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAid3R5d3djcnpqcDUueW9mbmhrZmMueHl6IiwgInBhdGgiOiAiL3ZpZGVvLzlUZlZFeWt1IiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICIxMDQuMjEuNzMuMTQiLCAicG9ydCI6ICI4ODgwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0NWY2M2U5Mi1mNzgyLTRjYWMtODRiOC1lNjFjYjVhNWJmZDAiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FkZW5jMzUuZml4ZWRsZm9hdC50b3AvbGlua3dzIiwgImhvc3QiOiAieWFnaG9vYjU1ZnJlZW5vZGVzLnJlcGFjbzY5NDM3NDAzLndvcmtlcnMuZGV2IiwgInRscyI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpXNzRYRkFMTEx1dzZtNUlB@java.ct.arvancode.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2022
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjUiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
```

