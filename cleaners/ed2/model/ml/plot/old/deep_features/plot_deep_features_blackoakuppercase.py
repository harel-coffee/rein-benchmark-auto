import matplotlib.pyplot as plt
import numpy as np


def plot_list(ranges, list_series, list_names):
    fig = plt.figure()
    ax = plt.subplot(111)

    for i in range(len(list_series)):
        ax.plot(ranges[i], list_series[i], label=list_names[i])

    ax.set_ylabel('fscore')
    ax.set_xlabel('labels')

    ax.legend(loc=4)

    plt.show()



fscore_deepfeatures_128u_3l_last_solo = []
fscore_deepfeatures_128u_3l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02187704546598862, 0.50409997765809278, 0.51586712399567725, 0.51499105519963573, 0.51499105519963573, 0.51500702670146559, 0.51500702670146559, 0.63841396871589673, 0.61884802134557804, 0.75004731949006298, 0.87177569631362462, 0.8717861557478368, 0.87186982424047665, 0.87187331015836222, 0.90051316911517021, 0.91752447324473863, 0.92313264253793648, 0.94480332145903367, 0.94480332145903367, 0.94480332145903367, 0.94480663035400136, 0.94826173879475129, 0.97066299139409284, 0.95419495029132928, 0.95394812680115271, 0.95394812680115271, 0.95380300808687468, 0.95386329295464445, 0.95326132913095285, 0.95823822103670264, 0.97396970753091117, 0.97444329636371196])
fscore_deepfeatures_128u_3l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.054929637345350966, 0.4994726560708751, 0.51687201862862564, 0.5605317091475911, 0.56054209694529245, 0.5605524845930695, 0.5605524845930695, 0.70698803673173694, 0.69272377849333722, 0.80949690367490845, 0.89195433291866089, 0.89195433291866089, 0.89195433291866089, 0.89196112316309395, 0.89237878423315875, 0.93214656972868115, 0.9388073127161698, 0.94240127388535033, 0.94240464202343299, 0.94241474630896427, 0.94240574254714071, 0.94771612347469725, 0.94236463421534045, 0.95472141771571117, 0.96957188119832038, 0.96957188119832038, 0.96990024688814702, 0.96990961295805111, 0.96977700759198471, 0.96903583385394143, 0.97097379769307512, 0.97218019969106806])
fscore_deepfeatures_128u_3l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.074814756280658673, 0.324277413025432, 0.35232578325582248, 0.4197181308516798, 0.4197181308516798, 0.4197181308516798, 0.4197181308516798, 0.56668889151191693, 0.6675289562889235, 0.78268967080899576, 0.89207836119556516, 0.89208847661480783, 0.89209859184934281, 0.89210533523641999, 0.89781880270870429, 0.964602582948341, 0.96812048357263825, 0.97088026970517205, 0.97087712246260771, 0.97088845165200988, 0.9708917874646682, 0.9691920636571667, 0.96449551352398155, 0.96981069916314877, 0.96846591919694969, 0.96846905116098569, 0.96868795954396425, 0.96870129786147086, 0.97032303021895594, 0.97797728046152099, 0.97751472404140183, 0.97961553347955088])
fscore_deepfeatures_128u_3l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.045981299114692134, 0.37464348471068182, 0.39399649258699987, 0.48543576143500367, 0.48543576143500367, 0.48545231338634887, 0.4854578306230693, 0.63483710163269658, 0.73855983071194564, 0.85634008631059333, 0.92445111271460412, 0.92445795043119194, 0.92449357774253127, 0.92451750705622104, 0.93055994021119359, 0.90538794741241735, 0.92427025923657891, 0.92559829007029981, 0.92528622065234856, 0.92527509838722122, 0.92525750125779749, 0.92870750225433873, 0.96583014229735464, 0.96753240526155948, 0.9683574779095464, 0.96870942736561383, 0.96876695193786577, 0.96879228039721232, 0.97000092402889337, 0.98088934224456104, 0.98156062070360528, 0.98158858344290612])
fscore_deepfeatures_128u_3l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.092828489412964191, 0.35201834308815544, 0.37888940550100747, 0.51929667411794345, 0.51930259527332345, 0.51930851638134767, 0.51930851638134767, 0.64680916175147274, 0.77966200935366059, 0.91013089005235603, 0.91207330697981126, 0.91207702399825064, 0.9120850586965138, 0.91209620936469704, 0.92494627434549315, 0.87921393292194761, 0.88055531886404304, 0.89647331285398857, 0.89647786554031972, 0.89622290724592479, 0.89623014921076616, 0.8987481899017461, 0.93797392088857534, 0.93844372813764732, 0.939920542182753, 0.93993630930494876, 0.94024361355957564, 0.94025975645105486, 0.94127794194116898, 0.96360790141332553, 0.9596018994505251, 0.96032272534859775])

last_128u_3l_solo_deepfeatures = list(np.mean(np.matrix(fscore_deepfeatures_128u_3l_last_solo), axis=0).A1)




fscore_deepfeatures_128u_2l_last_solo = []
fscore_deepfeatures_128u_2l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.019125183592937425, 0.41060766600213922, 0.42118326032026071, 0.43905889271678972, 0.43905889271678972, 0.43905889271678972, 0.43905889271678972, 0.62008730593860817, 0.65218991071793597, 0.71273414879158548, 0.83014940150543903, 0.83015682615842556, 0.83016425071716882, 0.83009325214886087, 0.82916526233007526, 0.85650461231613062, 0.92416208839500014, 0.93806611768442272, 0.93807988333468362, 0.93810127115486186, 0.9382080730044331, 0.94292411916254748, 0.96227371588363231, 0.9595615854324111, 0.95973335042625474, 0.95973079080201906, 0.95972947850892665, 0.95974464239359303, 0.95929855292978183, 0.93936515871032245, 0.94970278776552586, 0.94973320857778687])
fscore_deepfeatures_128u_2l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0075840544937738584, 0.36979836603172239, 0.38733788218136361, 0.41024076100681878, 0.41024076100681878, 0.41024633721154558, 0.41024633721154558, 0.48017424514466178, 0.49107401258168198, 0.66214308391707588, 0.80417318649067515, 0.80418213943459516, 0.80419402415194918, 0.80420297667175755, 0.8801470896659721, 0.93383473659689176, 0.93238176675656126, 0.9276395711192098, 0.92764311109203801, 0.92764923562442447, 0.92765325322681802, 0.93353379569005923, 0.93618606530723059, 0.935435335976608, 0.94391659860556199, 0.94391659860556199, 0.94391141351814078, 0.94391438967328578, 0.95012510001651063, 0.91357965016162646, 0.91469046863908898, 0.91425298294636614])
fscore_deepfeatures_128u_2l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.024323951953306028, 0.37827039004772001, 0.41665815457950284, 0.43492930923844425, 0.43492930923844425, 0.43492930923844425, 0.43492930923844425, 0.59813003283407828, 0.69430640631928142, 0.8139023474514151, 0.94702173891860819, 0.94703541906880806, 0.94703883905081754, 0.94704567894818903, 0.94627121237275824, 0.88087879681509873, 0.88050155931249574, 0.88206643909749405, 0.88205088560699096, 0.88206418158518352, 0.88206418158518352, 0.88464566110485643, 0.94546215317511384, 0.94082683925505206, 0.94499349845883562, 0.94502290581067683, 0.94504615694621108, 0.94505279993954927, 0.9453888385212047, 0.94693512191431961, 0.95336606113859657, 0.95559873003838314])
fscore_deepfeatures_128u_2l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.023749654253312883, 0.36679744109507401, 0.3793946668338693, 0.43337197394969057, 0.43338256317360113, 0.43338256317360113, 0.43338256317360113, 0.59151571770015654, 0.64328118120681765, 0.76282745438384436, 0.8742443701591871, 0.87425196969926988, 0.87423833479568991, 0.87425884153098365, 0.87401034885863504, 0.94785654126438545, 0.94809681889966801, 0.93202739619612363, 0.93202481946975413, 0.93210080334543854, 0.93215352599060763, 0.93470611573258056, 0.93604288093255616, 0.93691960367048543, 0.94907925147245209, 0.94909221747882511, 0.94914397215073354, 0.94918176779642882, 0.94958603801453723, 0.94890827013245527, 0.95342355263714218, 0.96764334638278238])
fscore_deepfeatures_128u_2l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.026848757444028447, 0.41393587477909621, 0.43142792983856887, 0.45357861454440929, 0.45357861454440929, 0.45359096171503854, 0.45359096171503854, 0.49484649727167512, 0.5276437344771695, 0.64636998396891487, 0.74118205045822427, 0.74118975419743149, 0.74118975419743149, 0.74119745784234825, 0.85750772578350443, 0.91214199592829048, 0.92138424224559701, 0.93733027147036119, 0.93733027147036119, 0.93738427286037795, 0.93752063387256512, 0.95014509557832771, 0.95138502403238057, 0.96560172135694744, 0.96599842956268134, 0.96599842956268134, 0.96625354062263691, 0.96642940239529007, 0.96578719028183957, 0.97299237964628105, 0.97318101921838129, 0.97393719290749836])

last_128u_2l_solo_deepfeatures = list(np.mean(np.matrix(fscore_deepfeatures_128u_2l_last_solo), axis=0).A1)


fscore_deepfeatures_128u_2l_avg_solo = []
fscore_deepfeatures_128u_2l_avg_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.034304308375833051, 0.42232447283922009, 0.53332571318037336, 0.52866468842729974, 0.52866468842729974, 0.52868464692297534, 0.52869961543939614, 0.67587456818955871, 0.72746841309332155, 0.80400895972135489, 0.9419585040306595, 0.94196549514011396, 0.94196899066019557, 0.94197598163106855, 0.94268231809511849, 0.95402332830766301, 0.95223279529732707, 0.96608928220001877, 0.96608928220001877, 0.96614953819750249, 0.96613707114860392, 0.96615422361972902, 0.96329276105060857, 0.96608080229410798, 0.96495452286121886, 0.96492983384758402, 0.96492960746722434, 0.96494540572118348, 0.96548764234935724, 0.96723114424084966, 0.9682639500272503, 0.96679353058626627])
fscore_deepfeatures_128u_2l_avg_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.027641551493535449, 0.36186182675265277, 0.37235025609354033, 0.41020212452050758, 0.41020212452050758, 0.41020212452050758, 0.41024317017486273, 0.58365802034160008, 0.67399329295240074, 0.81032989023106028, 0.92145867620633803, 0.92146930516135817, 0.92147639101498602, 0.92152244679418327, 0.92193447615047386, 0.94676854039988323, 0.94821651598625833, 0.96918997185481637, 0.96919017235152294, 0.96922055780418293, 0.96884045964464294, 0.9685927027097514, 0.91825428249586394, 0.91569712462402908, 0.91296602387511472, 0.91296881839246524, 0.91299157647289286, 0.9136460554371002, 0.91550885910188196, 0.96392169967739039, 0.93902926335157844, 0.93952126935406011])
fscore_deepfeatures_128u_2l_avg_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.076171422297585806, 0.39540711339546192, 0.44457052685703147, 0.52351308182370559, 0.52351308182370559, 0.52351845383630236, 0.52351845383630236, 0.6415877015453485, 0.73258020969722804, 0.82594991578321608, 0.89234147092490068, 0.89234888546756808, 0.89235259270167777, 0.8923600070954506, 0.91145364314589017, 0.91566172664353229, 0.93796814177260168, 0.95083005064715809, 0.95083371968473729, 0.95088770450134752, 0.95091212522299584, 0.95232229756681286, 0.97150066167887594, 0.97260508933685874, 0.97124932298248778, 0.97125908731885802, 0.97126627615710215, 0.9713088330109606, 0.97170255437971986, 0.95033915491538457, 0.95093689995365172, 0.95126566483337704])
fscore_deepfeatures_128u_2l_avg_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10211454809086515, 0.47482508963068681, 0.47859692904925299, 0.53101247974123145, 0.53101247974123145, 0.53101747089882367, 0.53101747089882367, 0.65453701123804209, 0.70952671003862011, 0.8443181620095177, 0.95740738912527679, 0.95740564019875607, 0.95742307426529383, 0.95742993560360512, 0.95871209996469431, 0.92825843555172982, 0.93054483908703989, 0.93049140324448154, 0.93050588429371361, 0.930522095853487, 0.93061887022445022, 0.93072940152068784, 0.97432543986015119, 0.92668382837882612, 0.92536817059049381, 0.92537466856532991, 0.92539966623938852, 0.92569624807626605, 0.92572455002903031, 0.92667134203112345, 0.96805536604482467, 0.96678410300603224])
fscore_deepfeatures_128u_2l_avg_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02005597014925373, 0.37483528583548442, 0.45079023760885928, 0.54407702972674976, 0.54407702972674976, 0.54407702972674976, 0.54407702972674976, 0.70370286782841396, 0.79865037812681794, 0.89403136296990116, 0.95501129511953309, 0.95501808832563539, 0.95506903455628067, 0.9551675165176583, 0.92485703954681198, 0.92650439708836996, 0.92697630891986393, 0.92760396013646151, 0.9276074745528311, 0.92712160807969657, 0.92748207747504263, 0.92492206100945795, 0.93215120720387046, 0.9237272416654464, 0.9233818519665532, 0.92338536165551777, 0.9238839322122363, 0.92399595445499338, 0.95696391234863465, 0.9680118439275992, 0.96852928115549308, 0.96937269372693735])

avg_128u_2l_solo_deepfeatures = list(np.mean(np.matrix(fscore_deepfeatures_128u_2l_avg_solo), axis=0).A1)



fscore_deepfeatures_128u_2l_last_plus = []
fscore_deepfeatures_128u_2l_last_plus.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.011565301564605623, 0.34540083680448785, 0.360866234041964, 0.48217929929992182, 0.48217929929992182, 0.48217929929992182, 0.48217929929992182, 0.66322509970388366, 0.78523961241355922, 0.91304980389850399, 0.96820755425886773, 0.96821429621570765, 0.96823789237082147, 0.96824463393119675, 0.96831878528120441, 0.95262258681699807, 0.94772432899765058, 0.94773346703692285, 0.94774699492190007, 0.94774699492190007, 0.94776390428899704, 0.93656205416294647, 0.95832658849124897, 0.96164747818379503, 0.96164747818379503, 0.96165409937987223, 0.96165409937987223, 0.96166072049150797, 0.97252945342174735, 0.97149658947260342, 0.97335904853744781, 0.97335904853744781])
fscore_deepfeatures_128u_2l_last_plus.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.030977916794644369, 0.36769410775334105, 0.39392195648264705, 0.48689874226465379, 0.48689874226465379, 0.48693188663470982, 0.48693188663470982, 0.65093262276360875, 0.75756728137299945, 0.87847735883095801, 0.96368367685133838, 0.96369047814373521, 0.96377888682173596, 0.96380948631125807, 0.94973933390117538, 0.92529109529265041, 0.87166872722017941, 0.87166872722017941, 0.87166872722017941, 0.87163249249345698, 0.87181215810154866, 0.88188093730208994, 0.91492930745267187, 0.93420523138832989, 0.93420523138832989, 0.93420880547013596, 0.93422667551960725, 0.93454735628176422, 0.93668343733836668, 0.93830172636871101, 0.97172973392690742, 0.97172973392690742])
fscore_deepfeatures_128u_2l_last_plus.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.011748396938833644, 0.45005774447398811, 0.45748874250056781, 0.5951557917379382, 0.5951557917379382, 0.5951669424898699, 0.5951669424898699, 0.76560033178477194, 0.7892350214493421, 0.85067615838354216, 0.86110151160260595, 0.86110880013311231, 0.86111244436338263, 0.86111973275395892, 0.86111973275395892, 0.89535019002559524, 0.9713209602032945, 0.9713209602032945, 0.97130892495980925, 0.97161891122120658, 0.97165110447296976, 0.96863648387950108, 0.96914672616757713, 0.96282106763740039, 0.96282106763740039, 0.96283921388931326, 0.96284251424789258, 0.9635873401461339, 0.96329262534614557, 0.96779577559359742, 0.9742128095380721, 0.9742128095380721])
fscore_deepfeatures_128u_2l_last_plus.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.016821580117195391, 0.38147060742480587, 0.39375500952348119, 0.50100166944908175, 0.50101254981091814, 0.50101798993260582, 0.50101798993260582, 0.66734813649174185, 0.75864871526690603, 0.88230745252253984, 0.93998228023991781, 0.93998903676508072, 0.93999579320411231, 0.94001268392487802, 0.90521468996463628, 0.93076493949818684, 0.93649422255051973, 0.93649422255051973, 0.93649772958855593, 0.93651526443179645, 0.93652227820719136, 0.93704926849905379, 0.93968839056448472, 0.93317917877071455, 0.93317917877071455, 0.93317917877071455, 0.9331895434996631, 0.93323661704559813, 0.95853268525451485, 0.96230608553888475, 0.97085591375624125, 0.97085591375624125])
fscore_deepfeatures_128u_2l_last_plus.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.041389200648459905, 0.42745316267853822, 0.47760832293564803, 0.61604519049203599, 0.61604519049203599, 0.61604519049203599, 0.61606183550089, 0.77513037127896789, 0.83800929514698785, 0.94388946651539518, 0.95293306873073713, 0.95293975011804943, 0.95294643142009383, 0.95287193147560323, 0.95296141118957434, 0.97045986299191644, 0.97103853353127223, 0.97103853353127223, 0.97104517494884823, 0.97109498284803319, 0.97119583283578237, 0.97119583283578237, 0.97339747622873329, 0.96970697215345525, 0.96970697215345525, 0.96971364034988361, 0.96973128996349889, 0.9698277675136463, 0.96927608883835714, 0.97290130160634103, 0.97998142773479846, 0.97998142773479846])

last_128u_2l_plus_deepfeatures = list(np.mean(np.matrix(fscore_deepfeatures_128u_2l_last_plus), axis=0).A1)



fscore_deepfeatures_128u_1l_last = []
fscore_deepfeatures_128u_1l_last.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.022194945393887892, 0.40432887704338843, 0.41397581290292229, 0.53927051231503309, 0.53927051231503309, 0.53928226585130357, 0.53928226585130357, 0.71500244131986945, 0.71715015974440888, 0.82618960452694001, 0.86041192667956246, 0.86042214781152826, 0.86045621692726248, 0.86047325072123659, 0.83011630494618116, 0.88026240503269348, 0.90071754250858738, 0.90071754250858738, 0.90072090187605613, 0.90101644583080021, 0.89710991787744787, 0.92799291083390656, 0.96914773278174593, 0.96139514371360835, 0.96139514371360835, 0.96139514371360835, 0.96140608772069991, 0.96630780602243149, 0.9644601193705914, 0.96404097446509496, 0.97370219574842998, 0.97370219574842998])
fscore_deepfeatures_128u_1l_last.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.051281414984893504, 0.40372888988966443, 0.4107892358221244, 0.55766909302372214, 0.55768644625182484, 0.55770379906236589, 0.55770379906236589, 0.71989783031721688, 0.8271003817880529, 0.96052648641639116, 0.96754958020514603, 0.96755295178008105, 0.96758666631834689, 0.96759340896177448, 0.95488421656895706, 0.95762616760735386, 0.92514306036015637, 0.92514306036015637, 0.92515001034554101, 0.92514066810080287, 0.92513517529183009, 0.93586587761140727, 0.94066210604245637, 0.94017964626354278, 0.94017964626354278, 0.94018291760682282, 0.94031920775686595, 0.94032792151629729, 0.94244541971266038, 0.92574024420239465, 0.9437868141442074, 0.9437868141442074])
fscore_deepfeatures_128u_1l_last.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.013523154139966537, 0.38418896328312446, 0.39105336013268249, 0.51603982094736878, 0.51603982094736878, 0.51603982094736878, 0.51603982094736878, 0.68641714408360721, 0.79390104834612818, 0.86073819902935311, 0.89473939831261096, 0.89474706686371241, 0.89475090109935862, 0.89476240364668258, 0.88810043287629215, 0.85831070760521377, 0.92523511267189773, 0.92523511267189773, 0.92524524046601175, 0.92525199222271426, 0.926317705277097, 0.93217989622812325, 0.97534920335443409, 0.97834669296421606, 0.97834669296421606, 0.97835663541700457, 0.97846598962708753, 0.97847592975809738, 0.97886053273794071, 0.97022857106137417, 0.969118594548389, 0.969118594548389])
fscore_deepfeatures_128u_1l_last.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.033989972019304794, 0.40219076343574955, 0.42010089932002631, 0.46646055130147457, 0.46646055130147457, 0.46646055130147457, 0.46646055130147457, 0.62235790873167307, 0.69378417375455648, 0.81883096981900572, 0.94770435823987309, 0.94771117016283823, 0.94771798199761137, 0.94772479374419427, 0.90971576192802694, 0.93496670673563931, 0.93496670673563931, 0.93496670673563931, 0.9349738990673897, 0.9349738990673897, 0.93500626335817294, 0.91669674562823777, 0.9164694293571205, 0.91290910639747846, 0.91290910639747846, 0.91291281058757789, 0.91326089178049541, 0.91335982213687705, 0.93039073080202639, 0.93426236098083881, 0.94337111267921214, 0.94337111267921214])
fscore_deepfeatures_128u_1l_last.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.022870865735822015, 0.42845801070397804, 0.43483475665598986, 0.58228685825846693, 0.58229272227162743, 0.58231031402005229, 0.58231031402005229, 0.66667424914507556, 0.70527993389015142, 0.83989417989417992, 0.84838787263325277, 0.84839941341332648, 0.8487669677591706, 0.84883616098409587, 0.91232843696882049, 0.95005466085793067, 0.95800406484548783, 0.95804074944150341, 0.95805408865418473, 0.95792320865543135, 0.95857325655790149, 0.96841791894795426, 0.95915839613840359, 0.96363928010009314, 0.96363928010009314, 0.96363928010009314, 0.96381808967211746, 0.96381808967211746, 0.94916483034274868, 0.956309296241863, 0.95978477163825071, 0.95978477163825071])

last_128u_1l_deepfeatures = list(np.mean(np.matrix(fscore_deepfeatures_128u_1l_last), axis=0).A1)


fscore_deepfeatures_128u_1l_last_solo = []
fscore_deepfeatures_128u_1l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.018409189505253033, 0.2994236212619712, 0.30588795444718136, 0.3639290649803561, 0.3639468210183594, 0.36395865816291467, 0.36395865816291467, 0.50241102328836618, 0.54989913148897074, 0.63151074742481372, 0.74309266572122246, 0.74310101462993405, 0.74310101462993405, 0.74310936342773271, 0.74021619906318337, 0.83241340912683948, 0.85164079386912939, 0.85933444059225372, 0.85933444059225372, 0.85944753494070614, 0.85939037773922899, 0.87085920962247487, 0.84546358256553267, 0.8773623230796731, 0.88194482952080555, 0.88194482952080555, 0.88222192510753195, 0.88241855004402692, 0.89732350486432766, 0.91803908294384917, 0.9289842945417095, 0.93198984357696113])
fscore_deepfeatures_128u_1l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0038850482774381539, 0.29437012123189682, 0.29913864518769151, 0.40132014820994771, 0.40132014820994771, 0.40133322427613283, 0.40133322427613283, 0.49140362607886995, 0.61884411217132462, 0.68322409877439161, 0.72911263737220067, 0.72912148543699462, 0.72912590942319067, 0.72913475730318311, 0.77557072008494432, 0.80088233465225345, 0.82750558777956051, 0.85015606946384537, 0.85016003531813911, 0.85023554810630353, 0.85023951331721626, 0.86269502358424743, 0.85814685553958803, 0.89240506329113911, 0.89931349361683932, 0.89931349361683932, 0.89929998157846258, 0.89929998157846258, 0.90346291627968689, 0.90785098798837771, 0.92611724779324167, 0.9249676879551767])
fscore_deepfeatures_128u_1l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.015008037777554507, 0.32898417355334253, 0.33380459113854077, 0.4058775997495796, 0.4058775997495796, 0.40588340206523288, 0.40589500656982397, 0.48394804473154135, 0.59922123028357133, 0.66690573007936449, 0.76580535002845762, 0.76581471588149586, 0.7658211758456489, 0.76556544560200546, 0.82525619464849498, 0.84603889485717421, 0.89891231473224453, 0.89680831756073531, 0.89682261890872317, 0.89683267597234873, 0.89712948133546888, 0.90418518195811914, 0.90934592095335742, 0.9118396891882169, 0.91881117256706613, 0.91880777863230423, 0.91881117256706613, 0.91885105167505265, 0.92011617612402297, 0.92177383620291176, 0.92811240883357982, 0.9317574303002597])
fscore_deepfeatures_128u_1l_last_solo.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.018580133836778947, 0.30630588345732324, 0.32479297144417751, 0.4262429991999086, 0.4262609868443612, 0.42627297837889322, 0.42627297837889322, 0.47924061265373019, 0.62407478388365623, 0.72808646288790835, 0.78790198259550825, 0.78787401912746147, 0.78799972820936459, 0.78801424729644676, 0.82494147426077746, 0.81500353193640507, 0.84811694500436685, 0.8606648255286552, 0.86070241811113835, 0.86097413503527032, 0.86097320102923092, 0.88116618537125668, 0.90735611584049514, 0.90455541598738542, 0.90642816324903319, 0.90642816324903319, 0.9064330399710292, 0.90643667315627552, 0.92389816070921538, 0.92808596188044745, 0.93585508587949606, 0.93367161786470509])
# #fscore_deepfeatures_128u_1l_last_solo.append()

last_128u_1l_solo_deepfeatures = list(np.mean(np.matrix(fscore_deepfeatures_128u_1l_last_solo), axis=0).A1)


fscore_all = []
fscore_all.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.019724363054314468, 0.34711857588253048, 0.36683973865301972, 0.50302073378485068, 0.50302073378485068, 0.50302073378485068, 0.50302073378485068, 0.68927914099271803, 0.78987634090775527, 0.91562398351946217, 0.96274558340716032, 0.96275571855244002, 0.96275909689018591, 0.96276923177138474, 0.96276923177138474, 0.95525757832562097, 0.9296087632841401, 0.9296087632841401, 0.9295631970563919, 0.92962265877217054, 0.93073721662776832, 0.92961768800185185, 0.94806689957432966, 0.95985053546435073, 0.95985053546435073, 0.95989644112001737, 0.95995281439798508, 0.95995281439798508, 0.96107176227848345, 0.96217488060091694, 0.96818632276802219, 0.96818632276802219])
fscore_all.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06325768492571085, 0.43590238699474054, 0.44687096288248473, 0.54632791030425987, 0.54634441773757025, 0.54636915914381434, 0.54572256891553239, 0.67348404904390513, 0.7382603956139191, 0.8698257510052827, 0.93311187597522882, 0.9331187979095773, 0.9331516714515109, 0.93420458642001369, 0.95484745240213098, 0.97224891604963204, 0.89224119470644636, 0.89224119470644636, 0.89225214303127753, 0.89230323235251485, 0.89193024274130084, 0.8903832557833643, 0.8857692971796618, 0.87424104334877994, 0.87424104334877994, 0.87424104334877994, 0.87425710801617362, 0.87475760572243133, 0.8761553987170092, 0.88226503467549944, 0.94375436601413365, 0.94375436601413365])
fscore_all.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.077347124000268011, 0.46175709810616072, 0.47326504459409485, 0.61372494703617153, 0.61373576425330367, 0.61373576425330367, 0.61411105351568118, 0.7533598534010052, 0.80056088320606167, 0.9284853606763569, 0.92891774777393199, 0.92891774777393199, 0.92892128530238427, 0.92376790562835076, 0.92763237442280722, 0.95983815375393366, 0.96848420339639063, 0.96848420339639063, 0.96850416557810093, 0.96851081946697726, 0.974058311176904, 0.97356833915652485, 0.9766624713255444, 0.97842535093922867, 0.97842535093922867, 0.97842535093922867, 0.97844844288869648, 0.97802102168889071, 0.97883266775481759, 0.97949389461190639, 0.9814345528442161, 0.9814345528442161])
fscore_all.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.041830521572757802, 0.43252256330195565, 0.44166900079436872, 0.57582193458247855, 0.57582193458247855, 0.57583337013557945, 0.57583337013557945, 0.73974023391023602, 0.80343210402899168, 0.93479842357302356, 0.95807940665439184, 0.95808278415113668, 0.95808278415113668, 0.95809291650999062, 0.95814170564041734, 0.97302937033752424, 0.94856643904324844, 0.94852438800846528, 0.94852789238983359, 0.94856643904324844, 0.94893859249075396, 0.94718949300983712, 0.94319700394304851, 0.94881400713764619, 0.94885545850667408, 0.94885891263986322, 0.94884054113556981, 0.94875789667435795, 0.95073307602123491, 0.95794831740316144, 0.97127995802996758, 0.97127995802996758])
fscore_all.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.029844774663824306, 0.38699193083843414, 0.4088931940312277, 0.48623366188897971, 0.48623366188897971, 0.48626623912310524, 0.48626623912310524, 0.58848328127230298, 0.65843586247679742, 0.78994887801636027, 0.89257349494408345, 0.89258091086244662, 0.89264466102631224, 0.89264836849893869, 0.94148183105238314, 0.96213939206275478, 0.9637235299610093, 0.9637235299610093, 0.96373687582705225, 0.96382671852061708, 0.96383005437564584, 0.96569694783359306, 0.97434033771593964, 0.97813173985727264, 0.97813173985727264, 0.97813834826668555, 0.97818460473944069, 0.97818460473944069, 0.97821623386911627, 0.98154625419403307, 0.98058829005531056, 0.98058829005531056])

average_0 = list(np.mean(np.matrix(fscore_all), axis=0).A1)
label_0 = [4, 8, 12, 16, 20, 24, 28, 38, 48, 58, 68, 78, 88, 98, 108, 118, 128, 138, 148, 158, 168, 178, 188, 198, 208, 218, 228, 238, 248, 258, 268, 278, 288, 298, 308, 318, 328, 338, 348, 358, 368, 378]


ranges = [label_0, label_0, label_0, label_0, label_0, label_0, label_0, label_0]
list = [average_0, last_128u_1l_solo_deepfeatures, last_128u_1l_deepfeatures, last_128u_2l_solo_deepfeatures, avg_128u_2l_solo_deepfeatures, last_128u_2l_plus_deepfeatures, last_128u_3l_solo_deepfeatures]
names = ["unigram + svd", "solo LSTM last- 128 units, 1 layer", "+ LSTM last- 128 units, 1 layer", "solo LSTM last- 128 units, 2 layer", "solo LSTM avg- 128 units, 2 layer", "+ LSTM last- 128 units, 2 layer", "solo LSTM last- 128 units, 3 layer"]

plot_list(ranges, list, names)