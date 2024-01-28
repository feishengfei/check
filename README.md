
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                    | cn             | cc   | isp                                  | ip              | chatgpt          |
|---:|:---------------------|:----------------------------------------|:---------------|:-----|:-------------------------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 18.169.206.216                          | United Kingdom | GB   | AMAZON-02                            | 18.134.130.161  | Yes (Region: GB) |
|  1 | [5](config/5.json)   | 37.252.10.45                            | Poland         | PL   | Artnet Sp. z o.o.                    | 37.252.10.45    | Yes (Region: PL) |
|  2 | [8](config/8.json)   | jseyu.arvancode.eu.Org                  | United Kingdom | GB   | AMAZON-02                            | 18.134.130.161  | Yes (Region: GB) |
|  3 | [11](config/11.json) | fast_2ray_telchannelll.fast2rayy.eu.org | United Kingdom | GB   | AMAZON-02                            | 18.134.130.161  | Yes (Region: GB) |
|  4 | [12](config/12.json) | series-a2-mec.samanehha.co              | United Kingdom | GB   | AMAZON-02                            | 13.40.181.177   | Yes (Region: GB) |
|  5 | [22](config/22.json) | gz.daxun.cyou                           | Taiwan         | TW   | Scloud Pte Ltd                       | 165.154.237.68  | Yes (Region: TW) |
|  6 | [25](config/25.json) | jseyu.arvancode.eu.org                  | United Kingdom | GB   | AMAZON-02                            | 18.134.130.161  | Yes (Region: GB) |
|  7 | [26](config/26.json) | data-us-v1.shwjfkw.cn                   | United States  | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138 | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@18.169.206.216:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%202
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpiemxMclJDUkhkWHA0U1NMMHZvSEJT@37.252.10.45:47580#github.com/freefq%20-%20%E6%B3%A2%E5%85%B0%20%205
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@jseyu.arvancode.eu.Org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%208
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@fast_2ray_telchannelll.fast2rayy.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2011
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1MTdUM0J2cFlhYWl1VzJj@series-a2-mec.samanehha.co:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BF%E5%B7%9E%E8%A5%BF%E9%9B%85%E5%9B%BE%E5%B8%82%E4%BA%9A%E9%A9%AC%E9%80%8A%28Amazon%29%E5%85%AC%E5%8F%B8%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2012
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMjIiLCAiYWRkIjogImd6LmRheHVuLmN5b3UiLCAicG9ydCI6ICIzODAxMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiYWM1ODUyZGYtOGNhZi00ZDg2LThjNzctOTNhNzA5MmY2NmYxIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiZ3ouZGF4dW4uY3lvdSIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@jseyu.arvancode.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2025
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjYiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImlkIjogImIxNDc4ZTI0LTQ5MTYtM2FiZS04ZjE3LTE1OTMxMDEyZWNiZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGF0YS11cy12MS5zaHdqZmt3LmNuIiwgInBhdGgiOiAiL2RlYmlhbiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCb2cwRUxtTU05RFN4RGRR@Fast_2ray_Telchannelll.fast2rayy.eu.org:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2027
```

