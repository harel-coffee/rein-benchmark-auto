import matplotlib.pyplot as plt
import numpy as np

labels = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 74, 84, 94, 104, 114, 124, 134, 144, 154, 164, 174, 184, 194, 204, 214, 224, 234, 244, 254, 264, 274, 284, 294, 304, 314, 324, 334, 344, 354, 364, 374, 384, 394, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 504, 514, 524, 534, 544, 554, 564, 574, 584, 594, 604, 614, 624, 634, 644, 654, 664, 674, 684, 694, 704, 714, 724, 734, 744, 754, 764, 774, 784, 794, 804, 814, 824, 834, 844, 854, 864, 874, 884, 894, 904]
ed2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03582089552238806, 0.044378698224852076, 0.044378698224852076, 0.044378698224852076, 0.044378698224852076, 0.044378698224852076, 0.05301914580265096, 0.05301914580265096, 0.05301914580265096, 0.05301914580265096, 0.06267806267806268, 0.06227106227106227, 0.06934306569343066, 0.07650273224043716, 0.07650273224043716, 0.0915032679738562, 0.09608540925266904, 0.109347442680776, 0.109347442680776, 0.109347442680776, 0.12068965517241378, 0.13220338983050847, 0.13781512605042018, 0.14093959731543626, 0.14093959731543626, 0.14715719063545152, 0.1505016722408027, 0.1505016722408027, 0.15177065767284992, 0.15878378378378377, 0.16915422885572143, 0.1697171381031614, 0.17880794701986757, 0.18512396694214875, 0.18729096989966554, 0.18940609951845908, 0.1956882255389718, 0.1956882255389718, 0.2017094017094017, 0.2017094017094017, 0.20477815699658705, 0.2169491525423729, 0.2276707530647986, 0.2276707530647986, 0.23172905525846701, 0.2381786339754816, 0.24125874125874128, 0.24956672443674177, 0.2525951557093426, 0.25263157894736843, 0.26480836236933797, 0.27816901408450706, 0.28368794326241137, 0.29276895943562614, 0.30175438596491233, 0.30472854640980734, 0.3052631578947368, 0.31010452961672474, 0.31010452961672474, 0.31010452961672474, 0.31064572425828973, 0.32000000000000006, 0.32582322357019056, 0.33057851239669417, 0.3430531732418525, 0.3458904109589041, 0.34871794871794876, 0.3499142367066896, 0.34707903780068733, 0.3499142367066896, 0.4072847682119205, 0.41254125412541254, 0.41254125412541254, 0.41254125412541254, 0.413907284768212, 0.413907284768212, 0.413907284768212, 0.42174629324546953]


nadeef = np.ones(len(labels)) * 0.061508180588018206
histogram = np.ones(len(labels)) * 0.19
gaussian = np.ones(len(labels)) * 0.03968
mixture = np.ones(len(labels)) * -1.0
openrefine = np.ones(len(labels)) * 0.0
katara = np.ones(len(labels)) * -1.0

fig = plt.figure()
ax = plt.subplot(111)

ax.plot(labels, ed2, label="ED2")
ax.plot(labels, nadeef, label="Nadeef")
ax.plot(labels, histogram, label="Histogram")
ax.plot(labels, gaussian, label="gaussian")
ax.plot(labels, mixture, label="mixture")
ax.plot(labels, openrefine, label="openrefine")
ax.plot(labels, katara, label="katara")

ax.set_ylabel('total fscore')
ax.set_ylim((0.0, 1.0))
ax.set_xlabel('labels')

ax.legend(loc=0)

plt.show()