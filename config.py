# config.py
# 全球智库及认知网站配置文件
# 可随时添加、修改或删除信息源
# 建议：如果官方 rsshub.app 无法连接，请更换为以下公共镜像：
# https://rss.lilywhite.cc
# https://rsshub.pseudo.moe
# https://rss.cloudnative.love
RSSHUB_PROXY = "https://rsshub.app"

THINK_TANKS_CONFIG = [
# ==================== 中国智库 (通过代理/聚合) ====================
    {
        "name": "CASS",
        "name_cn": "中国社会科学院",
        "rss": f"{RSSHUB_PROXY}/cass/news",
        "icon": "http://www.cass.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国哲学社会科学研究最高殿堂"
    },
    {
        "name": "AiSiXiang ThinkTank",
        "name_cn": "爱思想-智库专栏",
        "rss": f"{RSSHUB_PROXY}/aisixiang/thinktank/all",
        "icon": "http://www.aisixiang.com/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "深度思想门户，聚合国内顶级学者文章"
    },
    {
        "name": "SIIS",
        "name_cn": "上海国际问题研究院",
        "rss": f"{RSSHUB_PROXY}/siis/news",
        "icon": "http://www.siis.org.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国重要外交与地缘政治研究机构"
    },
    {
        "name": "IISS-PKU",
        "name_cn": "北大国际战略研究院",
        "rss": f"{RSSHUB_PROXY}/pku/iiss",
        "icon": "https://www.pku.edu.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "北京大学顶尖战略研究机构"
    },
    # ==================== 北美地区 ====================
    # 美国顶级智库
    {
        "name": "Brookings Institution",
        "name_cn": "布鲁金斯学会",
        "rss": "https://www.brookings.edu/feed/",
        "icon": "https://www.brookings.edu/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "美国最具影响力的智库之一"
    },
    {
        "name": "Carnegie Endowment for International Peace",
        "name_cn": "卡内基国际和平基金会",
        "rss": "https://carnegieendowment.org/rss/all",
        "icon": "https://carnegieendowment.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "国际事务研究顶级智库"
    },
    {
        "name": "Council on Foreign Relations",
        "name_cn": "外交关系委员会",
        "rss": "https://www.cfr.org/rss/feed/fellows/all",
        "icon": "https://www.cfr.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "美国外交政策权威机构"
    },
    {
        "name": "RAND Corporation",
        "name_cn": "兰德公司",
        "rss": "https://www.rand.org/pubs/rss.xml",
        "icon": "https://www.rand.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "全球知名政策研究机构"
    },
    {
        "name": "Peterson Institute for International Economics",
        "name_cn": "彼得森国际经济研究所",
        "rss": "https://www.piie.com/rss.xml",
        "icon": "https://www.piie.com/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "国际经济政策权威"
    },
    {
        "name": "Center for Strategic and International Studies",
        "name_cn": "战略与国际研究中心",
        "rss": "https://www.csis.org/rss.xml",
        "icon": "https://www.csis.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "国家安全与战略研究"
    },
    {
        "name": "Heritage Foundation",
        "name_cn": "传统基金会",
        "rss": "https://www.heritage.org/rss/",
        "icon": "https://www.heritage.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "保守派政策研究"
    },
    {
        "name": "American Enterprise Institute",
        "name_cn": "美国企业研究所",
        "rss": "https://www.aei.org/feed/",
        "icon": "https://www.aei.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "公共政策研究"
    },
    {
        "name": "Atlantic Council",
        "name_cn": "大西洋理事会",
        "rss": "https://www.atlanticcouncil.org/feed/",
        "icon": "https://www.atlanticcouncil.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "跨大西洋关系研究"
    },
    {
        "name": "Wilson Center",
        "name_cn": "威尔逊国际学者中心",
        "rss": "https://www.wilsoncenter.org/rss.xml",
        "icon": "https://www.wilsoncenter.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "国际问题研究"
    },
    {
        "name": "Urban Institute",
        "name_cn": "城市研究所",
        "rss": "https://www.urban.org/rss.xml",
        "icon": "https://www.urban.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "社会经济政策研究"
    },
    {
        "name": "Cato Institute",
        "name_cn": "卡托研究所",
        "rss": "https://www.cato.org/rss.xml",
        "icon": "https://www.cato.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "自由意志主义智库"
    },
    {
        "name": "Center for American Progress",
        "name_cn": "美国进步中心",
        "rss": "https://www.americanprogress.org/feed/",
        "icon": "https://www.americanprogress.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "进步派政策研究"
    },
    {
        "name": "Hoover Institution",
        "name_cn": "胡佛研究所",
        "rss": "https://www.hoover.org/rss.xml",
        "icon": "https://www.hoover.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "斯坦福大学附属智库"
    },

    # 加拿大智库
    {
        "name": "Centre for International Governance Innovation",
        "name_cn": "国际治理创新中心",
        "rss": "https://www.cigionline.org/rss.xml",
        "icon": "https://www.cigionline.org/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 2,
        "description": "国际治理研究"
    },
    {
        "name": "Canadian Global Affairs Institute",
        "name_cn": "加拿大全球事务研究所",
        "rss": "https://www.cgai.ca/rss.xml",
        "icon": "https://www.cgai.ca/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 2,
        "description": "加拿大外交政策"
    },

    # ==================== 欧洲地区 ====================
    # 英国智库
    {
        "name": "Chatham House",
        "name_cn": "查塔姆研究所",
        "rss": "https://www.chathamhouse.org/rss.xml",
        "icon": "https://www.chathamhouse.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 1,
        "description": "英国皇家国际事务研究所"
    },
    {
        "name": "International Institute for Strategic Studies",
        "name_cn": "国际战略研究所",
        "rss": "https://www.iiss.org/rss.xml",
        "icon": "https://www.iiss.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 1,
        "description": "军事与战略研究"
    },
    {
        "name": "Overseas Development Institute",
        "name_cn": "海外发展研究所",
        "rss": "https://odi.org/en/feed/",
        "icon": "https://odi.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "国际发展研究"
    },
    {
        "name": "Policy Exchange",
        "name_cn": "政策交流",
        "rss": "https://policyexchange.org.uk/feed/",
        "icon": "https://policyexchange.org.uk/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "英国政策研究"
    },
    {
        "name": "Institute for Government",
        "name_cn": "政府研究所",
        "rss": "https://www.instituteforgovernment.org.uk/rss.xml",
        "icon": "https://www.instituteforgovernment.org.uk/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "政府治理研究"
    },

    # 德国智库
    {
        "name": "German Council on Foreign Relations",
        "name_cn": "德国外交关系委员会",
        "rss": "https://dgap.org/en/feed",
        "icon": "https://dgap.org/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "德国外交政策研究"
    },
    {
        "name": "Kiel Institute for the World Economy",
        "name_cn": "基尔世界经济研究所",
        "rss": "https://www.ifw-kiel.de/rss.xml",
        "icon": "https://www.ifw-kiel.de/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "国际经济研究"
    },
    {
        "name": "Stiftung Wissenschaft und Politik",
        "name_cn": "德国国际与安全事务研究所",
        "rss": "https://www.swp-berlin.org/rss.xml",
        "icon": "https://www.swp-berlin.org/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "德国顶级安全政策智库"
    },

    # 法国智库
    {
        "name": "French Institute of International Relations",
        "name_cn": "法国国际关系研究所",
        "rss": "https://www.ifri.org/en/rss",
        "icon": "https://www.ifri.org/favicon.ico",
        "category": "法国智库",
        "country": "法国",
        "priority": 2,
        "description": "法国顶级国际关系智库"
    },

    # 意大利智库
    {
        "name": "Istituto Affari Internazionali",
        "name_cn": "国际事务研究院",
        "rss": "https://www.iai.it/en/rss.xml",
        "icon": "https://www.iai.it/favicon.ico",
        "category": "意大利智库",
        "country": "意大利",
        "priority": 2,
        "description": "意大利国际事务研究"
    },

    # 瑞典智库
    {
        "name": "Stockholm International Peace Research Institute",
        "name_cn": "斯德哥尔摩国际和平研究所",
        "rss": "https://www.sipri.org/rss.xml",
        "icon": "https://www.sipri.org/favicon.ico",
        "category": "瑞典智库",
        "country": "瑞典",
        "priority": 1,
        "description": "全球和平与安全研究权威"
    },

    # 比利时智库（欧盟）
    {
        "name": "Bruegel",
        "name_cn": "布鲁盖尔研究所",
        "rss": "https://www.bruegel.org/rss.xml",
        "icon": "https://www.bruegel.org/favicon.ico",
        "category": "欧盟智库",
        "country": "比利时",
        "priority": 1,
        "description": "欧洲经济政策研究"
    },
    {
        "name": "Centre for European Policy Studies",
        "name_cn": "欧洲政策研究中心",
        "rss": "https://www.ceps.eu/feed/",
        "icon": "https://www.ceps.eu/favicon.ico",
        "category": "欧盟智库",
        "country": "比利时",
        "priority": 2,
        "description": "欧盟政策研究"
    },
    {
        "name": "European Council on Foreign Relations",
        "name_cn": "欧洲对外关系委员会",
        "rss": "https://ecfr.eu/feed/",
        "icon": "https://ecfr.eu/favicon.ico",
        "category": "欧盟智库",
        "country": "比利时",
        "priority": 2,
        "description": "欧洲外交政策研究"
    },

    # ==================== 亚洲地区 ====================
    # 中国智库
    {
        "name": "Chinese Academy of Social Sciences",
        "name_cn": "中国社会科学院",
        "rss": "http://www.cssn.cn/rss/rss.xml",
        "icon": "http://www.cssn.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国最高哲学社会科学研究机构"
    },
    {
        "name": "China Institutes of Contemporary International Relations",
        "name_cn": "中国现代国际关系研究院",
        "rss": "https://www.cicir.ac.cn/rss.xml",
        "icon": "https://www.cicir.ac.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国顶级国际关系研究机构"
    },
    {
        "name": "Shanghai Institutes for International Studies",
        "name_cn": "上海国际问题研究院",
        "rss": "http://www.siis.org.cn/rss.xml",
        "icon": "http://www.siis.org.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国重要国际问题研究智库"
    },
    {
        "name": "China Center for International Economic Exchanges",
        "name_cn": "中国国际经济交流中心",
        "rss": "http://www.cciee.org.cn/rss.xml",
        "icon": "http://www.cciee.org.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "国际经济政策研究"
    },
    {
        "name": "Development Research Center of the State Council",
        "name_cn": "国务院发展研究中心",
        "rss": "http://www.drc.gov.cn/rss.xml",
        "icon": "http://www.drc.gov.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国政府核心智库"
    },
    {
        "name": "Peking University Institute of International Relations",
        "name_cn": "北京大学国际关系学院",
        "rss": "https://www.sis.pku.edu.cn/rss.xml",
        "icon": "https://www.pku.edu.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "北大国际关系研究"
    },
    {
        "name": "Tsinghua University Center for International Security",
        "name_cn": "清华大学国际安全研究中心",
        "rss": "http://www.tu.edu.cn/rss.xml",
        "icon": "http://www.tsinghua.edu.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "国际安全与战略研究"
    },
    {
        "name": "Fudan University Institute of International Studies",
        "name_cn": "复旦大学国际问题研究院",
        "rss": "http://www.iis.fudan.edu.cn/rss.xml",
        "icon": "http://www.fudan.edu.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "国际问题综合研究"
    },
    {
        "name": "Chongyang Institute for Financial Studies",
        "name_cn": "中国人民大学重阳金融研究院",
        "rss": "http://rdcy.ruc.edu.cn/rss.xml",
        "icon": "http://www.ruc.edu.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "金融与宏观经济研究"
    },

    # 日本智库
    {
        "name": "Japan Institute of International Affairs",
        "name_cn": "日本国际问题研究所",
        "rss": "https://www.jiia.or.jp/en/rss.xml",
        "icon": "https://www.jiia.or.jp/favicon.ico",
        "category": "日本智库",
        "country": "日本",
        "priority": 2,
        "description": "日本顶级国际关系智库"
    },
    {
        "name": "Asia Pacific Initiative",
        "name_cn": "亚太倡议",
        "rss": "https://apinitiative.org/en/feed/",
        "icon": "https://apinitiative.org/favicon.ico",
        "category": "日本智库",
        "country": "日本",
        "priority": 2,
        "description": "亚太地区政策研究"
    },

    # 韩国智库
    {
        "name": "Asan Institute for Policy Studies",
        "name_cn": "峨山政策研究院",
        "rss": "https://en.asaninst.org/feed/",
        "icon": "https://en.asaninst.org/favicon.ico",
        "category": "韩国智库",
        "country": "韩国",
        "priority": 2,
        "description": "韩国顶级政策研究机构"
    },
    {
        "name": "Korea Institute for International Economic Policy",
        "name_cn": "韩国对外经济政策研究院",
        "rss": "https://www.kiep.go.kr/rss.xml",
        "icon": "https://www.kiep.go.kr/favicon.ico",
        "category": "韩国智库",
        "country": "韩国",
        "priority": 2,
        "description": "国际经济政策研究"
    },

    # 印度智库
    {
        "name": "Observer Research Foundation",
        "name_cn": "观察家研究基金会",
        "rss": "https://www.orfonline.org/rss.xml",
        "icon": "https://www.orfonline.org/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 2,
        "description": "印度顶级智库"
    },
    {
        "name": "Gateway House",
        "name_cn": "门楼印度委员会",
        "rss": "https://www.gatewayhouse.in/feed/",
        "icon": "https://www.gatewayhouse.in/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 2,
        "description": "印度外交与经济政策"
    },
    {
        "name": "Centre for Policy Research",
        "name_cn": "政策研究中心",
        "rss": "https://cprindia.org/feed/",
        "icon": "https://cprindia.org/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 2,
        "description": "印度公共政策研究"
    },

    # 新加坡智库
    {
        "name": "ISEAS-Yusof Ishak Institute",
        "name_cn": "尤索夫伊萨东南亚研究院",
        "rss": "https://www.iseas.edu.sg/feed/",
        "icon": "https://www.iseas.edu.sg/favicon.ico",
        "category": "新加坡智库",
        "country": "新加坡",
        "priority": 2,
        "description": "东南亚研究权威"
    },
    {
        "name": "S. Rajaratnam School of International Studies",
        "name_cn": "拉惹勒南国际研究院",
        "rss": "https://www.rsis.edu.sg/feed/",
        "icon": "https://www.rsis.edu.sg/favicon.ico",
        "category": "新加坡智库",
        "country": "新加坡",
        "priority": 2,
        "description": "安全与战略研究"
    },

    # ==================== 中东地区 ====================
    # 以色列智库
    {
        "name": "Institute for National Security Studies",
        "name_cn": "国家安全研究所",
        "rss": "https://www.inss.org.il/feed/",
        "icon": "https://www.inss.org.il/favicon.ico",
        "category": "以色列智库",
        "country": "以色列",
        "priority": 2,
        "description": "以色列安全研究"
    },
    {
        "name": "Begin-Sadat Center for Strategic Studies",
        "name_cn": "贝京-萨达特战略研究中心",
        "rss": "https://besacenter.org/feed/",
        "icon": "https://besacenter.org/favicon.ico",
        "category": "以色列智库",
        "country": "以色列",
        "priority": 2,
        "description": "中东战略研究"
    },

    # 沙特智库
    {
        "name": "King Faisal Center for Research and Islamic Studies",
        "name_cn": "费萨尔国王研究中心",
        "rss": "https://kfcris.com/en/rss",
        "icon": "https://kfcris.com/favicon.ico",
        "category": "沙特智库",
        "country": "沙特阿拉伯",
        "priority": 2,
        "description": "伊斯兰世界研究"
    },

    # 阿联酋智库
    {
        "name": "Emirates Policy Center",
        "name_cn": "阿联酋政策中心",
        "rss": "https://epc.ae/feed/",
        "icon": "https://epc.ae/favicon.ico",
        "category": "阿联酋智库",
        "country": "阿联酋",
        "priority": 2,
        "description": "中东政策研究"
    },

    # 卡塔尔智库
    {
        "name": "Arab Center for Research and Policy Studies",
        "name_cn": "阿拉伯研究与政策研究中心",
        "rss": "https://www.dohainstitute.org/en/rss.xml",
        "icon": "https://www.dohainstitute.org/favicon.ico",
        "category": "卡塔尔智库",
        "country": "卡塔尔",
        "priority": 2,
        "description": "阿拉伯世界研究"
    },

    # 土耳其智库
    {
        "name": "Center for Economics and Foreign Policy Studies",
        "name_cn": "经济与外交政策研究中心",
        "rss": "https://edam.org.tr/en/feed",
        "icon": "https://edam.org.tr/favicon.ico",
        "category": "土耳其智库",
        "country": "土耳其",
        "priority": 2,
        "description": "土耳其外交政策"
    },

    # ==================== 大洋洲地区 ====================
    # 澳大利亚智库
    {
        "name": "Lowy Institute",
        "name_cn": "罗伊研究所",
        "rss": "https://www.lowyinstitute.org/rss.xml",
        "icon": "https://www.lowyinstitute.org/favicon.ico",
        "category": "澳大利亚智库",
        "country": "澳大利亚",
        "priority": 2,
        "description": "澳大利亚顶级智库"
    },
    {
        "name": "Australian Strategic Policy Institute",
        "name_cn": "澳大利亚战略政策研究所",
        "rss": "https://www.aspi.org.au/rss.xml",
        "icon": "https://www.aspi.org.au/favicon.ico",
        "category": "澳大利亚智库",
        "country": "澳大利亚",
        "priority": 2,
        "description": "战略与防务研究"
    },
    {
        "name": "Grattan Institute",
        "name_cn": "格拉顿研究所",
        "rss": "https://grattan.edu.au/feed/",
        "icon": "https://grattan.edu.au/favicon.ico",
        "category": "澳大利亚智库",
        "country": "澳大利亚",
        "priority": 2,
        "description": "公共政策研究"
    },

    # 新西兰智库
    {
        "name": "New Zealand Institute of International Affairs",
        "name_cn": "新西兰国际事务研究所",
        "rss": "https://www.nziia.org.nz/rss.xml",
        "icon": "https://www.nziia.org.nz/favicon.ico",
        "category": "新西兰智库",
        "country": "新西兰",
        "priority": 2,
        "description": "新西兰外交政策"
    },

    # ==================== 拉丁美洲 ====================
    # 巴西智库
    {
        "name": "Fundação Getulio Vargas",
        "name_cn": "热图利奥·瓦加斯基金会",
        "rss": "https://portal.fgv.br/en/rss.xml",
        "icon": "https://portal.fgv.br/favicon.ico",
        "category": "巴西智库",
        "country": "巴西",
        "priority": 2,
        "description": "巴西经济与社会政策"
    },
    {
        "name": "Brazilian Center for International Relations",
        "name_cn": "巴西国际关系中心",
        "rss": "https://cebri.org/en/feed",
        "icon": "https://cebri.org/favicon.ico",
        "category": "巴西智库",
        "country": "巴西",
        "priority": 2,
        "description": "巴西外交政策"
    },

    # 阿根廷智库
    {
        "name": "Argentine Council for International Relations",
        "name_cn": "阿根廷国际关系委员会",
        "rss": "https://www.cari.org.ar/feed/",
        "icon": "https://www.cari.org.ar/favicon.ico",
        "category": "阿根廷智库",
        "country": "阿根廷",
        "priority": 2,
        "description": "阿根廷国际关系研究"
    },

    # 墨西哥智库
    {
        "name": "Mexican Council on Foreign Relations",
        "name_cn": "墨西哥外交关系委员会",
        "rss": "https://www.consejomexicano.org/feed/",
        "icon": "https://www.consejomexicano.org/favicon.ico",
        "category": "墨西哥智库",
        "country": "墨西哥",
        "priority": 2,
        "description": "墨西哥外交政策"
    },

    # ==================== 非洲地区 ====================
    # 南非智库
    {
        "name": "South African Institute of International Affairs",
        "name_cn": "南非国际事务研究所",
        "rss": "https://saiia.org.za/feed/",
        "icon": "https://saiia.org.za/favicon.ico",
        "category": "南非智库",
        "country": "南非",
        "priority": 2,
        "description": "非洲国际关系研究"
    },
    {
        "name": "Institute for Security Studies",
        "name_cn": "安全研究所",
        "rss": "https://issafrica.org/feed",
        "icon": "https://issafrica.org/favicon.ico",
        "category": "南非智库",
        "country": "南非",
        "priority": 2,
        "description": "非洲安全研究"
    },

    # 肯尼亚智库
    {
        "name": "Africa Policy Institute",
        "name_cn": "非洲政策研究所",
        "rss": "https://africapolicyinstitute.org/feed/",
        "icon": "https://africapolicyinstitute.org/favicon.ico",
        "category": "肯尼亚智库",
        "country": "肯尼亚",
        "priority": 2,
        "description": "非洲政策研究"
    },

    # ==================== 国际组织 & 多边机构 ====================
    {
        "name": "International Crisis Group",
        "name_cn": "国际危机组织",
        "rss": "https://www.crisisgroup.org/rss.xml",
        "icon": "https://www.crisisgroup.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "冲突预防与解决"
    },
    {
        "name": "International Institute for Strategic Studies",
        "name_cn": "国际战略研究所",
        "rss": "https://www.iiss.org/rss.xml",
        "icon": "https://www.iiss.org/favicon.ico",
        "category": "国际组织",
        "country": "英国",
        "priority": 1,
        "description": "军事与战略分析"
    },

    # ==================== 认知类网站 ====================
    {
        "name": "Project Syndicate",
        "name_cn": "报业辛迪加",
        "rss": "https://www.project-syndicate.org/rss",
        "icon": "https://www.project-syndicate.org/favicon.ico",
        "category": "认知网站",
        "country": "国际",
        "priority": 1,
        "description": "全球知名评论网站"
    },
    {
        "name": "Foreign Affairs",
        "name_cn": "外交事务",
        "rss": "https://www.foreignaffairs.com/feed",
        "icon": "https://www.foreignaffairs.com/favicon.ico",
        "category": "认知网站",
        "country": "美国",
        "priority": 1,
        "description": "顶级国际关系期刊"
    },
    {
        "name": "Foreign Policy",
        "name_cn": "外交政策",
        "rss": "https://foreignpolicy.com/feed/",
        "icon": "https://foreignpolicy.com/favicon.ico",
        "category": "认知网站",
        "country": "美国",
        "priority": 1,
        "description": "国际政治与政策"
    },
    {
        "name": "The Economist",
        "name_cn": "经济学人",
        "rss": "https://www.economist.com/feeds/print-sections/77/business.xml",
        "icon": "https://www.economist.com/favicon.ico",
        "category": "认知网站",
        "country": "英国",
        "priority": 1,
        "description": "全球政治经济分析"
    },
    {
        "name": "Harvard Kennedy School",
        "name_cn": "哈佛肯尼迪学院",
        "rss": "https://www.hks.harvard.edu/rss.xml",
        "icon": "https://www.harvard.edu/favicon.ico",
        "category": "认知网站",
        "country": "美国",
        "priority": 2,
        "description": "公共政策研究"
    },
    {
        "name": "MIT Technology Review",
        "name_cn": "麻省理工科技评论",
        "rss": "https://www.technologyreview.com/feed/",
        "icon": "https://www.technologyreview.com/favicon.ico",
        "category": "认知网站",
        "country": "美国",
        "priority": 2,
        "description": "科技创新分析"
    },
    {
        "name": "Wired",
        "name_cn": "连线杂志",
        "rss": "https://www.wired.com/feed/rss",
        "icon": "https://www.wired.com/favicon.ico",
        "category": "认知网站",
        "country": "美国",
        "priority": 2,
        "description": "科技与文化"
    },
    {
        "name": "Aeon",
        "name_cn": "万古杂志",
        "rss": "https://aeon.co/feed.rss",
        "icon": "https://aeon.co/favicon.ico",
        "category": "认知网站",
        "country": "国际",
        "priority": 2,
        "description": "深度思想与文化"
    },
    {
        "name": "Quartz",
        "name_cn": "石英",
        "rss": "https://qz.com/feed",
        "icon": "https://qz.com/favicon.ico",
        "category": "认知网站",
        "country": "美国",
        "priority": 2,
        "description": "商业与科技"
    },
    {
        "name": "Stratfor",
        "name_cn": "斯特拉福战略预测",
        "rss": "https://worldview.stratfor.com/rss.xml",
        "icon": "https://www.stratfor.com/favicon.ico",
        "category": "认知网站",
        "country": "美国",
        "priority": 1,
        "description": "地缘政治分析"
    },

    # ==================== 顶级学术期刊 ====================
    {
        "name": "Nature",
        "name_cn": "自然",
        "rss": "https://www.nature.com/nature.rss",
        "icon": "https://www.nature.com/favicon.ico",
        "category": "学术期刊",
        "country": "英国",
        "priority": 1,
        "description": "顶级科学期刊"
    },
    {
        "name": "Science",
        "name_cn": "科学",
        "rss": "https://www.sciencemag.org/rss/news_current.xml",
        "icon": "https://www.sciencemag.org/favicon.ico",
        "category": "学术期刊",
        "country": "美国",
        "priority": 1,
        "description": "顶级科学期刊"
    },
    {
        "name": "The Lancet",
        "name_cn": "柳叶刀",
        "rss": "https://www.thelancet.com/rss",
        "icon": "https://www.thelancet.com/favicon.ico",
        "category": "学术期刊",
        "country": "英国",
        "priority": 2,
        "description": "顶级医学期刊"
    },

    # ==================== 经济与政策分析 ====================
    {
        "name": "Peterson Institute for International Economics",
        "name_cn": "彼得森国际经济研究所",
        "rss": "https://www.piie.com/rss.xml",
        "icon": "https://www.piie.com/favicon.ico",
        "category": "经济政策",
        "country": "美国",
        "priority": 1,
        "description": "国际经济政策"
    },
    {
        "name": "National Bureau of Economic Research",
        "name_cn": "美国国家经济研究局",
        "rss": "https://www.nber.org/rss.xml",
        "icon": "https://www.nber.org/favicon.ico",
        "category": "经济政策",
        "country": "美国",
        "priority": 2,
        "description": "经济研究权威"
    },
    {
        "name": "Centre for Economic Policy Research",
        "name_cn": "经济政策研究中心",
        "rss": "https://cepr.org/rss.xml",
        "icon": "https://cepr.org/favicon.ico",
        "category": "经济政策",
        "country": "英国",
        "priority": 2,
        "description": "欧洲经济研究"
    },  # ==================== 补强：科技、安全与新兴力量 ====================
    {
        "name": "Center for a New American Security",
        "name_cn": "新美国安全中心",
        "rss": "https://www.cnas.org/rss/all.xml",
        "icon": "https://www.cnas.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "专注印太安全、AI竞争及国防政策"
    },
    {
        "name": "Center for Security and Emerging Technology",
        "name_cn": "安全与新兴技术中心",
        "rss": "https://cset.georgetown.edu/feed/",
        "icon": "https://cset.georgetown.edu/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "乔治城大学旗下的AI与半导体政策权威"
    },
    {
        "name": "Royal United Services Institute",
        "name_cn": "英国皇家三军联合研究所",
        "rss": "https://rusi.org/rss.xml",
        "icon": "https://rusi.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "全球最古老的国防与安全研究智库"
    },
    {
        "name": "Vivekananda International Foundation",
        "name_cn": "维韦卡南达国际基金会",
        "rss": "https://www.vifindia.org/rss.xml",
        "icon": "https://www.vifindia.org/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 2,
        "description": "印度核心国家安全与战略决策智库"
    },
    {
        "name": "The Diplomat",
        "name_cn": "外交官杂志",
        "rss": "https://thediplomat.com/feed/",
        "icon": "https://thediplomat.com/favicon.ico",
        "category": "认知网站",
        "country": "国际",
        "priority": 1,
        "description": "深度观察亚太地区政治、安全与文化的权威窗口"
    },
    {
        "name": "War on the Rocks",
        "name_cn": "岩石上的战争",
        "rss": "https://warontherocks.com/feed/",
        "icon": "https://warontherocks.com/favicon.ico",
        "category": "认知网站",
        "country": "美国",
        "priority": 1,
        "description": "职业战略家、军官和学者的高质量讨论平台"
    }
]


# 按国家/地区统计
def get_country_stats():
    stats = {}
    for tank in THINK_TANKS_CONFIG:
        country = tank.get('country', '其他')
        if country not in stats:
            stats[country] = 0
        stats[country] += 1
    return stats


# 按类别统计
def get_category_stats():
    stats = {}
    for tank in THINK_TANKS_CONFIG:
        category = tank.get('category', '其他')
        if category not in stats:
            stats[category] = 0
        stats[category] += 1
    return stats
