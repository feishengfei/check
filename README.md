
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                    | cn             | cc   | isp                                  | ip              | chatgpt          |
|---:|:---------------------|:----------------------------------------|:---------------|:-----|:-------------------------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | jseyu.arvancode.eu.org                  | United Kingdom | GB   | AMAZON-02                            | 18.134.130.161  | Yes (Region: GB) |
|  1 | [7](config/7.json)   | series-a2-me.samanehha.co               | United Kingdom | GB   | AMAZON-02                            | 18.134.130.161  | Yes (Region: GB) |
|  2 | [8](config/8.json)   | 104.18.202.250                          | Canada         | CA   | AS-GLOBALTELEHOST                    | 23.157.40.5     | Yes (Region: US) |
|  3 | [9](config/9.json)   | fast_2ray_telchannelll.fast2rayy.eu.org | United Kingdom | GB   | AMAZON-02                            | 18.134.130.161  | Yes (Region: GB) |
|  4 | [16](config/16.json) | cfcdn2.sanfencdn9.com                   | Singapore      | SG   | Akamai Connected Cloud               | 192.46.228.134  | Yes (Region: US) |
|  5 | [20](config/20.json) | 104.21.73.14                            | France         | FR   | Akamai Connected Cloud               | 172.104.141.20  | Yes (Region: FR) |
|  6 | [32](config/32.json) | data-us-v1.shwjfkw.cn                   | United States  | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138 | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@jseyu.arvancode.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@series-a2-me.samanehha.co:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%207
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjEwNC4xOC4yMDIuMjUwIiwgInBvcnQiOiAiMjA4MiIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9uaW5hLmJvbmQvbGlua3Z3cyIsICJob3N0IjogImVyZmFubmV3ZnJlZW5vZGVzLnZkbW1zd3l6bXppZ29udm5qazQ0My53b3JrZXJzLmRldiIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@fast_2ray_telchannelll.fast2rayy.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%209
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICJjZmNkbjIuc2FuZmVuY2RuOS5jb20iLCAicG9ydCI6IDIwNTIsICJpZCI6ICI2NTcxNDBlNC1mYjUzLTQ0MDQtODBiNy1mY2JhYzY1MjY3MWYiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInl2aG5iZXZ4aGsxLnlvZm5oa2ZjLnh5eiIsICJwYXRoIjogIi92aWRlby8zNGtLWGJMTSIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIwIiwgImFkZCI6ICIxMDQuMjEuNzMuMTQiLCAicG9ydCI6ICI4ODgwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0NWY2M2U5Mi1mNzgyLTRjYWMtODRiOC1lNjFjYjVhNWJmZDAiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FkZW5jMzUuZml4ZWRsZm9hdC50b3AvbGlua3dzIiwgImhvc3QiOiAieWFnaG9vYjU1ZnJlZW5vZGVzLnJlcGFjbzY5NDM3NDAzLndvcmtlcnMuZGV2IiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMzIiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
```

