import numpy as np

from ml.datasets.flights.FlightHoloClean import FlightHoloClean
from ml.plot.old.user_effort_all_potential.PlotterLatex import PlotterLatex

data = FlightHoloClean()

label_potential = [4, 8, 12, 16, 26, 36, 46, 56, 66, 76, 86, 96, 106, 116, 126, 136, 146, 156, 166, 176, 186, 196, 206, 216, 226, 236, 246, 256, 266, 276, 286]

fscore_metadata_no_svd_absolute_potential = []
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.30257029498016214, 0.51009957325746791, 0.65832531280077, 0.78654824867777673, 0.81651549508692367, 0.8303065807459481, 0.84278801606094922, 0.84283069327298898, 0.85875012785107918, 0.84568221968201185, 0.86688511161171411, 0.87603139464681012, 0.8748236242693006, 0.88662041625371657, 0.8912142152023691, 0.88906311250490011, 0.89362545851095476, 0.896097513024673, 0.90286953949314652, 0.91048186785891705, 0.91118056255670932, 0.91922455573505646, 0.92562986947283221, 0.93261945651075862, 0.93468853778806471, 0.94117647058823528, 0.94639999999999991])
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.29274084124830391, 0.54129571291603895, 0.68159203980099503, 0.7947661240469811, 0.80162958320275779, 0.82753500212134079, 0.83166291675189208, 0.83218534752661244, 0.86115851822106204, 0.8646123260437375, 0.86871673565937313, 0.87662910338069577, 0.8809594023395263, 0.88582330496037565, 0.89249096767893754, 0.89981282632252979, 0.90447234209493921, 0.90822878593302381, 0.91340754605457597, 0.91459074733096091, 0.91646118946641686, 0.90965669544268213, 0.91497487437185931, 0.92323273242860027, 0.9250075903248659, 0.93063757381643486, 0.93175431553592936])
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.30139823925427239, 0.5021373610715304, 0.65031878371750851, 0.78150021070375064, 0.80094884488448848, 0.83580922595777951, 0.83631039531478768, 0.84550616800469947, 0.8550278792539896, 0.85014634146341472, 0.86112995445295082, 0.85755926933540616, 0.87508453289537236, 0.87468428210608118, 0.87586753916319648, 0.88460015835312755, 0.88510553564317018, 0.89041231992051673, 0.89673643487749233, 0.89794703957155608, 0.90212088021507519, 0.90809519068007571, 0.91132414619532665, 0.91359504545000503, 0.91750824917508245, 0.91995197118270977, 0.92340042054671068])
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.30139823925427239, 0.56022635408245758, 0.68972845336481703, 0.81684044855400362, 0.82383048418466576, 0.82875737238153346, 0.84386884571898446, 0.85468157112091059, 0.8637721569408483, 0.86784228254408569, 0.86830909270802414, 0.87416023262809572, 0.88034101288947531, 0.89219929542023158, 0.90444578555622612, 0.90211826121875305, 0.90808416389811741, 0.91134185303514381, 0.91545653471255228, 0.92048960095531895, 0.92490276254113901, 0.9292044209897441, 0.93399701343952213, 0.93365259902224873, 0.93430365865815967, 0.93880389429763567, 0.9436591678279912])
fscore_metadata_no_svd_absolute_potential.append([0.0, 0.0, 0.0, 0.0, 0.30257029498016214, 0.49273694807996543, 0.63855421686746994, 0.79033257591406714, 0.77163030877858585, 0.77019315188762061, 0.770310272996382, 0.78310855626796383, 0.78870030755211296, 0.81864235055724421, 0.8376125375125042, 0.85922224636106881, 0.88159560996200925, 0.89028607356177303, 0.90607962143812359, 0.90493282740231773, 0.90484482228823104, 0.90696721311475403, 0.90840703466504014, 0.91331582137805623, 0.91403544510083523, 0.92134603689438477, 0.92967409948542024, 0.93084944821302018, 0.93281680089713515, 0.93764669864271866, 0.94009779951100236])


nadeef_fscore = 0.59098550956688811

openrefine_fscore = 0.7366


dboost_models = ["Gaussian", "Histogram", "Mixture"]
dboost_sizes = [50, 100, 150, 200]
dboost_fscore_all = [
                        # Gaussian
                        [
                            [0.538528896673, 0.538528896673, 0.387106163138, 0.536971350614, 0.538528896673],
                            [0.387106163138, 0.538528896673, 0.538528896673, 0.536971350614, 0.536971350614],
                            [0.536971350614, 0.536971350614, 0.538528896673, 0.538528896673, 0.538528896673],
                            [0.536971350614, 0.538528896673, 0.538528896673, 0.387106163138, 0.538528896673]
                        ],
                        # Histogram
                        [
                            [0.56778474014, 0.56778474014, 0.56778474014, 0.56778474014, 0.50033101622],
                            [0.50033101622, 0.56555613267, 0.56778474014, 0.56778474014, 0.56778474014],
                            [0.56555613267, 0.56555613267, 0.593559042114, 0.56778474014, 0.56555613267],
                            [0.56778474014, 0.56555613267, 0.593559042114, 0.56778474014, 0.56778474014]
                        ],
                        # Mixture
                        [
                            [0.682196339434, 0.682196339434, 0.501574365623, 0.501574365623, 0.682196339434],
                            [0.682196339434, 0.527322985329, 0.501574365623, 0.527322985329, 0.682196339434],
                            [0.682196339434, 0.682196339434, 0.682196339434, 0.682196339434, 0.682196339434],
                            [0.682196339434, 0.554024161987, 0.682196339434, 0.594272844273, 0.682196339434]
                        ]
                    ]

dboost_matrix_f = np.array(dboost_fscore_all)
dboost_avg_f = np.mean(dboost_matrix_f, axis = 2)


PlotterLatex(data, label_potential, fscore_metadata_no_svd_absolute_potential,
         dboost_models, dboost_sizes, dboost_avg_f,
         nadeef_fscore,
         openrefine_fscore,
         None, xmax=200, filename="Flights")