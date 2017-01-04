# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_formats = ("{{city_name}}", )

    building_number_formats = ("%號", "%#號", "%##號", )
    postcode_formats = ("%####", "%##", )

    street_name_formats = ("{{street_name}}", )
    street_address_formats = ("{{street_name}}{{building_number}}", )

    address_formats = ("{{postcode}} {{city}}{{street_address}}", )
    secondary_address_formats = ('#樓', '之#')

    street_names = ("中正路", "中山路", "民生路", "中華路", "和平路",
                    "中興路", "仁愛路", "復興路", "民族路", "民權路",
                    "忠孝路", "信義路", "成功路", "新興路", "忠孝街",
                    "和平街", "信義街", "仁愛街", "文化路", "大同路",
                    "三民路", "新生路", "光復路", "自強路", "光明路",
                    "公園路", "民生街", "文化街", "中興街", "建國路",
                    "民權街", "自強街", "中山路１段", "中山路２段", "光明街",
                    "成功街", "永安街", "四維路", "新興街", "民族街",
                    "福德街", "大同街", "文昌街", "復興街", "博愛街",
                    "博愛路", "光華街", "太平路", "水源路", "新生街",
                    "四維街", "大仁街", "中央路", "大智街", "林森路",
                    "八德路", "長春路", "南街", "福德路", "光華路",
                    "八德街", "中山路３段", "東興路", "勝利街", "文昌路",
                    "三民街", "大勇街", "民有街", "自由路", "長安街",
                    "明德路", "明德街", "光復街", "德街", "忠義路",
                    "中和路", "自由街", "中正路１段", "永和街", "延平路",
                    "正義路", "五福街", "華興街", "育英路", "平和路",
                    "福安街", "中正路２段", "勝利路", "育英街", "興街",
                    "自立街", "民享街", "大智路", "民治街", "民治路",
                    "學府路", "中華街", "忠義街", "和街", "民富街",)

    cities = ("基隆市", "台北市", "新北市", "桃園縣", "新竹市",
              "新竹縣", "苗栗縣", "台中市", "彰化縣", "南投縣",
              "雲林縣", "嘉義市", "嘉義縣", "台南市", "高雄市",
              "屏東縣", "台東縣", "花蓮縣", "宜蘭縣", "澎湖縣",
              "金門縣", "連江縣")

    # from
    countries = ("阿爾巴尼亞", "剛果共和國", "阿爾及利亞", "丹麥",
                 "安哥拉", "多明尼加", "安圭拉", "多米尼克",
                 "阿根廷", "厄瓜多爾", "亞美尼亞", "埃及",
                 "阿路巴", "薩爾瓦多", "澳大利亞", "厄利垂亞",
                 "奧地利", "愛沙尼亞", "亞塞拜然", "衣索匹亞",
                 "巴哈馬", "斐濟", "巴林", "芬蘭", "孟加拉", "法屬玻里尼西亞",
                 "法國", "巴貝多", "加彭", "白俄羅斯", "喬治亞",
                 "比利時", "德國", "貝里斯", "迦納", "貝南", "直布羅陀",
                 "百慕達", "英國", "不丹", "希臘", "玻利維亞", "格瑞那達",
                 "波希尼亞及赫塞哥維那", "瓜地馬拉", "波札那", "幾內亞",
                 "巴西", "蓋亞那", "汶萊", "海地", "保加利亞", "宏都拉斯",
                 "布吉納法索", "香港", "蒲隆地", "匈牙利", "柬埔寨", "冰島",
                 "喀麥隆", "印度", "加拿大", "印尼", "維德角島", "依朗",
                 "開曼群島", "伊拉克", "中非共和國", "愛爾蘭", "查德", "以色列",
                 "智利", "義大利", "中國大陸", "牙買加", "哥倫比亞", "日本",
                 "剛果", "約旦", "科克群島", "肯亞", "哥斯大黎加", "韓國",
                 "象牙海岸", "科威特", "克羅埃西亞", "寮國", "塞浦路斯", "拉脫維亞",
                 "捷克", "賴索托", "盧森堡", "聖露西亞", "澳門", "聖文森及格瑞那丁",
                 "馬其頓", "聖多美及普林西比", "馬達加斯加", "沙烏地阿拉伯",
                 "馬拉威", "塞內加爾", "馬來西亞", "塞席爾", "馬爾地夫", "獅子山",
                 "馬利", "新加坡", "馬爾他", "斯洛伐克", "模里西斯", "斯洛維尼亞",
                 "茅利塔尼亞", "索羅門群島", "墨西哥", "索馬利亞",
                 "摩爾多瓦", "南非", "蒙古", "西班牙", "摩洛哥", "斯里蘭卡",
                 "緬甸", "蘇丹", "納米比亞", "蘇利南", "諾魯", "史瓦濟蘭",
                 "尼泊爾", "瑞典", "荷蘭", "瑞士", "新喀里多尼亞", "敘利亞",
                 "紐西蘭", "坦尚尼亞", "尼日", "泰國", "奈及利亞", "多哥",
                 "挪威", "千里達及托貝哥", "阿曼", "突尼西亞", "巴基斯坦", "土耳其",
                 "巴拿馬", "烏干達", "巴布亞紐幾內亞", "烏克蘭",
                 "巴拉圭", "阿拉伯聯合大公國", "秘魯", "美國", "菲律賓", "烏拉圭",
                 "波蘭", "委內瑞拉", "葡萄牙", "越南", "卡達", "西薩摩亞",
                 "羅馬尼亞", "葉門", "俄羅斯", "尚比亞", "盧安達", "辛巴威",
                 "聖克里斯多福及尼維斯")

    @classmethod
    def secondary_address(cls):
        return cls.numerify(cls.random_element(cls.secondary_address_formats))

    @classmethod
    def building_number(cls):
        return cls.numerify(cls.random_element(cls.building_number_formats))

    @classmethod
    def street_name(cls):
        return cls.random_element(cls.street_names)

    @classmethod
    def city_name(cls):
        return cls.random_element(cls.cities)
