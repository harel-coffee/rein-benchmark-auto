import numpy as np

from ml.plot.old.potential_latex.plotlatex_lib import plot_list_latex

label_potential = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 78, 88, 98, 108, 118, 128, 138, 148, 158, 168, 178, 188, 198, 208, 218, 228, 238, 248, 258, 268, 278, 288, 298, 308, 318, 328, 338, 348, 358, 368, 378, 388, 398, 408, 418, 428, 438, 448, 458, 468, 478, 488, 498, 508, 518, 528, 538, 548, 558, 568, 578, 588, 598, 608, 618, 628, 638, 648, 658, 668, 678, 688, 698, 708, 718, 728, 738, 748, 758, 768, 778, 788, 798, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 908, 918]


fscore_metadata_no_svd_absolute_potential = []
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.090909090909090912, 0.15851602023608768, 0.19504132231404955, 0.2884012539184953, 0.23266745005875442, 0.2791762013729977, 0.35268346111719612, 0.41014799154334036, 0.2386483632523759, 0.26340447683498175, 0.21414460687475306, 0.22028353326063249, 0.22028353326063249, 0.22351233671988385, 0.22351233671988385, 0.22939068100358423, 0.22939068100358423, 0.23375680580762254, 0.23950017355085043, 0.24498269896193772, 0.24680262703076394, 0.31688311688311693, 0.33917129431866722, 0.33917129431866722, 0.35254237288135593, 0.36691855583543243, 0.59618008185538884, 0.62337662337662336, 0.74451410658307204, 0.87316176470588236, 0.87419651056014691, 0.87419651056014691, 0.88138686131386856, 0.88138686131386856, 0.97897897897897901, 0.98605577689243029, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.090744101633393831, 0.11785714285714287, 0.14109347442680775, 0.24333333333333332, 0.2012422360248447, 0.26586826347305387, 0.34324942791762009, 0.40528634361233479, 0.23326133909287255, 0.25586353944562901, 0.28060956384655805, 0.29285014691478939, 0.29285014691478939, 0.29535452322738387, 0.29535452322738387, 0.30096153846153845, 0.30096153846153845, 0.3059051306873185, 0.3325393044306813, 0.32791208791208792, 0.33201927288655281, 0.3417391304347826, 0.38567222767419035, 0.44217321140398069, 0.46917808219178087, 0.46917808219178087, 0.48986486486486486, 0.50167973124300103, 0.52276559865092742, 0.57598039215686281, 0.57598039215686281, 0.57598039215686281, 0.5901639344262295, 0.59272727272727266, 0.59272727272727266, 0.60613349368610947, 0.60613349368610947, 0.99506416584402768, 0.99506416584402768, 0.99803149606299213, 0.99803149606299213, 0.99803149606299213, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.090909090909090912, 0.15540540540540543, 0.18679549114331723, 0.27828746177370034, 0.24769433465085641, 0.27918781725888325, 0.3603385731559855, 0.42508710801393734, 0.23600439077936333, 0.2598808879263671, 0.2849519743863394, 0.31374606505771246, 0.31374606505771246, 0.31815803244374674, 0.31815803244374674, 0.3235294117647059, 0.3235294117647059, 0.33144037170882812, 0.33144037170882812, 0.33830334190231365, 0.34171369933299128, 0.36202399582681272, 0.37013996889580097, 0.394910941475827, 0.394910941475827, 0.39878234398782353, 0.41348088531187122, 0.45468831849135671, 0.46910994764397901, 0.91335372069317033, 0.91335372069317033, 0.9155645981688707, 0.93799999999999994, 0.93799999999999994, 0.97405189620758481, 0.97405189620758481, 0.99314397649363373, 0.99314397649363373, 0.99314397649363373, 0.99314397649363373, 0.99314397649363373, 0.99803149606299213, 0.99803149606299213, 0.99803149606299213, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10108303249097472, 0.1672473867595819, 0.17996604414261463, 0.27652733118971057, 0.29206349206349208, 0.36969696969696964, 0.46065808297567951, 0.53206002728512958, 0.26456876456876455, 0.28850574712643678, 0.31465761177136387, 0.33842794759825329, 0.33842794759825329, 0.34475258292550298, 0.34475258292550298, 0.34810126582278483, 0.34810126582278483, 0.35125066524747206, 0.35649867374005301, 0.35997882477501325, 0.38308977035490605, 0.38308977035490605, 0.39123463388562263, 0.4112646121147715, 0.43491897543125979, 0.43537414965986398, 0.44302449414270495, 0.45991561181434598, 0.46234860452869936, 0.92616033755274263, 0.95803480040941658, 0.95803480040941658, 0.95803480040941658, 0.95803480040941658, 0.9758551307847082, 0.9758551307847082, 0.9758551307847082, 0.9758551307847082, 0.99506416584402768, 0.99506416584402768, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10074626865671642, 0.18214285714285716, 0.1884297520661157, 0.2821316614420063, 0.23002421307506052, 0.29205607476635514, 0.3664804469273743, 0.42626480086114105, 0.24533333333333332, 0.26659641728134881, 0.29090909090909095, 0.23269734380845489, 0.23269734380845489, 0.23893805309734517, 0.23893805309734517, 0.24381368267831152, 0.24381368267831152, 0.24445252819206983, 0.26027397260273971, 0.26143320129636299, 0.26652298850574707, 0.2833513124775261, 0.29985754985754987, 0.29985754985754987, 0.31261228889687387, 0.31666666666666671, 0.35257890685142418, 0.35511145272867023, 0.36203597397627252, 0.36203597397627252, 0.36203597397627252, 0.36203597397627252, 0.36203597397627252, 0.53658536585365857, 0.90544412607449853, 0.90544412607449853, 0.90544412607449853, 0.96439471007121058, 0.96439471007121058, 0.96859169199594719, 0.96859169199594719, 0.96859169199594719, 0.98199999999999998, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

average_metadata_no_svd_absolute_potential = list(np.mean(np.matrix(fscore_metadata_no_svd_absolute_potential), axis=0).A1)

fscore_linear_svm = []
fscore_linear_svm.append([0.0055594162612925642, 0.0069444444444444441, 0.0091476091476091499, 0.022829470771359391, 0.019214467363662051, 0.017619047619047618, 0.022360248447204967, 0.029529130087789304, 0.040712468193384227, 0.038714021208550747, 0.036968576709796676, 0.036279323513366067, 0.033965538614106852, 0.033557813035041663, 0.032936302433972033, 0.032806207641685493, 0.031090959563246038, 0.038768298838970219, 0.039455923580105905, 0.041267008699531565, 0.040158820192853092, 0.048357552814751494, 0.051322542439794706, 0.051083369206485867, 0.047135071439092659, 0.048185603807257588, 0.051091185924547457, 0.061632726617408547, 0.076480263157894732, 0.096889099976252668, 0.11394557823129252, 0.13810741687979541, 0.16545601291364001, 0.19254365266635204, 0.19254365266635204, 0.19576470588235292, 0.21785881252921926, 0.24412713035467526, 0.24628252788104088, 0.24801123069723913, 0.2404692082111437, 0.25645672859084728, 0.25780189959294436, 0.27959084266926448, 0.29102742910274293, 0.32347328244274809, 0.33643031784841076, 0.35877437325905298, 0.37066515065378053, 0.38488783943329391, 0.38679245283018865, 0.40243161094224916, 0.40339188370684437, 0.43225806451612903, 0.48476052249637153, 0.49418604651162784, 0.49418604651162784, 0.49418604651162784, 0.51082251082251084, 0.51641137855579866, 0.52307692307692311, 0.53807106598984766, 0.53963636363636369, 0.53963636363636369, 0.53761869978086185, 0.68599033816425126, 0.71090047393364941, 0.71090047393364941, 0.73488372093023258, 0.78217821782178221, 0.83454734651404794, 0.83454734651404794, 0.85947046843177188, 0.86178861788617889, 0.86530612244897964, 0.86530612244897964, 0.86530612244897964, 0.8717948717948717, 0.88121827411167508, 0.88121827411167508, 0.88798370672097748, 0.88979591836734695, 0.89549180327868849, 0.91231732776617958, 0.93535353535353549, 0.93535353535353549, 0.93535353535353549, 0.93535353535353549, 0.93535353535353549, 0.93535353535353549, 0.93535353535353549, 0.93535353535353549, 0.93535353535353549, 0.94810379241516962, 0.94810379241516962, 0.94810379241516962, 0.94841269841269837, 0.94945490584737369, 0.94945490584737369, 0.94945490584737369, 0.94945490584737369, 0.94945490584737369])
fscore_linear_svm.append([0.050167224080267567, 0.036340038935755999, 0.027669693039342844, 0.029084687767322499, 0.02535421327367636, 0.025426807119505995, 0.024319629415170817, 0.020042949176807445, 0.033183218772220906, 0.031996839818289553, 0.033235581622678402, 0.031953272633568112, 0.030034539720678783, 0.029515938606847699, 0.027962716378162448, 0.028533430056825047, 0.027070428997476484, 0.030184331797235023, 0.034974926064034975, 0.037687366167023555, 0.041312959818902088, 0.050160396617089528, 0.05759312320916906, 0.061793279184583529, 0.07275346659463354, 0.074140723411912898, 0.071493376882598436, 0.075787939515394434, 0.071453837990802974, 0.080980066445182713, 0.08698969858832506, 0.099778270509977826, 0.11667527103768716, 0.1354950781702374, 0.13640338093850188, 0.188373804267844, 0.18963616317530321, 0.18963616317530321, 0.2028673835125448, 0.21969427657305368, 0.22725638259618844, 0.23453700393278512, 0.2439568612867237, 0.2439568612867237, 0.25473449684366878, 0.2623445156426687, 0.25853658536585367, 0.26628895184135976, 0.2862854858056777, 0.29071661237785024, 0.29785478547854782, 0.29659643435980554, 0.34933201385452745, 0.35392980721700446, 0.35392980721700446, 0.36189516129032256, 0.36290322580645162, 0.38000000000000006, 0.38719512195121947, 0.38719512195121947, 0.39916405433646812, 0.3887991383952612, 0.75339805825242712, 0.75339805825242712, 0.76408787010506207, 0.77085330776605943, 0.79850046860356139, 0.79850046860356139, 0.80410447761194037, 0.80410447761194037, 0.81578947368421051, 0.86254980079681276, 0.87819253438113953, 0.87819253438113953, 0.88212180746561886, 0.88212180746561886, 0.88212180746561886, 0.90764647467725923, 0.90480863591756622, 0.91755577109602338, 0.91755577109602338, 0.93201970443349746, 0.95075376884422103, 0.95075376884422103, 0.95075376884422103, 0.95075376884422103, 0.95266868076535749, 0.9590409590409591, 0.9590409590409591, 0.9590409590409591, 0.96142433234421365, 0.96142433234421365, 0.9652432969215492, 0.9652432969215492, 0.97435897435897434, 0.97435897435897434, 0.97435897435897434, 0.97435897435897434, 0.97435897435897434, 0.97435897435897434, 0.97435897435897434, 0.97435897435897434])
fscore_linear_svm.append([0.0075471698113207548, 0.01167883211678832, 0.011845102505694762, 0.017481385561670441, 0.016880093131548313, 0.014998828216545581, 0.019265502709211322, 0.01839958340565874, 0.028324697754749564, 0.026825179088553575, 0.025574751734457897, 0.026037828543355439, 0.025299145299145301, 0.026012166981329979, 0.027175484244001156, 0.026740847092605886, 0.025965267239925812, 0.029501011463250171, 0.03066037735849057, 0.036114329857087679, 0.036954915003695493, 0.042718446601941754, 0.047833293866919251, 0.047956684285161782, 0.051869895400487184, 0.052706960756230305, 0.062598301352626617, 0.076319543509272475, 0.071997230875735563, 0.087301587301587297, 0.096183542907566727, 0.10496083550913839, 0.12602024159320926, 0.18028643639427128, 0.1841109709962169, 0.19583333333333333, 0.2059714409346603, 0.2059714409346603, 0.21446593776282594, 0.21473684210526317, 0.22644847412649269, 0.24007473143390937, 0.2466388502549838, 0.27305936073059361, 0.29100768187980119, 0.29100768187980119, 0.30646672914714157, 0.3070422535211268, 0.31559114460668869, 0.32279693486590039, 0.32680363115145727, 0.33854907539118062, 0.34111481657932347, 0.35724465558194773, 0.36517647058823532, 0.38732045567112433, 0.39581256231306083, 0.39581256231306083, 0.40993788819875776, 0.42857142857142866, 0.80108991825613074, 0.80108991825613074, 0.82407407407407396, 0.83502304147465434, 0.83502304147465434, 0.85610859728506794, 0.85610859728506794, 0.93046033300685604, 0.93046033300685604, 0.93150684931506855, 0.93150684931506855, 0.95432458697764821, 0.95432458697764821, 0.95432458697764821, 0.95348837209302328, 0.95450145208131643, 0.95450145208131643, 0.95450145208131643, 0.95635305528613002, 0.96644295302013428, 0.96743295019157094, 0.9844660194174758, 0.98736637512147729, 0.98736637512147729, 0.98736637512147729, 0.99315738025415445, 0.99315738025415445, 0.99315738025415445, 0.99315738025415445, 0.99315738025415445, 0.99510284035259555, 0.99510284035259555, 0.99510284035259555, 0.99510284035259555, 0.99705593719332675, 0.99705593719332675, 0.99705593719332675, 0.99705593719332675, 0.99705593719332675, 0.99705593719332675, 0.99705593719332675, 0.99705593719332675])
fscore_linear_svm.append([0.0029806259314456031, 0.0072529465095194914, 0.009440323668240054, 0.014689265536723164, 0.017484489565707841, 0.018185951352580127, 0.016506717850287907, 0.016575559865984836, 0.024240295099244691, 0.024424176843407013, 0.023417172593235037, 0.023941068139963169, 0.022775299366048368, 0.023374415639609011, 0.022952529994783519, 0.02420604182804028, 0.024015890213073311, 0.030802014722975592, 0.036538260778786927, 0.041337248701152018, 0.041742067800699723, 0.046696353351787213, 0.057150451887293993, 0.063161030835691939, 0.073230769230769224, 0.076167076167076173, 0.088492539873092094, 0.099083215796897037, 0.11382113821138214, 0.14363636363636365, 0.17284654877353112, 0.18686722591842639, 0.22727272727272727, 0.30761523046092187, 0.31600617601646941, 0.32041343669250649, 0.34001027221366203, 0.34001027221366203, 0.35802469135802467, 0.39570378745053703, 0.40711009174311924, 0.42338251986379111, 0.42338251986379111, 0.43693693693693691, 0.49713193116634796, 0.50571791613723005, 0.5243741765480896, 0.52937293729372925, 0.54427083333333337, 0.60698027314112291, 0.63651591289782239, 0.63872590108968985, 0.66259808195292069, 0.69852302345786266, 0.71084337349397597, 0.72217502124044175, 0.75488454706927188, 0.78125000000000011, 0.78125000000000011, 0.77606527651858559, 0.78706199460916448, 0.7884788478847885, 0.81481481481481477, 0.81481481481481477, 0.8339350180505416, 0.90322580645161299, 0.90322580645161299, 0.92454632282712523, 0.92454632282712523, 0.92337164750957845, 0.89693593314763242, 0.89693593314763242, 0.91304347826086951, 0.9156398104265403, 0.9156398104265403, 0.91337099811676081, 0.92117758784425452, 0.92117758784425452, 0.92117758784425452, 0.92117758784425452, 0.92117758784425452, 0.92117758784425452, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.92147587511825924, 0.93295019157088133, 0.93295019157088133, 0.93295019157088133, 0.9652432969215492, 0.96626984126984117, 0.96626984126984117, 0.96626984126984117])
fscore_linear_svm.append([0.0, 0.013182674199623353, 0.015767634854771784, 0.016452074391988557, 0.01384083044982699, 0.017205301092769121, 0.019850111403686449, 0.019051108261586371, 0.030589949016751636, 0.028557030068872835, 0.029036515618125824, 0.028127902348414491, 0.027573092464939386, 0.026257231864708502, 0.025324403516115528, 0.029128124384963587, 0.028597285067873301, 0.035398230088495575, 0.040854808296668758, 0.041036717062634988, 0.041920216362407031, 0.050691244239631339, 0.057596554972412867, 0.055909216717409359, 0.067146974063400575, 0.067156650814238356, 0.070217917675544791, 0.082817869415807557, 0.087184529662405766, 0.10720331013729546, 0.12153069806560135, 0.13703099510603589, 0.14335570469798659, 0.18865345181134657, 0.19253575165678408, 0.19910179640718562, 0.20195930670685755, 0.20558659217877093, 0.2105263157894737, 0.21060663868752386, 0.21808510638297871, 0.22064056939501778, 0.21705426356589147, 0.22714896927265654, 0.22714896927265654, 0.34906832298136642, 0.35692307692307701, 0.36896762370189373, 0.3870558375634518, 0.40125786163522015, 0.39975015615240478, 0.39251207729468596, 0.39251207729468596, 0.4063068526379624, 0.42453397474443771, 0.45040548970679972, 0.58841463414634143, 0.61032863849765262, 0.62519440124416792, 0.63009404388714729, 0.70157068062827221, 0.72777268560953257, 0.73473108477666371, 0.80206185567010324, 0.80206185567010324, 0.81790437436419128, 0.82785299806576407, 0.82785299806576407, 0.83796740172579098, 0.83796740172579098, 0.83957732949087405, 0.83957732949087405, 0.83957732949087405, 0.85770363101079472, 0.85966633954857707, 0.85966633954857707, 0.88590604026845643, 0.88590604026845643, 0.88590604026845643, 0.90066225165562919, 0.91538461538461535, 0.91538461538461535, 0.91538461538461535, 0.91538461538461535, 0.91538461538461535, 0.92627599243856329, 0.92627599243856329, 0.93018867924528303, 0.93018867924528303, 0.93018867924528303, 0.93018867924528303, 0.95274831243972991, 0.97733990147783256, 0.97733990147783256, 0.97733990147783256, 0.97733990147783256, 0.97733990147783256, 0.97733990147783256, 0.97733990147783256, 0.97733990147783256, 0.97733990147783256, 0.97733990147783256])

average_linear_svm = list(np.mean(np.matrix(fscore_linear_svm), axis=0).A1)


fscore_naive_bayes = []
fscore_naive_bayes.append([0.056572379367720464, 0.053082191780821922, 0.062918340026773767, 0.073045267489711935, 0.070881997583568251, 0.075114075114075099, 0.075876049811757884, 0.079459880550506359, 0.088369730827831394, 0.089340101522842649, 0.090163934426229511, 0.088572558323448, 0.085552310599553344, 0.086604886267902276, 0.084229941592376262, 0.083284799068142096, 0.081778483525208417, 0.07938199254128929, 0.082029598308668072, 0.082921152167588011, 0.083194170335509326, 0.086731391585760528, 0.086504610226320208, 0.08827193450791955, 0.088357982555934772, 0.081632653061224497, 0.081958850535623184, 0.085548318957929942, 0.086288209606986896, 0.093590247738891075, 0.095257154292575544, 0.10019863164864269, 0.10489014883061658, 0.10891343436938093, 0.11119651550089676, 0.11070686070686071, 0.11281779661016948, 0.11372652737371067, 0.11431595660227574, 0.11443850267379678, 0.11523963381798601, 0.11684782608695653, 0.12035303557100829, 0.12111468381564845, 0.12405609492988134, 0.1264864864864865, 0.12624227773301103, 0.12731668009669622, 0.12779724993259636, 0.13188602442333786, 0.13348041919470491, 0.13499308437067775, 0.13823857302118173, 0.138375350140056, 0.13876404494382022, 0.13922281241263629, 0.14048890137679124, 0.1405283867341203, 0.14372294372294372, 0.14389324049898461, 0.14387667713388522, 0.14417001723147616, 0.14607390300230949, 0.14720370906983482, 0.14819136522753792, 0.15403056637698534, 0.15081001472754049, 0.15555555555555556, 0.1561092764935455, 0.15748502994011976, 0.15975975975975976, 0.16043425814234016, 0.16270566727605118, 0.16589002795899346, 0.1656479217603912, 0.1672281776416539, 0.17863049950380416, 0.18243472363513058, 0.18169491525423728, 0.18611111111111112, 0.18611111111111112, 0.18951048951048952, 0.18970948547427371, 0.18977591036414565, 0.19136690647482013, 0.19689119170984454, 0.19850746268656713, 0.19954988747186797, 0.19954988747186797, 0.20014992503748127, 0.20150943396226415, 0.20472440944881887, 0.20480120030007504, 0.20628834355828224, 0.21347876899104012, 0.21397891448652867, 0.21294851794071762, 0.21384136858475894, 0.21859198755348114, 0.21901792673421666, 0.22787979966611022, 0.22845188284518825])
fscore_naive_bayes.append([0.040772532188841207, 0.044967880085653111, 0.060684312459651391, 0.063058823529411764, 0.068566340160284955, 0.080478087649402383, 0.085493099966341302, 0.091859360152043087, 0.09306742640075974, 0.094653812445223487, 0.093507881378573326, 0.094500800854244532, 0.09551760939167557, 0.096507597973873635, 0.093621149648314334, 0.091949240690659448, 0.094481937276697098, 0.097308934337997852, 0.097697439208091236, 0.10184746565608715, 0.10529019003595276, 0.10632780082987552, 0.10520517763701459, 0.11196554906182714, 0.10974822466107166, 0.11275590551181103, 0.11229428848015491, 0.11605670952851962, 0.11841674844618906, 0.11841674844618906, 0.11895424836601308, 0.12526389866291343, 0.14029084687767324, 0.1407942238267148, 0.14522635589421784, 0.14542020774315395, 0.14846743295019157, 0.15092502434274588, 0.14549078226208273, 0.14597815292949354, 0.14651279478173607, 0.14803625377643503, 0.14863498483316481, 0.1549367088607595, 0.15748841996911991, 0.16421968461120173, 0.16457765667574933, 0.1764705882352941, 0.18091560948703805, 0.183013698630137, 0.18500273672687464, 0.18784530386740328, 0.18708240534521159, 0.19232970807097885, 0.20451693851944794, 0.2115743621655258, 0.21446384039900249, 0.21890547263681592, 0.22586999343401185, 0.22641509433962265, 0.22264389626818468, 0.22560202788339673, 0.22814631122132673, 0.2292834890965732, 0.23960273122284295, 0.24572514249525021, 0.25081221572449641, 0.25294482331060136, 0.25108225108225113, 0.25806451612903225, 0.25941939468807906, 0.26533166458072588, 0.27023581899298921, 0.27568270481144347, 0.28514851485148512, 0.28647925033467198, 0.28940217391304346, 0.29781420765027322, 0.30160857908847183, 0.30843706777316737, 0.31145251396648044, 0.31036882393876131, 0.32225433526011554, 0.3272990586531499, 0.33113553113553112, 0.33900814211695041, 0.33866279069767441, 0.35818601076095313, 0.35941130906274205, 0.3701350277998412, 0.37131474103585654, 0.37956204379562042, 0.38398692810457513, 0.38336052202283855, 0.38599348534201955, 0.40572390572390571, 0.40675105485232066, 0.40672268907563025, 0.41226575809199317, 0.41538461538461535, 0.41538461538461535, 0.41309823677581864])
fscore_naive_bayes.append([0.054834054834054839, 0.058236272878535771, 0.077831827658095903, 0.081037277147487846, 0.080328617069831118, 0.077372262773722625, 0.07924305144884683, 0.08217013431656571, 0.083179784153724665, 0.080945884492951342, 0.081347576006573552, 0.082060717571297154, 0.083016371754589063, 0.086201452478686463, 0.086805555555555566, 0.087409277374566122, 0.085007278020378468, 0.082363473589973146, 0.083927157561361834, 0.082066372404773574, 0.083144894764306837, 0.085355055781831043, 0.089633671083398272, 0.090788308237378212, 0.092507829438689473, 0.095397090388743139, 0.10164271047227925, 0.105433901054339, 0.11171273867198632, 0.11859490815339994, 0.11768754301445286, 0.11768754301445286, 0.11825369542798213, 0.13015873015873014, 0.13280318091451293, 0.13602638087386645, 0.13996478873239437, 0.14381420276909335, 0.15605552896122546, 0.15926640926640928, 0.16574027286508336, 0.16759776536312848, 0.16999487967229901, 0.1721311475409836, 0.17656169334021682, 0.18239325250395361, 0.18237704918032785, 0.18510638297872339, 0.18902770233568714, 0.18890719384953322, 0.18746594005449593, 0.18958904109589045, 0.19105466593042517, 0.19104803493449782, 0.19898819561551434, 0.20550252667040986, 0.20742358078602618, 0.20856201975850713, 0.2227405247813411, 0.23651960784313722, 0.23850931677018633, 0.24322621298046629, 0.25140712945590993, 0.25396825396825395, 0.25061728395061733, 0.25521472392638034, 0.25747406955460644, 0.25622343655130542, 0.25656689065363469, 0.24736225087924971, 0.24970414201183427, 0.25222024866785081, 0.25892316999395038, 0.26029055690072639, 0.2588801926550271, 0.25656324582338902, 0.26328502415458938, 0.27222562844880444, 0.27995110024449882, 0.28553921568627449, 0.2857142857142857, 0.28796128251663639, 0.29104028863499704, 0.29719853836784405, 0.29940119760479045, 0.2988777318369758, 0.31272727272727274, 0.31159420289855072, 0.31167268351383876, 0.31386861313868614, 0.31444241316270566, 0.32226322263222634, 0.32695866748920421, 0.32897196261682243, 0.3335407591785936, 0.33601983880967146, 0.33541147132169574, 0.33415536374845872, 0.33780487804878045, 0.33818181818181819, 0.33787788974510968, 0.34397163120567376])
fscore_naive_bayes.append([0.0078277886497064575, 0.03439153439153439, 0.051380860629415548, 0.060908637044433354, 0.066981537140403613, 0.082311040759794216, 0.084507042253521125, 0.090965732087227427, 0.091615322796678278, 0.08758782201405152, 0.084175778832267387, 0.084965972365436168, 0.086590038314176249, 0.087322864802757555, 0.084963863916798874, 0.082782499213094121, 0.083385777218376339, 0.083988675684177408, 0.084479689270108432, 0.085984522785898548, 0.085808580858085806, 0.088218661639962295, 0.084157455885204568, 0.084137081879745529, 0.084005091217649555, 0.082815734989648032, 0.085115303983228516, 0.087640927462242071, 0.089425725789362157, 0.08957952468007313, 0.089995431703974421, 0.095048519532221959, 0.10030820958251611, 0.10030820958251611, 0.10030820958251611, 0.10644418872266972, 0.1104907434616515, 0.11281748375664502, 0.11347943560492345, 0.11603053435114505, 0.11551459293394778, 0.12303906490310675, 0.12362971985383678, 0.12917737789203085, 0.13014354066985645, 0.13017377567140601, 0.13426387504154205, 0.13502673796791442, 0.1356391997287216, 0.13807386952019332, 0.13855213023900245, 0.13927576601671307, 0.13937282229965156, 0.14414414414414414, 0.14404033129276198, 0.15773115773115773, 0.16287425149700599, 0.1687763713080169, 0.16927634363097757, 0.17021276595744683, 0.18095648427401981, 0.1838979322481302, 0.19099590723055934, 0.19216757741347903, 0.20635696821515889, 0.20814923907707414, 0.20896993592902907, 0.21099116781158, 0.21083743842364533, 0.217, 0.23634336677814941, 0.23728813559322032, 0.2400448681996635, 0.2425603593486805, 0.24508150646430582, 0.24957264957264957, 0.249714937286203, 0.24830699774266365, 0.24738867509620671, 0.25097168239866741, 0.25330396475770928, 0.25809994508511808, 0.25711159737417943, 0.25879805089334057, 0.26229508196721313, 0.26186579378068736, 0.26200873362445415, 0.26315789473684215, 0.26830631637786473, 0.27011817670230726, 0.27066001109262339, 0.2687224669603524, 0.27621195039458851, 0.27687113111986494, 0.27859569648924126, 0.28340080971659914, 0.28521536670547143, 0.28504672897196254, 0.28756629345904539, 0.28892835997631733, 0.28908554572271389, 0.28939660222612773])
fscore_naive_bayes.append([0.058823529411764712, 0.065140845070422518, 0.074122236671001304, 0.074557315936626276, 0.075653923541247475, 0.084793272599859845, 0.085861476817401264, 0.094334507996747086, 0.094484293841207018, 0.094778007821486071, 0.088994835121176008, 0.092045454545454541, 0.095738893925657306, 0.096429218778321557, 0.094576719576719565, 0.094963592233009708, 0.093264248704663211, 0.089808137161518559, 0.090401785714285726, 0.090790427846265398, 0.094497607655502372, 0.095411176737846423, 0.093949044585987268, 0.096339779005524859, 0.095487018644363125, 0.096528365791701945, 0.098208132322536196, 0.10338551146705496, 0.10501708325840677, 0.10286992172940738, 0.10286992172940738, 0.10743969187107238, 0.1087202718006795, 0.11593487913172175, 0.12513601741022851, 0.12828947368421051, 0.12948857453754081, 0.1324503311258278, 0.13439385628085571, 0.13640098603122433, 0.13694801565120179, 0.14256619144602853, 0.14411764705882354, 0.14503133393017012, 0.14980602805132795, 0.15571473061351604, 0.15660377358490565, 0.15837820715869497, 0.16233354470513636, 0.16228209191759113, 0.16579292267365664, 0.1654485049833887, 0.17009966777408639, 0.17118020728853225, 0.18194791295041027, 0.18142392482833394, 0.18365871294287778, 0.19781110660721524, 0.20032573289902281, 0.20640865584685808, 0.20770519262981579, 0.1947798987144527, 0.19398797595190381, 0.19492868462757529, 0.1945902301170771, 0.19272291083566576, 0.19334135579622944, 0.19365079365079366, 0.19564356435643565, 0.19839999999999999, 0.19879759519038073, 0.19959758551307846, 0.20321285140562251, 0.20429671665991081, 0.20711974110032361, 0.21160971593248251, 0.21902017291066284, 0.22691511387163563, 0.22764900662251655, 0.2308015107007973, 0.23238255033557048, 0.23337515683814306, 0.23613445378151257, 0.23761544920235092, 0.23642439431913112, 0.23993358239933582, 0.24173985780008367, 0.2443133951137321, 0.24776500638569607, 0.24734381640458988, 0.24659863945578234, 0.2519148936170213, 0.2544529262086514, 0.2592274678111588, 0.25933877200515243, 0.2653862941946748, 0.26625659050966605, 0.26802299867315349, 0.2723666813574262, 0.27925892453682782, 0.28065395095367845, 0.28221415607985484])

average_naive_bayes = list(np.mean(np.matrix(fscore_naive_bayes), axis=0).A1)



ranges = [label_potential, label_potential, label_potential]
list = [average_metadata_no_svd_absolute_potential, average_linear_svm, average_naive_bayes]
names = ["XGBoost", "Linear SVM", "Naive Bayes"]

plot_list_latex(ranges, list, names, "Hospital", x_max=800)