# import deepl

from .common import CommonTranslator, MissingAPIKeyException
# from .keys import DEEPL_AUTH_KEY
import json
import time
import requests


class DeeplTranslator(CommonTranslator):
    _LANGUAGE_CODE_MAP = {
        'CHS': 'ZH',
        'CHT': 'ZH',
        'JPN': 'JA',
        'ENG': 'EN-US',
        'CSY': 'CS',
        'NLD': 'NL',
        'FRA': 'FR',
        'DEU': 'DE',
        'HUN': 'HU',
        'ITA': 'IT',
        'PLK': 'PL',
        'PTB': 'PT-BR',
        'ROM': 'RO',
        'RUS': 'RU',
        'ESP': 'ES',
    }

    def __init__(self):
        super().__init__()
        # if not DEEPL_AUTH_KEY:
        #     raise MissingAPIKeyException('Please set the DEEPL_AUTH_KEY environment variable before using the deepl translator.')
        # self.translator = deepl.Translator(DEEPL_AUTH_KEY)

    def tranlate_deepl(self, input):
        time.sleep(1)
        try:
            x = requests.post("https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs",
                              data='{"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","sentences":[{"text":"nnnnn","id":0,"prefix":""}],"raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4}],"lang":{"preference":{"weight":{"DE":0.2061,"EN":0.39919,"ES":0.14976,"FR":0.17529,"IT":0.10836,"JA":0.11357,"NL":0.10912,"PL":0.10286,"PT":0.09812,"RU":5.57217,"ZH":1.25824,"BG":0.29197,"CS":0.07887,"DA":0.07415,"EL":0.07213,"ET":0.06832,"FI":0.08299,"HU":0.07433,"LT":0.0693,"LV":0.06013,"RO":0.07311,"SK":0.93016,"SL":0.07113,"SV":0.08597,"TR":0.07407,"ID":0.07307,"UK":0.35429,"KO":0.07338,"NB":0.08174},"default":"default"},"source_lang_user_selected":"ZH","target_lang":"RU"},"priority":1,"commonJobParams":{"mode":"translate","browserType":1},"timestamp":1679337700677},"id":58800031}' \
                              .replace("nnnnn", input)
                              .encode('utf-8'),
                              headers={
                                  "accept": "*/*",
                                  "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                                  "authority": "www2.deepl.com",
                                  "content-type": "application/json",
                                  "origin": "https://www.deepl.com",
                                  "referer": "https://www.deepl.com/",
                                  "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
                                  "sec-ch-ua-mobile": "?0",
                                  "sec-ch-ua-platform": "\"Windows\"",
                                  "sec-fetch-dest": "empty",
                                  "sec-fetch-mode": "cors",
                                  "sec-fetch-site": "same-site",
                                  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
                              },
                              cookies={
                                  "LMTBID": "v2|cc0dc037-06aa-4f90-af67-d7a3cb56fe50|b4250d714d3ddc99217fec02fce0bace",
                                  "__cf_bm": "LR8XGL3gj1f222C71sTUdFsncx02C02VdFbFPLedFtM-1679337573-0-Aa07+axjEIu3PCUC2y4lncBn2fzzN4qrIrUSOhc0BiS0Zw42NwL4RyyLNh2qVqbrQ1Vl5B6Wp3Fyi9/vYNMeNXw=",
                                  "dapSid": "%7B%22sid%22%3A%2241724b42-f936-415d-9ce8-ce24c8c98a86%22%2C%22lastUpdate%22%3A1679337700%7D",
                                  "dapUid": "75b4be0d-3d44-4dc3-bb2a-f8399880b245",
                                  "dapVn": "2",
                                  "privacySettings": "%7B%22v%22%3A%221%22%2C%22t%22%3A1679184000%2C%22m%22%3A%22LAX%22%2C%22consent%22%3A%5B%22NECESSARY%22%2C%22PERFORMANCE%22%2C%22COMFORT%22%2C%22MARKETING%22%5D%7D",
                                  "releaseGroups": "388.DM-493.2.7_471.DM-547.2.2_604.DM-595.2.2_633.DM-695.2.2_778.DM-705.2.2_866.DM-592.2.2_867.DM-684.2.4_975.DM-609.2.3_1085.TC-432.2.3_1086.TC-104.2.7_1092.SEO-44.2.2_1119.B2B-251.2.3_1219.DAL-136.2.3_1224.DAL-186.2.3_1437.DM-850.2.2_1442.DF-2765.2.3_1460.TC-502.2.1_1330.DF-3073.2.3_865.TG-1004.2.4_1766.DWFA-413.1.2_1767.B2B-364.1.1_1583.DM-807.2.5_1806.B2B-284.1.1_1808.DF-3339.2.1_1810.TC-93.2.1_1585.DM-900.2.3_1812.TC-704.2.1_1207.DWFA-96.2.3_1996.DM-822.1.1_1856.AAEXP-1167.2.1_220.DF-1925.1.9_1328.DWFA-285.2.2_1438.DM-768.2.2_976.DM-667.2.3_475.DM-544.2.2_1863.AAEXP-1174.2.1_774.DWFA-212.2.2_1873.AAEXP-1184.1.1_1246.DM-793.2.2_1444.DWFA-362.2.2_1779.DF-3349.2.2_863.DM-601.2.2_1871.AAEXP-1182.1.1_470.DM-542.2.2_1327.DWFA-391.2.2_1862.AAEXP-1173.1.1_1875.AAEXP-1186.1.1_1870.AAEXP-1181.1.1_1874.AAEXP-1185.1.1_1858.AAEXP-1169.2.1_1867.AAEXP-1178.1.1_1865.AAEXP-1176.2.1_469.DM-541.2.2_605.DM-585.2.3_1084.TG-1207.2.3_1332.DM-709.2.2_1459.DWFA-338.2.2_1775.DF-3044.2.2_1776.B2B-345.2.1_1783.TC-171.2.2_1857.AAEXP-1168.1.1_1868.AAEXP-1179.1.1_1866.AAEXP-1177.1.1_1864.AAEXP-1175.2.1_1861.AAEXP-1172.2.1_1859.AAEXP-1170.2.1_1872.AAEXP-1183.1.1_1869.AAEXP-1180.1.1_1860.AAEXP-1171.2.1",
                                  "userCountry": "RU"
                              },
                              auth=(),
                              )

            return json.loads(x.text)['result']['translations'][0]['beams'][0]['sentences'][0]['text']
        except:
            return input



    async def _translate(self, from_lang, to_lang, queries):
        print("queries " + "\n".join(queries))
        result = []
        for query in queries:
            result.append(self.tranlate_deepl(query))

        print("result " + "\n".join(result))
        return result

        # return self.translator.translate_text('\n'.join(queries), target_lang = to_lang).text.split('\n')
