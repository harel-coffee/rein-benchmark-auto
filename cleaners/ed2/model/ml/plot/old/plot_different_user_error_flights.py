import matplotlib.pyplot as plt
import numpy as np

from ml.datasets.flights import FlightHoloClean


def plot_list(ranges, list_series, list_names):
    fig = plt.figure()
    ax = plt.subplot(111)

    for i in range(len(list_series)):
        ax.plot(ranges[i], list_series[i], label=list_names[i])

    last = ranges[0][len(ranges[0]) - 1]
    baseline = 0.763
    baseline_reporter = 'HoloClean'

    ax.plot((0, last), (baseline, baseline), 'k-', color='orange', label='baseline reported by ' + baseline_reporter)

    ax.set_ylabel('F-score')
    ax.set_xlabel('Number of rows to label')

    ax.legend(loc=4)



    plt.show()

fscore_0 = []
fscore_0.append([0.0, 0.0, 0.0, 0.0, 0.3022774327122153, 0.49671676637968776, 0.65743690271992161, 0.75257944696657042, 0.75283680627192073, 0.78949889815080954, 0.79103877838055048, 0.79462532299741595, 0.79586990191017037, 0.79917184265010344, 0.81055742382553764, 0.83308149491286387, 0.8330145948666331, 0.8419377300308365, 0.85089463220675954, 0.84464431725265743, 0.84507618365886072, 0.8459251665812404, 0.8491414554374489, 0.87017048320387369])
fscore_0.append([0.0, 0.0, 0.0, 0.0, 0.29846100639806333, 0.50698602794411185, 0.65282201554338126, 0.76877339792997135, 0.77080356161371877, 0.79118253882071887, 0.79237104464672736, 0.79590737749057605, 0.7972027972027973, 0.81930693069306926, 0.82510096303199754, 0.82014853083629313, 0.819686223941543, 0.82251725969198086, 0.8320016820857864, 0.84796573875803005, 0.84891792568395263, 0.84415449932691322, 0.84934903905765646, 0.85723108594956254])
fscore_0.append([0.0, 0.0, 0.0, 0.0, 0.30169140490162233, 0.54260338606716629, 0.68801780635587984, 0.78817226457861123, 0.78867147270854787, 0.779789301421704, 0.78847687400318978, 0.78198236938292842, 0.77548853016142738, 0.79768786127167635, 0.80979403110550652, 0.79982882208195138, 0.80834955656500107, 0.81518116331577262, 0.82387932865944347, 0.84141519250780439, 0.84153574029757572, 0.84974629802216006, 0.85770423991726996, 0.86868480261812231])
fscore_0.append([0.0, 0.0, 0.0, 0.0, 0.29757785467128028, 0.53098071399261382, 0.66875527171948423, 0.77243655869610051, 0.77471169686985175, 0.76800858829844343, 0.78049823586015177, 0.76914539400665927, 0.77050997782705111, 0.80356581017304651, 0.81378438191590263, 0.83398170539375471, 0.83398170539375471, 0.84032904450537871, 0.85134993171551643, 0.86114469971785568, 0.86114469971785568, 0.87170227705888248, 0.87019854335029434, 0.8738848337388484])
fscore_0.append([0.0, 0.0, 0.0, 0.0, 0.30169140490162233, 0.54760269267756556, 0.65843113032736245, 0.77013054830287198, 0.77062689058099509, 0.77226277372262764, 0.79710872402369237, 0.78118348233290757, 0.76559900166389339, 0.78348846620801282, 0.79302108214767897, 0.80519480519480513, 0.82020583910943079, 0.82535034511608452, 0.83696437790397527, 0.85085771947527744, 0.8539894694208181, 0.86012992285830281, 0.86458439312239288, 0.87733549959382606])

average_0 = list(np.mean(np.matrix(fscore_0), axis=0).A1)
label_0 = [4, 8, 12, 16, 26, 36, 46, 56, 66, 76, 86, 96, 106, 116, 126, 136, 146, 156, 166, 176, 186, 196, 206, 216]


fscore_5 = []
fscore_5.append([0.0, 0.0, 0.0, 0.0, 0.29640921409214094, 0.47055468415799229, 0.62028542303771661, 0.72202011555745771, 0.72980561555075585, 0.75124378109452727, 0.76418030318241148, 0.7699018538713196, 0.77215942891136236, 0.79705009098745339, 0.80000000000000004, 0.80711770863069743, 0.80746524471529246, 0.80998746746360739, 0.81270837419101782, 0.82341289491928293, 0.82317979197622582, 0.8318739054290718, 0.83060319907496638, 0.83984110066853979])
fscore_5.append([0.0, 0.0, 0.0, 0.0, 0.26964317103181579, 0.54747996196168991, 0.67724620770128363, 0.78149532710280389, 0.79001113999257333, 0.78402255639097751, 0.79969272133666203, 0.80344557556773677, 0.80636656576506194, 0.80860131731886875, 0.81470616994230971, 0.82589956900872008, 0.82637010319607263, 0.83109972408356325, 0.82672729069882378, 0.82994272170649808, 0.83198898288412337, 0.84446197849886573, 0.85789116306140267, 0.86212299255777514])
fscore_5.append([0.0, 0.0, 0.0, 0.0, 0.27881756165821231, 0.52715086855423332, 0.65706743460523154, 0.74667230086625813, 0.75508919202518365, 0.75720076808192871, 0.75983370642788606, 0.77835372174994821, 0.77651165178113124, 0.77731049338393698, 0.78681364392678876, 0.78295236060670792, 0.78505673303361156, 0.7837572317432594, 0.79896238651102458, 0.80623798333689378, 0.8068035943517331, 0.81051735150095805, 0.82192071231715069, 0.83264615709905898])
fscore_5.append([0.0, 0.0, 0.0, 0.0, 0.23097112860892391, 0.48322518293524791, 0.62948702024593217, 0.74852985149008255, 0.77933535927850228, 0.80740880740880738, 0.81283521361198441, 0.8055305079651337, 0.80404931342086794, 0.79040135909959641, 0.80369074132993945, 0.82102102102102104, 0.82775312626058895, 0.84254723582925117, 0.85121927139895337, 0.85484511517077044, 0.85515873015873012, 0.86491758509704486, 0.87105960915250891, 0.87364904696404011])
fscore_5.append([0.0, 0.0, 0.0, 0.0, 0.12289156626506023, 0.4071840235893312, 0.55413105413105423, 0.64556282862968117, 0.69329214474845535, 0.7255486895376092, 0.72731168970320381, 0.73948696383515555, 0.74884015183466912, 0.74869611495476307, 0.75886900349465214, 0.76530825496342736, 0.78742762613730355, 0.77759965801004582, 0.78477243726074009, 0.80462618752581572, 0.82108919995912943, 0.83197389885807516, 0.84525252525252526, 0.85272745880667278])

average_5 = list(np.mean(np.matrix(fscore_5), axis=0).A1)
label_5 = [4, 8, 12, 16, 26, 36, 46, 56, 66, 76, 86, 96, 106, 116, 126, 136, 146, 156, 166, 176, 186, 196, 206, 216]


fscore_10 = []
fscore_10.append([0.0, 0.0, 0.0, 0.0, 0.30169140490162233, 0.56708196721311466, 0.59380139152435163, 0.72281126931232964, 0.70983885496947252, 0.70169281585466559, 0.71813502876173174, 0.70595771941063423, 0.71698113207547176, 0.72170212765957442, 0.77928816021583469, 0.78969867584193509, 0.79375325351379478, 0.78681881198677606, 0.80249524212307033, 0.80138786668068551, 0.80067283431455005, 0.82005594115818914, 0.8273166718091125, 0.83706265256305945])
fscore_10.append([0.0, 0.0, 0.0, 0.0, 0.29475465313028765, 0.45216883306557615, 0.59960861056751469, 0.6745953898970084, 0.66610373944511458, 0.65848965848965846, 0.66262814538676607, 0.68836901346281176, 0.68619705946894904, 0.7007628666595036, 0.7094609222775492, 0.70914674270673395, 0.7086544813917639, 0.71247150765223055, 0.72083423854008266, 0.72590684696286756, 0.73422106744614057, 0.74354263482113914, 0.75342613575051243, 0.76571672537090418])
fscore_10.append([0.0, 0.0, 0.0, 0.0, 0.036711891460494812, 0.32992654104120089, 0.47446457990115326, 0.60008818342151682, 0.62879931019616297, 0.6601354872329338, 0.69744835965978136, 0.70147406323843831, 0.75271797058196555, 0.76183447548761196, 0.77622750026626908, 0.78461372696907672, 0.79083837510803801, 0.78604344963791972, 0.79121366762813405, 0.80121858339680119, 0.80617122990004342, 0.80767111209081888, 0.8129812981298129, 0.81356678779870062])
fscore_10.append([0.0, 0.0, 0.0, 0.0, 0.0012187690432663011, 0.29705547421506429, 0.47836114502781163, 0.62601269980293417, 0.63379055083823221, 0.68000410382681842, 0.69032581453634079, 0.69559032716927449, 0.69942255090669636, 0.66932959084529853, 0.68131390036980644, 0.69121935414191593, 0.73813354786806118, 0.73783074126439108, 0.74797086368366272, 0.75142435112893013, 0.7877766069546891, 0.80891980360065474, 0.81495782948887308, 0.81803542673107887])
fscore_10.append([0.0, 0.0, 0.0, 0.0, 0.30081160421343467, 0.5224363482908988, 0.62064516129032266, 0.7337725456312777, 0.73418268192614999, 0.73469834665498746, 0.73576455534229046, 0.76016088060965281, 0.76068556919170549, 0.76680942184154188, 0.75573519772776931, 0.73406740073406751, 0.73547383624041773, 0.74259381171823557, 0.75965618539875968, 0.76980633802816889, 0.76843722563652328, 0.775536901776954, 0.78471696071003361, 0.77484696716750134])

average_10 = list(np.mean(np.matrix(fscore_10), axis=0).A1)
label_10 = [4, 8, 12, 16, 26, 36, 46, 56, 66, 76, 86, 96, 106, 116, 126, 136, 146, 156, 166, 176, 186, 196, 206, 216]

data = FlightHoloClean()

print data.shape

ranges = [np.array(label_0) / float(data.shape[1]),
          np.array(label_5) / float(data.shape[1]),
          np.array(label_10) / float(data.shape[1])]
list = [average_0, average_5, average_10]
names = ["no user error", "5% user error", "10% user error"]

plot_list(ranges, list, names)