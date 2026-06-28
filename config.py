# config.py
# 全球智库及认知网站配置文件
# 可随时添加、修改或删除信息源
# 建议：如果官方 rsshub.app 无法连接，请更换为以下公共镜像：
# https://rss.lilywhite.cc
# https://rsshub.pseudo.moe
# https://rss.cloudnative.love
# Google News 站点 RSS（用于无官方 RSS 的智库官网）
GNEWS_CN = "https://news.google.com/rss/search?q=site:{domain}&hl=zh-CN&gl=CN&ceid=CN:zh-Hans"
GNEWS_US = "https://news.google.com/rss/search?q=site:{domain}+when:7d&hl=en-US&gl=US&ceid=US:en"
GNEWS = GNEWS_US  # 适用于大多数国家智库官网的 Google News 站点订阅
GNEWS_SITE = "https://news.google.com/rss/search?q=site:{domain}&hl=en-US&gl=US&ceid=US:en"

THINK_TANKS_CONFIG = [
    # ==================== 中国智库 ====================
    {
        "name": "CICIR",
        "name_cn": "中国现代国际关系研究院",
        "rss": GNEWS_CN.format(domain="cicir.ac.cn"),
        "icon": "https://www.cicir.ac.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国顶级国际关系与安全研究机构"
    },
    {
        "name": "Development Research Center",
        "name_cn": "国务院发展研究中心",
        "rss": GNEWS_CN.format(domain="drc.gov.cn"),
        "icon": "http://www.drc.gov.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国政府核心决策咨询智库"
    },
    {
        "name": "CASS",
        "name_cn": "中国社会科学院",
        "rss": GNEWS_CN.format(domain="cssn.cn"),
        "icon": "http://www.cssn.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国哲学社会科学研究最高殿堂"
    },
    {
        "name": "SIIS",
        "name_cn": "上海国际问题研究院",
        "rss": GNEWS_CN.format(domain="siis.org.cn"),
        "icon": "http://www.siis.org.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国重要外交与地缘政治研究机构"
    },
    {
        "name": "CIIS",
        "name_cn": "中国国际问题研究院",
        "rss": GNEWS_CN.format(domain="ciis.org.cn"),
        "icon": "https://www.ciis.org.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国外交部直属国际问题研究机构"
    },
    {
        "name": "CCIEE",
        "name_cn": "中国国际经济交流中心",
        "rss": GNEWS_CN.format(domain="cciee.org.cn"),
        "icon": "http://www.cciee.org.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "国际经济政策与战略研究"
    },
    {
        "name": "CF40",
        "name_cn": "中国金融四十人论坛",
        "rss": GNEWS_CN.format(domain="cf40.com"),
        "icon": "https://www.cf40.com/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "金融与宏观经济政策顶尖智库"
    },
    {
        "name": "Chongyang Institute",
        "name_cn": "中国人民大学重阳金融研究院",
        "rss": GNEWS_CN.format(domain="rdcy.ruc.edu.cn"),
        "icon": "http://www.ruc.edu.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "金融、宏观与全球治理研究"
    },
    {
        "name": "People's Daily Theory",
        "name_cn": "人民网·理论",
        "rss": "http://www.people.com.cn/rss/theory.xml",
        "icon": "http://www.people.com.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "权威政策理论与思想动态"
    },
    {
        "name": "People's Daily Opinion",
        "name_cn": "人民网·观点",
        "rss": "http://www.people.com.cn/rss/opinion.xml",
        "icon": "http://www.people.com.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "政策评论与深度观点"
    },
    {
        "name": "Xinhua World",
        "name_cn": "新华网·国际",
        "rss": "http://www.news.cn/world/news_world.xml",
        "icon": "http://www.news.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "中国国际时事与外交动态"
    },
    {
        "name": "China Daily Opinion",
        "name_cn": "中国日报·评论",
        "rss": "http://www.chinadaily.com.cn/rss/opinion_rss.xml",
        "icon": "http://www.chinadaily.com.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 1,
        "description": "面向国际读者的中国政策评论"
    },
    {
        "name": "FT Chinese",
        "name_cn": "FT中文网",
        "rss": "http://www.ftchinese.com/rss/news",
        "icon": "http://www.ftchinese.com/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "国际财经与地缘政治中文分析"
    },
    {
        "name": "Sinocism",
        "name_cn": "Sinocism",
        "rss": "https://sinocism.com/feed",
        "icon": "https://sinocism.com/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "中国政治与政策英文简报"
    },
    {
        "name": "Fudan IIS",
        "name_cn": "复旦大学国际问题研究院",
        "rss": GNEWS_CN.format(domain="iis.fudan.edu.cn"),
        "icon": "http://www.fudan.edu.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "国际问题综合研究"
    },
    {
        "name": "PKU IISS",
        "name_cn": "北京大学国际战略研究院",
        "rss": GNEWS_CN.format(domain="iiss.pku.edu.cn"),
        "icon": "https://www.pku.edu.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "国际战略与安全研究"
    },
    {
        "name": "China Think Tanks",
        "name_cn": "中国智库网",
        "rss": GNEWS_CN.format(domain="chinathinktanks.org.cn"),
        "icon": "http://www.chinathinktanks.org.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "中国智库观点与实践聚合"
    },
    {
        "name": "Caixin",
        "name_cn": "财新网",
        "rss": GNEWS_CN.format(domain="caixin.com"),
        "icon": "https://www.caixin.com/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "财经与公共政策深度报道"
    },
    {
        "name": "Xinhua Politics",
        "name_cn": "新华网·时政",
        "rss": "http://www.news.cn/politics/news_politics.xml",
        "icon": "http://www.news.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "中国时政与政策动态"
    },
    {
        "name": "China Daily China",
        "name_cn": "中国日报·国内",
        "rss": "http://www.chinadaily.com.cn/rss/china_rss.xml",
        "icon": "http://www.chinadaily.com.cn/favicon.ico",
        "category": "中国智库",
        "country": "中国",
        "priority": 2,
        "description": "中国国内政策与治理"
    },
    # ==================== 北美地区 ====================
    # 美国顶级智库
    {
        "name": "Brookings Institution",
        "name_cn": "布鲁金斯学会",
        "rss": GNEWS_US.format(domain="brookings.edu"),
        "icon": "https://www.brookings.edu/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "美国最具影响力的智库之一"
    },
    {
        "name": "Carnegie Endowment for International Peace",
        "name_cn": "卡内基国际和平基金会",
        "rss": GNEWS_US.format(domain="carnegieendowment.org"),
        "icon": "https://carnegieendowment.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "国际事务研究顶级智库"
    },
    {
        "name": "Council on Foreign Relations",
        "name_cn": "外交关系委员会",
        "rss": "http://feeds.cfr.org/cfr_main",
        "icon": "https://www.cfr.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "美国外交政策权威机构"
    },
    {
        "name": "RAND Corporation",
        "name_cn": "兰德公司",
        "rss": "https://www.rand.org/pubs/research_reports.xml",
        "icon": "https://www.rand.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "全球知名政策研究机构"
    },
    {
        "name": "Peterson Institute for International Economics",
        "name_cn": "彼得森国际经济研究所",
        "rss": GNEWS_US.format(domain="piie.com"),
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
        "rss": GNEWS_US.format(domain="heritage.org"),
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
        "rss": GNEWS_US.format(domain="wilsoncenter.org"),
        "icon": "https://www.wilsoncenter.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "国际问题研究"
    },
    {
        "name": "Urban Institute",
        "name_cn": "城市研究所",
        "rss": GNEWS_US.format(domain="urban.org"),
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
        "rss": GNEWS_US.format(domain="americanprogress.org"),
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
    {
        "name": "Center for a New American Security",
        "name_cn": "新美国安全中心",
        "rss": GNEWS_US.format(domain="cnas.org"),
        "icon": "https://www.cnas.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "国防、印太安全与新兴技术政策"
    },
    {
        "name": "Hudson Institute",
        "name_cn": "哈德逊研究所",
        "rss": "https://www.hudson.org/rss.xml",
        "icon": "https://www.hudson.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "保守派外交与国防政策研究"
    },
    {
        "name": "German Marshall Fund",
        "name_cn": "德国马歇尔基金会",
        "rss": "https://www.gmfus.org/rss.xml",
        "icon": "https://www.gmfus.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "跨大西洋关系与全球民主"
    },
    {
        "name": "Quincy Institute",
        "name_cn": "昆西研究所",
        "rss": "https://quincyinst.org/feed/",
        "icon": "https://quincyinst.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 1,
        "description": "现实主义外交与克制战略"
    },
    {
        "name": "Defense Priorities",
        "name_cn": "国防优先事项",
        "rss": "https://www.defensepriorities.org/feed",
        "icon": "https://www.defensepriorities.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "有限军事干预与战略收缩"
    },
    {
        "name": "Stimson Center",
        "name_cn": "史汀生中心",
        "rss": GNEWS_US.format(domain="stimson.org"),
        "icon": "https://www.stimson.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "国际安全、防扩散与亚洲政策"
    },
    {
        "name": "New America",
        "name_cn": "新美国基金会",
        "rss": GNEWS_US.format(domain="newamerica.org"),
        "icon": "https://www.newamerica.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "科技、安全与社会政策创新"
    },
    {
        "name": "Center for Security and Emerging Technology",
        "name_cn": "安全与新兴技术中心",
        "rss": GNEWS_US.format(domain="cset.georgetown.edu"),
        "icon": "https://cset.georgetown.edu/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "AI、半导体与科技竞争政策"
    },
    {
        "name": "Foreign Policy Research Institute",
        "name_cn": "外交政策研究所",
        "rss": GNEWS_US.format(domain="fpri.org"),
        "icon": "https://www.fpri.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "历史视角下的美国外交"
    },
    {
        "name": "Middle East Institute",
        "name_cn": "中东研究所",
        "rss": GNEWS_US.format(domain="mei.edu"),
        "icon": "https://www.mei.edu/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "中东政治、安全与能源"
    },
    {
        "name": "Belfer Center",
        "name_cn": "贝尔弗中心",
        "rss": GNEWS_US.format(domain="belfercenter.org"),
        "icon": "https://www.belfercenter.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "哈佛肯尼迪学院安全与科技政策"
    },
    {
        "name": "Jamestown Foundation",
        "name_cn": "詹姆斯敦基金会",
        "rss": GNEWS_US.format(domain="jamestown.org"),
        "icon": "https://jamestown.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "欧亚安全与地缘政治分析"
    },
    {
        "name": "Manhattan Institute",
        "name_cn": "曼哈顿研究所",
        "rss": "https://www.manhattan-institute.org/rss.xml",
        "icon": "https://www.manhattan-institute.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "城市、经济与社会政策"
    },
    {
        "name": "Migration Policy Institute",
        "name_cn": "移民政策研究所",
        "rss": "https://www.migrationpolicy.org/rss.xml",
        "icon": "https://www.migrationpolicy.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "移民与难民政策研究"
    },
    {
        "name": "Aspen Institute",
        "name_cn": "阿斯彭研究所",
        "rss": "https://www.aspeninstitute.org/feed/",
        "icon": "https://www.aspeninstitute.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "领导力、民主与全球议题"
    },
    {
        "name": "National Bureau of Asian Research",
        "name_cn": "美国国家亚洲研究局",
        "rss": GNEWS_US.format(domain="nbr.org"),
        "icon": "https://www.nbr.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "亚洲安全与经济政策"
    },
    {
        "name": "Center for Strategic and Budgetary Assessments",
        "name_cn": "战略与预算评估中心",
        "rss": GNEWS_SITE.format(domain="csbaonline.org"),
        "icon": "https://csbaonline.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "美国国防预算与军事战略"
    },
    {
        "name": "R Street Institute",
        "name_cn": "R街研究所",
        "rss": GNEWS_SITE.format(domain="rstreet.org"),
        "icon": "https://www.rstreet.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "自由市场公共政策"
    },
    {
        "name": "Third Way",
        "name_cn": "第三条道路",
        "rss": GNEWS_SITE.format(domain="thirdway.org"),
        "icon": "https://www.thirdway.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "中间派进步政策"
    },
    {
        "name": "Information Technology and Innovation Foundation",
        "name_cn": "信息技术与创新基金会",
        "rss": GNEWS_SITE.format(domain="itif.org"),
        "icon": "https://www.itif.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "科技创新与产业政策"
    },
    {
        "name": "Bipartisan Policy Center",
        "name_cn": "两党政策中心",
        "rss": GNEWS.format(domain="bipartisanpolicy.org"),
        "icon": "https://bipartisanpolicy.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "跨党派公共政策对话"
    },
    {
        "name": "East-West Center",
        "name_cn": "东西方中心",
        "rss": GNEWS.format(domain="eastwestcenter.org"),
        "icon": "https://www.eastwestcenter.org/favicon.ico",
        "category": "美国智库",
        "country": "美国",
        "priority": 2,
        "description": "亚太与美国关系研究"
    },

    # 加拿大智库
    {
        "name": "Centre for International Governance Innovation",
        "name_cn": "国际治理创新中心",
        "rss": GNEWS.format(domain="cigionline.org"),
        "icon": "https://www.cigionline.org/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 1,
        "description": "国际治理与数字经济研究"
    },
    {
        "name": "Canadian Global Affairs Institute",
        "name_cn": "加拿大全球事务研究所",
        "rss": GNEWS.format(domain="cgai.ca"),
        "icon": "https://www.cgai.ca/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 1,
        "description": "加拿大外交与国防政策"
    },
    {
        "name": "Macdonald-Laurier Institute",
        "name_cn": "麦克唐纳-劳里尔研究所",
        "rss": GNEWS.format(domain="macdonaldlaurier.ca"),
        "icon": "https://www.macdonaldlaurier.ca/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 2,
        "description": "加拿大公共政策与国家安全"
    },
    {
        "name": "C.D. Howe Institute",
        "name_cn": "C.D.豪研究所",
        "rss": GNEWS.format(domain="cdhowe.org"),
        "icon": "https://www.cdhowe.org/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 2,
        "description": "加拿大经济与社会政策"
    },
    {
        "name": "Fraser Institute",
        "name_cn": "弗雷泽研究所",
        "rss": GNEWS.format(domain="fraserinstitute.org"),
        "icon": "https://www.fraserinstitute.org/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 2,
        "description": "自由市场与公共政策研究"
    },
    {
        "name": "Institute for Research on Public Policy",
        "name_cn": "公共政策研究研究所",
        "rss": GNEWS.format(domain="irpp.org"),
        "icon": "https://irpp.org/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 2,
        "description": "加拿大社会与经济政策"
    },
    {
        "name": "Asia Pacific Foundation of Canada",
        "name_cn": "加拿大亚太基金会",
        "rss": GNEWS.format(domain="asiapacific.ca"),
        "icon": "https://www.asiapacific.ca/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 2,
        "description": "加拿大与亚太关系"
    },
    {
        "name": "The Conference Board of Canada",
        "name_cn": "加拿大Conference Board",
        "rss": GNEWS.format(domain="conferenceboard.ca"),
        "icon": "https://www.conferenceboard.ca/favicon.ico",
        "category": "加拿大智库",
        "country": "加拿大",
        "priority": 2,
        "description": "加拿大经济与企业研究"
    },

    # ==================== 欧洲地区 ====================
    # 英国智库
    {
        "name": "Chatham House",
        "name_cn": "查塔姆研究所",
        "rss": GNEWS.format(domain="chathamhouse.org"),
        "icon": "https://www.chathamhouse.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 1,
        "description": "英国皇家国际事务研究所"
    },
    {
        "name": "International Institute for Strategic Studies",
        "name_cn": "国际战略研究所",
        "rss": GNEWS_SITE.format(domain="iiss.org"),
        "icon": "https://www.iiss.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 1,
        "description": "军事与战略研究"
    },
    {
        "name": "Royal United Services Institute",
        "name_cn": "英国皇家三军联合研究所",
        "rss": GNEWS.format(domain="rusi.org"),
        "icon": "https://rusi.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 1,
        "description": "国防与安全研究"
    },
    {
        "name": "Overseas Development Institute",
        "name_cn": "海外发展研究所",
        "rss": GNEWS.format(domain="odi.org"),
        "icon": "https://odi.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "国际发展研究"
    },
    {
        "name": "Policy Exchange",
        "name_cn": "政策交流",
        "rss": GNEWS.format(domain="policyexchange.org.uk"),
        "icon": "https://policyexchange.org.uk/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "英国政策研究"
    },
    {
        "name": "Institute for Government",
        "name_cn": "政府研究所",
        "rss": GNEWS.format(domain="instituteforgovernment.org.uk"),
        "icon": "https://www.instituteforgovernment.org.uk/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "政府治理研究"
    },
    {
        "name": "Centre for Economic Policy Research",
        "name_cn": "经济政策研究中心",
        "rss": GNEWS.format(domain="cepr.org"),
        "icon": "https://cepr.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "欧洲经济研究网络"
    },
    {
        "name": "Adam Smith Institute",
        "name_cn": "亚当·斯密研究所",
        "rss": GNEWS.format(domain="adamsmith.org"),
        "icon": "https://www.adamsmith.org/favicon.ico",
        "category": "英国智库",
        "country": "英国",
        "priority": 2,
        "description": "自由市场与古典自由主义"
    },

    # 德国智库
    {
        "name": "German Council on Foreign Relations",
        "name_cn": "德国外交关系委员会",
        "rss": GNEWS.format(domain="dgap.org"),
        "icon": "https://dgap.org/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 1,
        "description": "德国外交政策研究"
    },
    {
        "name": "Stiftung Wissenschaft und Politik",
        "name_cn": "德国国际与安全事务研究所",
        "rss": GNEWS.format(domain="swp-berlin.org"),
        "icon": "https://www.swp-berlin.org/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 1,
        "description": "德国顶级安全政策智库"
    },
    {
        "name": "Mercator Institute for China Studies",
        "name_cn": "墨卡托中国研究中心",
        "rss": GNEWS.format(domain="merics.org"),
        "icon": "https://merics.org/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "中国政治经济研究"
    },
    {
        "name": "Kiel Institute for the World Economy",
        "name_cn": "基尔世界经济研究所",
        "rss": GNEWS.format(domain="ifw-kiel.de"),
        "icon": "https://www.ifw-kiel.de/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "国际经济研究"
    },
    {
        "name": "ifo Institute",
        "name_cn": "伊福经济研究所",
        "rss": GNEWS.format(domain="ifo.de"),
        "icon": "https://www.ifo.de/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "德国经济景气与政策分析"
    },
    {
        "name": "German Institute for Economic Research",
        "name_cn": "德国经济研究所",
        "rss": GNEWS.format(domain="diw.de"),
        "icon": "https://www.diw.de/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "德国宏观经济与社会政策"
    },
    {
        "name": "Konrad Adenauer Foundation",
        "name_cn": "康拉德·阿登纳基金会",
        "rss": GNEWS.format(domain="kas.de"),
        "icon": "https://www.kas.de/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "德国外交与民主推广"
    },
    {
        "name": "Bertelsmann Stiftung",
        "name_cn": "贝塔斯曼基金会",
        "rss": GNEWS.format(domain="bti-project.org"),
        "icon": "https://www.bti-project.org/favicon.ico",
        "category": "德国智库",
        "country": "德国",
        "priority": 2,
        "description": "全球治理与转型指数"
    },

    # 法国智库
    {
        "name": "French Institute of International Relations",
        "name_cn": "法国国际关系研究所",
        "rss": GNEWS.format(domain="ifri.org"),
        "icon": "https://www.ifri.org/favicon.ico",
        "category": "法国智库",
        "country": "法国",
        "priority": 1,
        "description": "法国顶级国际关系智库"
    },
    {
        "name": "Foundation for Strategic Research",
        "name_cn": "法国战略研究基金会",
        "rss": GNEWS.format(domain="frstrategie.org"),
        "icon": "https://www.frstrategie.org/favicon.ico",
        "category": "法国智库",
        "country": "法国",
        "priority": 2,
        "description": "法国国防与战略研究"
    },
    {
        "name": "Institute for International and Strategic Relations",
        "name_cn": "法国国际与战略关系研究所",
        "rss": GNEWS.format(domain="iris-france.org"),
        "icon": "https://www.iris-france.org/favicon.ico",
        "category": "法国智库",
        "country": "法国",
        "priority": 2,
        "description": "法国外交与安全政策"
    },
    {
        "name": "Institut Montaigne",
        "name_cn": "蒙田研究所",
        "rss": GNEWS.format(domain="institutmontaigne.org"),
        "icon": "https://www.institutmontaigne.org/favicon.ico",
        "category": "法国智库",
        "country": "法国",
        "priority": 2,
        "description": "法国独立公共政策研究"
    },

    # 意大利智库
    {
        "name": "Istituto Affari Internazionali",
        "name_cn": "国际事务研究院",
        "rss": GNEWS.format(domain="iai.it"),
        "icon": "https://www.iai.it/favicon.ico",
        "category": "意大利智库",
        "country": "意大利",
        "priority": 1,
        "description": "意大利国际事务研究"
    },
    {
        "name": "Italian Institute for International Political Studies",
        "name_cn": "意大利国际政治研究学会",
        "rss": GNEWS.format(domain="ispionline.it"),
        "icon": "https://www.ispionline.it/favicon.ico",
        "category": "意大利智库",
        "country": "意大利",
        "priority": 2,
        "description": "地中海与欧洲安全研究"
    },
    {
        "name": "LUISS School of Government",
        "name_cn": "LUISS政府学院",
        "rss": GNEWS.format(domain="luiss.it"),
        "icon": "https://www.luiss.it/favicon.ico",
        "category": "意大利智库",
        "country": "意大利",
        "priority": 2,
        "description": "意大利政治与欧洲治理"
    },

    # 瑞典智库
    {
        "name": "Stockholm International Peace Research Institute",
        "name_cn": "斯德哥尔摩国际和平研究所",
        "rss": GNEWS.format(domain="sipri.org"),
        "icon": "https://www.sipri.org/favicon.ico",
        "category": "瑞典智库",
        "country": "瑞典",
        "priority": 1,
        "description": "全球和平与安全研究权威"
    },
    {
        "name": "Swedish Institute of International Affairs",
        "name_cn": "瑞典国际事务研究所",
        "rss": GNEWS.format(domain="ui.se"),
        "icon": "https://www.ui.se/favicon.ico",
        "category": "瑞典智库",
        "country": "瑞典",
        "priority": 2,
        "description": "北欧外交与安全政策"
    },
    {
        "name": "FOI Swedish Defence Research Agency",
        "name_cn": "瑞典国防研究局",
        "rss": GNEWS_SITE.format(domain="foi.se"),
        "icon": "https://www.foi.se/favicon.ico",
        "category": "瑞典智库",
        "country": "瑞典",
        "priority": 2,
        "description": "国防技术与安全研究"
    },
    {
        "name": "Stockholm Free World Forum",
        "name_cn": "斯德哥尔摩自由世界论坛",
        "rss": GNEWS.format(domain="frivarld.se"),
        "icon": "https://frivarld.se/favicon.ico",
        "category": "瑞典智库",
        "country": "瑞典",
        "priority": 2,
        "description": "民主、安全与地缘政治"
    },

    # 荷兰智库
    {
        "name": "Netherlands Institute of International Relations",
        "name_cn": "荷兰国际关系研究所",
        "rss": GNEWS.format(domain="clingendael.org"),
        "icon": "https://www.clingendael.org/favicon.ico",
        "category": "荷兰智库",
        "country": "荷兰",
        "priority": 2,
        "description": "荷兰顶级外交与安全智库"
    },
    {
        "name": "The Hague Centre for Strategic Studies",
        "name_cn": "海牙战略研究中心",
        "rss": GNEWS.format(domain="hcss.nl"),
        "icon": "https://hcss.nl/favicon.ico",
        "category": "荷兰智库",
        "country": "荷兰",
        "priority": 2,
        "description": "地缘政治与安全分析"
    },
    {
        "name": "Netherlands Scientific Council for Government Policy",
        "name_cn": "荷兰政府科学委员会",
        "rss": GNEWS_SITE.format(domain="wrr.nl"),
        "icon": "https://www.wrr.nl/favicon.ico",
        "category": "荷兰智库",
        "country": "荷兰",
        "priority": 2,
        "description": "荷兰长期政策研究"
    },

    # 西班牙智库
    {
        "name": "Elcano Royal Institute",
        "name_cn": "埃尔卡诺皇家研究所",
        "rss": GNEWS.format(domain="realinstitutoelcano.org"),
        "icon": "https://www.realinstitutoelcano.org/favicon.ico",
        "category": "西班牙智库",
        "country": "西班牙",
        "priority": 2,
        "description": "西班牙国际关系与欧洲研究"
    },
    {
        "name": "Barcelona Centre for International Affairs",
        "name_cn": "巴塞罗那国际事务中心",
        "rss": GNEWS.format(domain="cidob.org"),
        "icon": "https://www.cidob.org/favicon.ico",
        "category": "西班牙智库",
        "country": "西班牙",
        "priority": 2,
        "description": "地中海与全球治理"
    },

    # 挪威智库
    {
        "name": "Norwegian Institute of International Affairs",
        "name_cn": "挪威国际事务研究所",
        "rss": GNEWS.format(domain="nupi.no"),
        "icon": "https://www.nupi.no/favicon.ico",
        "category": "挪威智库",
        "country": "挪威",
        "priority": 2,
        "description": "北极、安全与和平研究"
    },
    {
        "name": "Fridtjof Nansen Institute",
        "name_cn": "弗里乔夫·南森研究所",
        "rss": GNEWS.format(domain="fni.no"),
        "icon": "https://www.fni.no/favicon.ico",
        "category": "挪威智库",
        "country": "挪威",
        "priority": 2,
        "description": "北极、能源与环境政策"
    },

    # 瑞士智库
    {
        "name": "Center for Security Studies",
        "name_cn": "苏黎世安全研究中心",
        "rss": GNEWS.format(domain="css.ethz.ch"),
        "icon": "https://css.ethz.ch/favicon.ico",
        "category": "瑞士智库",
        "country": "瑞士",
        "priority": 2,
        "description": "ETH苏黎世安全与战略研究"
    },
    {
        "name": "Avenir Suisse",
        "name_cn": "瑞士未来基金会",
        "rss": GNEWS.format(domain="avenir-suisse.ch"),
        "icon": "https://www.avenir-suisse.ch/favicon.ico",
        "category": "瑞士智库",
        "country": "瑞士",
        "priority": 2,
        "description": "瑞士经济与社会改革"
    },

    # 波兰智库
    {
        "name": "Polish Institute of International Affairs",
        "name_cn": "波兰国际事务研究所",
        "rss": GNEWS.format(domain="pism.pl"),
        "icon": "https://www.pism.pl/favicon.ico",
        "category": "波兰智库",
        "country": "波兰",
        "priority": 2,
        "description": "中东欧安全与欧盟政策"
    },
    {
        "name": "Centre for Eastern Studies",
        "name_cn": "东方研究中心",
        "rss": GNEWS.format(domain="osw.waw.pl"),
        "icon": "https://www.osw.waw.pl/favicon.ico",
        "category": "波兰智库",
        "country": "波兰",
        "priority": 2,
        "description": "东欧与俄罗斯研究"
    },

    # 奥地利智库
    {
        "name": "Institute for Human Sciences",
        "name_cn": "人文科学研究所",
        "rss": GNEWS.format(domain="iwm.at"),
        "icon": "https://www.iwm.at/favicon.ico",
        "category": "奥地利智库",
        "country": "奥地利",
        "priority": 2,
        "description": "中欧思想与公共政策"
    },
    {
        "name": "Austrian Institute of Economic Research",
        "name_cn": "奥地利经济研究所",
        "rss": GNEWS.format(domain="wifo.ac.at"),
        "icon": "https://www.wifo.ac.at/favicon.ico",
        "category": "奥地利智库",
        "country": "奥地利",
        "priority": 2,
        "description": "奥地利宏观经济分析"
    },

    # 比利时智库（欧盟）
    {
        "name": "Bruegel",
        "name_cn": "布鲁盖尔研究所",
        "rss": GNEWS.format(domain="bruegel.org"),
        "icon": "https://www.bruegel.org/favicon.ico",
        "category": "欧盟智库",
        "country": "比利时",
        "priority": 1,
        "description": "欧洲经济政策研究"
    },
    {
        "name": "Centre for European Policy Studies",
        "name_cn": "欧洲政策研究中心",
        "rss": GNEWS.format(domain="ceps.eu"),
        "icon": "https://www.ceps.eu/favicon.ico",
        "category": "欧盟智库",
        "country": "比利时",
        "priority": 2,
        "description": "欧盟政策研究"
    },
    {
        "name": "Egmont Institute",
        "name_cn": "埃格蒙特研究所",
        "rss": GNEWS.format(domain="egmontinstitute.be"),
        "icon": "https://www.egmontinstitute.be/favicon.ico",
        "category": "欧盟智库",
        "country": "比利时",
        "priority": 2,
        "description": "欧盟外交与非洲政策"
    },

    # ==================== 亚洲地区 ====================
    # 日本智库
    {
        "name": "Japan Institute of International Affairs",
        "name_cn": "日本国际问题研究所",
        "rss": GNEWS.format(domain="jiia.or.jp"),
        "icon": "https://www.jiia.or.jp/favicon.ico",
        "category": "日本智库",
        "country": "日本",
        "priority": 2,
        "description": "日本顶级国际关系智库"
    },
    {
        "name": "Asia Pacific Initiative",
        "name_cn": "亚太倡议",
        "rss": GNEWS.format(domain="apinitiative.org"),
        "icon": "https://apinitiative.org/favicon.ico",
        "category": "日本智库",
        "country": "日本",
        "priority": 2,
        "description": "亚太地区政策研究"
    },
    {
        "name": "Tokyo Foundation for Policy Research",
        "name_cn": "东京政策研究基金会",
        "rss": GNEWS_SITE.format(domain="tkfd.or.jp"),
        "icon": "https://www.tkfd.or.jp/favicon.ico",
        "category": "日本智库",
        "country": "日本",
        "priority": 2,
        "description": "日本外交与经济政策"
    },
    {
        "name": "Research Institute of Economy Trade and Industry",
        "name_cn": "日本经济产业研究所",
        "rss": GNEWS.format(domain="rieti.go.jp"),
        "icon": "https://www.rieti.go.jp/favicon.ico",
        "category": "日本智库",
        "country": "日本",
        "priority": 2,
        "description": "日本产业政策与创新"
    },
    {
        "name": "National Institute for Defense Studies",
        "name_cn": "日本防卫研究所",
        "rss": GNEWS.format(domain="nids.mod.go.jp"),
        "icon": "https://www.nids.mod.go.jp/favicon.ico",
        "category": "日本智库",
        "country": "日本",
        "priority": 2,
        "description": "日本防卫与安全战略"
    },

    # 韩国智库
    {
        "name": "Asan Institute for Policy Studies",
        "name_cn": "峨山政策研究院",
        "rss": GNEWS.format(domain="asaninst.org"),
        "icon": "https://en.asaninst.org/favicon.ico",
        "category": "韩国智库",
        "country": "韩国",
        "priority": 1,
        "description": "韩国顶级政策研究机构"
    },
    {
        "name": "Korea Institute for International Economic Policy",
        "name_cn": "韩国对外经济政策研究院",
        "rss": GNEWS.format(domain="kiep.go.kr"),
        "icon": "https://www.kiep.go.kr/favicon.ico",
        "category": "韩国智库",
        "country": "韩国",
        "priority": 2,
        "description": "国际经济政策研究"
    },
    {
        "name": "Korea Institute for National Unification",
        "name_cn": "韩国统一研究院",
        "rss": GNEWS.format(domain="kinu.or.kr"),
        "icon": "https://www.kinu.or.kr/favicon.ico",
        "category": "韩国智库",
        "country": "韩国",
        "priority": 2,
        "description": "朝鲜半岛统一与安全"
    },
    {
        "name": "Sejong Institute",
        "name_cn": "世宗研究所",
        "rss": GNEWS_SITE.format(domain="sejong.org"),
        "icon": "https://www.sejong.org/favicon.ico",
        "category": "韩国智库",
        "country": "韩国",
        "priority": 2,
        "description": "韩国外交与安全战略"
    },
    {
        "name": "Korea Development Institute",
        "name_cn": "韩国开发研究院",
        "rss": GNEWS.format(domain="kdi.re.kr"),
        "icon": "https://www.kdi.re.kr/favicon.ico",
        "category": "韩国智库",
        "country": "韩国",
        "priority": 2,
        "description": "韩国宏观经济与发展政策"
    },
    {
        "name": "Korea Economic Research Institute",
        "name_cn": "韩国经济研究院",
        "rss": GNEWS_SITE.format(domain="keri.org"),
        "icon": "https://www.keri.org/favicon.ico",
        "category": "韩国智库",
        "country": "韩国",
        "priority": 2,
        "description": "韩国产业与经济政策"
    },

    # 印度智库
    {
        "name": "Observer Research Foundation",
        "name_cn": "观察家研究基金会",
        "rss": GNEWS.format(domain="orfonline.org"),
        "icon": "https://www.orfonline.org/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 1,
        "description": "印度顶级智库"
    },
    {
        "name": "Gateway House",
        "name_cn": "门楼印度委员会",
        "rss": GNEWS.format(domain="gatewayhouse.in"),
        "icon": "https://www.gatewayhouse.in/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 2,
        "description": "印度外交与经济政策"
    },
    {
        "name": "Centre for Policy Research",
        "name_cn": "政策研究中心",
        "rss": GNEWS_SITE.format(domain="cprindia.org"),
        "icon": "https://cprindia.org/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 2,
        "description": "印度公共政策研究"
    },
    {
        "name": "Institute for Defence Studies and Analyses",
        "name_cn": "国防研究与分析研究所",
        "rss": GNEWS.format(domain="idsa.in"),
        "icon": "https://www.idsa.in/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 1,
        "description": "印度国防与战略研究"
    },
    {
        "name": "United Service Institution of India",
        "name_cn": "印度联合服务学会",
        "rss": GNEWS.format(domain="usiofindia.org"),
        "icon": "https://www.usiofindia.org/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 2,
        "description": "印度军事与安全事务"
    },
    {
        "name": "Carnegie India",
        "name_cn": "卡内基印度中心",
        "rss": GNEWS.format(domain="carnegieindia.org"),
        "icon": "https://carnegieindia.org/favicon.ico",
        "category": "印度智库",
        "country": "印度",
        "priority": 2,
        "description": "印度外交与科技政策"
    },

    # 印度尼西亚智库
    {
        "name": "Centre for Strategic and International Studies Jakarta",
        "name_cn": "雅加达战略与国际问题研究中心",
        "rss": GNEWS.format(domain="csis.or.id"),
        "icon": "https://www.csis.or.id/favicon.ico",
        "category": "印度尼西亚智库",
        "country": "印度尼西亚",
        "priority": 2,
        "description": "东南亚最大智库之一"
    },
    {
        "name": "Institute for Development of Economics and Finance",
        "name_cn": "印尼经济财政发展研究所",
        "rss": GNEWS.format(domain="indef.or.id"),
        "icon": "https://indef.or.id/favicon.ico",
        "category": "印度尼西亚智库",
        "country": "印度尼西亚",
        "priority": 2,
        "description": "印尼经济与发展政策"
    },

    # 马来西亚智库
    {
        "name": "Institute of Strategic and International Studies Malaysia",
        "name_cn": "马来西亚战略与国际问题研究所",
        "rss": GNEWS.format(domain="isis.org.my"),
        "icon": "https://www.isis.org.my/favicon.ico",
        "category": "马来西亚智库",
        "country": "马来西亚",
        "priority": 2,
        "description": "马来西亚外交与经济政策"
    },

    # 泰国智库
    {
        "name": "Thailand Development Research Institute",
        "name_cn": "泰国发展研究所",
        "rss": GNEWS.format(domain="tdri.or.th"),
        "icon": "https://www.tdri.or.th/favicon.ico",
        "category": "泰国智库",
        "country": "泰国",
        "priority": 2,
        "description": "泰国经济与发展政策"
    },

    # 菲律宾智库
    {
        "name": "Stratbase ADR Institute",
        "name_cn": "Stratbase战略研究所",
        "rss": GNEWS.format(domain="stratbase.org"),
        "icon": "https://stratbase.org/favicon.ico",
        "category": "菲律宾智库",
        "country": "菲律宾",
        "priority": 2,
        "description": "菲律宾外交与安全政策"
    },

    # 越南智库
    {
        "name": "Diplomatic Academy of Vietnam",
        "name_cn": "越南外交学院",
        "rss": GNEWS.format(domain="dav.edu.vn"),
        "icon": "https://dav.edu.vn/favicon.ico",
        "category": "越南智库",
        "country": "越南",
        "priority": 2,
        "description": "越南外交与国际关系"
    },

    # 巴基斯坦智库
    {
        "name": "Institute of Strategic Studies Islamabad",
        "name_cn": "伊斯兰堡战略研究所",
        "rss": GNEWS.format(domain="issi.org.pk"),
        "icon": "https://issi.org.pk/favicon.ico",
        "category": "巴基斯坦智库",
        "country": "巴基斯坦",
        "priority": 2,
        "description": "巴基斯坦安全与外交"
    },

    # 伊朗智库
    {
        "name": "Institute for Iran-Eurasia Studies",
        "name_cn": "伊朗欧亚研究所",
        "rss": GNEWS.format(domain="irstudies.org"),
        "icon": "https://irstudies.org/favicon.ico",
        "category": "伊朗智库",
        "country": "伊朗",
        "priority": 2,
        "description": "伊朗地区与外交研究"
    },

    # 新加坡智库
    {
        "name": "ISEAS-Yusof Ishak Institute",
        "name_cn": "尤索夫伊萨东南亚研究院",
        "rss": GNEWS.format(domain="iseas.edu.sg"),
        "icon": "https://www.iseas.edu.sg/favicon.ico",
        "category": "新加坡智库",
        "country": "新加坡",
        "priority": 2,
        "description": "东南亚研究权威"
    },
    {
        "name": "S. Rajaratnam School of International Studies",
        "name_cn": "拉惹勒南国际研究院",
        "rss": GNEWS.format(domain="rsis.edu.sg"),
        "icon": "https://www.rsis.edu.sg/favicon.ico",
        "category": "新加坡智库",
        "country": "新加坡",
        "priority": 2,
        "description": "安全与战略研究"
    },
    {
        "name": "Lee Kuan Yew School of Public Policy",
        "name_cn": "李光耀公共政策学院",
        "rss": GNEWS.format(domain="lkyspp.nus.edu.sg"),
        "icon": "https://lkyspp.nus.edu.sg/favicon.ico",
        "category": "新加坡智库",
        "country": "新加坡",
        "priority": 2,
        "description": "亚洲公共政策与治理"
    },

    # ==================== 中东地区 ====================
    # 以色列智库
    {
        "name": "Institute for National Security Studies",
        "name_cn": "国家安全研究所",
        "rss": GNEWS.format(domain="inss.org.il"),
        "icon": "https://www.inss.org.il/favicon.ico",
        "category": "以色列智库",
        "country": "以色列",
        "priority": 2,
        "description": "以色列安全与战略研究"
    },
    {
        "name": "Begin-Sadat Center for Strategic Studies",
        "name_cn": "贝京-萨达特战略研究中心",
        "rss": GNEWS.format(domain="besacenter.org"),
        "icon": "https://besacenter.org/favicon.ico",
        "category": "以色列智库",
        "country": "以色列",
        "priority": 2,
        "description": "中东战略研究"
    },
    {
        "name": "Mitvim Institute",
        "name_cn": "Mitvim外交政策研究所",
        "rss": GNEWS.format(domain="mitvim.org.il"),
        "icon": "https://mitvim.org.il/favicon.ico",
        "category": "以色列智库",
        "country": "以色列",
        "priority": 2,
        "description": "以色列进步派外交政策"
    },

    # 沙特智库
    {
        "name": "King Faisal Center for Research and Islamic Studies",
        "name_cn": "费萨尔国王研究中心",
        "rss": GNEWS.format(domain="kfcris.com"),
        "icon": "https://kfcris.com/favicon.ico",
        "category": "沙特智库",
        "country": "沙特阿拉伯",
        "priority": 2,
        "description": "伊斯兰世界研究"
    },
    {
        "name": "King Abdullah Petroleum Studies and Research Center",
        "name_cn": "阿卜杜拉石油研究智库",
        "rss": GNEWS.format(domain="kapsarc.org"),
        "icon": "https://www.kapsarc.org/favicon.ico",
        "category": "沙特智库",
        "country": "沙特阿拉伯",
        "priority": 2,
        "description": "能源经济与气候政策"
    },

    # 阿联酋智库
    {
        "name": "Emirates Policy Center",
        "name_cn": "阿联酋政策中心",
        "rss": GNEWS.format(domain="epc.ae"),
        "icon": "https://epc.ae/favicon.ico",
        "category": "阿联酋智库",
        "country": "阿联酋",
        "priority": 2,
        "description": "中东政策研究"
    },
    {
        "name": "Emirates Center for Strategic Studies and Research",
        "name_cn": "阿联酋战略研究与中心",
        "rss": GNEWS.format(domain="ecssr.ae"),
        "icon": "https://ecssr.ae/favicon.ico",
        "category": "阿联酋智库",
        "country": "阿联酋",
        "priority": 2,
        "description": "海湾安全与战略研究"
    },
    {
        "name": "TRENDS Research and Advisory",
        "name_cn": "TRENDS研究与咨询",
        "rss": GNEWS.format(domain="trendsresearch.org"),
        "icon": "https://trendsresearch.org/favicon.ico",
        "category": "阿联酋智库",
        "country": "阿联酋",
        "priority": 2,
        "description": "中东地缘政治分析"
    },

    # 卡塔尔智库
    {
        "name": "Arab Center for Research and Policy Studies",
        "name_cn": "阿拉伯研究与政策研究中心",
        "rss": GNEWS.format(domain="dohainstitute.org"),
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
        "rss": GNEWS.format(domain="edam.org.tr"),
        "icon": "https://edam.org.tr/favicon.ico",
        "category": "土耳其智库",
        "country": "土耳其",
        "priority": 2,
        "description": "土耳其外交政策"
    },
    {
        "name": "Foundation for Political Economic and Social Research",
        "name_cn": "SETA基金会",
        "rss": GNEWS.format(domain="setav.org"),
        "icon": "https://www.setav.org/favicon.ico",
        "category": "土耳其智库",
        "country": "土耳其",
        "priority": 2,
        "description": "土耳其外交与安全研究"
    },

    # 埃及智库
    {
        "name": "Al-Ahram Center for Political and Strategic Studies",
        "name_cn": "金字塔政治与战略研究中心",
        "rss": GNEWS.format(domain="acpss.ahram.org.eg"),
        "icon": "http://www.ahram.org.eg/favicon.ico",
        "category": "埃及智库",
        "country": "埃及",
        "priority": 2,
        "description": "埃及与中东战略研究"
    },

    # ==================== 大洋洲地区 ====================
    # 澳大利亚智库
    {
        "name": "Lowy Institute",
        "name_cn": "罗伊研究所",
        "rss": GNEWS.format(domain="lowyinstitute.org"),
        "icon": "https://www.lowyinstitute.org/favicon.ico",
        "category": "澳大利亚智库",
        "country": "澳大利亚",
        "priority": 1,
        "description": "澳大利亚顶级智库"
    },
    {
        "name": "Australian Strategic Policy Institute",
        "name_cn": "澳大利亚战略政策研究所",
        "rss": GNEWS.format(domain="aspi.org.au"),
        "icon": "https://www.aspi.org.au/favicon.ico",
        "category": "澳大利亚智库",
        "country": "澳大利亚",
        "priority": 2,
        "description": "战略与防务研究"
    },
    {
        "name": "Grattan Institute",
        "name_cn": "格拉顿研究所",
        "rss": GNEWS.format(domain="grattan.edu.au"),
        "icon": "https://grattan.edu.au/favicon.ico",
        "category": "澳大利亚智库",
        "country": "澳大利亚",
        "priority": 2,
        "description": "公共政策研究"
    },
    {
        "name": "United States Studies Centre",
        "name_cn": "美国研究中心",
        "rss": GNEWS.format(domain="ussc.edu.au"),
        "icon": "https://www.ussc.edu.au/favicon.ico",
        "category": "澳大利亚智库",
        "country": "澳大利亚",
        "priority": 2,
        "description": "澳美关系与印太战略"
    },

    # 新西兰智库
    {
        "name": "New Zealand Institute of International Affairs",
        "name_cn": "新西兰国际事务研究所",
        "rss": GNEWS_SITE.format(domain="nziia.org.nz"),
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
        "rss": GNEWS.format(domain="fgv.br"),
        "icon": "https://portal.fgv.br/favicon.ico",
        "category": "巴西智库",
        "country": "巴西",
        "priority": 1,
        "description": "巴西经济与社会政策"
    },
    {
        "name": "Brazilian Center for International Relations",
        "name_cn": "巴西国际关系中心",
        "rss": GNEWS.format(domain="cebri.org"),
        "icon": "https://cebri.org/favicon.ico",
        "category": "巴西智库",
        "country": "巴西",
        "priority": 1,
        "description": "巴西外交政策"
    },
    {
        "name": "Institute of Applied Economic Research",
        "name_cn": "巴西应用经济研究所",
        "rss": GNEWS.format(domain="ipea.gov.br"),
        "icon": "https://www.ipea.gov.br/favicon.ico",
        "category": "巴西智库",
        "country": "巴西",
        "priority": 2,
        "description": "巴西宏观经济与公共政策"
    },
    {
        "name": "Alexandre de Gusmão Foundation",
        "name_cn": "亚历山大·古斯芒基金会",
        "rss": GNEWS.format(domain="funag.gov.br"),
        "icon": "https://funag.gov.br/favicon.ico",
        "category": "巴西智库",
        "country": "巴西",
        "priority": 2,
        "description": "巴西外交与国际关系"
    },

    # 阿根廷智库
    {
        "name": "Argentine Council for International Relations",
        "name_cn": "阿根廷国际关系委员会",
        "rss": GNEWS.format(domain="cari.org.ar"),
        "icon": "https://www.cari.org.ar/favicon.ico",
        "category": "阿根廷智库",
        "country": "阿根廷",
        "priority": 2,
        "description": "阿根廷国际关系研究"
    },
    {
        "name": "Centro de Estudios de Estado y Sociedad",
        "name_cn": "国家与社会研究中心",
        "rss": GNEWS.format(domain="cedes.org"),
        "icon": "https://www.cedes.org/favicon.ico",
        "category": "阿根廷智库",
        "country": "阿根廷",
        "priority": 2,
        "description": "阿根廷公共政策研究"
    },

    # 智利智库
    {
        "name": "Libertad y Desarrollo",
        "name_cn": "自由与发展研究所",
        "rss": GNEWS.format(domain="lyd.org"),
        "icon": "https://www.lyd.org/favicon.ico",
        "category": "智利智库",
        "country": "智利",
        "priority": 2,
        "description": "智利经济与社会政策"
    },
    {
        "name": "Centro de Estudios Publicos",
        "name_cn": "智利公共研究中心",
        "rss": GNEWS.format(domain="cepchile.cl"),
        "icon": "https://www.cepchile.cl/favicon.ico",
        "category": "智利智库",
        "country": "智利",
        "priority": 2,
        "description": "智利政治经济研究"
    },

    # 哥伦比亚智库
    {
        "name": "Fedesarrollo",
        "name_cn": "哥伦比亚发展基金会",
        "rss": GNEWS.format(domain="fedesarrollo.org.co"),
        "icon": "https://www.fedesarrollo.org.co/favicon.ico",
        "category": "哥伦比亚智库",
        "country": "哥伦比亚",
        "priority": 2,
        "description": "哥伦比亚经济与发展"
    },

    # 墨西哥智库
    {
        "name": "Mexican Council on Foreign Relations",
        "name_cn": "墨西哥外交关系委员会",
        "rss": GNEWS.format(domain="consejomexicano.org"),
        "icon": "https://www.consejomexicano.org/favicon.ico",
        "category": "墨西哥智库",
        "country": "墨西哥",
        "priority": 2,
        "description": "墨西哥外交政策"
    },
    {
        "name": "Mexican Institute for Competitiveness",
        "name_cn": "墨西哥竞争力研究所",
        "rss": GNEWS.format(domain="imco.org.mx"),
        "icon": "https://imco.org.mx/favicon.ico",
        "category": "墨西哥智库",
        "country": "墨西哥",
        "priority": 2,
        "description": "墨西哥经济改革与治理"
    },

    # ==================== 非洲地区 ====================
    # 南非智库
    {
        "name": "South African Institute of International Affairs",
        "name_cn": "南非国际事务研究所",
        "rss": GNEWS.format(domain="saiia.org.za"),
        "icon": "https://saiia.org.za/favicon.ico",
        "category": "南非智库",
        "country": "南非",
        "priority": 2,
        "description": "非洲国际关系研究"
    },
    {
        "name": "Institute for Security Studies",
        "name_cn": "安全研究所",
        "rss": GNEWS.format(domain="issafrica.org"),
        "icon": "https://issafrica.org/favicon.ico",
        "category": "南非智库",
        "country": "南非",
        "priority": 2,
        "description": "非洲安全研究"
    },

    # 尼日利亚智库
    {
        "name": "Nigerian Institute of International Affairs",
        "name_cn": "尼日利亚国际事务研究所",
        "rss": GNEWS_SITE.format(domain="niia.gov.ng"),
        "icon": "https://niia.gov.ng/favicon.ico",
        "category": "尼日利亚智库",
        "country": "尼日利亚",
        "priority": 2,
        "description": "尼日利亚外交政策"
    },

    # 肯尼亚智库
    {
        "name": "Kenya Institute for Public Policy Research and Analysis",
        "name_cn": "肯尼亚公共政策研究与分析研究所",
        "rss": GNEWS.format(domain="kippra.or.ke"),
        "icon": "https://www.kippra.or.ke/favicon.ico",
        "category": "肯尼亚智库",
        "country": "肯尼亚",
        "priority": 1,
        "description": "肯尼亚国家级政策智库"
    },
    {
        "name": "Institute of Economic Affairs Kenya",
        "name_cn": "肯尼亚经济事务研究所",
        "rss": GNEWS.format(domain="ieakenya.or.ke"),
        "icon": "https://www.ieakenya.or.ke/favicon.ico",
        "category": "肯尼亚智库",
        "country": "肯尼亚",
        "priority": 2,
        "description": "肯尼亚经济改革与治理研究"
    },
    {
        "name": "Partnership for African Social and Governance Research",
        "name_cn": "非洲社会治理研究伙伴组织",
        "rss": GNEWS.format(domain="pasgr.org"),
        "icon": "https://www.pasgr.org/favicon.ico",
        "category": "肯尼亚智库",
        "country": "肯尼亚",
        "priority": 2,
        "description": "非洲公共政策与社会研究"
    },

    # ==================== 国际组织 & 多边机构 ====================
    {
        "name": "International Crisis Group",
        "name_cn": "国际危机组织",
        "rss": GNEWS.format(domain="crisisgroup.org"),
        "icon": "https://www.crisisgroup.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "冲突预防与解决"
    },
    {
        "name": "International Committee of the Red Cross",
        "name_cn": "红十字国际委员会",
        "rss": GNEWS.format(domain="icrc.org"),
        "icon": "https://www.icrc.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "国际人道主义与冲突地区研究"
    },
    {
        "name": "Amnesty International",
        "name_cn": "大赦国际",
        "rss": GNEWS.format(domain="amnesty.org"),
        "icon": "https://www.amnesty.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "人权研究与倡导"
    },
    {
        "name": "Human Rights Watch",
        "name_cn": "人权观察",
        "rss": GNEWS.format(domain="hrw.org"),
        "icon": "https://www.hrw.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "全球人权调查与报告"
    },
    {
        "name": "United Nations University",
        "name_cn": "联合国大学",
        "rss": GNEWS.format(domain="unu.edu"),
        "icon": "https://unu.edu/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 2,
        "description": "全球治理与发展研究"
    },
    {
        "name": "OECD",
        "name_cn": "经合组织",
        "rss": GNEWS.format(domain="oecd.org"),
        "icon": "https://www.oecd.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 2,
        "description": "国际经济政策与合作"
    },
    {
        "name": "European Council on Foreign Relations",
        "name_cn": "欧洲对外关系委员会",
        "rss": "https://ecfr.eu/feed/",
        "icon": "https://ecfr.eu/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "欧洲外交政策与全球秩序"
    },
    {
        "name": "World Bank",
        "name_cn": "世界银行",
        "rss": GNEWS.format(domain="worldbank.org"),
        "icon": "https://www.worldbank.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "全球发展与经济研究"
    },
    {
        "name": "International Monetary Fund",
        "name_cn": "国际货币基金组织",
        "rss": GNEWS.format(domain="imf.org"),
        "icon": "https://www.imf.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "全球经济与金融政策"
    },
    {
        "name": "United Nations Development Programme",
        "name_cn": "联合国开发计划署",
        "rss": GNEWS.format(domain="undp.org"),
        "icon": "https://www.undp.org/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "全球可持续发展"
    },
    {
        "name": "NATO",
        "name_cn": "北约",
        "rss": GNEWS.format(domain="nato.int"),
        "icon": "https://www.nato.int/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 1,
        "description": "跨大西洋安全与防务"
    },
    {
        "name": "Carnegie Europe",
        "name_cn": "卡内基欧洲中心",
        "rss": GNEWS.format(domain="carnegieeurope.eu"),
        "icon": "https://carnegieeurope.eu/favicon.ico",
        "category": "国际组织",
        "country": "国际",
        "priority": 2,
        "description": "欧洲外交与全球民主"
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
        "rss": GNEWS_US.format(domain="piie.com"),
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
    # ==================== 补强：科技、安全与新兴力量 ====================
    {
        "name": "Vivekananda International Foundation",
        "name_cn": "维韦卡南达国际基金会",
        "rss": GNEWS.format(domain="vifindia.org"),
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


SOURCE_TYPE_LABELS = {
    'think_tank': '智库',
    'international': '国际组织',
    'media': '认知媒体',
    'journal': '学术期刊',
    'policy': '经济政策',
}


def get_source_type(category):
    """将配置中的 category 映射为来源类型（与国家级智库标签解耦）。"""
    if category == '国际组织':
        return 'international'
    if category == '认知网站':
        return 'media'
    if category == '学术期刊':
        return 'journal'
    if category == '经济政策':
        return 'policy'
    return 'think_tank'


def get_source_type_label(category):
    return SOURCE_TYPE_LABELS[get_source_type(category)]


# 按类别统计
def get_category_stats():
    stats = {}
    for tank in THINK_TANKS_CONFIG:
        category = tank.get('category', '其他')
        if category not in stats:
            stats[category] = 0
        stats[category] += 1
    return stats
