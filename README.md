
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                    | cn              | cc   | isp                              | ip             | chatgpt          |
|---:|:---------------------|:----------------------------------------|:----------------|:-----|:---------------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 77.246.106.242                          | The Netherlands | NL   | Servers Tech Fzco                | 77.246.106.242 | Yes (Region: NL) |
|  1 | [4](config/4.json)   | java.ct.arvancode.eu.Org                | United Kingdom  | GB   | AMAZON-02                        | 18.132.198.231 | Yes (Region: GB) |
|  2 | [5](config/5.json)   | series-a2.samanehha.co                  | United Kingdom  | GB   | AMAZON-02                        | 18.132.198.231 | Yes (Region: GB) |
|  3 | [6](config/6.json)   | jseyu.arvancode.eu.org                  | United Kingdom  | GB   | AMAZON-02                        | 18.134.130.161 | Yes (Region: GB) |
|  4 | [8](config/8.json)   | fast_2ray_telchannelll.fast2rayy.eu.org | United Kingdom  | GB   | AMAZON-02                        | 18.134.130.161 | Yes (Region: GB) |
|  5 | [10](config/10.json) | series-a1.samanehha.co                  | United Kingdom  | GB   | AMAZON-02                        | 18.132.198.231 | Yes (Region: GB) |
|  6 | [12](config/12.json) | v1.arvancode.eu.org                     | United Kingdom  | GB   | AMAZON-02                        | 18.132.198.231 | Yes (Region: GB) |
|  7 | [13](config/13.json) | 104.18.202.250                          | France          | FR   | AS-GLOBALTELEHOST                | 149.7.16.197   | Yes (Region: CA) |
|  8 | [17](config/17.json) | cfcdn3.sanfencdn9.com                   | Japan           | JP   | Eons Data Communications Limited | 38.207.152.144 | Yes (Region: US) |
|  9 | [26](config/26.json) | 104.21.73.14                            | France          | FR   | Akamai Connected Cloud           | 172.232.33.23  | Yes (Region: CA) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCNUpvUHJpdFVsQ2J1Rm9QempwSHVS@77.246.106.242:10220#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpXNzRYRkFMTEx1dzZtNUlB@java.ct.arvancode.eu.Org:443#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Amazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%204
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcHMzRndtRGpMcldhT1Zn@series-a2.samanehha.co:443#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Amazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%205
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@jseyu.arvancode.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%206
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@fast_2ray_telchannelll.fast2rayy.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%208
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpXNzRYRkFMTEx1dzZtNUlB@series-a1.samanehha.co:443#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Amazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2010
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcHMzRndtRGpMcldhT1Zn@v1.arvancode.eu.org:443#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Amazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2012
vmess://eyJhZGQiOiAiMTA0LjE4LjIwMi4yNTAiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiZXJmYW5uZXdmcmVlbm9kZXMudmRtbXN3eXptemlnb252bmprNDQzLndvcmtlcnMuZGV2IiwgImlkIjogIjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvbmluYS5ib25kL2xpbmt2d3MiLCAicG9ydCI6ICIyMDgyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiY2ZjZG4zLnNhbmZlbmNkbjkuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImt2anFxa256anA2LnlvZm5oa2ZjLnh5eiIsICJpZCI6ICI1OGVjYjY2Zi04YjU1LTRiMmEtOTdjOS03Yjg3ZTE4OWQyZjciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3ZpZGVvL1pvOThQWWZFIiwgInBvcnQiOiAiMjA1MiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTciLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI2IiwgImFkZCI6ICIxMDQuMjEuNzMuMTQiLCAicG9ydCI6ICI4ODgwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0NWY2M2U5Mi1mNzgyLTRjYWMtODRiOC1lNjFjYjVhNWJmZDAiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FkZW5jMzUuZml4ZWRsZm9hdC50b3AvbGlua3dzIiwgImhvc3QiOiAieWFnaG9vYjU1ZnJlZW5vZGVzLnJlcGFjbzY5NDM3NDAzLndvcmtlcnMuZGV2IiwgInRscyI6ICIifQ==
```

