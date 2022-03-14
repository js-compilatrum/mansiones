import datetime
import time
from typing import Union

import feedparser

TEST_RSS_URL = "http://feeds.bbci.co.uk/news/rss.xml"
TEST_RSS_DATA = """
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet title="XSL_formatting" type="text/xsl" href="/shared/bsp/xsl/rss/nolsol.xsl"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0" xmlns:media="http://search.yahoo.com/mrss/">
    <channel>
        <title><![CDATA[BBC News - Home]]></title>
        <description><![CDATA[BBC News - Home]]></description>
        <link>https://www.bbc.co.uk/news/</link>
        <image>
            <url>https://news.bbcimg.co.uk/nol/shared/img/bbc_news_120x60.gif</url>
            <title>BBC News - Home</title>
            <link>https://www.bbc.co.uk/news/</link>
        </image>
        <generator>RSS for Node</generator>
        <lastBuildDate>Sat, 12 Mar 2022 20:32:17 GMT</lastBuildDate>
        <copyright><![CDATA[Copyright: (C) British Broadcasting Corporation, see http://news.bbc.co.uk/2/hi/help/rss/4498287.stm for terms and conditions of reuse.]]></copyright>
        <language><![CDATA[en-gb]]></language>
        <ttl>15</ttl>
        <item>
            <title><![CDATA[Ukraine war: Protests after Russians 'abduct' Melitopol mayor]]></title>
            <description><![CDATA[The president accuses the Russians of "moving to a new stage of terror" as Melitopol residents protest.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60719123?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60719123</guid>
            <pubDate>Sat, 12 Mar 2022 09:45:51 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Roman Abramovich: Premier League disqualifies Chelsea owner as director of club]]></title>
            <description><![CDATA[The Premier League disqualifies Chelsea owner Roman Abramovich as a director of the club and sleeve sponsor Hyundai suspend deal with the European champions.]]></description>
            <link>https://www.bbc.co.uk/sport/football/60720343?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/sport/football/60720343</guid>
            <pubDate>Sat, 12 Mar 2022 18:39:10 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ukraine invasion: Javid says Russia will pay for war crimes as UK sends aid]]></title>
            <description><![CDATA[The UK says it is sending more medical aid to Ukraine after 25 attacks on health centres.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60719152?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60719152</guid>
            <pubDate>Sat, 12 Mar 2022 12:11:30 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ukraine war: Evacuations 'extremely difficult' amid shelling]]></title>
            <description><![CDATA[New attempts are under way to get civilians out of bombed Ukrainian cities as Russia's attack intensifies.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60721323?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60721323</guid>
            <pubDate>Sat, 12 Mar 2022 17:55:59 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ukraine war: Pictures of war intensifying in third week]]></title>
            <description><![CDATA[Images from Russia's invasion of Ukraine show a conflict turning deadlier nearly three weeks on.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60720169?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60720169</guid>
            <pubDate>Sat, 12 Mar 2022 12:15:39 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Sarah Everard: Protesters demand 'radical change' to Met Police]]></title>
            <description><![CDATA[Protesters demand change a year since clashes with police at an unauthorised vigil for Sarah Everard,]]></description>
            <link>https://www.bbc.co.uk/news/uk-england-london-60720907?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-england-london-60720907</guid>
            <pubDate>Sat, 12 Mar 2022 19:45:48 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Saudi Arabia executes 81 men in one day]]></title>
            <description><![CDATA[The range of charges on which the men were convicted included terrorism and holding "deviant beliefs".]]></description>
            <link>https://www.bbc.co.uk/news/world-middle-east-60722057?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-middle-east-60722057</guid>
            <pubDate>Sat, 12 Mar 2022 15:17:09 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Six Nations: Ireland see off brave 14-man England]]></title>
            <description><![CDATA[Ireland keep their hopes of a Six Nations title alive as they finally see off a valiant, spirited England.]]></description>
            <link>https://www.bbc.co.uk/sport/rugby-union/60722384?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/sport/rugby-union/60722384</guid>
            <pubDate>Sat, 12 Mar 2022 19:12:28 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Brexit: Micheál Martin and Boris Johnson discuss NI Protocol]]></title>
            <description><![CDATA[Micheál Martin and Boris Johnson met prior to attending the Ireland-England rugby match on Saturday.]]></description>
            <link>https://www.bbc.co.uk/news/uk-northern-ireland-60723231?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-northern-ireland-60723231</guid>
            <pubDate>Sat, 12 Mar 2022 18:23:07 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Body of missing hillwalker found in Glen Coe]]></title>
            <description><![CDATA[Neil Gillingham, from Kilmarnock, went missing on a walk with his dog last Sunday on Stob Coire Sgreamhach.]]></description>
            <link>https://www.bbc.co.uk/news/uk-scotland-north-east-orkney-shetland-60722612?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-scotland-north-east-orkney-shetland-60722612</guid>
            <pubDate>Sat, 12 Mar 2022 16:05:38 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Cost of living: Energy bills to rise 14 times faster than wages, says TUC]]></title>
            <description><![CDATA[An analysis by the Trades Union Congress suggests bills will rise 14 times faster than pay this year.]]></description>
            <link>https://www.bbc.co.uk/news/uk-60719158?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-60719158</guid>
            <pubDate>Sat, 12 Mar 2022 10:53:30 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ben Nevis climbing victim was father-to-be]]></title>
            <description><![CDATA[Samuel Crawford, 28, was "one of the brightest lights in our congregation" says his family minister.]]></description>
            <link>https://www.bbc.co.uk/news/uk-northern-ireland-60719333?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-northern-ireland-60719333</guid>
            <pubDate>Sat, 12 Mar 2022 13:38:12 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Manchester United 3-2 Tottenham Hotspur: Cristiano Ronaldo scores hat-trick in thriller]]></title>
            <description><![CDATA[Cristiano Ronaldo scores a hat-trick as Manchester United beat Tottenham to move into the Champions League places.]]></description>
            <link>https://www.bbc.co.uk/sport/football/60628394?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/sport/football/60628394</guid>
            <pubDate>Sat, 12 Mar 2022 20:11:51 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Under threat of Russian bombs, Lviv hides away its priceless heritage]]></title>
            <description><![CDATA[The picturesque western city of Lviv is racing to protect is cultural and religious artefacts.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60707531?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60707531</guid>
            <pubDate>Sat, 12 Mar 2022 00:25:31 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ukraine maps: At-a-glance guide to the Russia war]]></title>
            <description><![CDATA[Russian troops have expanded their offensive as they continue attempts to cut off the capital Kyiv.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60506682?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60506682</guid>
            <pubDate>Sat, 12 Mar 2022 17:28:30 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[War in Ukraine: How Russia is recruiting mercenaries]]></title>
            <description><![CDATA[Social media channels and private messaging groups are being used to recruit, the BBC has learned.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60711211?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60711211</guid>
            <pubDate>Sat, 12 Mar 2022 00:32:16 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ukraine: What are chemical weapons and could Russia use them?]]></title>
            <description><![CDATA[There are fears Russia could use non-conventional weapons and, in so doing, cross a major red line.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60708350?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60708350</guid>
            <pubDate>Fri, 11 Mar 2022 22:00:02 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Jeremy Bowen: Ukraine's capital becomes fortress]]></title>
            <description><![CDATA[As Russian forces continue their slow advance, Kyiv's residents fear the worst for their city.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60714515?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60714515</guid>
            <pubDate>Fri, 11 Mar 2022 20:04:59 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ukraine war: Fact-checking Russia's biological weapons claims]]></title>
            <description><![CDATA[The BBC finds no evidence for Russian claims that Ukraine is developing biological weapons with US support.]]></description>
            <link>https://www.bbc.co.uk/news/60711705?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/60711705</guid>
            <pubDate>Fri, 11 Mar 2022 19:03:49 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Battle for Mykolaiv: 'We are winning this fight, but not this war']]></title>
            <description><![CDATA[In the southern city of Mykolaiv, Ukrainian forces are battling to stop the Russian advance.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60711659?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60711659</guid>
            <pubDate>Fri, 11 Mar 2022 19:21:01 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[What sanctions are being imposed on Russia over Ukraine invasion?]]></title>
            <description><![CDATA[Western nations have imposed severe sanctions on Russia over its invasion of Ukraine.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60125659?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60125659</guid>
            <pubDate>Fri, 11 Mar 2022 15:12:07 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Will Nato get involved if dirty bombs are used in Ukraine? And other questions]]></title>
            <description><![CDATA[BBC correspondents Lyse Doucet and Jenny Hill answer readers' questions on Ukraine]]></description>
            <link>https://www.bbc.co.uk/news/world-60711951?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-60711951</guid>
            <pubDate>Fri, 11 Mar 2022 16:00:22 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[WATCH: Disposal experts defuse unexploded bomb in Ukraine]]></title>
            <description><![CDATA[An unexploded 500kg (1102lb) bomb was discovered in Chernihiv in northern Ukraine.]]></description>
            <link>https://www.bbc.co.uk/news/world-europe-60689562?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-europe-60689562</guid>
            <pubDate>Thu, 10 Mar 2022 09:12:48 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Intimate image abuse: His confession protected him]]></title>
            <description><![CDATA[Georgie received an anonymous tip-off on Facebook that intimate photos of her were being shared online.]]></description>
            <link>https://www.bbc.co.uk/news/uk-politics-60693849?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-politics-60693849</guid>
            <pubDate>Sat, 12 Mar 2022 00:00:50 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Watch: Otters in Singapore cross road with police escort]]></title>
            <description><![CDATA[Why did the otters cross the road? They were outside Singapore's presidential palace, so that may be a clue.]]></description>
            <link>https://www.bbc.co.uk/news/world-asia-60720259?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-asia-60720259</guid>
            <pubDate>Sat, 12 Mar 2022 10:38:48 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Console 'scalper' on stockpiling PlayStations for profit]]></title>
            <description><![CDATA[Omar Mehtab spoke to a 'scalper;' a person who stockpiles popular products and resells them for profit.]]></description>
            <link>https://www.bbc.co.uk/news/technology-60719023?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/technology-60719023</guid>
            <pubDate>Sat, 12 Mar 2022 09:21:11 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Rod Stewart fixes potholes near his Harlow home]]></title>
            <description><![CDATA[The singer shovels gravel on the road and claims his Ferrari cannot get through the potholes.]]></description>
            <link>https://www.bbc.co.uk/news/uk-england-essex-60722727?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-england-essex-60722727</guid>
            <pubDate>Sat, 12 Mar 2022 17:49:34 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[The friends who explore abandoned buildings]]></title>
            <description><![CDATA[Alex, Alistair and Theo are among a community of "urban explorers" who document the history of decaying structures.]]></description>
            <link>https://www.bbc.co.uk/news/uk-scotland-60700824?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-scotland-60700824</guid>
            <pubDate>Sat, 12 Mar 2022 10:21:13 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Transplant mum reunited with sons after six months in Papworth]]></title>
            <description><![CDATA[Her heart surgeon describes 48-year-old Nicola Sharpe's survival as "against all the odds".]]></description>
            <link>https://www.bbc.co.uk/news/uk-england-cambridgeshire-60707013?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-england-cambridgeshire-60707013</guid>
            <pubDate>Fri, 11 Mar 2022 12:42:28 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Boy, 11, walks from Northern Ireland to Old Trafford for charity]]></title>
            <description><![CDATA[Ben Dickinson's walk from Northern Ireland to fund 75,000 meals was inspired by Marcus Rashford.]]></description>
            <link>https://www.bbc.co.uk/news/uk-england-manchester-60721987?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-england-manchester-60721987</guid>
            <pubDate>Sat, 12 Mar 2022 15:13:13 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[‘This world is crazy but music helps me survive’]]></title>
            <description><![CDATA[A musician asylum seeker from Iran is reunited with his instrument in Northern Ireland.]]></description>
            <link>https://www.bbc.co.uk/news/uk-northern-ireland-60601085?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-northern-ireland-60601085</guid>
            <pubDate>Sat, 12 Mar 2022 06:33:30 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Week in pictures: 5-11 March 2022]]></title>
            <description><![CDATA[A selection of powerful images from all over the globe, taken in the past seven days.]]></description>
            <link>https://www.bbc.co.uk/news/in-pictures-60699864?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/in-pictures-60699864</guid>
            <pubDate>Sat, 12 Mar 2022 00:10:45 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Martin Compston: Plucked to stardom from a school corridor]]></title>
            <description><![CDATA[The Scot made his acting debut in Ken Loach's gritty drama Sweet Sixteen, released 20 years ago.]]></description>
            <link>https://www.bbc.co.uk/news/uk-scotland-60707536?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-scotland-60707536</guid>
            <pubDate>Sat, 12 Mar 2022 10:20:56 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ukraine: Spam website set up to reach millions of Russians]]></title>
            <description><![CDATA[A Norwegian computer expert has made a system for volunteers to email millions of Russian people about the war]]></description>
            <link>https://www.bbc.co.uk/news/technology-60697261?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/technology-60697261</guid>
            <pubDate>Sat, 12 Mar 2022 00:35:07 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[More to be done to make gymnastics safer - whistleblower]]></title>
            <description><![CDATA[Former gymnast Rachael Denhollander tells the BBC there is still work to be done to make the sport safer for children.]]></description>
            <link>https://www.bbc.co.uk/sport/gymnastics/60684784?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/sport/gymnastics/60684784</guid>
            <pubDate>Sat, 12 Mar 2022 17:45:46 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Farming Wales: The farmer making vodka from sheep milk]]></title>
            <description><![CDATA[Bryn Perry, from Pembrokeshire, recycles leftover whey from his cheese-making to produce the spirit.]]></description>
            <link>https://www.bbc.co.uk/news/uk-wales-60692167?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-wales-60692167</guid>
            <pubDate>Sat, 12 Mar 2022 07:08:04 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[The race is on for affordable energy for the UK's homes and businesses]]></title>
            <description><![CDATA[War in Ukraine has focused minds on how to get enough affordable energy for homes and businesses.]]></description>
            <link>https://www.bbc.co.uk/news/uk-politics-60712673?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/uk-politics-60712673</guid>
            <pubDate>Sat, 12 Mar 2022 00:19:48 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Australia floods: 'I'm angry it's happening again']]></title>
            <description><![CDATA[Australians are reeling from one of their worst natural disasters, but many despair at a sense of déjà vu.]]></description>
            <link>https://www.bbc.co.uk/news/world-australia-60686223?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/world-australia-60686223</guid>
            <pubDate>Fri, 11 Mar 2022 16:57:06 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Ukraine: How China is censoring online discussion of the war]]></title>
            <description><![CDATA[The authorities are struggling to keep a lid on pro- and anti-Russian views being discussed online.]]></description>
            <link>https://www.bbc.co.uk/news/60684682?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/news/60684682</guid>
            <pubDate>Sat, 12 Mar 2022 00:14:55 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA['Salah must decide if he wants icon status - or money' - will Liverpool forward stay at Anfield?]]></title>
            <description><![CDATA[Mohamed Salah scores as Liverpool beat Brighton at the end of a week in which speculation around his future at the club continued.]]></description>
            <link>https://www.bbc.co.uk/sport/football/60722135?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/sport/football/60722135</guid>
            <pubDate>Sat, 12 Mar 2022 18:48:17 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Scotland bounce back with disjointed win in Italy - highlights & report]]></title>
            <description><![CDATA[Scotland recover from successive Six Nations defeats by overcoming Italy with a disjointed bonus-point victory in Rome.]]></description>
            <link>https://www.bbc.co.uk/sport/rugby-union/60723050?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/sport/rugby-union/60723050</guid>
            <pubDate>Sat, 12 Mar 2022 16:32:49 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Six Nations: Scotland's Chris Harris scores brilliant length-of-the-field try against Italy]]></title>
            <description><![CDATA[Scotland's Chris Harris finishes off a brilliant try against Italy with help from team-mates Ali Price and Kyle Steyn in the Six Nations.]]></description>
            <link>https://www.bbc.co.uk/sport/av/rugby-union/60722768?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/sport/av/rugby-union/60722768</guid>
            <pubDate>Sat, 12 Mar 2022 16:39:44 GMT</pubDate>
        </item>
        <item>
            <title><![CDATA[Man Utd 3-2 Tottenham: Ralf Rangnick says that Cristiano Ronaldo had his best performance of his reign]]></title>
            <description><![CDATA[Manchester United manager Ralf Rangnick says Ronaldo's hat-trick performance in his side's 3-2 win over Tottenham was the best of his reign.]]></description>
            <link>https://www.bbc.co.uk/sport/av/rugby-union/60724348?at_medium=RSS&amp;at_campaign=KARANGA</link>
            <guid isPermaLink="false">https://www.bbc.co.uk/sport/av/rugby-union/60724348</guid>
            <pubDate>Sat, 12 Mar 2022 20:20:41 GMT</pubDate>
        </item>
    </channel>
</rss>"""


def show_rss():
    """
    only for testing to check how feedparser really works
    :return:
    """
    d = feedparser.parse(TEST_RSS_DATA)
    print(d['feed']['title'])
    print(d.keys())
    print(d['entries'][0])
    print(d)


NO_ARTICLE_RESULTS = {'source': '', 'url': '', 'articles': {}}


class Mansiones:
    """
    Preparing article titles for NLP in easu way from RSS with python only

    """

    def __init__(self, fresh_article_has_hours=6):
        self.default_hours_back = fresh_article_has_hours

    def parse_rss_str(self, fetched_data: str) -> dict:
        """
        Get formated data from fetched result. Feedparser is based on defualt urllib and to speed up for async
        downloading I prefer fetch first RSS str from net with asyncio and after that further processing it.

        :param fetched_data: str with fetched RSS result. If it will be provided as link it will be fetch here!
        :return: channel data to use in other context offline
        """

        try:
            data = feedparser.parse(fetched_data)
        except Exception as e:
            print(f'Parsing error inside Feedparse: {e}')
            return NO_ARTICLE_RESULTS

        if data['feed'] == {} and data['entries'] == []:
            return NO_ARTICLE_RESULTS

        feed = data['feed']
        return {'source': feed['title'],
                'url': feed['link'],
                'articles': {art['title']: art['link'] for art in data['entries']
                             if self.is_date_in_range(art['published_parsed'])
                             }
                }

    def is_date_in_range(self, checked_date: time.struct_time):
        """
        To avoid too much text to analysis only latest article title is used
        :param checked_date:
        :return:
        """
        art_date = checked_date
        parsed_date = datetime.datetime(art_date.tm_year, art_date.tm_mon, art_date.tm_mday, art_date.tm_hour,
                                        art_date.tm_min, art_date.tm_sec)
        today = datetime.datetime.today()
        date_offset = datetime.timedelta(hours=self.default_hours_back)
        return today - date_offset <= parsed_date <= today + date_offset

    def prepare_articles_titles_as_txt(self, articles_to_show: Union[list[dict], dict]) -> str:
        """
        For NLP analysis is better generate all articles as text. At this stage is raw text without preparing for
        analysing. I think is better here will be more elastic instead one format as it can depend on source on
        the future.

        :param articles_to_show: list of title of dict with titles as keys
        :return: raw article titles
        """

        if 'articles' in articles_to_show:
            article_data = articles_to_show['articles']
        else:
            article_data = articles_to_show

        return ' '.join(list(article_data.keys()))


if __name__ == '__main__':
    show_rss()
    # hack for testing as RSS sample is dated 2022/12/3
    passed_hours = (datetime.datetime.now() - datetime.datetime(2022, 3, 12, 1, 1, 1, 1)).days * 24
    mansiones = Mansiones(fresh_article_has_hours=passed_hours)
    arts = mansiones.parse_rss_str(TEST_RSS_DATA)
    print(mansiones.prepare_articles_titles_as_txt(arts))
