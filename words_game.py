import random

unit1 = [
    [],
    []
]
unit2 = [
    [],
    []
]
unit3 = [
    [],
    []
]
unit4 = [
    [],
    []
]
unit5 = [
    [],
    []
]
unit6 = [
    [],
    []
]
unit7 = [
    [],
    []
]
unit8 = [
    [],
    []
]
unit9 = [
    [],
    []
]
unit10 = [
    [],
    []
]
unit11 = [
    [],
    []
]
unit12 = [
    [],
    []
]
unit13 = [
    ['胡须','淡黄色的','墨镜','制服','胡子','鞋跟','衣服袖子','面部的','表情','联系','链条','飞机','紧急情况','祈祷','有天赋的','精确地','起草','描述','学术的','预言','值得','失败','错误的','协会','因此','可能性','残疾','完全地','复活节','大使馆','控告','闪电','个性','职员','售票员','屠夫','喜爱运动的','独立的','整洁的','自私的','敏锐的','特点','渴望','满意','收获','生物学','菠萝','桃子','和善','要求','航空公司','在船上','潮湿的','助手','独立','诗人','翻译员','家庭教师','眼泪','脸颊','拥抱','不安的','错误','雷声','羊毛','松树','种子','松鼠','麻雀','流血','破的','减轻','躲避','学者','长凳','家庭主妇','邮政编码','天文学','过敏的','忧虑','复习','口头的','稻草','怒视','部分','喜爱文学的','瞥一眼','蒸汽','证实','图书馆管理员','文件','叹息','感激的','有罪的','相像的','缺点','账户','纽扣','鹦鹉','笼子','评判','部分时间地','爪子','酸奶','蜂蜜','咀嚼','卫星','皱纹','额头','大厦','大腿部','专心致志于','含盐的','胡萝卜','豌豆','同伴','奉献','永远'],
    ['beard','blond','sunglasses','uniform','moustache','heel','sleeve','facial','expression','connection','chain','aircraft','emergency','pray','gifted','accurately','draw up','description','academic','predict','deserve','failure','mistaken','association','thus','possibility','disability','entirely','Easter','embassy','accuse','lighting','personality','clerk','conductor','butcher','athletic','independent','neat','selfish','sharp','characteristic','desire','satisfaction','harvest','biology','pineapple','peach','kindness','requirement','airline','aboard','damp','assistant','independence','poet','translator','tutor','tear','cheek','hug','upset','fault','thunder','wool','pine','seed','squirrel','sparrow','bleed','broken','relief','shelter','scholar','bench','housewife','postcode','astronomy','allergic','anxiety','revision','oral','straw','glare','section','literary','glance','steam','confirm','librarian','file','sign','grateful','guilty','alike','shortcoming','account','button','parrot','cage','judge','part-time','claw','yoghurt','honey','chew','satellite','wrinkle','forehead','block','lap','devote','salty','carrot','pea','companion','devotion','forever']
]
unit14 = [
    ['木匠','化学家','接待员','营业员','打字员','保险','津贴','学费','收入','奖赏','工资','收费','总结','指导','段落','时间表','机构','援助','泵','资料','鹿','负责','接管','话题','收据','错误','液体','理解','咨询','图表','随意的','吵架','细谈','大声说出','坐直','托儿所','衣领','约会','童年','打字机','片刻','战斗','民间的','品德','基础','玉米','牛','霜冻','附近的','陡峭的','谷物','嘴唇','泥浆','智慧','习语','低级的','初中','宇宙','信任','人类','鸟窝','羽毛','反转','克服','理解','审查','违法的','取得成功','投入','尽责的','存在','荣耀的事','不断地','在底下','弯腰','舞台','犹豫','腕','旋转','判断力','跟上','减少','大量增加','分割','分支','运转','精力充沛的','回答','灵活的','羡慕','打扰','大陆','以防万一','舒适','奴隶','激增','恐慌','算术','随信附上','简历','由于','此外','资格'],
    ['carpenter','chemist','receptionist','shop assistant','typist','insurance','bonus','fee','income','reward','wage','charge','summaray','guidance','paragraph','timetable','institute','aid','pump','data','deer','charge','take charge of','topic','receipt','error','liquid','comprehension','consult','chart','casual','quarrel','go into details','speak up','sit up','nursery','collar','appointment','childhood','typewriter','instant','battle','civil','moral','basis','corn','cattle','frost','surrounding','steep','grain','lip','mud','wisdom','idiom','junior','junior high','universe','believe in','mankind','nest','feather','turn over','overcome','grasp','inspect','illegal','pay off','commit','committed','existence','glory','constantly','beneath','bend','stage','hesitate','wrist','twist','judgemnet','keep up with','decrease','multiply','division','branch','operate','dynamic','respond','flexible','envy','bother','continent','in case','comfort','slave','boom','panic','arithmetic','enclose','curriculum vitae','due to','in addition','qualification']
]
unit15 = [
    ['箭','氧气','打勾','公牛','拼写','由后向前地','改正','简化','罐子','稳定的','坦率地','解雇','空白的','被充满','怀疑','块','喉咙','现状','最高级别的','谚语','邮费','航空邮政','使用者','指导','除···之外','埋葬','字母表','辨别','练习','格言','保守的','任务','非传统的','惩罚','名誉','少量的','不严谨的','品行不端','遵守','温和的','接收者','速度','杰出的','反映','挑选','在某种程度上','误解','角','三角形','原子','倒','火药','火焰','使爆炸','缺乏','吐口水','拉','酸','洋葱','我们的','权利','值得努力的','间谍','胶水','同伴','同学','获得','习惯于','思考','职衔','官僚的','值得的','宗教','保卫','倾向于','忽视','不情愿的','假设','赞成','强烈要求','启发','影子','传统的','王国','文明','极其重要的','有益的','景象','假设','使适应','总的来说','设备','欣赏','生物化学','合唱团'],
    ['arrow','oxygen','tick','ox','spelling','backwards','correction','simplify','jar','secure','frankly','lay off','blank','swell','suspect','lump','throat','status','chief','saying','postage','airmail','user','instruct','aside from','bury','alphabet','distinguish','drill','motto','conservative','assignment','alternative','punishment','reputation','slight','loose','loose conduct','obey','mild','receiver','pace','outstanding','reflect','select','to a certain extent','misunderstand','angle','triangle','atom','pour','powder','flame','set off','lack','spit','drag','acid','onion','ours','access','worthwhile','spy','glue','fellow','fellow students','acquire','be accustomed to','thinking','rank','bureaucratic','worthy','religion','defence','tend to','ignore','unwilling','assumption','approve','urge','inspire','shadow','conventional','kingdom','civilisation','vital','beneficial','image','assume','adapt','as a whole','facility','appreciation','biochemistry','choir']
]
print(len(unit15[0]))
print(len(unit15[1]))
unit16 = [
    [],
    []
]
unit17 = [
    [],
    []
]
unit18 = [
    [],
    []
]
unit19 = [
    [],
    []
]
unit20 = [
    [],
    []
]
unit21 = [
    [],
    []
]
unit22 = [
    [],
    []
]
unit23 = [
    [],
    []
]
unit24 = [
    [],
    []
]

all_wards = [unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,unit11,unit12,unit13,unit14,unit15,unit16,unit17,unit18,unit19,unit20,unit21,unit22,unit23,unit24]

print('此程序运用进行 BS 版高中英语单词练习，相关功能如下：∠ (ᐛ 」∠ )')
print('----------------------')
print('·输入 1 进行英语拼写练习')
print()
print('·输入 2 进行单词翻译练习')
print()
print('·单走一个 6 即可查看单词表')
print('----------------------')
print('PS:任意过程输入 q 可立即结束此程序')
print('----------------------')
choice = input('_(:з」∠ )_ 请选择：')

if choice == '1' :
    unit = input('请输入某一单元相应的阿拉伯数字序号：')
    unit = int(unit) - 1
    que = all_wards[unit][0]
    ans = all_wards[unit][1]
    passed_words = []
    judge = 0
    times = -1
    while True:
        length = int(len(que))
        index_list = [i for i in range(len(que))]
        times += 1
        if length > 0 :
            if times > 0:
                if judge % 2 == 0:
                    random.shuffle(index_list)
                    index = index_list[0]
            else:
                random.shuffle(index_list)
                index = index_list[0]
            judge = 2
            print('----------------------')
            print('当前词库单词剩余数：' + str(len(que)))
            print('----------------------')
            print('Please spell:' + que[index])
            answer = input('请拼写：')
            if answer == ans[index]:
                print('Great!' + '∠ (ᐛ 」∠ )')
                que.pop(index)
                ans.pop(index)
                judge += 2
                continue
            elif answer == 'pass':
                print('·answer : '+ ans[index]+ ' ∠ (ᐛ 」∠ )')
                word = [que[index],ans[index]]
                passed_words.append(word)
                que.pop(index)
                ans.pop(index)
                continue
            elif answer == 'q':
                if int(len(passed_words)) == 0:
                    break
                else:
                    print('(¦3[▓▓]')
                    print('已自动结束运行，此次 pass 单词如下：')
                    for word in passed_words:
                        print(word)
                    print('----------------------')
                    print('共计 ' + str(len(passed_words)) + ' 个单词')
                    break
            else:
                judge += 1
                print('Error!')
                print('现在你可以继续回答，也可以输入 pass 查看答案后回答下一个')
                continue
        else:
            print('----------------------')
            print('当前词库单词剩余数：' + str(len(que)))
            print('----------------------')
            if int(len(passed_words)) == 0:
                print('已自动结束运行')
                break
            else:
                print('(¦3[▓▓]')
                print('已自动结束运行，此次 pass 单词如下：')
                for word in passed_words:
                    print(word)
                print('----------------------')
                print('共计 ' + str(len(passed_words)) + ' 个单词')
                break
elif choice == '2' :
    unit = input('请输入某一单元相应的阿拉伯数字序号：')
    unit = int(unit) - 1
    que = all_wards[unit][1]
    ans = all_wards[unit][0]
    passed_words = []
    judge = 0
    times = -1
    while True:
        length = int(len(que))
        index_list = [i for i in range(len(que))]
        times += 1
        if length > 0 :
            if times > 0:
                if judge % 2 == 0:
                    random.shuffle(index_list)
                    index = index_list[0]
            else:
                random.shuffle(index_list)
                index = index_list[0]
            judge = 2
            print('----------------------')
            print('当前词库单词剩余数：' + str(len(que)))
            print('----------------------')
            print('请翻译：' + que[index])
            answer = input('Please translate:')
            if answer == ans[index]:
                print('Great!' + '∠ (ᐛ 」∠ )')
                que.pop(index)
                ans.pop(index)
                judge += 2
                continue
            elif answer == 'pass':
                print('·answer : '+ ans[index]+ ' ∠ (ᐛ 」∠ )')
                word = [que[index],ans[index]]
                passed_words.append(word)
                que.pop(index)
                ans.pop(index)
                continue
            elif answer == 'q':
                if int(len(passed_words)) == 0:
                    break
                else:
                    print('(¦3[▓▓]')
                    print('已自动结束运行，此次 pass 单词如下：')
                    for word in passed_words:
                        print(word)
                    print('----------------------')
                    print('共计 ' + str(len(passed_words)) + ' 个单词')
                    break
            else:
                print('Error!')
                print('现在你可以继续回答，也可以输入 pass 查看答案后回答下一个')
                judge += 1
                continue
        else:
            print('----------------------')
            print('当前词库单词剩余数：' + str(len(que)))
            print('----------------------')
            if int(len(passed_words)) == 0:
                print('已自动结束运行')
                break
            else:
                print('(¦3[▓▓]')
                print('已自动结束运行，此次 pass 单词如下：')
                for word in passed_words:
                    print(word)
                print('----------------------')
                print('共计 ' + str(len(passed_words)) + ' 个单词')
                break
elif choice == '6':
    unit = input('请输入某一单元相应的阿拉伯数字序号：')
    unit = int(unit) - 1
    chinese = all_wards[unit][0]
    english = all_wards[unit][1]
    unit_words = []
    print('第' + str(unit) + '单元单词如下：')
    print('----------------')
    for i,j in zip(chinese,english):
        unit_words.append([i,j])
        print([i,j])
    print('----------------')
    print('共计 ' + str(len(unit_words)) + ' 个单词')

     
