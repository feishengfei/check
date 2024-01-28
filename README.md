
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                      | cn             | cc   | isp                                  | ip              | chatgpt          |
|---:|:---------------------|:--------------------------|:---------------|:-----|:-------------------------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 18.171.89.31              | United Kingdom | GB   | AMAZON-02                            | 18.132.198.231  | Yes (Region: GB) |
|  1 | [5](config/5.json)   | v1.arvancode.eu.org       | United Kingdom | GB   | AMAZON-02                            | 18.132.198.231  | Yes (Region: GB) |
|  2 | [6](config/6.json)   | series-a2.samanehha.co    | United Kingdom | GB   | AMAZON-02                            | 18.132.198.231  | Yes (Region: GB) |
|  3 | [8](config/8.json)   | series-a2-me.samanehha.co | United Kingdom | GB   | AMAZON-02                            | 18.134.130.161  | Yes (Region: GB) |
|  4 | [11](config/11.json) | cfcdn3.sanfencdn9.com     | Japan          | JP   | Eons Data Communications Limited     | 38.207.152.135  | Yes (Region: US) |
|  5 | [13](config/13.json) | java.ct.arvancode.eu.Org  | United Kingdom | GB   | AMAZON-02                            | 18.132.198.231  | Yes (Region: GB) |
|  6 | [22](config/22.json) | cfcdn2.sanfencdn9.com     | Singapore      | SG   | Akamai Connected Cloud               | 192.53.173.42   | Yes (Region: US) |
|  7 | [23](config/23.json) | data-us-v1.shwjfkw.cn     | United States  | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138 | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcHMzRndtRGpMcldhT1Zn@18.171.89.31:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcHMzRndtRGpMcldhT1Zn@v1.arvancode.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%205
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTptcHMzRndtRGpMcldhT1Zn@series-a2.samanehha.co:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%206
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@series-a2-me.samanehha.co:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%208
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDExIiwgImFkZCI6ICJjZmNkbjMuc2FuZmVuY2RuOS5jb20iLCAicG9ydCI6ICI4MCIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAiIiwgImlkIjogIjVhMWJkNjY2LTQ0MWEtNDQ0Ni05YjRiLTM1MzhmNjIwOWQzMSIsICJzbmkiOiAiIiwgImhvc3QiOiAiYWd6YmpzenVqcDQueW9mbmhrZmMueHl6IiwgInBhdGgiOiAiL3ZpZGVvL2liQ1Q2ejU1In0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpXNzRYRkFMTEx1dzZtNUlB@java.ct.arvancode.eu.Org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2013
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIyIiwgImFkZCI6ICJjZmNkbjIuc2FuZmVuY2RuOS5jb20iLCAicG9ydCI6IDIwNTIsICJpZCI6ICIwNTNkMjY3NS00ODAzLTQ4ZWUtODIzOS02ZTQ5OTg3MWFjNDIiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogIjduQWk3NGpKc2cxLnlvZm5oa2ZjLnh5eiIsICJwYXRoIjogIi92aWRlby9jOWVmeFJDaSIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjMiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImlkIjogImIxNDc4ZTI0LTQ5MTYtM2FiZS04ZjE3LTE1OTMxMDEyZWNiZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGF0YS11cy12MS5zaHdqZmt3LmNuIiwgInBhdGgiOiAiL2RlYmlhbiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIn0=
```

